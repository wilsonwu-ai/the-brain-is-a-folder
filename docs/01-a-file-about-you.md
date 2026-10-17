# Chapter one: a file about you

Every run starts by reading who you are. Without that, the assistant writes like a stranger, because it is one. This chapter builds the two files that fix it: `about/me.md` and `about/voice.md`. The course this repo adapts starts in the same place, with a file built from your sent mail [[1]](../SOURCES.md).

> **Like you're five.**
> Before a new helper starts, you hand them a card.
> The first side says who you are and who matters to you.
> The second side says how you talk, with a few real things you have said.
> Now they can speak for you without sounding like a robot.

## What goes in each file

**`about/me.md`** holds slow facts: things that stay true for months.

- Who you are and what you do, in a few plain sentences.
- What you are working on right now, one line per project.
- The people who matter: name, relationship, and one line on how you work with them.
- Standing preferences: when you want to be interrupted, what you never want done on your behalf.
- Where to look for fast facts, as pointers: "check the calendar for today's meetings", not a copy of the meetings.

**`about/voice.md`** describes how you write.

- Typical length of a reply.
- How you open and how you sign off.
- Words and phrases you use, and ones you would never use.
- A few real examples, pasted in whole, with the situation each one answers.

Keep both files short enough to read in a minute or two. They are loaded often, and a long file competes with the task for the model's attention (see [chapter eight](08-what-breaks.md)).

## Path A: build them from your sent mail

This is the fastest route if you have a mailbox with a good history.

1. Pick a spread of your own sent emails. You want variety: a quick reply, a long explanation, a polite no, a hard message, a message to a stranger, a message to a close colleague. A couple of dozen is plenty; more adds length, not signal.
2. Remove anything private that is not needed: account numbers, passwords, other people's personal details. Never paste secrets into any chat.
3. Give the assistant the batch and ask it to describe patterns, not to copy sentences. Ask for length, openers, sign-offs, favourite phrases, and what you avoid.
4. Read the draft of `voice.md` out loud. If a line does not sound like you, strike it. You are the editor; the assistant is the note-taker.
5. Add three or four of the emails as verbatim examples at the bottom, each with a one-line note on when you would write like that.

Reading your mail for this purpose is a one-time job that you run by hand and supervise. It is not the scheduled filing job. Keep that separation: the first time you hand over mail, you are watching, and it only needs to read.

## Path B: build them by interview

No mailbox history, or you would rather not hand it over? Use an interview.

Tell the assistant to ask you one question at a time, wait for your answer, and only then ask the next one. One at a time matters: a list of many questions gets shallow answers. Good questions to cover:

- What do you do, in the way you would explain it at a dinner party?
- What are you working on this month?
- Who are the people you write to most, and what is each one like?
- Think of a message you were proud of. What made it good?
- What annoys you in other people's writing?
- What should the assistant never do without asking?

After the last answer, the assistant drafts both files and shows them to you. Edit before saving. [Chapter seven](07-one-paste.md) shows how this interview is built into the bootstrap prompt.

## A short example (an illustration, invented)

The names and content below are made up to show the effect. They are not from a real person.

Imagine the request: "Reply to Dana and say we need to move Thursday's meeting."

**Before** (no files, the assistant knows nothing about you):

> Dear Dana, I hope this message finds you well. I am writing to inform you that I will unfortunately be unable to attend our scheduled meeting on Thursday. Would it be possible to reschedule at a mutually convenient time? Kind regards.

**After** (the assistant has read `about/me.md` and `about/voice.md`):

> Hi Dana, Thursday has fallen apart on my side. Can we try Friday morning or early next week? Tell me what works and I will move things around. Thanks, Sam

The second version is shorter, uses the sign-off the person actually uses, and knows Dana is a colleague, not a client. Nothing clever happened. The assistant read a card.

## What not to put in these files

- Passwords, keys, tokens, or raw account numbers. Ever. If the assistant needs to know that a payment account exists, write "the business account, ask me for details", never the number. See [chapter two](02-the-folder.md).
- Anything that changes by the day. That is a fast fact and belongs at its source.
- Opinions about other people that you would not want read out loud. Assume anything in the folder could be seen by someone else someday.

## Keeping it alive

You will outgrow these files. Do not rewrite them from scratch. When the assistant gets your tone wrong, add a dated line to `rules.md` instead ([chapter six](06-rules.md)). Once a month, skim `about/me.md` and cross out whatever stopped being true. A stale card is worse than none, because the assistant trusts it.

Done when: a fresh run, given nothing but the folder, drafts a short reply that you would send with only a light edit, and neither file contains a secret.
