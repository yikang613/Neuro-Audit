# Neuroimaging rigor pitfall catalog

The failure modes that most often sink a neuroimaging / brain-network paper. This is
`neuro-audit`'s domain moat: a general academic-writing engine does not know these; a
neuroimaging reviewer does.

It is also the **anti-hallucination device** for every reviewer/auditor agent. A prompted
"reviewer" persona invents plausible-sounding critiques. This catalog constrains it to a
fixed set of **known, checkable failure modes**, and forces every finding to carry evidence.

## How an agent must use this catalog

1. **No quote, no finding.** Every reported issue must cite the exact sentence, table cell,
   figure, or line from the manuscript/notebook it refers to. A finding that cannot quote its
   target is discarded as unverifiable — treat it as a hallucination, not a finding.
2. **Check only what is on this list** (plus obvious internal contradictions). Do not free-form
   grade novelty, significance, or "quality." Those require the full field state and are
   hallucination-prone. Out of scope here.
3. **Surface candidates, do not render verdicts.** Each finding is a question for a human to
   confirm, tagged with a severity and the evidence quote. The agent is a pitfall-surfacer, not
   an authority.
4. **Numbers must be grounded.** Any statistic the agent asserts must come from a captured
   computation (the run-ledger), never narrated from memory. If a number is not in the ledger,
   it is a `[STAT: …]` placeholder, not a claim.
