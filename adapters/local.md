# Adapter: Local (open model)

How to run the brain with an open model on your own hardware. This is the setup with the most control and the least convenience, and it has one hard limit: it does not run while your computer is off. The same five questions are answered in the same order in every adapter. This is a snapshot of documentation that carries no dates, so check the live docs before relying on it.

## 1. Where does the instructions file go?

It depends on which agent program you run on top of the model. The Hugging Face docs show that a local model server can expose an OpenAI-compatible endpoint, and name several open agent programs that point at it, including Pi, OpenClaw, Hermes Agent, OpenCode and llama-agent [[30]](../SOURCES.md). Which instructions file each one loads is not covered by the sources we checked; check each program's docs. `AGENTS.md` is an open format that many tools read [[32]](../SOURCES.md), so it is the right file to try first. Then confirm, by asking the agent what it read, that yours is actually loaded.

## 2. Where does the folder live?

On your own disk. This is the best case for privacy: the folder, the model and the agent are all on a machine you control. According to the docs, one command fetches the model and then serves it through an OpenAI-compatible API on your own computer, and the example address is `localhost:8080` [[30]](../SOURCES.md). One of the agents, OpenClaw, includes local memory search using a local embedding model (a model that turns text into numbers so similar text can be found), and Hermes Agent points its session search at a local endpoint [[30]](../SOURCES.md). Treat memory search as a search aid. The files stay the source of truth.

Back the folder up and keep a version history ([chapter two](../docs/02-the-folder.md)). There is no vendor holding a copy for you.

## 3. What runs while the laptop is closed?

Nothing, unless you leave a machine on. Apple's archived docs say launchd is the preferred scheduler on macOS and cron is deprecated. A calendar-interval job that was missed during sleep runs when the machine wakes. If the machine stays off at the scheduled time, though, neither kind of job ever runs [[29]](../SOURCES.md). That page is archived and dated 2016, so check for newer guidance [[29]](../SOURCES.md). Linux and Windows schedulers are not covered by the sources we checked.

So local is the one setup in this repo that does not run with the laptop closed. Your options:

- **An always-on machine**, such as a small home server or a spare desktop that never sleeps [[29]](../SOURCES.md).
- **Keep-awake settings** on a laptop that stays plugged in. That is our suggestion, and a fragile one: the scheduler only fires while the machine is awake [[29]](../SOURCES.md).
- **Accept catch-up behaviour.** Jobs run when you open the lid. For a morning page, that may be fine: it is ready a few minutes after you wake the machine.

Because the job runs on your hardware, there is no vendor-set minimum interval to worry about, but the advice from [chapter three](../docs/03-filing.md) still applies: a few runs a day, not hourly.

## 4. How do mail and calendar connect?

Not covered by the sources we checked. The Hugging Face docs say llama-agent supports subagents and connector servers [[30]](../SOURCES.md), so a connector is possible in principle, but we have no confirmed mail or calendar connector to point to. Check each agent's docs. A local setup also lets you take a safer route: export mail to files on a schedule using a read-only tool you trust, drop the files into `raw/`, and let the agent never touch the mailbox at all. The agent then holds no mail credentials and cannot send mail. That removes the outbound leg of the lethal trifecta [[18]](../SOURCES.md) only if the agent also has no other way to reach the outside world (fetching URLs, calling outside services, opening links). The exported mail is still untrusted content, as [chapter eight](../docs/08-what-breaks.md) explains. This is our suggestion, not something the sources test.

## 5. Where do skills go?

Not covered by the sources we checked. Whether a given open agent loads `SKILL.md` folders is a question for that agent's docs. The skill format is an open specification [[31]](../SOURCES.md). If an agent does not load skills, you can still keep the same `skills/` folder and tell the agent in `AGENTS.md` to read the right `SKILL.md` when a task matches. That is the same method done by hand.

## Quick setup

- Start the local model server, then point one agent program at it.
- Put the template files in your folder and check the agent reads `AGENTS.md`.
- Decide how your scheduled jobs will survive the machine being off, and say which option you picked in `AGENTS.md`.
- Approve each scheduled job one at a time ([chapter seven](../docs/07-one-paste.md)).
