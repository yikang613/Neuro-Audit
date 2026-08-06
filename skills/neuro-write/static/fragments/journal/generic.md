# Journal profile: generic defaults

The journal-agnostic fallback. A real venue routes to this fragment plus its own
runtime overlay (`.neuro-audit/journal/<slug>/{venue,format,style}.yaml`), which
supplies the hard numbers. This file gives sensible defaults and, more
importantly, tells the writer where a value must come from the profile rather
than a guess. `journal/example.md` is the worked example of a fully-specified venue.

## Declared, never inferred

Every surface convention below is a *declared* profile field. Where the runtime
overlay specifies a value, that value wins and is hard. Where it is silent,
apply the stated default **and** flag the field as `NOT-CHECKED` rather than
presenting a guess as a rule. Do not infer a venue's constraints from its name.

## Section layout (default)

A neuroimaging methods paper typically runs:

1. **Introduction** — clinical/scientific motivation, gap, contribution.
2. **Related work** (optional).
3. **Methods** — problem formulation, architecture, training.
4. **Experiments / Results** (sometimes merged, sometimes split).
5. **Interpretability / biomarker analysis** (where it is a substantive
   contribution).
6. **Discussion** — interpretation, comparison, limitations, future work.
7. **Conclusion** — short, usually one paragraph.
8. **References**.

Sub-sections nest 2–3 levels deep when warranted; every numbered header has
content. The exact section-numbering scheme (e.g. `1.1.1` decimal vs. another) is
a declared profile field.

## Citation form (default)

Default to author–year, `(Author, year)`, grouped at the end of a clause and
separated by semicolons for multiple references. Whether the venue actually uses
author–year or a numeric scheme is a **declared** field — consult the overlay.
In the draft, always use `[CITE:]` placeholders and let the build render the
declared form.

## Figure and table references (default)

Default rendered form is "Fig. N" / "Table N" (period after "Fig"), figures
numbered in order of first appearance, each cited at least once from the body.
The exact rendered string is a declared field. In the draft, use `[FIG: N]` /
`[TABLE: N]` placeholders.

## Abstract, keywords, structure (consult the profile)

There is **no** safe default word limit, keyword count, or highlights
requirement — these vary widely across venues and a wrong guess is a real error.
Read them from the profile; if absent, report `NOT-CHECKED` and ask. The same
holds for required auxiliary artefacts (highlights, graphical abstract, CRediT
statement, data-availability statement, AI-disclosure placement) and accepted
submission file formats.

## Language variant

Write in American or British English, consistently — never a mixture. The chosen
variant is a project decision; if unstated, pick one and apply it throughout.

## Where the hard constraints live

For any of: abstract length, section numbering, citation rendering,
figure-reference rendering, required highlights/graphical-abstract, table style,
keyword rules, CRediT, AI-disclosure placement, and submission formats — the
authoritative source is the venue overlay. See `journal/example.md` for a fully
worked instance of every one of these fields.
