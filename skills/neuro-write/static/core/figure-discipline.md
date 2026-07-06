# Figure discipline (journal-agnostic)

The generic figure method: a three-level information hierarchy, colourblind-safe
semantic colour, editable-vector output discipline, and caption conventions. The
paper's specific figure *plan* — which figure carries which result, and the
paper-wide colour assignments — belongs to the project profile supplied at
runtime, not here.

## Three mandatory matplotlib rcParams

Put these at the top of every figure-generation script:

```python
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
plt.rcParams['svg.fonttype'] = 'none'    # text stays editable in Illustrator
```

`svg.fonttype = 'none'` is the key one — it keeps text as `<text>` nodes in the
SVG rather than converting to paths, so post-hoc editing (font substitution,
label fixes, journal-style adjustments) stays possible.

## Output format

- Primary output is always `.svg` (vector, editable in Illustrator or Inkscape).
- Secondary raster preview is `.png` at 300 dpi.
- For multi-panel figures, save the assembled figure as both `.svg` and `.png`.
  Save individual panels as `.svg` if a co-author may recompose the layout.

Match the venue's declared resolution and format requirements at export (the
venue profile carries the artwork-resolution table); the discipline above is the
authoring default that keeps those options open.

## Three-level information hierarchy

Multi-panel figures must obey a three-level hierarchy:

1. **Overview** — the first panel (top-left, typically) shows the global pattern
   or the experimental setup.
2. **Deviation** — the middle panels show where the data deviates from baseline,
   expectation, or other groups.
3. **Relationship** — the last panel(s) show how variables relate, or how the
   model's internal structure relates to the biology.

**No two panels may answer the same scientific question.** Panel redundancy is
the most common reviewer complaint about figures. Audit every multi-panel figure
against this rule before submitting. When laying out the paper's figures, assign
each panel a single question from the overview → deviation → relationship arc;
the concrete assignment is a project-profile decision, not a framework constant.

## Semantic colour

Use colour to encode *meaning*, not for decoration.

- Prefer a colourblind-safe categorical palette (e.g. Tableau-10, which follows
  Wong 2011 and prints legibly in greyscale).
- Fix one paper-wide convention that maps each recurring entity (a tissue class,
  a model family, a condition) to one colour, and reuse it in every figure. The
  specific mapping is declared in the project profile; the rule is only that it
  is consistent across the manuscript.
- For sequential data use a perceptually uniform colourmap (viridis, magma); for
  signed data use a diverging colourmap centred at zero.

Avoid:
- Rainbow / jet colourmaps for sequential data.
- Red–green dichotomies for categorical comparison — they fail for the ~8% of
  male readers with red–green colour-vision deficiency.

## Chart-type checklist

Standard idioms by use case:

| Use case                     | Chart type                                   | Notes                                        |
|------------------------------|----------------------------------------------|----------------------------------------------|
| Performance across models    | Forest plot or grouped bar                   | Grouped bar for 4–12 models; forest for 12+. |
| Performance across stages    | Heatmap or line plot                         | Heatmap for 4–6 conditions; line if continuous. |
| Effect size with CI          | Forest plot                                  | Mandatory error bars; vertical line at zero. |
| Ablation effect              | Horizontal bar                               | Sort by effect size descending.              |
| Stage-dependent pattern      | Line plot with CI band                       | Fill-between for the band.                   |
| Distribution across groups   | Box plot or violin                           | Show individual points if n < 30 per group.  |
| Correlation                  | Scatter + linear fit                         | Show 95% CI on the fit; report r and p in the caption. |
| Network / circuit anatomy    | 3D rendered isosurface                       | A dedicated 3D-rendering tool (e.g. PyVista).|
| Sequential heatmap           | Diverging colourmap if signed; sequential if magnitude only | |

## Caption conventions

- The caption starts with the noun phrase describing the figure's content
  ("Overall framework of the proposed method") — never "Fig. 1 shows".
- 3–6 sentences: the first gives the high-level purpose; the rest describe
  panels and any colour bars or axis units.
- Use (a), (b), (c) markers for subpanels, in both the caption and the figure.
- Explain colour and symbol encoding explicitly.
- End with statistical information where relevant ("ρ values are Spearman
  correlations across n = 290 subjects; q-values are BH-FDR adjusted").
- The rendered figure-reference form in body prose (e.g. "Fig. 1A" vs "Figure
  1A") is declared by the venue profile; in the draft, use the `[FIG: N]`
  placeholder and let the build resolve it.

## When to apply

Defer figure regeneration until the prose is close to final. Figures are easier
to revise than prose, and the prose sometimes shifts which result should be
foregrounded — which changes the layout. Plan a focused pass to redraw the
paper's figures once the Methods and Results are locked.
