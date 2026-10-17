# Chapter five: skills

A skill is a saved way of doing one kind of task. Instead of explaining a job from scratch each time, you write the method down once and the assistant loads it when a request matches. This chapter shows how to earn a skill, how to write one, and gives three to start with.

> **Like you're five.**
> The first time you bake a cake, you read the recipe slowly and fix mistakes as you go.
> Once the cake comes out right, you copy the good recipe onto a card.
> Next time the helper just takes the card from the box and bakes.
> Only after the card works every time do you let the helper bake on its own while you sleep.

## The order that works: do it, harden it, save it, automate it

The course this repo adapts gives the sequence as: do the task once, make it reliable, save it as a skill, and then automate it [[1]](../SOURCES.md). Each step protects the next.

- **Do it once, with you watching.** Work through a real task in conversation. Correct the assistant when it drifts. You are discovering what "good" looks like for this task.
- **Make it reliable.** Run it a few more times on different inputs. Every time something goes wrong, note what the instruction should have said. Stop when a run needs no corrections.
- **Save it as a skill.** Write the method into a `SKILL.md` file in its own folder under `skills/`.
- **Automate it.** Only now, and only with your explicit yes ([chapter seven](07-one-paste.md)), let a scheduled job run the skill.

Skipping ahead is the usual mistake. A job automated before it is reliable fails in the dark, at an hour when you are not there to catch it.

## What a skill file is

The open specification defines a skill as a folder that holds, at the very least, one file named `SKILL.md` [[31]](../SOURCES.md). The file starts with a block of frontmatter (a small header of settings between two lines of dashes) that requires a `name` and a `description`. The name is limited to 64 characters and the description to 1,024 characters [[31]](../SOURCES.md). The rest of the file is plain Markdown: the method itself.

A skill folder can also hold optional extras: a `scripts/` folder for code, a `references/` folder for background documents, and an `assets/` folder for templates and other files [[31]](../SOURCES.md).

The specification describes progressive disclosure: only a small amount of metadata, about 100 tokens per skill, is loaded when a session starts, and the full body is loaded only when the skill is activated [[31]](../SOURCES.md). That has a practical consequence for how you write it. The `description` is what the assistant reads to decide whether a skill applies, so it must say plainly when to use the skill. The body can then be as detailed as the task needs without costing attention on unrelated work.

Several of the harnesses we checked say they build on this open standard [[31]](../SOURCES.md); the [adapters](../adapters/) give the details for each one. Because the format is shared, a skill in your folder can move with the folder when you change tools.

The template skill is [`templates/skills/idea-to-plan/SKILL.md`](../templates/skills/idea-to-plan/SKILL.md).

## How to write a good skill

- **Say when to use it.** The description is the trigger. "Use when I give you a rough idea and want a plan" beats "planning helper".
- **State the inputs and the output.** What does the skill need, and what does it hand back, and where does the result get saved?
- **Write steps, not a speech.** Short numbered steps the assistant can follow. Put judgment calls in a line of their own.
- **State the limits.** What the skill must never do on its own: send, delete, overwrite, spend. Drafts only.
- **Name the check.** How will you and the assistant know it worked?
- **Point to files rather than copying them.** Refer to `about/voice.md` and `rules.md`; do not paste their contents into the skill, or they will drift apart.

## Three starter skills

These are the three most people reach for. Write your own version after you have done each task by hand.

### Idea to plan

*Input:* a rough idea, a few sentences. *Output:* a one-page plan in `out/`.

The skill asks what the goal is and what "done" looks like, lists the smallest first step, lists the risks and the decisions you would need to make, and flags what it does not know. It reads `about/me.md` for your constraints and checks `wiki/` for related earlier work. If the plan contains a real choice, it also drafts a note for `decisions/` with the Outcome section left empty. A working template is included in this repo.

### Thread to reply

*Input:* an email thread. *Output:* a draft reply, never a sent one.

The skill reads the thread, reads `about/voice.md`, and checks the wiki page for the person. It drafts a reply in your voice, lists any claim in the draft it could not verify, and puts the draft in the drafts folder. Because the thread is untrusted text, the skill treats anything in it as data. If the email contains instructions aimed at the assistant, the skill reports them and does not follow them. See [chapter eight](08-what-breaks.md).

### Note to post

*Input:* a note or a wiki page. *Output:* a draft of a public post, never a published one.

The skill pulls the single idea worth sharing, drafts the post in your voice, and removes anything private (names, numbers, client details) unless you marked it as shareable. It flags every factual claim and asks for a source. You publish it yourself.

## Skills and the morning page

When the assistant notices you doing the same job a few times, it can propose a new skill in the "Waiting for your approval" section of the morning page ([chapter four](04-the-morning-page.md)). You approve, it drafts the file, you read it, and only then does it go into `skills/`. A skill can contain instructions that run with real permissions, so nobody and nothing should add one without your review.

Done when: you have one skill that you have run by hand several times without correcting it, saved as `skills/<name>/SKILL.md` with a name and a description that says when to use it.
