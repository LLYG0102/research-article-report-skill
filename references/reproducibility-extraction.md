# Reproducibility Extraction Guide

Use this reference when preparing the computational-method, wet-lab, cost, and reproduction sections of a report.

## PDF Extraction Targets

Before drafting, extract or inspect:

- title, authors, venue, year, DOI;
- abstract and introduction problem framing;
- all main result headings;
- all main figure captions and any key Extended Data/Supplementary captions;
- Methods or Supplementary Methods availability;
- data availability and code availability;
- acknowledgements when they reveal compute resources, facilities, or special reagents.

If the PDF text order is broken because of two-column layout, use captions, page rendering, and section headings to reconstruct the sequence. If a figure cannot be visually inspected, say so and avoid claims about visual patterns not stated in text/caption.

## Computational Reproduction Fields

For every computational pipeline, look for:

- input object and output object;
- dataset source, size, filters, redundancy removal, train/validation/test split;
- feature representation;
- model architecture or algorithm family;
- loss/objective and negative/positive sampling;
- training schedule, optimizer, batch size, hardware, random seeds, and checkpoints;
- inference settings: sampling temperature, diffusion steps, beam size, thresholds, number of candidates;
- ranking/filtering metrics and cutoff values;
- baselines and ablations;
- statistical tests and confidence intervals;
- released code, license, model weights, data links, and version numbers.

When details are absent, write `论文未披露` and explain why it matters. Example: `论文未披露训练随机种子和完整超参数，这会影响严格复现，但不影响理解主结论。`

## Wet-Lab Reproduction Fields

For each experiment, extract:

- purpose: what claim it validates;
- figure location;
- biological material: construct, protein, cell line, organism, target, ligand, antibody, mutant;
- controls: positive, negative, mock, wild type, mutant, known binder, vehicle;
- readout: affinity, activity, localization, expression, stability, structure, phenotype;
- replicate/sample count when disclosed;
- decision gate: what result counts as success;
- failure-sensitive steps: expression, purification, solubility, labeling, target quality, assay window.

## Cost Estimate Rules

Only estimate when the user asks or the skill's default report asks for wet-lab cost. Always mark estimates as estimates.

Use broad ranges and state dependencies. A useful format is:

- small reproduction: only a few key constructs or one benchmark;
- medium project: enough candidates for a publishable validation set;
- near-original scale: hundreds/thousands of constructs, high-throughput screening, structural biology, or animal work.

High-cost items to call out separately:

- large gene/library synthesis;
- protein expression and purification at scale;
- SPR/BLI/ITC assay development;
- high-throughput cell screening;
- cryo-EM/X-ray structure determination;
- animal efficacy or pharmacokinetics;
- commercial target proteins or antibodies.

Do not estimate experiments that the paper did not perform unless explicitly framed as `若要进一步验证`.

## Final Reproduction Section

The report should leave the reader with a practical view:

- the minimum viable reproduction route;
- the hardest missing details;
- the highest-risk experimental bottleneck;
- the approximate cost tier;
- what result would convince you that the reproduction succeeded.
