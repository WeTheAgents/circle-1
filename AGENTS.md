# Circle-1 contributor instructions

Read [the newcomer guide](docs/start_here.md) for the project's purpose and
current document map. Historical WEA examples do not assign current work.

- Keep scanners target-independent. Accept a repository root and profile as
  explicit inputs.
- Do not import packages from a scanned repository.
- Do not add GitHub, ledger, escrow, or task-index writes.
- Use only the Python standard library unless an accepted change authorizes a
  dependency.
- Add focused pytest evidence for each scanner behavior.
- Run `python -m pytest -q`, `ruff check src tests`, and `pyright src` before
  publication.
