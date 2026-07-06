#!/usr/bin/env python3
"""Content firewall: fail if private journal/project content is committed.

The public-framework / private-content boundary (see NOTICE) says the repo may
contain only:
  - the framework code/docs;
  - synthetic example profiles named ``*.example.yaml``;
  - the single MIA reference journal profile, which must carry a
    ``provenance: public-guidelines`` stamp (built from MIA's public Guide for
    Authors, never from copyrighted exemplars).

Anything else that looks like a real venue/project profile, any exemplar PDF, or
any committed ``.neuroscribe/`` overlay is a leak. This runs in CI and locally.

Exit 0 = clean. Exit 1 = a boundary violation was found.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# YAML profiles allowed in-tree: synthetic examples anywhere, plus the MIA
# reference profile (which must be provenance-stamped, checked below).
ALLOWLIST_DIR_PREFIXES = ("skills/neuro-write/static/fragments/journal/mia/",)
PROVENANCE_MARKER = "provenance: public-guidelines"

# Markers that identify a file as a *real* (declared) venue/project profile
# rather than a synthetic example or a schema.
PROFILE_MARKERS = ("declared_by:", "venue_name:")


def _tracked_or_working_files() -> list[Path]:
    """All files under the repo, excluding .git and Python caches."""
    out: list[Path] = []
    for p in REPO.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(REPO).as_posix()
        if rel.startswith(".git/") or "__pycache__/" in rel:
            continue
        out.append(p)
    return out


def main() -> int:
    violations: list[str] = []

    for path in _tracked_or_working_files():
        rel = path.relative_to(REPO).as_posix()

        # 1) No exemplar PDFs, ever.
        if path.suffix.lower() == ".pdf":
            violations.append(f"{rel}: PDF committed (exemplars must stay private)")
            continue

        # 2) No committed runtime overlay or exemplars directory.
        if rel.startswith(".neuroscribe/") or "/exemplars/" in rel:
            violations.append(f"{rel}: private runtime overlay committed")
            continue

        # 3) YAML profiles: allow *.example.yaml; allow the provenance-stamped
        #    MIA reference; deny any other file that looks like a real profile.
        if path.suffix.lower() in (".yaml", ".yml"):
            name = path.name
            if name.endswith(".example.yaml"):
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                text = ""
            looks_like_profile = any(m in text for m in PROFILE_MARKERS)
            if not looks_like_profile:
                continue  # schema, manifest, workflow yaml, etc. — fine
            allowlisted = any(rel.startswith(p) for p in ALLOWLIST_DIR_PREFIXES)
            if allowlisted and PROVENANCE_MARKER in text:
                continue
            if allowlisted:
                violations.append(
                    f"{rel}: MIA reference profile missing '{PROVENANCE_MARKER}' stamp"
                )
            else:
                violations.append(
                    f"{rel}: real journal/project profile committed (keep it in a "
                    f"private .neuroscribe/ overlay)"
                )

    if violations:
        print("content firewall: FAIL")
        for v in violations:
            print(f"  - {v}")
        return 1

    print("content firewall: OK (no private journal/project content committed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
