# Journal profile: Medical Image Analysis (MIA)

> Worked example. Every rule below is a *declared* profile value, built from
> MIA's public *Guide for Authors* (Elsevier) — not inferred from the venue
> name and not drawn from any copyrighted exemplar. It shows what a fully
> specified venue fragment looks like; the framework reads these as data.

## Identity and scope

MIA is the official journal of the MICCAI Society. It publishes original
research on medical and biological image analysis, emphasising computer vision,
virtual reality, and robotics applied to biomedical imaging. Modalities of
interest include MR, ultrasound, CT, nuclear medicine, X-ray, and optical/
confocal microscopy. Methodological scope spans representation, feature
extraction, segmentation, registration, longitudinal analysis, shape/motion
analysis, atlas-based methods, and computational anatomy. Frame the manuscript
so its contribution lands inside this scope.

## Abstract

- **250-word maximum.** Hard limit.
- Single paragraph, no structured headers; must stand alone.
- State purpose, principal results, and major conclusions.
- Avoid references; if one is essential, give author(s) and year(s) inline, in
  full.
- Avoid non-standard abbreviations; define any essential one on first mention
  within the abstract.

## Section numbering

- Decimal numbering: `1`, then `1.1`, then `1.1.1`, `1.1.2`, then `1.2`, etc.
- The abstract is **not** numbered.
- Cross-references cite the section number ("as introduced in §2.3"), never
  "see above".
- The **Discussion is required** and must interpret the results against the
  cited literature, not merely restate them.
- Acknowledgements go in their own section directly before the reference list.
- Appendices are lettered A, B, C…; equations, figures, and tables inside carry
  the prefix (Eq. (A.1), Fig. A.1, Table A.1).

## Citations — author–year (declared)

MIA uses **author–year** in-text citations, `(Author, year)`. This is the
declared value of the profile's citation-style field; the framework reads it
from the venue profile, and this fragment is the worked instance. Forms:

- One author: `(Allan, 2020)`.
- Two authors: `(Allan and Jones, 2019)`.
- Three or more: `(Kramer et al., 2023)`.
- Multiple in one parenthetical, alphabetical then chronological, separated by
  semicolons: `(Allan, 2020a, 2020b; Allan and Jones, 2019)`.
- Narrative form: `Kramer et al. (2023) have recently shown…`.
- Reference list: alphabetised by first author, then chronological; append
  a/b/c to the year for same-author-same-year; abbreviate journal names per the
  LTWA; provide DOIs when available. Datasets carry a `[dataset]` prefix.

In drafts, `[CITE:]` placeholders resolve to this form; the biology reviewer
suggests the specific `(Author, year)` that supports each load-bearing claim.

## Figure references

- Body prose uses **"Fig. 1A"** — period after "Fig", not "Figure 1A".
- Subfigure forms: "Fig. 5A", "Fig. 5A–C".
- Each figure is a separate file, numbered in order of appearance, cited at
  least once from the body.
- Captions: a brief noun-phrase title plus a description; define every symbol
  and abbreviation.
- Colour must be legible for readers with colour-vision deficiency.
- Generative AI may **not** create or alter manuscript figures, except where AI
  is itself the research method — then document model name, version, provider in
  the methods.

## Tables

- Editable text only, never images; numbered consecutively; each cited from the
  body.
- **Three-line style** (top rule, header rule, bottom rule). **Avoid vertical
  rules and shaded cells.**
- **Caption above** the table; notes beneath the body.
- Self-reference the proposed method as **"Ours"** in the methods column.
- Report `mean ± std` in a single cell; highlight the best result per column
  (red or bold — red is the common MIA convention).
- Use tables sparingly; do not duplicate content already in prose or a figure.

## Highlights

- Required at submission.
- **3 to 5** bullet points capturing the novel results and new methods.
- Each ≤ **85 characters including spaces** — a hard constraint.
- Submitted as a separate editable file with "highlights" in the filename.
- Phrase each as a self-contained claim (they drive search-engine
  discoverability).

## Graphical abstract

- Required at submission.
- **531 × 1328 px (h × w)** or proportionally larger; readable at 5 × 13 cm.
- Preferred types: TIFF, EPS, PDF, or MS Office.
- Obtain permission for any third-party content.
- Generative AI is **not permitted** for the graphical abstract.

## Keywords

- Provide **1 to 7** for indexing.
- Avoid multi-word keywords joined by "and"/"of" (prefer a compact adjectival
  phrase such as "graph transformer" over "transformers for graph-based brain
  networks").
- Use abbreviations only if firmly established in the field.

## Math, units, notation

- **SI units** required; give the SI equivalent for any non-SI unit.
- Equations as **editable text**, not images; numbered consecutively in order of
  reference; variables italic; small inline fractions with a solidus (X/Y).

## Language variant

American **or** British English, applied consistently — never mixed.

## Author contributions — CRediT

The corresponding author acknowledges contributions via the CRediT taxonomy
(Conceptualization, Data curation, Formal analysis, Funding acquisition,
Investigation, Methodology, Project administration, Resources, Software,
Supervision, Validation, Visualization, Writing – original draft, Writing –
review and editing). Prepare the statement in its own section near the
acknowledgements before submission.

## Generative-AI disclosure

Declare any use of generative AI in manuscript preparation at submission. AI used
to *write* the manuscript is disclosed in a dedicated section placed **before
the reference list**; authors are responsible for verifying all AI-generated
content, including citations (which can be fabricated). AI is not permitted for
figure creation/alteration except where AI is the research method itself.

## Research data, funding, conflicts

- **Option C**: deposit research data in a repository and cite/link it (with a
  `[dataset]` reference), or state why sharing is impossible. A data-availability
  statement is required at submission.
- Disclose all funding sources; if none, state so explicitly.
- Declare conflicts of interest via Elsevier's declarations tool.

## Submission formats

- Accepted source formats: `.doc`, `.docx`, `.tex`. **PDF is not accepted.**
- Word documents must be **single-column**; double-column is only for LaTeX.
- An Elsevier LaTeX template is provided and encouraged for technical papers.
