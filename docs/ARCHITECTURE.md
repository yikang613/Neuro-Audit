# Architecture

neuroscribe is one Claude Code **plugin** containing several stage **sub-skills**,
a shared domain layer, a local **MCP server**, a **hook**, and helper **scripts**.
This document records the invariants that make it safe and reusable — the parts a
reviewer should read first.

## The three layers

Manuscript knowledge separates cleanly into three layers, and only the first
ships as code:

- **Layer A — Framework (baked in, shared).** The writer→reviewers→revise loop,
  the review dimensions, the hedging/overclaim/anti-pattern taxonomies, the
  methods-structure template, the figure discipline. Journal-agnostic. Lives in
  `skills/*/static/core/` and `agents/`.
- **Layer B — Journal profile (runtime data).** Word limits, citation style,
  required sections, exemplar patterns. Supplied per-journal at runtime as
  validated YAML; only MIA ships as a worked example.
- **Layer C — Project profile (runtime data).** Terminology/notation glossaries,
  the figure plan, repo paths. Supplied per-manuscript, always private.

## The runtime user-data plane

A shipped skill can only `Read` files inside the plugin. It has **no** facility
to read arbitrary user files by convention. Therefore the **agent**, not the
manifest, resolves and loads Layer B/C data:

1. **Discovery.** Honor `$NEUROSCRIBE_HOME`; else walk up from the working
   directory for a `.neuroscribe/` directory (git-style); else **halt and ask**.
   Never guess a path.
2. **Overlay.** After loading in-plugin fragments, `Read`
   `.neuroscribe/journal/<slug>/{venue,format,style}.yaml` and
   `.neuroscribe/project/<name>/project.yaml` and apply them as the
   **highest-priority data overlay**.

The `journal` axis therefore ships **only** two prose fragments — `generic` and
`mia`. A real venue routes to `generic` prose plus its runtime YAML overlay. The
manifest is not a venue registry.

## Invariants

- **Grounded, not asserted.** `mcp/neuro-stats` computes statistics and appends
  a record `{value, ci, n, df, seed, input_hash, code_version, timestamp}` to
  `.neuroscribe/run-ledger.jsonl`. The writer and rigor auditor may cite **only**
  ledger numbers. `hooks/grounding_guard.py` (a `PreToolUse` hook) blocks any
  manuscript write containing a number absent from the ledger.
- **Declared, never inferred.** Journal rules carry `declared_by: scholar`;
  `venue_name` is display-only and never used for lookup. Unstated fields report
  `NOT-CHECKED`, never a guessed default.
- **Generator ≠ evaluator.** The rigor auditor runs in a fresh context (and,
  where possible, a different model) from the writer, to avoid frame-lock — a
  known failure mode where a verifier sharing the generator's context rubber-
  stamps its errors.
- **Auditor, not runner.** neuroscribe never invokes or parses a preprocessing
  pipeline and never reads imaging data. `neuro-preprocess` emits documentation
  scaffolds only.
- **Public framework, private content.** Enforced by `.gitignore` and
  `scripts/lint_no_journal_content.py` (allowlist + provenance stamp).

## Reuse boundary

Structural concepts (schema-validated venue profiles; router-based progressive
disclosure) were re-implemented independently from public field lists and
patterns. No differently-licensed source files are vendored into this repo.
