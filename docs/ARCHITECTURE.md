# Architecture

neuro-audit is one Claude Code **plugin** containing several stage **sub-skills**,
a shared domain layer, helper **scripts**, and a planned grounding spine (a local **MCP server** + a **hook**).
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
  validated YAML. No real journal ships in-tree — only a synthetic `example`
  fixture, alongside the journal-agnostic `generic` default.
- **Layer C — Project profile (runtime data).** Terminology/notation glossaries,
  the figure plan, repo paths. Supplied per-manuscript, always private.

## The runtime user-data plane

A shipped skill can only `Read` files inside the plugin. It has **no** facility
to read arbitrary user files by convention. Therefore the **agent**, not the
manifest, resolves and loads Layer B/C data:

1. **Discovery.** Honor `$NEURO_AUDIT_HOME`; else walk up from the working
   directory for a `.neuro-audit/` directory (git-style); else **halt and ask**.
   Never guess a path.
2. **Overlay.** After loading in-plugin fragments, `Read`
   `.neuro-audit/journal/<slug>/{venue,format,style}.yaml` and
   `.neuro-audit/project/<name>/project.yaml` and apply them as the
   **highest-priority data overlay**.

The `journal` axis therefore ships **only** the journal-agnostic `generic`
default plus a synthetic `example` fixture — no real journal. A real venue routes
to `generic` prose plus its runtime YAML overlay. The manifest is not a venue
registry.

## Invariants

- **Grounded, not asserted.** Every statistic is either reconciled against a
  results file the user provides, or held as a `[STAT:]` placeholder — never
  narrated from memory. _Planned for v1.0:_ a local `mcp/neuro-stats` server that
  captures `{value, ci, n, df, seed, input_hash, code_version, timestamp}` to
  `.neuro-audit/run-ledger.jsonl`, and a `hooks/grounding_guard.py` `PreToolUse`
  hook that blocks any manuscript write containing a number absent from the
  ledger. Until then the discipline is enforced by the writer and reviewers, not
  automatically.
- **Declared, never inferred.** Journal rules carry `declared_by: scholar`;
  `venue_name` is display-only and never used for lookup. Unstated fields report
  `NOT-CHECKED`, never a guessed default.
- **Generator ≠ evaluator.** Reviewer/auditor agents run in a fresh context (and,
  where possible, a different model) from the writer, to avoid frame-lock — a
  known failure mode where a verifier sharing the generator's context rubber-
  stamps its errors.
- **Auditor, not runner.** neuro-audit never invokes or parses a preprocessing
  pipeline and never reads imaging data. `neuro-preprocess` emits documentation
  scaffolds only.
- **Public framework, private content.** Enforced by `.gitignore` and
  `scripts/lint_no_journal_content.py` (allowlist + provenance stamp).

## Reuse boundary

Structural concepts (schema-validated venue profiles; router-based progressive
disclosure) were re-implemented independently from public field lists and
patterns. No differently-licensed source files are vendored into this repo.
