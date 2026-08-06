[![eval-gate](https://github.com/yikang613/Neuro-Audit/actions/workflows/eval-gate.yml/badge.svg)](../../actions)
![license](https://img.shields.io/badge/license-Apache--2.0-blue)

# neuro-audit

**An AI-agent _auditor_ (and writer) for neuroimaging manuscripts — for any
journal you declare.** It flags the domain pitfalls that quietly sink
neuroimaging papers — subject-level data leakage, site/scanner confounds,
circular analysis, effect-size inflation, causal/clinical overclaim — each
finding **grounded in a quote from your own text**, and it refuses to invent
statistics or citations.

I built neuro-audit after I nearly shipped a **seed-fold provenance bug** in my
own paper: a cross-validation number in the draft no longer matched the code
that generated it, and three rounds of human proofreading missed it. neuro-audit
is the reviewer I wish I'd had — it reconciles the numbers in your draft against
the results you actually computed, flags leakage and overclaim before a referee
does, and enforces journal rules that are **declared, never guessed**.

Scope note: **neuro-audit audits the neuroimaging _domain_, and adapts to your
_journal_.** The rigor checks are the same whether you submit to NeuroImage,
Medical Image Analysis, Human Brain Mapping, or Nature Neuroscience — because
they are about the _science_, not the venue. The journal you declare only
changes the writing/formatting layer.

> **Honest status (v0.x).** What works today: **`neuro-write`** and
> **`neuro-review`** (including the rigor pitfall audit, driven by the
> [pitfall catalog](skills/_shared/core/rigor-pitfall-catalog.md)). Still being
> built toward v1.0: **active grounding enforcement** (a stats MCP + a
> write-blocking hook), a standalone **`neuro-rigor`** skill, and a
> reporting-standard (COBIDAS) check. Items below are marked accordingly.

## What it does

| Capability | How you use it | State |
|---|---|---|
| **Rigor audit** of a draft | `/neuro-review` runs a panel of independent reviewer agents; the methodology reviewer applies the neuroimaging **pitfall catalog** and reports each issue **with a quote** and a severity — it surfaces candidates, it does not render a verdict. | ✅ ships |
| **Journal-styled drafting** | `/neuro-write <section>` drafts Methods/Results/etc. in your declared journal's style; every number is a `[STAT:]` placeholder and every reference is search-verified — nothing is invented. | ✅ ships |
| **Grounding (opt-in)** | Point it at the results file you exported (from wherever you ran the analysis); it flags any number in the draft that isn't in that file. **It never re-runs your code.** | ✅ ships (manual); 🚧 auto-enforcement (MCP + hook) toward v1.0 |
| **Reporting-standard audit** | Checks Methods completeness against neuroimaging reporting standards (e.g. COBIDAS). | 🚧 roadmap |
| **de-AI lens (optional)** | Flags AI-tells (em-dashes, over-hedging, altitude drift, dangling pronouns) and suggests edits — **flags, does not silently rewrite**. | 🚧 roadmap |
| **Journal profiles** `neuro-venue` · **Methods scaffolds** `neuro-preprocess` · **lit-scan** `neuro-litscan` | Runtime venue profiles, preprocessing documentation, neuroimaging-framed literature scan. | 🚧 v1.1–v1.2 |

## When to use it (manuscript lifecycle)

| Moment | Reach for | State |
|---|---|---|
| Drafting Methods/Results | `/neuro-write` — in-journal style, `[STAT:]` placeholders you fill from your real runs | ✅ |
| **Draft done, before submission** | **`/neuro-review` — the flagship: catch the domain pitfalls a referee would flag, before they do** | ✅ |
| After analysis, before finalizing numbers | opt-in grounding — reconcile the draft's numbers against your results file | ✅ |
| Switching target journal | only the style/format layer changes; the rigor audit re-runs unchanged | ✅ |
| Responding to reviewers | re-audit the revised draft | ✅ |

## Install

_Not yet published. Once released:_

```
/plugin marketplace add yikang613/Neuro-Audit
/plugin install neuro-audit@neuro-audit
```

## Usage

neuro-audit is a **content-agnostic framework**: it ships the process, you
supply the content at runtime.

1. **Declare your journal.** Name the venue you're targeting. Optionally paste
   its public author guidelines and a few exemplar-paper patterns so the writer
   can match style — values are recorded only as you state or confirm them
   (**declared, never inferred**).
2. **Provide your project context** in a private overlay. Create a `.neuro-audit/`
   directory in your repo (git-ignored; **never committed**) holding your journal
   profile, project terminology/notation, and — if you want grounding — the
   results file to reconcile against. Discovery order: `$NEURO_AUDIT_HOME` → walk
   up from the working directory → otherwise it halts and asks.
3. **Draft** — `/neuro-write methods` (or any section). You get journal-styled
   prose with `[STAT:]` placeholders and search-verified citations.
4. **Audit** — `/neuro-review <section-or-file>`. You get a prioritized list of
   grounded findings (each with a quote), for **you** to confirm — human in the
   loop, always.

## Design principles

- **Grounded, not asserted.** A statistic is either reconciled against a results
  artifact **you** provide, or it stays a `[STAT:]` placeholder — never narrated
  from the model's memory. Grounding is **opt-in** and **never re-runs your
  analysis** (auditor, not runner). Automatic enforcement (a stats MCP that
  captures `{value, ci, n, seed, input_hash}` + a `PreToolUse` hook that blocks
  an ungrounded write) is the v1.0 target.
- **Surface candidates, not verdicts.** Every finding carries a quote and a
  severity; the human decides. neuro-audit does not judge novelty or
  significance — those need the full field state and are hallucination-prone.
- **Generator ≠ evaluator.** Reviewer/auditor agents run in a fresh context from
  the writer, bounded to the fixed **pitfall catalog** — a persona told to
  "review" invents plausible critiques; a checklist grounded in quotes does not.
- **Declared, never inferred.** Journal rules come only from values you state or
  confirm. An unstated rule is `NOT-CHECKED`, never guessed.
- **Public framework, private content.** The framework is Apache-2.0 and open;
  your exemplar PDFs and unpublished manuscript content stay in the private,
  never-committed `.neuro-audit/` overlay (see [`NOTICE`](NOTICE)).
- **Specialize, don't reinvent.** The moat is neuroimaging domain knowledge (the
  [pitfall catalog](skills/_shared/core/rigor-pitfall-catalog.md), atlas/modality
  conventions), not generic audit or writing machinery.

## Roadmap

- **v1.0** — `neuro-write` + `neuro-review` + `neuro-rigor` (active grounding
  enforcement, standalone rigor auditor, COBIDAS reporting check); evaluated,
  CI-gated.
- **v1.1** — `neuro-venue` (runtime journal profiles) + `neuro-preprocess`
  (Methods documentation scaffolds) + the optional de-AI lens.
- **v1.2** — `neuro-litscan` + public release.

### Future directions

- A **community-contributed pitfall catalog** — new neuroimaging failure modes,
  each added with a checkable criterion and the evidence a reviewer must quote.
- Reporting standards beyond COBIDAS (journal- and modality-specific checklists).
- Deeper citation grounding (CrossRef / PubMed verification, reference-manager export).
- Broader modality / atlas coverage in the shared domain layer.
- Behavioral evals for the grounding hook and each reviewer dimension.
- Optional cross-cohort / external-validation reporting checks.

## License

Apache-2.0 (framework). See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE) for the
public-framework / private-content boundary.
