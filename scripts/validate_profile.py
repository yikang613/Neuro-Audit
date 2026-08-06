#!/usr/bin/env python3
"""Validate a neuro-audit profile YAML against its JSON schema.

Usage:
  validate_profile.py --selftest              # validate every shipped *.example.yaml
  validate_profile.py <file.yaml> --kind venue|format|style|project

Graceful degradation: if PyYAML or jsonschema is not installed, the script does
a minimal structural check and reports NOT-VALIDATED (exit 0) rather than
crashing — a user without the optional deps still gets an honest result. In CI
the deps are installed, so validation is real.

Schemas live at ``skills/_shared/contracts/<kind>.schema.json``. At Phase 0 no
schemas or examples exist yet, so --selftest reports "nothing to validate" and
passes.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTRACTS = REPO / "skills" / "_shared" / "contracts"

try:
    import yaml  # type: ignore
    _HAVE_YAML = True
except ImportError:
    _HAVE_YAML = False

try:
    import jsonschema  # type: ignore
    _HAVE_JSONSCHEMA = True
except ImportError:
    _HAVE_JSONSCHEMA = False


def _kind_from_filename(path: Path) -> str | None:
    # e.g. journal_venue.example.yaml -> "journal_venue"
    stem = path.name
    for suffix in (".example.yaml", ".yaml", ".yml"):
        if stem.endswith(suffix):
            return stem[: -len(suffix)]
    return None


def _schema_path(kind: str) -> Path:
    return CONTRACTS / f"{kind}.schema.json"


def validate_one(path: Path, kind: str) -> tuple[str, str]:
    """Return (status, detail). status in {OK, FAIL, NOT-VALIDATED}."""
    if not _HAVE_YAML:
        return "NOT-VALIDATED", "PyYAML not installed"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return "FAIL", f"YAML parse error: {exc}"
    if not isinstance(data, dict):
        return "FAIL", "profile is not a mapping"

    schema_path = _schema_path(kind)
    if not schema_path.exists():
        return "NOT-VALIDATED", f"no schema at {schema_path.relative_to(REPO)}"
    if not _HAVE_JSONSCHEMA:
        return "NOT-VALIDATED", "jsonschema not installed"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.ValidationError as exc:  # type: ignore[attr-defined]
        return "FAIL", f"schema violation: {exc.message}"
    return "OK", "valid"


def selftest() -> int:
    if not CONTRACTS.exists():
        print("validate_profile --selftest: nothing to validate (no contracts yet)")
        return 0
    examples = sorted(CONTRACTS.glob("*.example.yaml"))
    if not examples:
        print("validate_profile --selftest: nothing to validate (no *.example.yaml yet)")
        return 0
    failed = False
    for ex in examples:
        kind = _kind_from_filename(ex)
        status, detail = validate_one(ex, kind or "")
        print(f"  {status:14} {ex.relative_to(REPO)}  ({detail})")
        if status == "FAIL":
            failed = True
    print("validate_profile --selftest:", "FAIL" if failed else "OK")
    return 1 if failed else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file", nargs="?", help="profile YAML to validate")
    ap.add_argument("--kind", help="venue|format|style|project (or full schema stem)")
    ap.add_argument("--selftest", action="store_true", help="validate all shipped examples")
    args = ap.parse_args()

    if args.selftest or not args.file:
        return selftest()

    path = Path(args.file)
    kind = args.kind or _kind_from_filename(path) or ""
    status, detail = validate_one(path, kind)
    print(f"{status}: {path} ({detail})")
    return 1 if status == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
