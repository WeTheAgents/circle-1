# Circle-1

Circle-1 measures how predictable a repository is for software agents. It
contains portable repository scanners, measurement specifications, and the
evidence that produced the first WeTheAgents baseline.

The source was extracted from
[`WeTheAgents/wetheagents`](https://github.com/WeTheAgents/wetheagents). Git
history for the selected Circle-1 files is preserved.

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
