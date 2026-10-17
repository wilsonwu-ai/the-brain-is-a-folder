#!/usr/bin/env python3
"""
A deterministic, rule-based filing step. Python standard library only. No model.

    python3 demo/filer.py <brain-folder> [--now "YYYY-MM-DD HH:MM"]

It does what chapter three describes, with the guardrails from chapter eight
enforced in code instead of asked for in a prompt:

  * Reads every email in raw/. It never writes there.
  * Files each ordinary email as a wiki page (with a `sources:` header and
    links), updates the person page, then rebuilds wiki/index.md.
  * Scans each email for text that is aimed at the agent rather than at the
    reader. A match is NOT filed and NOT followed. The email is named in
    wiki/log.md and in the index's housekeeping list, and nothing it says is
    copied into the wiki.
  * Every write goes through safe_write(), which only allows paths inside
    wiki/. about/, rules.md, skills/ and raw/ cannot be written by this
    program, whatever an email says and whether or not the scan catches it.

Two honest limits, both pinned by tests:

  1. The scan is a tripwire made of regular expressions. A rephrased attack
     can walk past it. The write guard is the real defence, and it does not
     depend on detection.
  2. This filer regenerates the pages it owns from raw/ on every run, so it is
     idempotent. A real filing job would merge with hand edits instead.
"""

import argparse
import os
import re
import sys
from datetime import datetime
from email import message_from_string, policy
from email.utils import parseaddr
from pathlib import Path

WRITABLE = "wiki"

# Each pattern has a plain name so the log can say why a source was flagged
# without quoting the hostile text itself.
INJECTION_PATTERNS = [
    ("addresses-the-assistant",
     r"\b(note|message|instructions?)\s+(to|for)\s+(the\s+)?(assistant|agent|ai|model)\b"
     r"|\b(assistant|ai agent|language model)\s*[,:]"),
    ("overrides-instructions",
     r"\b(ignore|disregard|forget|override)\b[^.]{0,40}\b(instructions?|rules?|prompt)\b"),
    ("asks-to-change-rules",
     r"\b(add|create|write|append|edit|change|update|delete|remove)\b[^.]{0,30}\brules?\b"),
    ("names-a-protected-file",
     r"\b(rules\.md|agents\.md|skill\.md)\b|\babout/"),
    ("standing-forward-order",
     r"\b(always|automatically|from now on|every time)\b[^.]{0,40}\b(forward|send|cc|bcc|copy)\b"),
    ("asks-for-secrecy",
     r"\bdo not (mention|tell|reveal|show)\b"),
]
_COMPILED = [(name, re.compile(rx, re.IGNORECASE)) for name, rx in INJECTION_PATTERNS]


class GuardrailError(Exception):
    """Raised when the filer is asked to write outside wiki/."""


def safe_write(brain, rel_path, text):
    """Write text to brain/rel_path, but only if it lands inside brain/wiki/.

    Checked twice: lexically (so wiki/../rules.md is refused) and on the real
    filesystem path (so a symlink that points out of wiki/ is refused).
    """
    brain = Path(brain)
    allowed = brain / WRITABLE
    target = brain / rel_path

    lexical = os.path.normpath(target)
    allowed_lexical = os.path.normpath(allowed)
    if not _inside(lexical, allowed_lexical):
        raise GuardrailError(f"refused: {rel_path} is outside {WRITABLE}/")

    real = os.path.realpath(target)
    allowed_real = os.path.realpath(allowed)
    if not _inside(real, allowed_real):
        raise GuardrailError(f"refused: {rel_path} resolves outside {WRITABLE}/")

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def _inside(path, folder):
    return path != folder and os.path.commonpath([path, folder]) == folder


def scan_for_injection(subject, body):
    """Return the names of every tripwire pattern the text matches, in fixed order."""
    text = f"{subject}\n{body}"
    return [name for name, rx in _COMPILED if rx.search(text)]


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


