# Prose style rules (journal-agnostic)

The framework's writing machinery: voice and tense, the hedging ladder, the
overclaim taxonomy, effect-size honesty, the anti-pattern list, sentence and
paragraph rules, and numeric/acronym conventions. These are venue-agnostic. The
venue-specific surface conventions — how a figure reference or an in-text
citation is *rendered*, the abstract word limit, the section-numbering scheme —
are declared by the venue profile (see `fragments/journal/`), not here.

## Voice and tense

- **First person plural** ("we") throughout Methods and Experiments, unless the
  venue profile declares otherwise. Never "I"; never "the authors" except when
  referring to other works.
- **Past tense** for what was done experimentally: "we trained the model for 50
  epochs", "subjects were excluded if…".
- **Present tense** for architectural description: "the encoder comprises three
  modules", "the attention layer embeds node features".
- **Present tense** for biological / clinical claims: "the disorder progresses
  through a continuum", "the tract connects the medial temporal lobe to the
  posterior cingulate".
- Active voice for design choices ("we adopt domain randomisation"); passive is
  acceptable for impersonal procedures ("AUC was computed by ROC analysis").

### Per-section tense profile

Each section has a dominant tense; mixing tenses within a section reads as
careless or non-native. Calibrate to the table.

| Section       | Dominant tense                              | Mode                                                                 |
|---------------|---------------------------------------------|----------------------------------------------------------------------|
| Abstract      | Mixed (present + past)                       | Background = present; methods/results = past; implications = present.|
| Introduction  | Present                                      | Prior work in past ("Smith et al. demonstrated…"); current knowledge in present. |
| Methods       | Past for procedures, present for architecture| "We trained the model…" (past); "the model comprises three modules" (present). |
| Results       | Past + quantitative detail                   | "AUC reached 0.62 ± 0.07 on the target task." Avoid present tense — it overgeneralises. |
| Discussion    | Mixed                                        | Past for the recap, present for interpretation, conditional for implications. |
| Conclusion    | Present + future                             | Contribution in present; outlook in conditional ("may", "could").    |

The most common slip is **present tense in Results** ("the model achieves AUC =
0.62"), which reads as a general claim about the model rather than a specific
finding. Use past tense unless the statement is genuinely universal.

## Sentence-length and paragraph-position rule

Keep every sentence at **≤ 30 words** unless there is a clear structural reason
to go longer (a multi-clause methods sentence, for example). Sentences over 40
words almost always benefit from being split, joined by a semicolon, or
refactored.

The **last sentence of every paragraph** breaks this rule most often, because
writers try to summarise too much in the closing line. When reviewing or
revising, scrutinise paragraph-final sentences more than paragraph-initial ones.

When two clauses must stay together, prefer a semicolon for parallel
construction or an em-dash for parenthetical elaboration. Avoid comma splices.

## Hedging ladder — match verb strength to evidence strength

Mismatched hedging is the single most common trigger for an "overclaiming"
review comment. The verb must match the strength of the supporting evidence.

| Evidence strength                              | Acceptable verbs                     | Example                                                                                       |
|------------------------------------------------|--------------------------------------|-----------------------------------------------------------------------------------------------|
| Direct, replicated, multi-cohort               | demonstrate, show, establish         | "We demonstrate that ablating the module reduces test AUC by 0.04 (Cohen's d = 0.75, p = 0.001)." |
| Direct but single-cohort                       | reveal, indicate, find               | "We find that the top-ranked region survives BH-FDR correction (q = 0.045)."                   |
| Correlational                                  | be associated with, correlate with, track | "The feature was associated with the CSF marker (ρ = −0.18, q = 0.04)."                    |
| Moderate evidence with biological reading       | suggest, point to, be consistent with| "These results suggest the model captures coupling inaccessible to the baseline."             |
| Speculative / interpretive                     | may, could, might reflect            | "The disruption may reflect a process that precedes gray-matter change."                       |
| Future-directional                             | could enable, might allow            | "This framework could enable early-stage screening."                                          |

Reserve "demonstrate" and "show" for statistically robust results, ideally
replicated across cohorts or seeds. Use "suggest" or "may reflect" when
interpreting a single-cohort result with a modest effect. Never use "prove" —
empirical science does not prove.

## Overclaim taxonomy — four patterns to avoid

When a reviewer flags an overclaim it is almost always one of these four.

1. **Absolutes** — "uniquely", "only", "definitively", "necessarily". They
   imply no alternative explanation is possible, which science rarely supports.
   - Avoid: "The method uniquely captures cross-region coupling."
   - Prefer: "The method is, to our knowledge, the first to model this coupling
     explicitly."

2. **Unwarranted causation** — causal verbs ("drives", "causes", "produces")
   applied to correlational evidence (ρ, regression coefficients, ablation
   deltas). Correlation does not imply causation, particularly in
   cross-sectional neuroimaging.
   - Avoid: "Coupling drives disease progression."
   - Prefer: "Coupling is associated with disease stage (ρ = −0.12, p = 0.003)."

3. **Scope expansion** — generalising beyond the population, modality, or task
   actually tested.
   - Avoid: "Our method works on any brain network."
   - Prefer: "Our method was evaluated on resting-state functional connectivity
     from one cohort and may extend to other parcellations and modalities,
     though this is not tested here."

4. **Unverified "first" claims** — asserting novelty without a literature check.
   - Avoid: "We are the first to combine these two representations."
   - Prefer: "To our knowledge, this is the first model to combine them
     [CITE: novelty-check]." When in doubt, hedge with "to our knowledge".

When the self-check or the biology reviewer flags any of these, replace the verb
with the appropriate weaker rung from the hedging ladder.

## Effect-size adjective bands

Adjectives must match the reported magnitude — this is the effect-size-honesty
half of the shared discipline style tier, applied to prose. Do not call a small
effect "substantial" because it reached significance; a p-value is not a
magnitude. Use conventional bands as a floor, and always report the number
alongside the adjective so the reader can judge.

| Cohen's d      | Correlation \|r\| / ρ | Admissible adjective                     |
|----------------|-----------------------|------------------------------------------|
| < 0.2          | < 0.1                 | negligible, marginal                     |
| 0.2 – 0.5      | 0.1 – 0.3             | small, modest                            |
| 0.5 – 0.8      | 0.3 – 0.5             | moderate                                 |
| ≥ 0.8          | ≥ 0.5                 | large; "substantial" only here           |

"Significant" means statistically significant and must be paired with the test
and threshold — never used as a synonym for "large". If an effect is
significant but small, say both: "a small but significant effect (d = 0.28,
p = 0.01)".

