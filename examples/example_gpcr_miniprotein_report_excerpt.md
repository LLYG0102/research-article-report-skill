# 示例片段：GPCR miniprotein 设计类文章

这类文章不能只写“设计了 GPCR binder”，而要强调证据链：计算生成候选、高通量细胞筛选、体外结合验证、功能验证、结构验证和体内药理。报告开头应先说明 GPCR 靶点为什么难：膜蛋白构象动态强、正构/变构位点复杂、binding 不必然带来 signaling modulation，因此设计 miniprotein 不只是找到一个能贴上去的蛋白。

逐图时，Fig. 1a 应介绍 RFdiffusion、motif-guided RFdiffusion 和 MetaGen 的互补关系。RFdiffusion 负责从约束生成 backbone，motif-guided 版本把关键结合构象固定住，MetaGen 则更像 scaffold mining 和过滤 pipeline，而不是一个全新的神经网络。若文章使用 AlphaFold metaproteome scaffold mining、Rosetta RifDock、ProteinMPNN、AF2 initial guess 和 Rosetta metrics，报告要把这些步骤串成候选生成和筛选路线。

Fig. 1b 这类细胞筛选图要讲清 assay logic。例如 RD/retention display 不是普通荧光图，而是把 GPCR-binder 结合转化为 ER retention 或共定位表型。Fig. 1f-g 若比较 OPS-RD、yeast display 和 SPR，就要解释三者分别读出细胞内共定位、展示体系结合和体外亲和力；它们一致时，说明筛选信号不是单纯成像伪影。

功能图必须区分 binding、agonism、antagonism 和 allosteric modulation。剂量依赖曲线如果只显示结合增强，不能写成激动剂；只有 cAMP、calcium mobilization、β-arrestin recruitment 或类似 signaling readout 支持时，才可以讨论功能调控。结构图也要区分 AF2 预测模型、设计模型和实验结构；若没有 cryo-EM 或 X-ray，就不能写成“结构已证实”。