class Email:
    def __init__(self, path):
        self.path = Path(path)
        self.stem = self.path.stem
        self.raw_ref = f"raw/{self.path.name}"
        msg = message_from_string(self.path.read_text(encoding="utf-8"), policy=policy.default)
        self.subject = str(msg["Subject"] or "(no subject)").strip()
        name, address = parseaddr(str(msg["From"] or ""))
        self.address = address
        self.sender = name.strip() or (address.split("@")[0] if address else "unknown sender")
        self.date = self.stem[:10] if re.match(r"\d{4}-\d{2}-\d{2}", self.stem) else "undated"
        part = msg.get_body(preferencelist=("plain",))
        self.body = part.get_content() if part is not None else ""
        self.flags = scan_for_injection(self.subject, self.body)

    @property
    def person_slug(self):
        return slugify(self.sender) or "unknown"


def summarize(body, limit=280):
    """Extractive summary: the first one or two sentences after the greeting."""
    paragraphs = [" ".join(p.split()) for p in re.split(r"\n\s*\n", body.strip()) if p.strip()]
    if paragraphs and len(paragraphs[0]) <= 30 and paragraphs[0].endswith(","):
        paragraphs = paragraphs[1:]
    if not paragraphs:
        return "(empty message)"
    sentences = re.split(r"(?<=[.!?])\s+", paragraphs[0])
    return " ".join(sentences[:2])[:limit]


def topic_page(email):
    return (
        "---\n"
        f"title: {email.subject}\n"
        "type: topic\n"
        "sources:\n"
        f"  - {email.raw_ref}\n"
        "---\n"
        f"# {email.subject}\n\n"
        f"From [{email.sender}](../people/{email.person_slug}.md), {email.date}. "
        f"Source: `{email.raw_ref}`.\n\n"
        "Summary, copied from the first sentences of the email (this filer has no model):\n\n"
        f"> {summarize(email.body)}\n\n"
        "Facts here are as of the email date. Check the app they live in before relying on them.\n\n"
        "Back to the [index](../index.md).\n"
    )


def person_page(name, emails):
    lines = [
        "---",
        f"title: {name}",
        "type: person",
        "sources:",
    ]
    lines += [f"  - {e.raw_ref}" for e in emails]
    lines += ["---", f"# {name}", "", "Emails filed from this sender:", ""]
    lines += [f"- [{e.subject}](../topics/{e.stem}.md), {e.date}" for e in emails]
    lines += ["", "Back to the [index](../index.md).", ""]
    return "\n".join(lines)


def _read(path):
    return path.read_text(encoding="utf-8") if path.exists() else None


def _replace_section(text, heading, body_lines):
    """Replace everything under '## heading' up to the next '## ' heading."""
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        out.append(lines[i])
        if lines[i] == f"## {heading}":
            out.append("")
            out.extend(body_lines)
            i += 1
            while i < len(lines) and not lines[i].startswith("## "):
                i += 1
            if i < len(lines):
                out.append("")
            continue
        i += 1
    return "\n".join(out)


def build_index(template, benign, people, flagged):
    people_lines = []
    for slug in sorted(people):
        emails = people[slug]
        latest = max(e.date for e in emails)
        people_lines.append(
            f"- [{emails[0].sender}](people/{slug}.md): writes to me by email (latest filed {latest})."
        )
    topic_lines = [
        f"- [{e.subject}](topics/{e.stem}.md): email from {e.sender}, {e.date}."
        for e in sorted(benign, key=lambda e: e.stem)
    ]
    flagged_lines = [
        f"- `{e.raw_ref}` (matched: {', '.join(e.flags)}). Not filed. Open it yourself if you want to see it."
        for e in flagged
    ] or ["- none"]

    text = template
    text = _replace_section(text, "People", people_lines or ["- None yet."])
    text = _replace_section(text, "Projects", ["- None yet."])
    text = _replace_section(text, "Topics", topic_lines or ["- None yet."])
    text = _replace_section(text, "Housekeeping", [
        "- Log of what was filed and when: [log.md](log.md).",
        "- Pages with no incoming links (orphans): none. (Every page above is linked from here.)",
        "- Pages that may be stale: not checked by this demo.",
        "- Sources flagged for your review:",
        *[f"  {line}" for line in flagged_lines],
    ])
    return text.rstrip("\n") + "\n"


