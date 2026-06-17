# Model Report Style Guide

This reference distills the two model report excerpts in `examples/` into reusable writing rules. Read it before drafting a full paper report.

## Common Style Signals

The report should first explain the task and evidence chain, then enter figure details. Do not start by translating the abstract. A good opening tells the reader:

- what the field wants to do;
- what previous methods could not do;
- what the paper changes technically;
- what evidence would convince us that the change is real.

The body should be mostly continuous prose. Figure sections can be structured, but each subfigure still needs interpretation, not only a caption rewrite. Use a compact rhythm:

`Fig. 2b 做了什么。读数/颜色/坐标代表什么。它说明什么。它把证据链从哪一步推进到哪一步。`

## ProteinMPNN-Style Reports

For a sequence-design or structure-to-sequence model paper, do not summarize it as "a model that generates sequences". Start from the inverse protein-folding problem: given a backbone, find sequences that fold to it.

Key details to preserve:

- inputs: backbone atoms such as N, Cα, C, O and virtual Cβ;
- representation: residue graph, node/edge features, message passing;
- decoding: autoregressive or random decoding order, tied positions, fixed residues or motifs;
- benchmarks: sequence recovery, AlphaFold single-sequence recapitulation, Rosetta comparison, designed-backbone robustness;
- experimental or structural validation when present.

The figure reading should explain why each result matters. For example, a sequence recovery plot is not only "higher is better"; it tests whether the model learns native sequence constraints. A redesign/rescue figure is more important for design because it asks whether generated sequences make non-natural backbones fold as intended.

## GPCR Miniprotein-Style Reports

For de novo binder or miniprotein papers, the report must preserve the evidence chain:

`computational design -> high-throughput screen -> binding validation -> functional assay -> structural validation -> in vivo or pharmacology if present`.

Do not conflate:

- `binding`: the designed protein physically interacts with the target;
- `agonism`: it activates receptor signaling;
- `antagonism`: it blocks signaling;
- `allosteric modulation`: it changes signaling through a non-orthosteric mechanism;
- `target engagement`: it binds in cells or organisms under relevant conditions.

If a paper uses a pipeline such as RFdiffusion plus MetaGen, explain what each part contributes. MetaGen-like pipelines are often not new neural networks; they may be scaffold-mining and filtering workflows using AlphaFold metaproteome structures, docking, ProteinMPNN, AF2 initial guess, and Rosetta metrics.

For cell-screening figures, explain the phenotype that converts binding into an observable signal. For example, ER-retention or co-localization screens should be described as assay logic, not just microscopy images.

## PBCNet/Drug-Design-Style Reports

For structure-based drug design papers, define the prediction task precisely. Do not say "predicts affinity" unless the paper truly predicts absolute affinity. Identify whether the task is:

- absolute binding affinity;
- relative affinity within one target and chemical series;
- binding pose;
- activity cliff;
- lead-optimization ranking;
- ADMET or developability.

When reading figures, preserve the connection between data construction, pair definitions, equivariant architecture, augmentation, benchmarks, ablations, and mechanism validation. A method may be useful only within a narrow design regime; state that boundary.

## Good Report Habits

- Explain why a method is appropriate for the paper's problem.
- Name baselines and controls. A model result without a baseline is weak evidence.
- Preserve hard numbers: hit rate, Kd, IC50, RMSD, pAE, AUC, sample count, resolution, enrichment, or success threshold.
- Say when an experiment validates only one layer of the claim. Binding does not prove function; predicted structure does not prove experimental structure.
- End with research-facing implications: what can be borrowed, what is hard to reproduce, and what would be the next experiment.
