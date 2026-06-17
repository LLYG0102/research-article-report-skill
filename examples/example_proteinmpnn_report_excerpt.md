# 示例片段：ProteinMPNN 类文章

这类文章的核心不是“提出一个会生成序列的模型”这么简单，而是要证明深度学习序列设计可以在真实实验中替代或改进 Rosetta。阅读报告开头应先说明蛋白设计的反问题：给定 backbone，寻找能折叠到该结构并满足功能约束的序列。ProteinMPNN 的重要性在于，它把 backbone 看成 residue graph，用 message passing 学习结构到序列的映射，并通过 random decoding order、固定位置和 tied positions 支持 motif、靶蛋白界面、同源寡聚体、异源复合物、重复蛋白和纳米颗粒设计。

逐图时，Fig. 1a 不能只写“模型结构示意图”。要说明模型输入是 N、Cα、C、O 和 virtual Cβ 等 backbone 几何信息，encoder 更新节点和边特征，decoder 按某个顺序逐步生成氨基酸。Fig. 1b 的重点是 random decoding order：它让模型既能从已有上下文预测未设计位点，也能保留固定 motif 或固定靶蛋白。Fig. 1c 的 tied positions 是对称设计的关键，因为它把多个对称位点约束为相同氨基酸选择。

Fig. 2 的 benchmark 要分层解释。Sequence recovery 高说明模型能恢复天然结构约束，但这不等价于设计成功；训练噪声可能降低 PDB recovery，却提高对设计 backbone 的鲁棒性。更关键的是 ProteinMPNN redesign 能让 Rosetta NTF2 scaffold 更容易被 AlphaFold 单序列预测回目标结构，这个结果把“模型会预测天然序列”推进到“模型能救回人工设计骨架”。

如果论文有实验验证，报告要说明验证的是哪一层：表达和可溶性证明蛋白能制备，CD/thermal melt 证明折叠和稳定，晶体结构或 cryo-EM 才证明原子级结构是否接近设计模型。不要把 AlphaFold 预测写成实验结构，也不要把 sequence recovery 写成真实功能。
