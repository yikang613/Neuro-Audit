# Discipline style tier (the HARD tier)

Style resolves in three priorities: **discipline conventions (HARD, this file) >
target-journal conventions (STRONG) > author's personal style (SOFT, applied
only where it does not conflict)**. The rules here are neuroimaging reporting
conventions that override both journal house style and personal preference,
because violating them is a scientific error, not a stylistic one.

## Causal language (the load-bearing rule)

- Observational / correlational imaging findings take **associational** language:
  "associated with", "related to", "predicts" (in the statistical sense, stated).
  Reserve "drives", "causes", "leads to", "produces" for designs that license a
  causal claim (intervention, longitudinal mediation, lesion). Cross-sectional
  FC/SC differences do not.
- A trained model **relies on / is sensitive to / weights** a feature. It does
  not "discover", "identify", or "reveal" a region that was **predefined** in an
  atlas or ROI set. Discovery language requires that the thing was not built in.

## Effect-size honesty

- The adjective must match the magnitude. A correlation of r ≈ 0.2 is **modest**
  / **weak**, not "strong" or "robust". An AUC gain inside overlapping confidence
  intervals is **comparable**, not "superior".
- Report the magnitude and its uncertainty (CI, or the test), not just a
  direction or a p-value. "Significant" is not a synonym for "large".
- Comparative claims ("A outperforms B") require the appropriate test
  (e.g. a paired/DeLong comparison for AUCs), not a bare point-estimate gap.

## Multiplicity and selection

- Any many-comparisons result (edge-wise, region-wise, voxel-wise) states its
  correction (FDR / permutation / cluster) and the threshold. An uncorrected
  "significant edge" is not a finding.
- Do not describe a feature selected *because* it was significant as if it were
  independently validated (circular analysis / double-dipping).

## Hedging

- Match certainty to evidence: a single-cohort, cross-sectional result is
  "suggests" / "is consistent with", not "demonstrates" / "establishes".
- Generalization beyond the studied cohort/scanner/atlas is a claim that needs
  support; flag it rather than asserting it.
