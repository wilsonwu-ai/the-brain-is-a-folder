# Chapter six: rules

The brain gets better only if corrections stick. `rules.md` is where they stick. This chapter covers how to write rules, the weekly review that keeps your decisions from vanishing, and the health checks that keep the wiki honest.

> **Like you're five.**
> Every time the helper makes a mistake, you write one line on a sticky note with today's date.
> The notes go on a board that the helper reads before doing anything.
> Once a week you and the helper look at the board together.
> Notes that are old and wrong come down. Notes that matter stay.

## `rules.md`: one dated line per correction

The pattern is simple. When the assistant gets something wrong, you do not only fix that output. You add one line to `rules.md`, with the date, and every run reads that file before it begins. One builder describes the same pattern as a rulings folder where each correction becomes one dated line and every run reads it before drafting [[13]](../SOURCES.md). In that design the assistant reads the hub pages first, then searches the rulings, then drafts [[13]](../SOURCES.md).

Keep the file in this shape:

- **Newest first**, so the freshest correction is read first.
- **One line each.** If a rule needs a paragraph, it is two rules, or it belongs in a skill.
- **A date on every line**, in the same format, so you can find and retire old ones.
- **Say what to do, not only what not to do.** "Greet clients by first name" beats "stop being so formal".
- **Include the scope** when it is narrow: "In replies to suppliers, ...".

Example lines (invented, to show the format):

```
YYYY-MM-DD  In replies to suppliers, quote the order number in the first line.
YYYY-MM-DD  Never schedule meetings before mid-morning.
YYYY-MM-DD  Sign short replies with first name only.
```

Who writes the rules? You decide. The assistant may propose a line, and the morning page is a good place for that proposal, but a rule changes how every future run behaves, so a human approves each one.

## Rules are read by every run

Both the filing job and the morning-page job read `rules.md`, along with `about/`, before they do anything else. That is why rules are powerful, and also why they are a target. If a hostile email could talk the assistant into adding a rule, that email would steer every later run. This is the reason the filing job must not be able to edit `rules.md` ([chapter three](03-filing.md)), and why a human promotes anything into it ([chapter eight](08-what-breaks.md)).

## Decision notes with an empty Outcome

For any real choice, write one short note in `decisions/`: the date, what you decided, why, what you expected, and an **Outcome section left empty**. The empty section is the useful part. It is a promise to come back.

A decision note is cheap to write and expensive to reconstruct later. The template is in [`templates/decisions/TEMPLATE.md`](../templates/decisions/TEMPLATE.md).

## The weekly review

Once a week, a scheduled job builds a review page in `pages/`, using the same fixed shape as the morning page ([chapter four](04-the-morning-page.md)). Its special job is to surface decisions you made and forgot. It should list:

- **Decisions with an empty Outcome** that are old enough to check, oldest first, each with a link.
- **Rules added this week**, so you can spot ones that conflict or were too broad.
- **Rules that never mattered**, if you can tell, as candidates to retire.
- **Wiki pages not touched in a long time** that still claim to be current.
- **Open questions** that have been open all week.

You spend a short sitting going through it. For each old decision, fill in the Outcome in a line or two: what actually happened, and whether you would decide the same way again. If a pattern shows up, turn it into a rule. This is a human-sized version of what the research literature calls reflection: agents synthesizing memories over time into higher-level insights that guide later behaviour [[9]](../SOURCES.md). You are the reflecting part; the job just brings the material.

## Health checks: lint the wiki

A wiki that is only ever added to will rot. Run a health check (programmers call it a lint, after the tool that catches errors in code) on a schedule, weekly or so. The idea is old in this space: the original wiki post describes running health checks over the wiki to find inconsistent data and suggest new connections [[2]](../SOURCES.md). A company-brain builder built a lint skill that finds duplicates and orphans [[14]](../SOURCES.md).

What your health check should look for:

- **Duplicates.** Two pages about the same person or project. Propose a merge; do not merge silently.
- **Orphans.** Pages with no links pointing to them, which means they will never be found. Propose links, or propose deletion.
- **Stale claims.** Statements that were true once. Per its README, one builder's rule is that every stored fact is timeless, dated, or a pointer, so a bare status or count cannot sit in a page unmarked [[36]](../SOURCES.md). Another project stamps each checked claim with a last-verified date [[40]](../SOURCES.md).
- **Contradictions.** Two pages that disagree. Keep both with dates and sources until you resolve them.
- **Broken links and missing sources.**
- **Rules that conflict** with each other.

The health check reports; it does not fix. Its output goes to the weekly review, and you approve the fixes. The same permission rules apply as for filing: the job may write a report, and may not change `about/` or `rules.md`.

## Keeping `rules.md` from growing forever

Prune it during the weekly review. Merge near-duplicates. Move a rule that applies to one task into that task's skill. Retire rules that no longer apply, and note the retirement in `pages/` so the history is not lost. A long list of rules is read on every run, and a long input has its own cost; see [chapter eight](08-what-breaks.md).

## The loop

Together, these form a loop: a run gets something wrong, you add a dated line, every run reads it first, and once a week you review what the system has been doing and clean it up. That loop is the real asset. The model reading it can change; the loop keeps getting better.

Done when: `rules.md` has at least a few dated lines, a decision note exists with an empty Outcome, and you have run one weekly review and one health check and acted on what they reported.
