# Contributing to neuroscribe

Thanks for your interest. neuroscribe is a Claude Code plugin: a set of skills,
agents, a local MCP server, hooks, and helper scripts. A few rules keep it
coherent and safe.

## Ground rules (the invariants)

1. **Never commit private content.** No exemplar PDFs, no real journal profiles
   (only synthetic `*.example.yaml` fixtures), no project/manuscript content. The
   `.gitignore` and `scripts/lint_no_journal_content.py` enforce this; CI fails
   if you cross the line.
2. **Grounded numbers only.** Any statistic surfaced to the user must come from
   a captured `neuro-stats` tool-call recorded in the run-ledger. Prompts must
   not invite the model to state a number it did not compute.
3. **Declared, never inferred.** Journal rules are recorded only from
   user-stated or user-confirmed values (`declared_by: scholar`). Do not add
   code or prompts that guess limits from a journal's name.
4. **Auditor, not runner.** neuroscribe never invokes or parses the output of a
   preprocessing pipeline binary/container and never reads `.nii.gz`/DICOM.
   Preprocessing support is documentation scaffolding only.
5. **Clean-room reuse.** Adapt concepts from other packs; do not copy files from
   differently-licensed projects into this Apache-2.0 repo.

## Development

- Python helpers live in `scripts/`; install `requirements.txt`.
- Every skill ships an `evals/evals.json`; **no new stage lands without a
  passing eval** (the eval-gate CI enforces this).
- Run the checks locally before opening a PR:
  ```
  python scripts/lint_no_journal_content.py
  python scripts/validate_profile.py --selftest
  python scripts/run_evals.py --ci
  ```

## Adding a journal

You don't edit the plugin to support a new journal — you create a runtime
profile in your own `.neuroscribe/` overlay via `neuro-venue`. No real journal
ships in-tree; only a synthetic `example` fixture, for tests and demonstration.
