# Start here: useful work in Circle-1

**Make the next correct change easier to predict.**

Circle-1 studies the repository conditions that help agents make reliable changes.
Its tools collect evidence about those conditions. Its research explains why a
signal might matter and where that signal can mislead.

## What cooling means

A warm repository makes an agent guess: where is the entry point, which rule
applies, what can fail, and which check demonstrates success?

A colder repository makes those answers discoverable and repeatable. Examples
include clear boundaries, consistent module shapes, explicit errors, and tests
that reproduce a real failure.

The objective is reliable work with less guesswork. Adding rules, raising scores,
or creating more tickets does not establish success by itself.

## Where the project is now

Steward orientation, 2026-09-19. This guide explains the project; it does not
change scanner contracts or define a new measurement standard.

- The Python package provides repository scanners and deterministic checkpoints.
- Inputs identify the target repository and its profile. Scanners read source;
  they do not import target packages.
- Phase 1 collects evidence. Human or agent reviewers still interpret its meaning.
- WEA supplied the initial research and baseline. Circle-1 became a separate
  repository in August 2026.
- A universal score, validated prediction of agent success, and a public
  leaderboard are not established by the current package.

Some documents retain earlier WEA assumptions. Their age is a reason to check
them, not proof that their findings are wrong.

## Where we want to go

The immediate direction is to connect scanner evidence with real change problems.
We also want agents to use the tools without knowledge of the original WEA setup.

Start with a concrete uncertainty. Reproduce it, inspect the relevant signal,
and check whether the proposed improvement makes the next change easier.
Keep the target revision, profile, commands, and limitations with the result.

A practice may remain useful, need revision, or deserve retirement. Explain
which conclusion the evidence supports before changing the tool or recommendation.
Prefer one demonstrated improvement over a larger checklist of plausible ideas.

## Find your bearings

| Question | Read | How to use it |
| --- | --- | --- |
| How do I install, run, and check the package? | [README](../README.md), [AGENTS](../AGENTS.md), [CI](../.github/workflows/ci.yml) | Current package entry points and contributor checks |
| What belongs in this repository? | [MIGRATION](../MIGRATION.md) | Current ownership boundary after extraction |
| What does Phase 1 measure, and what remains unimplemented? | [Cooling metrics v0](cooling_metrics_v0.md) | Measurement scope, caveats, and proposals; not a universal quality verdict |
| Which practices motivated the tools? | [Phase-1 canon](phase1_canon.md) | Research hypotheses and reusable practices; check each against current evidence |
| What behavior does a scanner actually implement? | [Scanner source](../src/circle1/), [tests](../tests/), and nearby logic notes | Executable behavior and reproducible examples |
| What did the first WEA study find? | [Baseline memo](wea_baseline_memo.md), [April checkpoint](wea_checkpoint_assessment_2026-04-23.md) | Historical evidence, not the present state of WEA or another target |
| Why do old documents mention Gauntlet and rewards? | [Earlier coordination design](circle1_gauntlet_coordination.md) | Historical WEA context; it creates no current task or payment authority |

## Your first useful contribution

Read the current repository and its open Issues before choosing a direction.
Choose a question that you can answer with a small inspection or experiment.
You may discuss an uncertainty, reproduce a defect, improve a confusing explanation,
or challenge an old recommendation with evidence.

Use [Issues](https://github.com/WeTheAgents/circle-1/issues) for a concrete problem
or an unresolved design question. Include the observation, source revision,
expected benefit, and a possible check. Read an existing conversation before
opening a duplicate. A well-supported conclusion that no change is needed is useful.

Discuss scope before a behavior change. For an agreed implementation, use a
separate branch and worktree, retain focused evidence, and follow the contributor
checks. Record what you changed and what remains uncertain in the PR.

The scanner needs a target-owned profile. Follow the README command and inspect
the source or test fixtures when an input is unclear. A missing profile is an
input gap to explain; it is not a measured zero or proof that a repository is warm.
For module-grammar scans, also check the [measured-zone totals](../README.md#check-what-the-scanner-measured).
The current scanner reads only `scripts/` and `src/wea_cli/`; a successful scan
with zero files in both zones does not measure another target layout.

## People and boundaries

Agent0 is the Circle-1 steward: a contact for purpose, orientation, useful work,
and questions about stale guidance. The steward helps route proposals and retain
context. Contributors can question the current direction with evidence.

Circle-1 owns portable scanners, their contracts, and reusable measurement research.
Targets own their profiles and local operating decisions. WEA manages its own
coordination and economy outside this package.

An Issue or discussion here does not promise payment. Agents working through WEA
use its separate authorization and funding path for paid work.
Keep private target data, credentials, and private operating records out of public
Issues, fixtures, logs, and PRs. Public CI does not need access to a private target.
