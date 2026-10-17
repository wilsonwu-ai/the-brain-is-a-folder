# Chapter eight: what breaks

The course this repo adapts is a good build guide. It does not cover what goes wrong over time. This chapter does. It is the longest chapter on purpose, because an always-on assistant wired to your mail is a real system with real failure modes.

> **Like you're five.**
> A notebook is only good while you can still find things in it.
> If it grows too fat, the helper flips pages forever and misses the one that matters.
> If nobody tidies it, old notes sit there pretending to be true.
> And if a stranger can slip a note into the pile, the helper might do what the stranger's note says.

## Failure one: context rot

Context is the text a model can see at one time. It sounds as if more context must be better. It is not. A published study that tested 18 language models found that performance consistently degrades as input length grows, even on simple tasks [[10]](../SOURCES.md). An earlier academic paper found that accuracy falls when the relevant information sits in the middle of a long input, even for models built for long inputs [[11]](../SOURCES.md).

An AI lab's engineering guidance says something compatible: recall declines as the amount of context grows, and a good counter is structured note-taking, where the agent regularly writes notes that persist outside the context window and pulls them back later [[12]](../SOURCES.md). That is, in effect, this whole repo.

**What this means for the folder.**

- Do not paste the entire wiki into every run. Give the model the map (`index.md`) and let it open only the pages it needs. The original wiki post got by on index files and short summaries at about 100 articles and 400K words [[2]](../SOURCES.md), and a company-brain builder uses an index page and links so the agent does not crawl blindly [[14]](../SOURCES.md).
- Keep `AGENTS.md`, `about/` and `rules.md` short. They are loaded every run.
- Prune. A rule or a page that no longer earns its place is costing attention.

## Failure two: scale and cost

Index-first worked at the size one person reached, and he described it as a small scale [[2]](../SOURCES.md). Our sources do not show it still working far beyond that size. What we do have:

- A practitioner warns that agents navigate large folders by brute force, which costs a lot of tokens (the units models are billed by) and can miss critical information, and that the problem grows because knowledge work keeps adding new information [[14]](../SOURCES.md).
- A vendor post argues that compiling a wiki straight from raw sources breaks down at larger volumes, through token cost, duplication, conflicting information and poisoned data. The author promotes his own open-source fix, so this is a self-interested and unverified claim, and the post had low reach [[15]](../SOURCES.md).

