#!/usr/bin/env python3
"""
One command, no installation, no API key, about a second:

    python3 demo/run_demo.py

Builds a sample brain, lands three emails (one carries an injected instruction),
runs the deterministic filing step, then shows the evidence: which files changed
and which did not. The output is identical on every run.
"""

import hashlib
import shutil
import sys
from pathlib import Path

import bootstrap
import filer

FIXED_NOW = "2026-10-17 06:00"
PROTECTED = ["about", "rules.md", "skills", "AGENTS.md", "raw"]


def digest(path):
    """sha256 over every file under path (or the file itself), in sorted order."""
    h = hashlib.sha256()
    files = [path] if path.is_file() else sorted(p for p in path.rglob("*") if p.is_file())
    for f in files:
        h.update(str(f.relative_to(path.parent)).encode())
        h.update(f.read_bytes())
    return h.hexdigest()[:12]


def main():
    dest = Path(__file__).resolve().parent / "out" / "brain"
    if dest.exists():
        shutil.rmtree(dest)  # only ever the demo's own scratch folder
    bootstrap.build_brain(dest)

    print("1. Built a sample brain from templates/ and dropped 3 emails in raw/:")
    for p in sorted((dest / "raw").iterdir()):
        print(f"     raw/{p.name}")

    before = {name: digest(dest / name) for name in PROTECTED}
    print("\n2. Fingerprints before filing (sha256, first 12 characters):")
    for name, value in before.items():
        print(f"     {name:<10} {value}")

    print("\n3. Ran the filing step (rules only, no model):")
    report = filer.file_brain(dest, FIXED_NOW)
    for ref in report["filed"]:
        print(f"     filed    {ref}")
    for ref, flags in report["flagged"]:
        print(f"     FLAGGED  {ref}  (matched: {', '.join(flags)})")

    after = {name: digest(dest / name) for name in PROTECTED}
    print("\n4. Fingerprints after filing:")
    unchanged = True
    for name, value in after.items():
        same = value == before[name]
        unchanged = unchanged and same
        print(f"     {name:<10} {value}  {'unchanged' if same else 'CHANGED'}")

    print("\n5. wiki/log.md now reads:")
    for line in (dest / "wiki" / "log.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("- "):
            print(f"     {line}")

    leaked = any("evil.test" in p.read_text(encoding="utf-8") for p in (dest / "wiki").rglob("*.md"))
    print(f"\n6. Injected address found anywhere in wiki/: {'YES' if leaked else 'no'}")

    if not unchanged or leaked:
        print("\nGUARDRAIL FAILURE")
        return 1
    print("\nGuardrails held. This proves the filing logic, not any language model.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