## Anti-patterns — never in body prose

These read as engineering-report style and would be flagged in review.

1. **Parenthetical numeric breakdowns.**
   - Avoid: "Subject counts were 295 (217 CN + 78 patients), 335 (217 + 118)…"
   - Prefer: "Cohort sizes ranged from 266 to 335 participants (Table 1)."

2. **Inline pseudocode / function-call syntax.**
   - Avoid: "Splits were generated by `StratifiedKFold(shuffle=True,
     random_state=seed)`."
   - Prefer: "Fold assignment used stratified k-fold splitting with shuffling,
     seeded by the base seed."

3. **Bullet lists for non-enumerable content.** Bullets are for genuine
   enumerations (a fixed set of input conditions, the contributions list), not
   for paragraphs of methodology.

4. **Factorial-design arithmetic in prose.**
   - Avoid: "This design (5 tasks × 4 inputs × 12 models + ours) yielded 260
     combinations."
   - Prefer: "Every model was evaluated under every combination of task and
     input representation."

5. **Magic numbers in body prose.**
   - Avoid: "We used ten seeds (42, 142, 242, …, 942) and five folds per seed."
   - Prefer: "Cross-validation was repeated under ten independent random-seed
     initialisations with five stratified folds per repetition." Exact values
     belong in a supplementary methods note.

6. **Colloquialisms.**
   - Avoid: "vanilla model", "the headline result", "lots of methods".
   - Prefer: "the original model", "the principal finding", "many methods".

7. **Three or more sentences opening with "We" in a row.** Vary the openers.
   - Avoid: "We trained X. We then evaluated Y. We finally compared Z."
   - Prefer: "Following training, X was evaluated against Y and then compared
     to Z."

8. **Forward references** to figures not yet introduced. Introduce an object at
   its point of first use (per the inventory's first-reference order).

9. **Equation-as-pseudocode.** Equations are part of prose flow, not code
   blocks. Use display math with consecutive numbers, referenced as "Eq. (N)".

## Preferred patterns

- **Lead with rationale**: "To control for both seed-dependent and
  fold-dependent variability, we adopted repeated cross-validation with ten
  random-seed initialisations and five stratified folds per seed."
- **Semicolons** join closely related clauses: "AUC was the primary metric; F1
  and sensitivity were secondary."
- **Em-dashes** for parenthetical elaboration: "the top-ranked tract — an
  early-disrupted structure in this condition — surfaced in both ablation modes."
- **Logical connectives at sentence openings**: "To assess this…", "Following
  these definitions…", "Accordingly…", "Crucially…", "Importantly…".
- **Effect sizes travel with p-values**: "ρ = −0.18 (q = 0.04, age-adjusted
  ρ = −0.16, p = 0.005)".
- **Sample sizes on first use**: "n = 290".
- **Acronyms defined on first use** in each section, then used freely.
- **Citations grouped at the end of a clause**, not mid-sentence interruptions.

## Numerical and statistical reporting

- Two decimal places for percentages and p-values ("78.50%", "p = 0.043").
- Three or four decimals for small deltas ("ΔAUC = +0.0256").
- Format `mean ± std` in tables ("AUC = 0.62 ± 0.07"); spell it out in prose
  when the variation matters.
- State multiple-comparison correction explicitly: "p-values were adjusted by
  the Benjamini–Hochberg procedure with a false-discovery-rate threshold of
  q < 0.05".
- Never report a bare "p < 0.05" without an effect size in the same clause.
- Name statistical tests on first use ("one-sample t-test", "Spearman's rank
  correlation ρ", "Welch's two-sample t-test").

## Acronyms and terminology

Define each acronym on first use within each new section, then use it freely.
Do not maintain acronym expansions here: the canonical neuroimaging expansions
live in the shared terminology ledger, and any manuscript-specific vocabulary
(project terms, coined names, notation) lives in the project glossary supplied
at runtime. Consult those for the controlled vocabulary rather than coining
variants — a term must appear identically everywhere it is used. Project-specific
names appear as plain text (no italics, no quote-marks) and become standard
vocabulary after first use.

## Figure references and citations — declared by the venue

The *content* rule is here; the *rendering* is in the venue profile. In the
draft, always use the placeholders `[FIG: N]`, `[FIG: NX]`, and `[TABLE: N]`;
the build resolves them to the venue's rendered form (e.g. "Fig. 1A" vs
"Figure 1A"). Likewise, group citations at the end of a clause and use `[CITE:]`
placeholders — the venue profile declares whether the rendered form is
author–year or numeric. Do not hard-code either surface form in prose.
