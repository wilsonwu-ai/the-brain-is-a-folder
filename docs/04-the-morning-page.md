# Chapter four: the morning page

The morning page is the one thing you actually read. A scheduled job builds it overnight from the wiki and from live apps, and it lands in `pages/` before you sit down. The course this repo adapts has a morning page too [[1]](../SOURCES.md). Ours has a stricter shape, designed so you can tell what is solid from what is a guess.

> **Like you're five.**
> Each morning a helper leaves a single sheet of paper on your desk.
> The top half says: here is what I know for sure.
> Next: here is what I am guessing.
> Then: here is what I already did, and here is what is waiting for your yes.
> The bottom says: here are the things I could not figure out.
> You can read the whole sheet over a cup of tea.

## One page, five sections

The page has exactly these sections, in this order. Fixed headings make it easy to skim, and easy to check by machine.

**Facts.** Things the job read from a source of truth in this run, each with where it came from: today's meetings from the calendar, an unpaid invoice from the accounting app, a reply received. These are fast facts, so they are fetched live and never copied from an old page [[1]](../SOURCES.md). If the job cannot reach the source, it says so here instead of filling the gap from memory.

**Guesses.** Anything inferred. "Dana probably wants Friday because she mentioned travel." "This thread looks urgent." Each guess is labelled as a guess and says what it is based on. This section exists because a model writes a guess in the same confident voice as a fact. Labelling is the only defence.

**Done.** What the job did on its own, and where the result is. Filed three notes and updated two pages. Built this page. Created drafts. This section should be dull. If it is long, the job is doing too much unsupervised.

**Waiting for your approval.** Everything that needs a human yes. Drafted replies (never sent), proposed changes to `about/` or `rules.md`, proposed new skills, proposed scheduled jobs. Each item is one line plus a link, and you answer by editing the page or telling the assistant. Nothing in this section happens until you approve it. That is the point of the section.

**Open questions.** What the job could not work out and wants to know. "Two notes mention a Q-something budget but I cannot find which; which one is current?" Questions are cheap, and answering one often becomes a new line in `rules.md`.

## The attention list

Underneath the five sections, add a short attention list: the handful of people, projects or threads that deserve your attention today. Rebuild it every run from what you touched, not from a fixed list you maintain by hand.

Good signals to build it from:

- Threads you replied to recently.
- Pages in the wiki you opened or edited.
- Decisions with an empty Outcome that are getting old.
- Items waiting on someone else for a long time.

The list is a suggestion, not a to-do list. It is allowed to be wrong, and your corrections feed `rules.md`.

## Keep it to one page

If the page gets long, you will stop reading it, and then the brain is feeding no one. Give the job a ceiling on length. If there is more to say, link to detail instead of pasting it. Prefer short lines over paragraphs. Put the approvals near the top of your attention by keeping everything above them tight.

A weekly review uses the same shape on a longer timescale and is covered in [chapter six](06-rules.md).

## How the job runs

The morning page job is separate from the filing job ([chapter three](03-filing.md)). It reads three kinds of input:

- `about/` and `rules.md`, always first.
- `wiki/index.md` and the pages it points to, for slow facts and the state of projects.
- Live reads from apps, for fast facts.

It writes one file: today's page in `pages/`. That is deliberate. A job whose only output is a file can be inspected and rolled back. If it also needs to create drafts, give it permission to create drafts only, never to send. Draft folders are reviewed by you.

Schedule it to finish before you wake up, with a little slack. If a source is down, the page should still appear, with that section marked "could not read".

## A short example (an illustration, invented)

```
Facts
- Calendar: two meetings today, the first at mid-morning with Dana. (source: calendar, read this run)
- Invoice for the print job is still unpaid. (source: accounting app, read this run)

Guesses
- Dana may want to move the Friday check-in; her last note mentioned travel. (basis: wiki/people/dana.md)

Done
- Filed four new notes. Updated the print-job page. Drafted a reply to Dana.

Waiting for your approval
- Send the draft reply to Dana? (draft waiting in your mail drafts)
- Add a rule: "Never schedule anything before mid-morning"? (seen in two corrections)

Open questions
- Which of the two budget notes is current?
```

Notice that nothing in Done or Waiting has been sent anywhere. Notice, too, that the facts name their source.

## Why the sections matter

A brain you cannot check is a brain you will eventually stop trusting. Splitting facts from guesses makes errors easy to spot. A fixed list of approvals makes it hard for an action to slip through. And the open-questions section turns the assistant's confusion into your next improvement.

Done when: tomorrow morning there is a page in `pages/` with all five sections, the facts name their sources, nothing has been sent on your behalf, and you read it in a few minutes.
