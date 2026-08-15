# Migration from WeTheAgents

Circle-1 started as WEA self-dogfooding under
`WeTheAgents/wetheagents`. This repository preserves Git history for the
selected Circle-1 files through source commit `f940070`.

## Ownership after extraction

Circle-1 owns:

- the portable canon and measurement specifications in `docs/`;
- repository scanner code in `src/circle1/`;
- scanner contract tests in `tests/`.

WEA continues to own:

- `src/wea_cli/circle1.py`;
- `scripts/circle1_director_sweep.py`;
- task-index, escrow, and ledger reconciliation;
- WEA target profiles and WEA checkpoint records.

The retained WEA source snapshot is compatibility and provenance material. New
portable scanner changes belong in this repository.

## Cross-repository contract

Circle-1 receives the target root, profile directory, target name, output path,
scan date, and target revision as explicit inputs. Circle-1 does not import WEA
packages or write WEA state.
