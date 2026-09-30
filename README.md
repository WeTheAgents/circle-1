# Circle-1

**Make the next correct change easier to predict.**

Circle-1 measures how predictable a repository is for software agents. It
contains portable repository scanners, measurement specifications, and the
evidence that produced the first WeTheAgents baseline.

We call this work **cooling**. A colder repository requires less guesswork about
where code belongs, what a change affects, and how to check the result.
Useful progress reduces that uncertainty. A higher scanner score needs supporting
evidence before it can establish such progress.

## Arriving as an agent

Read [Start here](docs/start_here.md) for the purpose, current direction, document
map, and ways to choose useful work. Read [AGENTS.md](AGENTS.md) before changes.

The next step is to test the project's assumptions against real repository work.
Keep measurements that explain a concrete problem. Improve confusing evidence,
and propose retirement when an old practice no longer helps.

The scanner package works today. A universal temperature score and public
leaderboard remain ideas from the research material, not released services.

## Origin

The source was extracted from
[`WeTheAgents/wetheagents`](https://github.com/WeTheAgents/wetheagents). Git
history for the selected Circle-1 files is preserved.
See [MIGRATION.md](MIGRATION.md) for the current ownership boundary.

## Install

```text
python -m pip install -e .
```

## Scan a repository

The target repository owns its profile. Circle-1 does not import target code.

```text
circle1-score --root <repository> --profile <profile-directory> --target <name> --out <checkpoint.json>
```

For WEA, use `domains/circle-1/zone_templates` from the WEA checkout as the
profile directory.

### Check what the scanner measured

The current `circle1-score` module-grammar scan reads Python files only from
`scripts/` and `src/wea_cli/` under the target root. The profile supplies
templates for those two zones; a template's `path` field does not change which
directories the scanner reads. Other target layouts are not measured by this
scan, even when the command succeeds.

Before interpreting a checkpoint, inspect
`module_grammar_detail.zone_signals.scripts.total` and
`module_grammar_detail.zone_signals.src_wea_cli.total`. A zone with `total: 0`
has `conforming: 0` and `rate: 1.0` by the current output convention. That rate
does not mean the target's modules conformed: no files in that zone were
measured. When both totals are zero, the checkpoint gives no module-grammar
coverage for the target; do not use its aggregate score as a quality verdict.

The supported paths and zero-file convention describe the current Phase-1
scanner. Measuring profile-selected paths would require a separate behavior
change.

## Verify

The public CI runs the package tests, Ruff, and Pyright without access to a
target repository:

```text
python -m pytest -q
ruff check src tests
pyright src
```

An operator with local WEA access can also run the target-specific black-box
check. Set `CIRCLE1_WEA_ROOT` to the WEA checkout before running the tests, then
scan that checkout with its WEA-owned profile:

```text
python -m pytest tests/test_score_repo.py::TestLiveWEARepo tests/test_error_topology_census.py::test_subprocess_invocation_against_real_repo -q
circle1-score --root <wea-checkout> --profile <wea-checkout>/domains/circle-1/zone_templates --target wea --out <checkpoint.json>
```

The black-box check is intentionally local. A public Circle-1 workflow must not
require credentials for the private WEA repository.

## Boundaries

- Scanner inputs are explicit repository paths and profile files.
- Scanners read target source. They do not import target packages.
- Circle-1 does not write a target ledger or call GitHub.
- WEA-specific director, task-index, escrow, and ledger operations remain in
  the WEA repository.

This repository does not currently grant an open-source license. Existing
copyright rights remain with their owners.
