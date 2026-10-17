# Chapter two: the folder

The folder is the brain. This chapter explains the layout, how to decide what goes where, and what must never go in at all.

> **Like you're five.**
> The notebook has sections, like tabs in a binder.
> One tab says who you are. One holds the things that just arrived.
> One holds the neat pages the assistant wrote about them.
> And on the very first page is a note that says: read this first, then go to the tabs.

## The layout

We use this exact tree everywhere in the repo.

```
brain/
  AGENTS.md            the first file every run reads; short, points to the rest
  about/
    me.md              who you are, what you are working on, who matters
    voice.md           how you write, with examples
  rules.md             one dated line per correction, newest first
  raw/                 everything that comes in, never edited
  wiki/
    index.md           the map; read before anything else in wiki/
    log.md             what was filed, when
    ...                one page per person, project or topic
  decisions/           one dated note per decision, with an empty Outcome
  pages/               morning pages and weekly reviews
  skills/              one folder per skill, each with a SKILL.md
  out/                 finished work
```

What each part is for:

- **`AGENTS.md`** is the entry point. It is short and it points at everything else.
- **`about/`** is slow facts about you, written by you (or drafted by the assistant and approved by you).
- **`rules.md`** is the list of corrections, newest first. Every run reads it before it does anything.
- **`raw/`** is the inbox archive. Things land here and are never changed afterwards.
- **`wiki/`** is the assistant's tidy version of what is in `raw/`: one page per person, project or topic, plus the map (`index.md`) and the diary (`log.md`).
- **`decisions/`** is where choices get written down with an Outcome section left empty, to be filled in later. See [chapter six](06-rules.md).
- **`pages/`** is where the morning page and weekly review are written.
- **`skills/`** holds saved procedures, one folder each.
- **`out/`** is finished work: drafts you approved, documents you sent.

## Why `AGENTS.md` is the entry point

`AGENTS.md` is an open file format for guiding coding agents, and its homepage lists many tools that read it [[32]](../SOURCES.md). Some tools read it natively [[24]](../SOURCES.md), some can be set to read it [[27]](../SOURCES.md), and at least one can read it in place of its own instructions file [[21]](../SOURCES.md). Pick it as the one place to write down how the brain works and you can swap tools without rewriting anything. The [adapters](../adapters/) show how each tool finds it.

Two habits keep this file useful:

1. **Keep it short.** At least one tool documents a default size cap on the combined instructions it will load, at 32 KiB [[24]](../SOURCES.md). A short file also leaves more of the model's attention for the task. `AGENTS.md` should say what the folder is, the order to read things in, and the few hard rules. It should point to everything else, not contain it.
2. **Remember that instructions are advice, not enforcement.** One tool's docs say plainly that these files are treated as context, not enforced configuration, and that a separate hook mechanism is the way to enforce something [[21]](../SOURCES.md). So anything dangerous must be blocked by permissions and connector settings, not just by a sentence in the file. [Chapter eight](08-what-breaks.md) comes back to this.

The template is in [`templates/AGENTS.md`](../templates/AGENTS.md).

## Slow facts and fast facts

This is the most important distinction in the folder.

- **Slow facts** rarely change: who your accountant is, how you sign emails, what a project is for. They live in files.
- **Fast facts** change constantly: today's meetings, whether an invoice is paid, a balance, a stock level. They stay in the app that owns them, and each run reads them live when it needs them [[1]](../SOURCES.md).

If you copy a fast fact into a file, you have created a second copy that goes wrong the moment the first one changes, and it will look just as confident as the right one. When a file must mention a fast fact, store a pointer instead ("check the calendar for this week's meetings") or store the value with a date and a note that it may be old. Per its README, one builder enforces exactly this with a linter: every stored fact must be timeless, dated, or a pointer [[36]](../SOURCES.md).

A quick test for any line you are about to write: "Will this still be true in three months?" If yes, it can go in a file. If no, point at the source.

## What never goes in the folder

The folder is plain text. It gets read by software, backed up, synced and sometimes shared. Treat it as something that could leak.

- **Passwords, keys and tokens.** Use a password manager. If a task needs a secret, the harness's own secret storage supplies it at run time, outside the folder.
- **Raw financial account numbers**, card numbers, government ID numbers and similar. Refer to accounts by nickname ("the main business account") and let the assistant ask you.
- **Other people's private details** that you have no reason to keep. Store what you need to work with them, nothing more.
- **Anything you could not stand to see in a log**, because the folder's contents will end up in logs and context windows.

Also decide early which parts of the folder are allowed to leave your machine. A folder that syncs to a cloud service, or that a cloud-run job copies, is in someone else's building. That may be fine. Just make it a choice.

## Starting small

You do not need every directory on day one. A good first version is `AGENTS.md`, `about/me.md`, `about/voice.md` and an empty `rules.md`. Add `raw/` and `wiki/` when you set up filing ([chapter three](03-filing.md)). Add `pages/` with the morning page ([chapter four](04-the-morning-page.md)). Add `skills/` when you have done a task enough times to save it ([chapter five](05-skills.md)).

## Keep it under version control

Even if you never share the folder, keep a history of changes. When the assistant rewrites a page badly, you want to roll back. When a rule turns out to be wrong, you want to see when it was added. A history also lets you review exactly what a scheduled job changed overnight, which becomes important in [chapter three](03-filing.md).

Done when: your folder matches the tree above, `AGENTS.md` fits on one screen, and a search of the whole folder for the words "password" and "account number" turns up no actual secrets.