def update_log(existing, new_lines):
    """Insert new_lines at the top of the entries, dropping the template's examples."""
    lines = existing.split("\n")
    first = next((i for i, line in enumerate(lines) if line.startswith("- ")), len(lines))
    header = "\n".join(lines[:first]).rstrip()
    old = [ln for ln in lines[first:] if ln.startswith("- ") and not ln.startswith("- YYYY-MM-DD")]
    return header + "\n\n" + "\n".join(new_lines + old) + "\n"


def file_brain(brain, now):
    """Run one filing pass over brain/raw/. Returns a report dict."""
    brain = Path(brain)
    emails = [Email(p) for p in sorted((brain / "raw").glob("*.eml"))]
    benign = [e for e in emails if not e.flags]
    flagged = [e for e in emails if e.flags]

    log_path = brain / "wiki" / "log.md"
    log_text = _read(log_path)
    index_path = brain / "wiki" / "index.md"
    index_template = _read(index_path)
    if log_text is None or index_template is None:
        raise FileNotFoundError("wiki/index.md and wiki/log.md must exist; build the brain first")

    added, updated = [], []

    def write_page(rel, text):
        before = _read(brain / rel)
        if before == text:
            return
        safe_write(brain, rel, text)
        (updated if before is not None else added).append(rel.replace("wiki/", "", 1))

    new_benign = [e for e in benign if not (brain / "wiki" / "topics" / f"{e.stem}.md").exists()]
    new_flagged = [e for e in flagged if e.raw_ref not in log_text]

    people = {}
    for e in benign:
        write_page(f"wiki/topics/{e.stem}.md", topic_page(e))
        people.setdefault(e.person_slug, []).append(e)
    for slug in sorted(people):
        write_page(f"wiki/people/{slug}.md", person_page(people[slug][0].sender, people[slug]))

    write_page("wiki/index.md", build_index(index_template, benign, people, flagged))

    new_log = []
    if new_benign or new_flagged:
        pages_added = sorted(p for p in added if p != "index.md")
        pages_updated = sorted(p for p in updated if p != "index.md")
        changed = []
        if pages_added:
            changed.append("added " + ", ".join(pages_added))
        if pages_updated:
            changed.append("updated " + ", ".join(pages_updated))
        changed.append("rebuilt index.md")
        new_log.append(
            f"- {now} · {len(new_benign) + len(new_flagged)} items from raw/ "
            f"({len(new_benign)} filed, {len(new_flagged)} flagged) · "
            f"{'; '.join(changed)} · {len(new_flagged)} flagged"
        )
        for e in new_flagged:
            new_log.append(
                f"- {now} · {e.raw_ref} reads as an instruction aimed at the agent "
                f"(matched: {', '.join(e.flags)}) · not filed, nothing in it was followed, "
                f"flagged for your review"
            )
        safe_write(brain, "wiki/log.md", update_log(log_text, new_log))

    return {
        "filed": [e.raw_ref for e in new_benign],
        "flagged": [(e.raw_ref, e.flags) for e in new_flagged],
        "added": sorted(added),
        "updated": sorted(updated),
        "log_lines": new_log,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1].strip())
    parser.add_argument("brain")
    parser.add_argument("--now", default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    args = parser.parse_args(argv)
    report = file_brain(args.brain, args.now)
    for ref in report["filed"]:
        print(f"filed    {ref}")
    for ref, flags in report["flagged"]:
        print(f"FLAGGED  {ref}  (matched: {', '.join(flags)})")
    if not report["filed"] and not report["flagged"]:
        print("nothing new in raw/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
