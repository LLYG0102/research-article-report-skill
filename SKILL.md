---
name: research-article-report
description: Create detailed Chinese research paper reading reports from PDFs, DOI links, arXiv links, publisher pages, or extracted paper text. Use when the user asks for 论文阅读报告, 论文总结, 文献精读, 组会汇报, 复现分析, paper report, figure-by-figure reading, or a report that explains background, method, figures, computational steps, wet-lab validation, costs, limitations, and research启发.
---

# Research Article Reading Report

## Purpose

Turn a research paper into a Chinese lab-meeting style reading report. The report must be source-grounded, figure-aware, and useful for reproduction planning. It is not an abstract rewrite.

The default output is a complete Markdown report unless the user asks for another format. Write mostly in connected Chinese prose. Use bullets only for comparable checklists such as wet-lab steps, reproduction risks, or cost ranges.

## Required References

Before drafting a full report, read these bundled references when available:

- `references/model-report-style.md`: style signals distilled from the two model reports and domain-specific writing patterns.
- `references/reproducibility-extraction.md`: fields to extract for methods, code/data, computational pipelines, wet-lab validation, and reproduction cost.

Use templates and checklists only as scaffolds; do not paste them mechanically.

## Workflow

1. **Extract the paper before writing.**
   - For PDFs, extract text in reading order and inspect figure pages or captions. Do not rely only on the abstract.
   - Capture title, authors when useful, venue, year, DOI, article type, abstract, introduction, main result sections, figure captions, methods or supplementary method links, data/code availability, and limitations.
   - If extraction fails for figures, state the limitation and base the report on captions/text instead of inventing visual details.

2. **Build a source evidence ledger.**
   - Identify the paper's main question, previous bottleneck, proposed route, and what counts as success.
   - Record every main figure and subfigure. For each subfigure, know what it shows, what metric/readout it uses, what conclusion it supports, and whether it is computational prediction, wet experiment, structural validation, or statistical analysis.
   - Record all numbers that matter: dataset scale, train/test split, baselines, success rate, affinity, RMSD, pAE/pLDDT/AUC/FDR, replicate count, hit rate, structure resolution, or cost-relevant throughput.

3. **Classify the paper before choosing emphasis.**
   - AI/model paper: emphasize task definition, inputs/outputs, architecture, training data, objectives, evaluation splits, baselines, ablations, inference/filtering, and failure modes.
   - Protein/drug/structure design paper: emphasize design specification, generation/screening pipeline, sequence or molecule filtering, wet-lab validation, binding versus function, and structural confirmation.
   - Experimental biology paper: emphasize assay design, controls, replicates, mechanism, causality limits, and validation chain.
   - Review/perspective: emphasize thesis, conceptual framework, evidence base, unresolved questions, and how the framework changes research planning.

4. **Draft in the standard report shape.**
   - Title block with paper metadata and source.
   - `文章主要想解决什么问题`
   - `方法思想与技术路线`
   - `逐图阅读`, covering all main figures and important Extended Data/Supplementary figures when they carry key evidence.
   - `文章中所有由计算机完成的部分和重要方法`
   - `复现需要抓住的关键条件`
   - `文章中完成的湿实验内容和大致成本估计`
   - `启发与局限`

5. **Write subfigure paragraphs, not caption dumps.**
   - Each subfigure discussion should answer: `画了什么 -> 读数/坐标/颜色是什么意思 -> 证明什么 -> 它在证据链中推进了哪一步`.
   - Group subfigures only when they are genuinely one result block, for example `Fig. 2c-e`.
   - Distinguish computational structure predictions from experimental structures. Distinguish binding from function, affinity from activity, and in silico success from wet-lab success.

6. **Make reproduction useful.**
   - Separate paper-disclosed facts from inference. Use phrases such as `论文披露`, `作者没有给出`, `以下为复现时需要补齐`, and `以下为粗略估计`.
   - Extract enough information for a reader to attempt reproduction: data, preprocessing, model/checkpoint, training or inference settings, filtering thresholds, hardware/software, wet-lab assay, controls, replicates, and decision gates.
   - If the paper omits key details, say exactly what is missing and where it would affect reproduction.

7. **Cost estimates must be bounded and labelled.**
   - If the paper does not disclose cost, write `论文没有披露真实经费，以下为粗略估计`.
   - Give ranges, not precise single prices. Separate small reproduction, medium project, and near-original scale when enough information exists.
   - Only estimate experiments that the paper performed or that are necessary for reproduction.

## Quality Gate

Before finalizing, verify:

- The report explains the scientific problem, why previous work was insufficient, and what the paper's route changes.
- Every main figure is covered with subfigure-level references such as `Fig. 1a`.
- The report includes concrete metrics or named experiments, not only qualitative praise.
- Computational work, wet-lab work, and author conclusions are separated.
- Reproduction-critical missing details are named instead of silently filled in.
- Cost and feasibility claims are explicitly labelled as estimates or inference.
- The final section gives research-facing启发 and bounded limitations.

## Output Style

Use fluent Chinese. Keep standard English terms when they improve precision, such as `RFdiffusion`, `ProteinMPNN`, `binder`, `active learning`, `pAE`, `BLI`, `SPR`, `cryo-EM`, `IC50`, `EC50`, `AUC`, `FDR`, and `ablation`. Explain specialized terms briefly on first use when needed.

Avoid long bullet-only answers. The reader should feel they are reading a senior student's group-meeting report: narrative, specific, and honest about uncertainty.
