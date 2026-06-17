# 示例片段：PBCNet2.0 类文章

结构深度学习药物设计文章应先说明任务设定。不要只写“模型预测亲和力”，而要讲清楚它预测的是 absolute affinity、relative affinity、binding pose、activity cliff，还是 lead optimization 中的优先级排序。任务定义错了，后面所有指标解释都会偏。

如果是 PBCNet2.0 类文章，开头应强调：模型不是泛化到任意小分子的全局打分函数，而是面向同一靶点、同一化学系列中两个结构相近配体的 relative affinity prediction。这个边界很重要，因为它决定了模型适合 lead optimization，而不是替代 docking score 或通用 ADMET 预测器。

逐图时，数据构建图要解释 reference/query pair 如何产生，为什么成对输入能把靶点、构象和化学系列背景固定住。模型图要解释 equivariant message passing 如何处理 3D 复合物，sign-flip augmentation 为什么能把“哪个配体更强”变成对称学习问题。Benchmark 图要说明使用什么数据集、什么 split、什么 baseline，以及指标对应排序、方向判断还是数值误差。

消融实验不能只写“性能下降”。要说明下降对应哪个设计选择：如果去掉 pairwise formulation，说明相对比较信息很关键；如果去掉结构等变模块，说明 3D pose 信息不是装饰；如果去掉 augmentation，说明模型可能学到输入顺序偏差。最后的机制或 case study 部分要回到化学解释，说明模型是否捕捉到氢键、疏水填充、构象冲突或 activity cliff，而不是只报告一个更高的 AUC。
