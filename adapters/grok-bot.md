# Adapter: Grok Bot

How to run the brain on Grok Bot. The same five questions are answered in the same order in every adapter. This adapter is thin on purpose. Beyond the vendor's own Grok Bot 101 guide [[28]](../SOURCES.md) and the course this repo adapts [[1]](../SOURCES.md), our sources say little, and we would rather say so than guess.

> **About the evidence.** The guide is a vendor page, not reference documentation. When we checked, the product's main page returned an access error, and the guide's index lists titles only [[28]](../SOURCES.md). The course is promotional for this product [[1]](../SOURCES.md). Read both with that in mind, and check the current docs.

## 1. Where does the instructions file go?

Not in our sources. The guide we read does not describe an always-loaded instructions file, so we cannot say whether `AGENTS.md` is read natively [[28]](../SOURCES.md). A safe approach, which is our suggestion and not a documented feature, is to write in your first message or in the bot's own setup text: "Read `AGENTS.md` in the brain folder before every task." Then test that it does.

## 2. Where does the folder live?

The guide says a bot runs on a cloud computer with a filesystem [[28]](../SOURCES.md). So the folder would live on that cloud computer, not on your laptop. The course this repo adapts argues the same thing: the brain belongs in files on that computer, not in the bot's chat memory, which holds only condensed notes of past work [[1]](../SOURCES.md). How the filesystem persists between runs, how you back it up, and how you copy files in and out are not covered by the sources we checked; check the current docs. Whatever you choose, keep your own copy of the folder somewhere you control, since the folder is the asset.

## 3. What runs while the laptop is closed?

The guide says a bot can run on its own schedule or listen for event triggers, and it runs on that cloud computer [[28]](../SOURCES.md). That is the strongest fit in this repo for the laptop-closed requirement. Minimum intervals, run limits and costs are not covered by the sources we checked; check the current docs. The popular builds that run only while a note-taking app stays open on a laptop are the contrast the course draws [[1]](../SOURCES.md). A public demo of the idea running on this product indexes saved videos into a wiki-style Markdown index [[5]](../SOURCES.md).

## 4. How do mail and calendar connect?

The guide lists Gmail, Google Calendar and Drive among the accounts a bot can connect [[28]](../SOURCES.md). Whether a connection can be read-only, and whether runs may use connected tools without asking each time, is not covered by the sources we checked. Ask before you connect, and read [chapter eight](../docs/08-what-breaks.md): a bot that runs on its own, reads your mail and can act is the exact setup the lethal-trifecta warning is about [[18]](../SOURCES.md).

## 5. Where do skills go?

The guide says the bot supports the same connector servers, plugins and skills as another popular coding tool [[28]](../SOURCES.md). That suggests the `SKILL.md` folder shape from [chapter five](../docs/05-skills.md) should carry over, but we have not confirmed it, and the folder where skills are placed is not in our sources. Check the current docs.

## Quick setup

- Create a folder on the bot's computer using the layout in [chapter two](../docs/02-the-folder.md), and keep your own copy elsewhere.
- Paste the [bootstrap prompt](../templates/bootstrap-prompt.md) and answer the interview.
- Ask the bot to show you every schedule it proposes. Approve one at a time ([chapter seven](../docs/07-one-paste.md)), and do not connect mail until you have decided what it may do with it.