5. **Generator ≠ evaluator.** The auditor runs in a fresh context from the writer, and each
   surviving finding should pass an adversarial second look ("is this actually in the paper? is
   it actually a problem?") before it is reported.

**In scope:** methodological rigor, statistical validity, and internal consistency that are
checkable against the artifact. **Out of scope:** novelty, significance, whether a result is
scientifically *true*, and any domain claim beyond the model's knowledge.

---

## The catalog

Each entry: the failure mode, the concrete thing to check, the evidence the agent must quote to
ground a finding, and what a clean paper looks like.

### 1. Subject-level data leakage
**Failure mode:** The same subject appears in both training and test — via repeat visits/sessions,
siblings (e.g. HCP twins), or naive random splits over scans rather than subjects. Inflates
performance, sometimes massively.
**Check:** Is the train/test (and CV) split done at the **subject/family** level, not the scan
level? Are repeat sessions and related individuals kept together on one side?
**Quote:** the sentence describing the split unit (e.g. "we randomly split the 745 scans…") and
any statement of scans-per-subject.
**Clean:** "subject-disjoint (and family-disjoint) folds"; split unit stated explicitly.

### 2. Site / scanner confound and harmonization leakage
**Failure mode:** Class is confounded with site/scanner (e.g. patients scanned at one site), so
the model learns acquisition, not biology. Or ComBat/harmonization is fit on the **whole**
dataset before splitting, leaking test information.
**Check:** Is site/scanner cross-tabulated against the label? Is any harmonization (ComBat) fit
**inside training folds only**? Do subject-disjoint folds silently fail to control site?
**Quote:** the harmonization sentence and any site×group table (or its absence).
**Clean:** class shown balanced across sites, or site modeled/residualized; ComBat fit on train,
applied to test.

### 3. Circular analysis / double-dipping
**Failure mode:** Features, ROIs, or thresholds are selected using the **full** dataset (or the
labels), then the same data is used to evaluate — non-independent selection inflates effects.
**Check:** Was feature/ROI/edge selection performed **inside** the CV loop, blind to test folds?
Any "we selected the top-k regions that differed between groups, then classified" pattern?
**Quote:** the feature-selection sentence and where it sits relative to the split.
**Clean:** all selection, scaling, and tuning fit on training folds only; nested CV.

### 4. Class-imbalance mishandling
**Failure mode:** Reporting raw accuracy on imbalanced data (a 85%-majority classifier "scores"
85%), no stratification, or synthetic oversampling that fabricates non-physiological samples.
**Check:** Given the class ratio, is **balanced accuracy / AUROC / AUPRC-vs-prevalence** reported
instead of raw accuracy? Is the split stratified? Is any resampling done inside training folds?
**Quote:** the class counts and the headline metric sentence.
**Clean:** prevalence stated; imbalance-aware metrics; PR curve read against the no-skill floor.

### 5. Improper cross-validation and false-precision CIs
**Failure mode:** Tuning on the test set (no nested CV); averaging per-fold AUCs at tiny
per-fold n; reporting mean±SD across folds/seeds **as if it were a confidence interval** (folds
share training data → SD understates variance → false confidence).
**Check:** Is hyperparameter/threshold tuning in an **inner** loop? Are out-of-fold predictions
**pooled** before computing AUC? Are CIs proper (DeLong / bootstrap), not fold-SD?
**Quote:** the CV description and the "±" reported with the headline metric.
**Clean:** nested CV; pooled out-of-fold scoring; DeLong/bootstrap CI; seed spread as stability only.

### 6. Uncorrected multiple comparisons
**Failure mode:** Mass-univariate testing (thousands of edges/voxels/regions) without correction,
or selective reporting of the surviving few. Also cluster-forming-threshold abuse.
**Check:** Are p-values corrected (BH-FDR / permutation / cluster-level FWE)? Is the number of
tests stated? Any "p<0.05" on a connectome without correction?
**Quote:** the correction sentence (or the uncorrected p and the count of tests).
**Clean:** correction method named; number of comparisons reported; permutation for network stats.

### 7. Small-n overfitting and effect-size inflation
**Failure mode:** Tiny n against a huge feature space; a single impressive number with no CI; a
model-vs-model ranking on differences smaller than the sampling noise.
**Check:** Is n (per class) reported next to the feature dimensionality? Is a CI / power ceiling
given? Are claimed differences larger than the CI? (e.g. with ~50 positives, AUROC CI ≈ ±0.08–0.10.)
**Quote:** n per class, feature count, and the claimed gap between models.
**Clean:** CI on the headline; minimum-detectable-difference acknowledged; no claims inside the noise.

### 8. Atlas / parcellation mismatch and node misalignment
**Failure mode:** Different atlases (or node counts) across cohorts or pipeline stages; nodes not
aligned to the same region across subjects; mixing 246 vs 248-node graphs.
**Check:** Is a single atlas named and used consistently across all cohorts and stages? Is node
count fixed and node correspondence guaranteed?
**Quote:** the atlas/parcellation sentence(s) across cohorts.
**Clean:** one named atlas (e.g. Brainnetome-246 / Schaefer / AAL), consistent node count, aligned indices.

### 9. Head-motion and physiological confounds
**Failure mode:** Motion differs by group (patients move more) and drives "findings"; no scrubbing
/ censoring / motion regressors reported; global-signal decisions unstated.
**Check:** Is framewise displacement (or equivalent) compared **between groups**? Are motion
confounds regressed / high-motion frames censored? Is exclusion criteria stated?
**Quote:** the motion-QC sentence, and any group motion comparison.
**Clean:** motion QC reported; group motion compared and controlled; censoring thresholds stated.

### 10. Reverse inference and causal/clinical overclaim
**Failure mode:** Correlational imaging phrased as causal ("X impairs connectivity"); a
group-difference sold as a clinical "biomarker" or diagnostic tool; region → cognitive-process
reverse inference without independent support.
**Check:** Do claims exceed a correlational, cross-sectional, single-cohort design? Words like
"causes / restores / biomarker / diagnostic" against a design that cannot support them?
**Quote:** the overreaching claim sentence and the design that limits it.
**Clean:** associational language; "feasibility/association" framing; clinical utility not asserted
without external validation. (See also `style-discipline-tier.md`.)

### 11. Absent confound control (age, sex, education, TIV)
**Failure mode:** Groups differ in age/sex/education (or brain size), and those, not the disease,
drive the effect. No demographics-only baseline reported.
**Check:** Are nuisance covariates controlled (regressed / matched)? Is a **demographics-only
baseline** (e.g. age+sex → label) reported so the imaging model must beat it?
**Quote:** the covariate sentence and the demographics table (group comparisons of age/sex).
**Clean:** covariates modeled; demographics-only baseline reported; imaging beats it beyond CI.

### 12. Threshold / metric chosen on the test set; wrong metric for the question
**Failure mode:** Operating threshold picked to maximize a test-set number; a metric that ignores
prevalence or the clinical asymmetry of errors; F1/accuracy where sensitivity@fixed-specificity
is what matters.
**Check:** Is the decision threshold selected on **inner/training** folds only? Does the metric
match the question and the class prevalence?
**Quote:** the threshold-selection sentence and the reported operating point.
**Clean:** threshold tuned on training folds; metric justified against prevalence and error costs.

---

## Severity guidance (for triage, not verdicts)

- **Fatal (invalidates a claim):** leakage (1, 3), test-set tuning/threshold (5, 12), class×site
  confound (2). These break the central result if present.
- **Major (weakens / bounds a claim):** imbalance metric (4), multiplicity (6), small-n CI (7),
  confounds (9, 11), causal overclaim (10).
- **Correctness (must fix, may not change the headline):** atlas mismatch (8), reporting gaps.

Report the evidence quote and severity; let the human decide. A pitfall that is checked and
**absent** is worth stating too ("subject-level splitting confirmed") — it builds trust and
shows the check ran.
