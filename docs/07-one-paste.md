# Chapter seven: one paste

You do not have to build the folder by hand. This chapter shows how to bootstrap the whole brain with one message, and states the one rule that protects you while it happens: no scheduled job is switched on until you say yes to it.

> **Like you're five.**
> Imagine handing your new helper a single sheet that says: set up my notebook, ask me what you need to know, and show me the plan.
> The helper builds the binder, asks you questions one at a time, and writes the first pages.
> Then it says, "I would like to set an alarm clock to do this each day. Is that okay?"
> And it waits for you to say yes. The alarm clock never goes off until you do.

## What the paste does

The file [`templates/bootstrap-prompt.md`](../templates/bootstrap-prompt.md) is a single message you paste into your assistant, in whichever tool you use. It tells the assistant to:

- Create the folder tree from [chapter two](02-the-folder.md), using the files in `templates/` as starting points.
- Interview you, one question at a time, to draft `about/me.md` and `about/voice.md` ([chapter one](01-a-file-about-you.md)), or to read a batch of your sent emails if you prefer.
- Write a short `AGENTS.md` that points at everything else.
- Create an empty `rules.md`, an empty `wiki/index.md` and `wiki/log.md`, and a first morning-page template.
- Show you what it made, and ask you to correct it.
- Propose, but not create, the scheduled jobs: filing ([chapter three](03-filing.md)), the morning page ([chapter four](04-the-morning-page.md)), the weekly review and health check ([chapter six](06-rules.md)).

The prompt is meant to be edited. Read it first. Change the names, remove anything that does not fit, and add anything you care about. It is plain text, and you are the author of how your brain works.

## The rule: every scheduled job waits for your yes

This is the part to take seriously. A scheduled job is a run with no one watching, and it can touch real accounts. So the bootstrap prompt is built around one hard rule: **the assistant may propose a job, but it may not switch one on until you have said yes to that specific job.**

For each job, the assistant should show you, in plain words:

- **What it does**, in a sentence.
- **When it runs**, and how often.
- **What it can read**: which folders, which connectors.
- **What it can write**: which folders, and whether it can create drafts.
- **What it cannot do**: send, delete, edit `about/` or `rules.md`.
- **How to turn it off.**

Then it waits. A vague "yes, go ahead with everything" is not enough; approve jobs one at a time so you know what each one is allowed to do. If a job needs more permission than it listed, it asks again.

The reason is the same one as in [chapter three](03-filing.md): the assistant's instructions are advice, while permissions are the real limit. Check the permissions on the connector or scheduler itself, not only the wording of the prompt.

## Order of operations

A sensible order for your first sitting:

- **Paste and answer.** Let the assistant build the folder and interview you. Edit what it writes.
- **Run by hand.** Drop a few notes into `raw/` and run filing once, by hand, watching. Fix what it gets wrong, and record each fix as a dated line in `rules.md`.
- **Generate one morning page by hand.** Read it. Correct it.
- **Switch on filing**, read-only on mail, on a small number of runs a day.
- **A few days later, switch on the morning page.**
- **Later still**, the weekly review and health check.

Take your time. A brain that works is built over weeks. There is no prize for turning everything on in one afternoon, and a good chance of a mess.

## Where the paste goes

Any tool that can read and write files in a folder will do. Where the folder lives, where the instructions file goes, how scheduled jobs are created and how mail connects differ between tools. Those details are in the [adapters](../adapters/), one file per tool, each answering the same five questions in the same order. Pick the adapter that matches your setup, follow its notes, then paste.

## What can go wrong during bootstrap

- **The assistant writes your voice file from too little evidence.** Give it more emails, or edit by hand.
- **It invents facts about you to fill gaps.** Read `about/me.md` line by line before saving it. Delete anything you did not say.
- **It tries to turn everything on at once.** That is the situation the rule above exists for. Say no and go one job at a time.
- **It asks for broad access "to be safe".** Offer the smallest access that does the job, and widen it later if you must.

## If you want to start over

Because the brain is a folder under version control ([chapter two](02-the-folder.md)), you can always roll back. The scheduled jobs are the only things outside the folder: list them, and switch them off before you restart.

Done when: the folder exists with the template files filled in by you, you have read the bootstrap prompt before using it, and no scheduled job is running that you did not individually approve.
