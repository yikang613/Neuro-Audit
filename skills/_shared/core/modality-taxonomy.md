# Neuroimaging modality taxonomy

Shared vocabulary so every stage describes data consistently. The user's
*project* profile names the specific atlas, cohort, and pipeline; this file
gives the discipline-standard categories those choices instantiate.

## Modalities

- **fMRI (functional MRI).** BOLD signal. Resting-state or task. Yields
  **functional connectivity (FC)** — statistical dependence (usually Pearson or
  partial correlation) between regional time series.
- **dMRI (diffusion MRI).** Water-diffusion signal. Yields microstructural
  scalars (FA, MD, RD, AD) and, via tractography, a **structural connectivity
  (SC)** network — streamline counts / weights between regions.
- **sMRI (structural MRI).** T1/T2 anatomy. Yields morphometry (cortical
  thickness, volume, surface area) and the anatomical basis for parcellation.

## Levels of analysis (state which one)

- **Voxel / vertex level** — dense maps; mass-univariate testing territory.
- **Region / parcel level** — signals averaged within atlas nodes.
- **Network / connectome level** — a node×node matrix (FC or SC). Most
  brain-network deep-learning works here (e.g. a fixed 200-300 node connectome
  per subject). Preprocessing/QC of the *upstream* pipeline still governs its
  validity even when the day-to-day unit is the matrix.

## Connectome construction, briefly

- **Nodes** = atlas parcels (Brainnetome, Schaefer, AAL, Desikan-Killiany, …). The node set and
  ordering must be identical across every subject and cohort compared.
- **Edges** = FC (correlation of fMRI time series) or SC (tractography weight).
- **Common derived features** = edge weights, node strength/degree, graph-theory
  metrics (compute these with an established library, never re-derive by hand;
  metric definitions differ silently between libraries).

## What is in scope for neuro-audit

Describing, QC-checklisting, documenting, and auditing pipelines that produce the
above — and writing them up. **Running** the pipelines is out of scope (see
`neuro-invariants.md`, "auditor, not runner").
