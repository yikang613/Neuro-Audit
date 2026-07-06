# Paper-anatomy scaffold

The structural skeleton a neuroimaging methods paper hangs on: section layout,
the five-movement abstract, and the standard patterns for methods, results,
tables, captions, and discussion. These are *structural* patterns and are
venue-agnostic.

Concrete exemplar **content** — the actual published papers whose voice you are
matching — is supplied at runtime. The user or the venue profile provides a
small set of target exemplars (real papers in the venue and subfield); read
those for the lexical register, sentence rhythm, and citation density, and
mirror them. This file gives the shape; the runtime exemplars give the voice.
Where a pattern below has a rendering choice (citation form, self-reference
token, best-result highlight colour), that choice is declared by the venue
profile (`fragments/journal/`), not fixed here.

## Section structure (top-level)

1. **Introduction** — clinical/scientific motivation, gap, contribution.
2. **Related work** (optional; common in newer papers).
3. **Methods / Method** — problem formulation, architecture, training.
4. **Experiments / Experimental setup + Results** (merged in some papers, split
   in others).
5. **Model interpretability** (where it is a substantive contribution).
6. **Discussion** — interpretation, comparison, limitations, future work.
7. **Conclusion(s)** — short, one paragraph.
8. **References**.

Sub-section nesting goes 2–3 levels deep when warranted. Every numbered header
has content; empty headers are never used.

## Abstract — five-movement flow

250–300 words (subject to the venue's declared limit), single paragraph, no
structured headers. Five movements:

1. **Problem framing** (2–3 sentences) — the broader scientific or clinical need.
2. **The gap** (1–2 sentences) — what existing methods fail to address.
3. **The contribution** (1–2 sentences) — "We propose X, a Y framework that does
   Z", with the key technical idea named.
4. **The validation** (3–4 sentences) — datasets, principal numerical results,
   comparative deltas.
5. **The implication** (1–2 sentences) — what this enables or what the result
   means biologically.

Conventions: no citations in the abstract; numbers are comparative deltas
("3% to 20% improvement"), not absolute rankings; specific dataset names are
normal; a code-availability one-liner is common.

## Introduction — 4–6 paragraphs

- **¶1** — motivation at the broadest level, narrowing to the specific task.
- **¶2** — biological/methodological motivation for the chosen approach.
- **¶3** — review of existing methods, organised by family (CNN → GNN →
  Transformer); each family gets 1–2 sentences.
- **¶4** — the unaddressed gap.
- **¶5** — the proposed method, summarising technical contributions in 3–5
  sentences.
- **(Optional) ¶6 or bullet list** — 3–4 explicit contribution bullets.

## Methods

- Opens with §X.1 "Overview" / "Problem formulation" / "Notation".
- Each subsequent subsection covers one architectural component (see
  `static/core/methods-structure.md` for the 4-beat per-component template).
- Loss functions get their own subsection toward the end.
- Implementation details (optimiser, learning rate) go at the end of Methods or
  in the Experiments setup.
- Each subsection opens with a motivating sentence (the *why*) before the *what*.
- Equations are introduced with prose, numbered on the right margin, referenced
  as "Eq. (N)".

## Experiments / Results

Standard subsection layout:

1. **Datasets / Data acquisition** — cohort sources, inclusion criteria, scan
   parameters (in prose, not a table).
2. **Experimental settings / Implementation** — optimiser, hyperparameters,
   schedule, hardware.
3. **Evaluation metrics** — explicit list, abbreviations on first use.
4. **Comparison with state of the art** — prose intro naming each baseline by
   category, then a results table.
5. **Ablation study** — table or figure of component-wise removal effects.
6. **(Optional) Hyperparameter sensitivity** — line plots or tables.
7. **(Optional) Interpretability / biomarker analysis** — where substantive.

Tables dominate the numerical presentation. The scaffold:

```
Table N
Classification performance of all competing models on task X
in terms of ACC (%), SEN (%), SPE (%), F1 (%), and AUC (%).
[best-result highlight convention — declared by the venue profile]

Method     Modality  ACC(%)       SEN(%)       SPE(%)       F1(%)        AUC(%)
Baseline-A FC        69.38±1.89   36.86±4.11   88.73±2.17   45.37±3.93   62.79±1.33
...
Ours       FC, SC    76.55±0.60   52.38±3.52   89.92±1.80   70.88±2.47   68.15±1.05
```

- The self-reference token for the proposed method ("Ours") and the
  best-per-column highlight (red or bold) are venue conventions — take them from
  the profile.
- `mean ± std` in a single cell; caption above the table; three-line style (no
  vertical rules) where the venue calls for it.

## Discussion

Length 1–3 pages, 4–6 paragraphs. Some papers subdivide (§ The model / §
Limitations); others flow as unsubdivided prose. Common pattern:

1. **¶1** — principal-findings recap: method + strongest empirical result.
2. **¶2–3** — biological / interpretive significance, with supporting citations.
3. **¶4** — comparison to state of the art: why the method beats / matches /
   trails specific baselines.
4. **¶5** — limitations: dataset, sample size, effect sizes.
5. **¶6** — future work.
6. **Closing sentence** into the Conclusion.

The Discussion never introduces numerical results absent from the Results.

## Numerical-reporting register

Results and abstracts pair an effect size with its context, e.g. "achieves an
accuracy of 97% within 10 mm spatial resolution"; "a decrease in connection
efficacy was associated with worse outcome (R = 0.73, p < 0.001)"; "outperforms
the baseline by 3% to 20%"; "a Dice improvement of 1.06% and 4.30% for the two
tasks respectively". Use the runtime exemplars to calibrate how dense and how
hedged this reporting should be for the target venue.

## Caption and passage register

- Captions start with the noun phrase describing the content ("Overall framework
  of the proposed method"), never "Fig. 1 shows".
- A dataset passage names each dataset with a citation, states the task each
  serves, and grounds in related work with grouped citations — no bullet lists,
  no inline arithmetic, no pseudocode.

The exact lexical texture of these captions and passages should be copied in
*register* (not content) from the runtime-supplied exemplars.
