# Adapter: Codex and ChatGPT

How to run the brain on Codex (the coding agent) and ChatGPT (where scheduled tasks are managed). The same five questions are answered in the same order in every adapter. This is a snapshot of documentation that carries no dates, so check the live docs before relying on it.

## 1. Where does the instructions file go?

Codex builds its instructions from `AGENTS.md` files. It starts with a global file in `~/.codex`, then walks from the project root down to your current directory, taking one file per directory and joining them in that order [[24]](../SOURCES.md). When two files disagree, the one nearest your working directory wins, because it comes last in the combined text [[24]](../SOURCES.md). An `AGENTS.override.md` file takes priority over the plain one [[24]](../SOURCES.md). There is a default size cap of 32 KiB on the combined instructions, set by a `project_doc_max_bytes` setting [[24]](../SOURCES.md), so keep the file short.

Codex also keeps local memory files under `~/.codex/memories`, but the memories page says to keep required guidance in `AGENTS.md` or checked-in documentation [[24]](../SOURCES.md). The older docs address now redirects to the current docs site [[24]](../SOURCES.md).

## 2. Where does the folder live?

On your machine for desktop work, as a folder or repo with `AGENTS.md` at the root. For tasks that run on the web, the picture is different: web tasks use uploaded context and connected tools, and cannot work in a local folder [[25]](../SOURCES.md). If you want a web task to use the brain, you have to give it the files by upload. How best to keep a cloud copy in sync is not covered by the sources we checked; check the current docs.

## 3. What runs while the laptop is closed?

Scheduled tasks, with caveats. They are managed in the ChatGPT web or desktop app. The Codex command line and editor extensions do not provide that interface [[25]](../SOURCES.md). You create one by asking in plain language in a chat, then review it in the Scheduled tab [[26]](../SOURCES.md).

- Desktop local tasks need the machine awake with the app open whenever a task uses local files [[25]](../SOURCES.md).
- Web tasks use uploaded context and connected tools [[25]](../SOURCES.md), and connected-tools-only tasks can run on the web or in the cloud "when available" [[26]](../SOURCES.md).
- Team tasks run in the cloud under a service account [[25]](../SOURCES.md).

Our reading, which is an inference from those pages and not a stated guarantee: a laptop-closed job works only when it needs no local files. A minimum interval is not stated in the sources we checked.

## 4. How do mail and calendar connect?

Gmail and Google Calendar are connected under Plugins and used on each run. The walkthrough example is meeting briefs prepared from calendar events and related emails, linked back to their sources [[26]](../SOURCES.md). Whether a connector can be set to read-only is not covered by the sources we checked, so check the permission settings before you grant access. Read [chapter eight](../docs/08-what-breaks.md) first.

## 5. Where do skills go?

Codex documents skills built on the open Agent Skills standard [[31]](../SOURCES.md). In a scheduled task, a skill preserves the method, so the task repeats the same steps each run [[26]](../SOURCES.md). The exact folders where Codex looks for skills are not in our sources; check the current docs.

## Quick setup

- Keep `AGENTS.md` short and at the root of the folder.
- Decide which jobs genuinely need local files. Those need the desktop app running; the rest can be web tasks.
- Create each scheduled task by hand, one at a time, and read the Scheduled tab before you approve it ([chapter seven](../docs/07-one-paste.md)).
