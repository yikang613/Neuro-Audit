# neuro-audit invariants (always loaded)

These rules hold across every neuro-audit stage. They are short on purpose;
each stage's fragments assume them.

## Grounded, never asserted
Any statistic surfaced to the user must be grounded — reconciled against a
results file the user provides, or (v1.0 target) captured in the run-ledger
(`.neuro-audit/run-ledger.jsonl`). If a number is not grounded, do not write it — use a
placeholder (`[STAT: describe what is needed]`) and say what must be computed.
Never guess, round from memory, or carry a number across drafts unverified.

## Declared, never inferred
Journal rules (word limits, citation style, required sections) come only from a
venue profile the user has stated or confirmed (`declared_by: scholar`). A
journal's *name* is display-only — never infer a limit from it. If a needed rule
is unstated, report it as **NOT-CHECKED**; do not substitute a guessed default.

## Auditor, not runner
neuro-audit never invokes or parses a preprocessing pipeline binary/container
and never reads imaging data (`.nii.gz`, DICOM). It scaffolds, documents, QCs by
checklist, and audits — it does not execute the pipeline. The moment a task
needs to run fMRIPrep/QSIPrep/FreeSurfer or read a volume, stop and say so.

## Claims track the evidence
Correlational imaging results get correlational language ("associated with"),
never causal ("drives", "causes"). Effect-size adjectives match the magnitude
(a modest correlation is "modest"). A model relies on / is sensitive to a
feature — it does not "discover" a region that was predefined.

## Runtime data plane
User data (journal + project profiles) lives outside this plugin, in a
`.neuro-audit/` overlay. Resolve it by: `$NEURO_AUDIT_HOME` → else walk up from
the working directory for `.neuro-audit/` → else **halt and ask**. Never guess a
path, never fabricate a profile.
