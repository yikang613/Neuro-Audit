# Stance — surface the claim, evidence, and boundary before writing prose

Run this intake on a section *before* drafting a single sentence. Prose written
without a fixed stance drifts into overclaim, because the writer decides how
strongly to phrase a result while phrasing it. Decide first; phrase second.

For the section as a whole, and again for each paragraph that carries a
substantive result, make three things explicit.

## 1. Claim — what does this passage assert?

State it in one sentence, plainly, before any hedging. "Cross-tissue features
raise classification AUC over the gray-matter-only baseline." "The proposed
module removes the fixed-partition assumption of prior graph encoders." If you
cannot write the claim in one sentence, the paragraph is doing two jobs and
should be split.

## 2. Evidence — what backs the claim, and how strong is it?

Name the support and classify it. Every claim rests on exactly one of:

- **Empirical result** — a number from the project's results (the run-ledger /
  captured tool-calls). Note the effect size, the uncertainty (CI / std / n),
  whether it is single-cohort or replicated, and whether it survived
  multiple-comparison correction. This determines the verb.
- **Method description** — a design choice being reported. No hedging needed;
  state what was done in the past tense.
- **Prior claim** — an assertion carried from the literature. It needs a
  citation placeholder (`[CITE:]`), not an empirical hedge.

Map evidence strength to a hedging rung (see `style-rules.md`): replicated /
multi-cohort → "demonstrate, show"; single-cohort direct → "reveal, find";
correlational → "is associated with"; interpretive → "suggest, may reflect".
The verb the paragraph is allowed to use is now fixed.

## 3. Boundary — what does the evidence *not* support?

Write the boundary down even if it never reaches the page; it stops scope
creep. Ask:

- **Causality.** Is the evidence correlational (Spearman ρ, regression
  coefficients, ablation deltas on a classifier)? If so, no causal verb may be
  used — honour the correlational-imaging limits in the shared discipline
  style tier.
- **Population / modality scope.** What cohort, modality, parcellation, and
  task was this actually tested on? The claim may not generalise past that
  without a stated caveat.
- **Effect magnitude.** Is the effect small? Then the adjective must say so —
  no "substantial" on a negligible delta (see the effect-size adjective bands
  in `style-rules.md`).
- **Novelty.** Is a "first"/"only"/"uniquely" claim actually verified against
  the literature? If not, hedge to "to our knowledge" or drop it.

## Output of the intake

The intake yields, per result-bearing paragraph, a one-line triple —
**claim / evidence-and-rung / boundary**. Carry that triple into drafting: the
claim becomes the topic sentence, the rung fixes the verb, and the boundary
becomes either an explicit caveat or a silent constraint on how far the prose
reaches. This is what keeps the draft's assertiveness matched to its support
from the first draft, rather than being walked back by a reviewer afterwards.
