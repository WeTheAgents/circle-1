#!/usr/bin/env python3
"""Circle-1 checkpoint scanner for a repository profile.

Produces a structural checkpoint JSON targeting the module_grammar dimension.
Detects declared zone templates and measures file conformance for session-1 zones
(scripts/ and src/wea_cli/).

Usage:
    circle1-score --root . --profile domains/circle-1/zone_templates \\
        --target wea --scan-date 2026-04-23 --repo-sha c07e079

Output is a JSON checkpoint record written to stdout or to an explicit path.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from .zone_grammar import score_module_grammar


def scan_repository(
    root: Path,
    profile_dir: Path,
    target: str,
    scan_date: str,
    repo_sha: str,
) -> dict:
    if not root.exists():
        raise FileNotFoundError(f"Repo root does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Repo root is not a directory: {root}")

    if not profile_dir.is_dir():
        raise NotADirectoryError(f"Profile directory does not exist: {profile_dir}")

    mg = score_module_grammar(root, profile_dir)
    declared_zones = mg["zones_with_declared_templates"]

    if declared_zones:
        template_note = f"Zone templates declared for: {declared_zones}."
    else:
        template_note = (
            "No zone templates declared — using empirical dominant shape only."
        )

    return {
        "scan_date": scan_date,
        "repo_sha": repo_sha,
        "target": target,
        "structural": {
            "module_grammar": {
                "declared": mg["declared"],
                "enforced": mg["enforced"],
                "exercised": mg["exercised"],
            },
        },
        "module_grammar_detail": {
            "zones_with_declared_templates": declared_zones,
            "zone_signals": mg["zone_signals"],
        },
        "notes": [
            "Phase-1 scan: module_grammar dimension only.",
            template_note,
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Circle-1 checkpoint scanner")
    parser.add_argument("--root", default=".", help="Repo root directory")
    parser.add_argument("--profile", required=True, help="Zone-template directory")
    parser.add_argument("--target", required=True, help="Stable target name")
    parser.add_argument(
        "--scan-date",
        default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        help="ISO date for the checkpoint record",
    )
    parser.add_argument(
        "--repo-sha",
        default="",
        help="Git SHA to record in the checkpoint",
    )
    parser.add_argument("--out", default=None, help="Explicit checkpoint output path")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    profile_dir = Path(args.profile).resolve()
    try:
        result = scan_repository(
            root,
            profile_dir,
            args.target,
            args.scan_date,
            args.repo_sha,
        )
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    payload = json.dumps(result, indent=2)

    if args.out:
        out_path = Path(args.out).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload + "\n", encoding="utf-8")
        print(f"Saved: {out_path}", file=sys.stderr)
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
