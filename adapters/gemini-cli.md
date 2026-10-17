# Adapter: Gemini CLI

How to run the brain on Gemini CLI. The same five questions are answered in the same order in every adapter. This adapter has the most gaps, because the sources we checked do not cover scheduling at all. This is a snapshot of documentation that carries no dates, so check the live docs before relying on it.

> **A warning first.** A banner on the Gemini CLI docs says the tool was replaced by Antigravity CLI for unpaid-tier and Google One users on 18 June 2026, so the pages we read may not match the product you have [[27]](../SOURCES.md). Check which tool you are actually running.

## 1. Where does the instructions file go?

The tool reads `GEMINI.md` files and joins them on every prompt: a global file in `~/.gemini`, files in your workspace and its parent directories, and files found just in time as it works [[27]](../SOURCES.md). A file can pull in others with `@file.md` imports, and the `/memory show` and `/memory reload` commands let you see and refresh what is loaded [[27]](../SOURCES.md).

To use the shared entry point, set the `context.fileName` property to a list of names. The docs' own example is a list containing `AGENTS.md`, `CONTEXT.md` and `GEMINI.md`, and `GEMINI.md` is the default name [[27]](../SOURCES.md). So either list `AGENTS.md` in that setting, or keep a short `GEMINI.md` that imports it with `@AGENTS.md`.

## 2. Where does the folder live?

Anywhere in your workspace, as plain files, with `AGENTS.md` at the root and the setting above. The docs we read describe workspace and parent-directory files [[27]](../SOURCES.md). A cloud location for the folder is not covered by the sources we checked; check the current docs.

## 3. What runs while the laptop is closed?

Not covered by the sources we checked; check the current docs. We found no scheduler documentation for Gemini CLI, and the extensions page, which lists what an extension can package, does not mention scheduling [[27]](../SOURCES.md).

What that means in practice: until you find an official scheduler, treat this tool as one you run by hand or on a machine you control. If you wire it to a system scheduler on your own computer, you inherit the limits in the [local adapter](local.md). In particular, a computer that is off does not run the job [[29]](../SOURCES.md). Do not assume it works with the lid closed.

## 4. How do mail and calendar connect?

The extensions page says an extension can package prompts, MCP servers (a standard way to connect outside tools), custom commands, themes, hooks, sub-agents and agent skills [[27]](../SOURCES.md). So a connector server could arrive through an extension. Which mail and calendar connectors exist, and whether they can be made read-only, is not covered by the sources we checked; check the current docs. The caution in [chapter eight](../docs/08-what-breaks.md) applies in full: grant read access only.

## 5. Where do skills go?

The Gemini CLI skills page documents skills that are based on the open Agent Skills standard, and it documents a `~/.agents/skills` alias [[31]](../SOURCES.md). A folder per skill with a `SKILL.md` inside, as in [chapter five](../docs/05-skills.md), is the shape to use. Where the tool discovers workspace-level skills is not in our sources; check the current docs.

## Quick setup

- Confirm which tool you are on, given the banner above.
- Put `AGENTS.md` at the root and list it in `context.fileName`, or import it from `GEMINI.md`.
- Run filing and the morning page by hand. Do not schedule anything until you have confirmed, from the current docs, how scheduling works and what it is allowed to do ([chapter seven](../docs/07-one-paste.md)).
