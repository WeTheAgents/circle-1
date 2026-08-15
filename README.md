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

## Boundaries

- Scanner inputs are explicit repository paths and profile files.
- Scanners read target source. They do not import target packages.
- Circle-1 does not write a target ledger or call GitHub.
- WEA-specific director, task-index, escrow, and ledger operations remain in
  the WEA repository.

This repository does not currently grant an open-source license. Existing
copyright rights remain with their owners.