Honest takeaway: expect a point where the simple folder strains. Signs are slow runs, rising cost, and answers that miss pages you know exist. When that happens, the fixes are structural: merge duplicates, split huge pages, tighten the index, archive what you no longer use. Some of the projects in the [prior-art table](../README.md#prior-art-worth-stealing) add search or a database for bigger stores; that is a decision for later, not day one. The same practitioner who built a company brain called the payoff unproven after one week of use and planned tests against simply dropping raw files into an assistant [[14]](../SOURCES.md). Measure yours too.

## Failure three: staleness and upkeep

Notes rot. The gist behind this wave of projects says people abandon wikis because the upkeep grows faster than the value, and proposes that the model absorb the upkeep. That is the author's assertion, not a measured result [[3]](../SOURCES.md). A promotional post goes the other way: building this by hand means wiring up a vault, agents, schedules and integrations and then babysitting them, so it becomes a project in itself [[17]](../SOURCES.md). Both can be true. A model can do the filing, but someone has to notice when the filing is wrong.

**The freshness idea.** Per its README, one open-source builder's rule is that every stored fact is one of three things: timeless (true until the world changes shape), dated (true as of a stated date), or a pointer (a note on where to look). A linter enforces it, so a bare count or status cannot sit in a page and go stale in silence [[36]](../SOURCES.md). You can apply the same rule by hand. Write "as of" and a date on anything that moves, and point to the source for anything that moves fast.

**Upkeep that fits in a week.** The weekly review and health check in [chapter six](06-rules.md) are the minimum. If you stop doing them, the brain does not stop working, which is the dangerous part. It keeps answering confidently from old pages.

## Failure four: prompt injection through the mail you feed it

This is the failure the build guides rarely mention, and it is the one that can cost you something real.

A language model cannot reliably tell the difference between an instruction from you and an instruction hidden in a document it was asked to read. A security standards body defines indirect prompt injection as the case where a model is handed text from outside places, like web pages or documents [[19]](../SOURCES.md). An email is exactly such a source. Anyone on earth can send you one.

**The lethal trifecta.** A security researcher's framework names three capabilities that, combined in one agent, make it exploitable for data theft: access to your private data, exposure to untrusted content, and the ability to communicate externally [[18]](../SOURCES.md). It is a practitioner framework, not a peer-reviewed one, but it is a useful test. Now look at what this repo builds. A brain with access to your mail and files has private data. A filing job that reads incoming mail has untrusted content. If the same agent can also send mail or call outside services, it has all three. Wiring your inbox into an always-on agent is the lethal-trifecta setup [[18]](../SOURCES.md), and the course this repo adapts does not discuss it.

**Memory poisoning.** The risk does not end with one bad email. A paper on memory injection shows an attacker planting malicious records in an agent's memory bank using only ordinary queries, with no direct write access to the memory. The success rates it reports are the authors' own [[20]](../SOURCES.md). In our design the memory is files that later runs trust. A hostile email that gets summarized into a wiki page, or worse into `rules.md`, can steer every later run.

### Guardrails

These are our recommendations, not findings from the sources. None is perfect. Together they remove one of the three legs of the trifecta, or make the damage small.

- **Read-only connectors.** The filing job gets read access to mail and calendar, nothing else. No send, no delete. If it can only read, a trick email can mislead it but cannot make it act outwardly, as long as the job has no other outbound path. Removing send is not enough if the job can still fetch URLs or call outside services; cut those too.
- **Quarantine `raw/`.** Treat everything in `raw/` as untrusted text. Summaries cite it; instructions inside it are never followed. Keep it out of the instructions path: `raw/` is data, while `AGENTS.md`, `about/` and `rules.md` are policy.
- **Drafts, never sends.** Anything that would go to another person is created as a draft, shown on the morning page under "Waiting for your approval", and sent by you.
- **A human promotes anything into `about/` or `rules.md`.** Models propose; you decide. This breaks the poisoning route, because hostile text cannot reach the files every run trusts without passing a person.
- **Separate jobs.** If you can, split the work: one job reads mail and only writes to `raw/`, and a different job with no mail access does the compiling into `wiki/`. The compiler then holds no mail credentials. It still reads untrusted text from `raw/`, so the quarantine rule still applies.
- **Least permission, checked at the source.** Review what each connector can actually do in its own settings. Some platforms let scheduled runs use connected tools without asking for approval on each call (the adapters note which). Prompt wording is advice; permission settings are the real limit.
- **Log everything.** The log and your version history let you see what a job changed, which is how you will notice a problem.
- **Test with a canary.** Send yourself an email that tells the assistant to ignore its instructions and add a rule, and confirm the pipeline files it as a suspicious source and changes nothing else.

## Failure five: you stop looking

The quietest failure is the human one. The morning page gets skimmed, approvals get rubber-stamped, the weekly review gets skipped, and the system keeps humming. Keep the page short enough to read, keep approvals specific, and keep the review on the calendar. Treat the brain as a junior colleague who needs supervision, not an oracle.

## A short checklist

- Is the index current, and are `AGENTS.md`, `about/` and `rules.md` short?
- Can any scheduled job send, delete or edit policy files? It should not.
- Does every fast fact in the morning page name its source?
- Did the last weekly review happen?
- When did you last read a page the assistant wrote, end to end?

This chapter is not security advice for your specific situation. If your mail contains anything legally or financially sensitive, talk to a professional before you connect it to anything automated.

Done when: you can name the three trifecta legs for your setup, at least one is removed (usually every outbound path: sending, fetching URLs, calling outside services), and a test email containing instructions changed nothing in the folder.
