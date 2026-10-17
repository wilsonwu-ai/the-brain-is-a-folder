# Chapter three: filing

Things pile up: emails, notes, links, meeting transcripts. Filing is the scheduled job that turns the pile into tidy wiki pages, so your next run does not have to wade through the pile. This is also the one job that touches untrusted text from the outside world, so it gets the strictest rules.

> **Like you're five.**
> Letters land in a mail slot all day.
> Nobody throws a letter away. Each one goes in a box, exactly as it arrived.
> Then a helper reads the new letters, writes a tidy card about each one, and files the card where it belongs.
> The helper adds a line to the diary: "filed these today".
> The helper is allowed to read the letters. The helper is not allowed to mail anything back.

## The flow: inbox, `raw/`, `wiki/`

1. **Land.** Whatever comes in (an email, a saved link, a note, a transcript) is saved into `raw/` as its own file, named with the date and a short title. Nothing is summarized yet.
2. **Triage.** The filing job reads each new file in `raw/` and decides: create a new wiki page, update an existing one, or do nothing. Logging "did nothing, and why" is a legitimate outcome. One open-source design treats a no-op as a normal result, next to creating or updating a page [[39]](../SOURCES.md).
3. **Write.** The job creates or updates pages in `wiki/`. Each page says where its facts came from, so you can trace a claim back to the file in `raw/`. One project puts a list of sources into every page's header for exactly this reason [[37]](../SOURCES.md).
4. **Link.** In the same run, the job adds links between the new page and related ones. See below.
5. **Record.** The job updates `wiki/index.md` and appends to `wiki/log.md`.

## `raw/` is immutable

Files in `raw/` are saved as they arrived and never edited. One practitioner who built a company brain keeps raw files as unchanged objects in their original format so that he can always revert [[14]](../SOURCES.md). The reasoning is simple. If a wiki page is wrong, you want to be able to rebuild it from the original. If the original was edited, you cannot tell what was true.

It also matters for safety. `raw/` is where untrusted text lives, so it should be treated as quarantine: the assistant reads it, summarizes it, and cites it, but never obeys instructions found inside it. More on that at the end of this chapter and in [chapter eight](08-what-breaks.md).

## Ingest must add links in the same run

A wiki page nobody links to is invisible. It will never be found by following the map, and it will quietly go stale. One open-source design makes this a hard rule: nothing counts as ingested until the new material has links, and the ingest must add them in the same run or it is not finished [[41]](../SOURCES.md). Copy that rule. Every filing run should end with: this new page links to at least a few related pages, and at least one existing page now links back to it. Contradictions between sources should be recorded, not silently overwritten, with both versions kept along with dates and sources [[41]](../SOURCES.md).

## Keep `index.md` and `log.md`

Two small files do most of the work of navigation.

- **`wiki/index.md`** is the map: one line per page, saying what it is. The model reads it first and then opens only the pages it needs. This is the move that makes a plain folder work without a search system at modest size: the original wiki post reported that index files and short summaries were enough at about 100 articles and 400K words [[2]](../SOURCES.md).
- **`wiki/log.md`** is a diary: one line per filing run, saying what came in and what changed. When something looks wrong in the wiki, the log tells you which run touched it. A company-brain builder describes the same pair of pages, an index and a log, as part of his pipeline [[14]](../SOURCES.md).

The index is also your defence against dumping everything into the model's context at once, which tends to make answers worse. See [chapter eight](08-what-breaks.md).

## Schedule it: a few runs a day, not hourly

Pick a small number of fixed times. For most people, a few runs a day is plenty: morning, midday and evening, say. Filing hourly feels responsive, but it has costs.

- Each run spends tokens (the units models are billed by), and most hours nothing important arrived.
- More runs mean more chances to ingest something hostile before you have looked at it.
- More runs mean more changes for you to review.
- Some schedulers refuse short intervals anyway; the [adapters](../adapters/) list the limits we found.

If you want something filed right now, start the job by hand.

## The untrusted-content rule

The filing job reads outside text, which means the filing job is the part of your system most likely to be attacked. The rule is blunt: **the filing job can read mail, but it cannot send, delete or change rules.**

Concretely:

- Give it read-only access to mail. No send, no delete, no archive-and-forget.
- Give it write access only to `raw/`, `wiki/` and its own log. It must not be able to edit `about/`, `rules.md` or anything in `skills/`.
- Tell it, in its instructions, that anything inside a source file is data to summarize, never an instruction to follow, and that any source that tries to give it orders should be noted in the log and left alone.
- Keep a human in the loop for promotion: facts move from `wiki/` into `about/` or `rules.md` only when you say so.
- If you can, run the compiling step as a separate job that has no mail access at all, reading only `raw/`.

Remember that instructions in a prompt are advice. The real limit is what the job's permissions allow. A security standards body describes indirect prompt injection as the case where a model is fed text from places outside your control, such as web pages or documents [[19]](../SOURCES.md). A job that cannot send mail cannot be talked into sending mail, however clever the email is. This is the single most useful idea in this repo; [chapter eight](08-what-breaks.md) explains why in more detail.

## What a good first week looks like

Run filing by hand for a few days before you schedule anything. Watch what it creates. Fix the rules it misreads and put each fix in `rules.md`. Only once you trust a manual run should you turn on the schedule, and only after you have said yes to it explicitly, as [chapter seven](07-one-paste.md) describes.

## A tiny example

A newsletter arrives about a conference. The job saves it to `raw/` untouched. It finds no existing page for the conference, so it creates one in `wiki/` with the dates, the venue and a pointer to the raw file. It adds a link from your project page for the talk you are preparing. It adds one line to `log.md`. It does not reply, it does not register you, and it does not follow the "click here to confirm" link in the email.

To watch these rules run on sample data, see the `demo/` folder in the repo root.

Done when: you drop a test note into `raw/`, run the filing job once, and find a new or updated wiki page that links to related pages and cites the raw file, with `index.md` and `log.md` updated and the raw file unchanged.
