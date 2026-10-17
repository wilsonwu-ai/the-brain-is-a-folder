# Adapter: Claude Code

How to run the brain on Claude Code. The same five questions are answered in the same order in every adapter. This is a snapshot of documentation that carries no dates, so check the live docs before relying on it.

## 1. Where does the instructions file go?

Claude Code loads a file called `CLAUDE.md` at the start of every session [[21]](../SOURCES.md). The docs also say it can read a repo's `AGENTS.md` in place of `CLAUDE.md` [[21]](../SOURCES.md), so the template `AGENTS.md` can sit at the root of your folder as the one entry point. If you want to be safe, our suggestion (not from the docs) is to add a short `CLAUDE.md` that tells the assistant to read `AGENTS.md`.

Two cautions from the same docs. The files are treated as context, not as enforced configuration; the docs point to a hook mechanism for enforcement [[21]](../SOURCES.md). And Claude Code keeps a separate auto-memory that it writes itself, of which the first 200 lines or 25KB load each session [[21]](../SOURCES.md). Treat that as a convenience. The folder is the source of truth.

## 2. Where does the folder live?

Make it a repository. This matters for scheduled work: routines clone repos fresh on each run and have no access to your local files [[22]](../SOURCES.md). Anything a routine needs must therefore be committed to the repo it clones. Keep the repo private, and review [chapter two](../docs/02-the-folder.md) on what never goes in the folder.

## 3. What runs while the laptop is closed?

Routines. The docs describe them as running on Anthropic-managed cloud infrastructure, so work continues even with your laptop shut, and they can be started by a schedule, an API call or a GitHub event [[22]](../SOURCES.md). The limits we found:

- The feature is labelled a research preview, so details may change [[22]](../SOURCES.md).
- The minimum schedule interval is one hour [[22]](../SOURCES.md). That fits the "few runs a day" advice in [chapter three](../docs/03-filing.md) comfortably.
- You create them with the `/schedule` command or on the routines page of the web app [[22]](../SOURCES.md).
- Included connectors can perform writes without asking permission on each call [[22]](../SOURCES.md). That is the reason to grant the filing job read-only access and to read [chapter eight](../docs/08-what-breaks.md).

Whether Claude Code's desktop app offers a separate local scheduler that works with the lid closed is not covered by the sources we checked; check the current docs.

## 4. How do mail and calendar connect?

Gmail and Google Calendar reach Claude Code through hosted connectors rather than local sign-in. Once you connect them in the web app they appear in Claude Code automatically [[23]](../SOURCES.md). The docs also let you configure other connector servers at local, project or user scope, with project scope stored in a `.mcp.json` file [[23]](../SOURCES.md).

For routines specifically, local servers do not appear. Use hosted connectors, or commit a `.mcp.json` to the repo [[22]](../SOURCES.md).

## 5. Where do skills go?

Skills follow the open Agent Skills standard [[31]](../SOURCES.md): a folder per skill with a `SKILL.md` inside. Routines use skills that are committed to the repository [[22]](../SOURCES.md), so keep them in `skills/` in your folder. The exact folders where Claude Code discovers skills are not in our sources; check the current docs, and copy or link the folders there if needed.

## Quick setup

- Put the folder in a private repo with `AGENTS.md` at the root.
- Connect mail and calendar as hosted connectors, read-only where the connector lets you choose.
- Run each job by hand first. Then create a routine for each, one at a time, with a yes from you each time ([chapter seven](../docs/07-one-paste.md)).
