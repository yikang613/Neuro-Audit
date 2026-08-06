#!/usr/bin/env python3
"""Discover and check neuro-audit evals.

Each sub-skill ships ``skills/<name>/evals/evals.json``. This runner discovers
them, verifies they are well-formed, and (in later phases) executes the
deterministic checks each eval declares. It backs guardrail G1: no new stage
lands without a passing eval.

Usage:
  run_evals.py            # human-readable summary
  run_evals.py --ci       # same, but exit 1 on any malformed/failed eval

At Phase 0 there are no eval files yet, so it reports "0 evals" and passes —
the gate is wired and green from the first commit.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"


def discover() -> list[Path]:
    if not SKILLS.exists():
        return []
    return sorted(SKILLS.glob("*/evals/evals.json"))


def check_file(path: Path) -> tuple[int, list[str]]:
    """Return (num_evals, errors) for one evals.json."""
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return 0, [f"{path.relative_to(REPO)}: invalid JSON ({exc})"]
    evals = data.get("evals")
    if not isinstance(evals, list):
        return 0, [f"{path.relative_to(REPO)}: missing 'evals' list"]
    for i, ev in enumerate(evals):
        if not isinstance(ev, dict) or "prompt" not in ev:
            errors.append(f"{path.relative_to(REPO)}[{i}]: eval needs a 'prompt'")
    return len(evals), errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ci", action="store_true", help="exit non-zero on any error")
    args = ap.parse_args()

    files = discover()
    total = 0
    all_errors: list[str] = []
    for f in files:
        n, errs = check_file(f)
        total += n
        all_errors.extend(errs)
        print(f"  {f.relative_to(REPO)}: {n} eval(s)")

    if not files:
        print("run_evals: 0 evals discovered (none defined yet) — OK")
        return 0

    print(f"run_evals: {total} eval(s) across {len(files)} file(s)")
    if all_errors:
        print("run_evals: FAIL")
        for e in all_errors:
            print(f"  - {e}")
        return 1 if args.ci else 0
    print("run_evals: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
