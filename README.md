# Research Article Report Skill

一个用于生成中文科研论文阅读报告的 Agent skill。它面向论文 PDF、DOI/arXiv 链接或已提取正文，目标不是写普通摘要，而是生成适合组会、项目调研和复现规划的长文报告。

## 能做什么

这个 skill 会指导 Agent 先抽取论文元数据、正文结构、图注、Methods、数据/代码可用性和关键指标，再输出一份结构化中文阅读报告。报告重点包括：

- 文章解决的科学问题、过去方法的瓶颈和本文路线；
- 方法思想、输入输出、数据、模型/实验系统、baseline、ablation 和评价指标；
- 按 `Fig. 1a`、`Fig. 1b`、`Fig. 2c-e` 这种子图级别逐图解读；
- 单独总结所有计算机完成的部分和重要方法；
- 单独整理复现条件、缺失细节、风险点、湿实验内容和粗略成本估计；
- 区分论文事实、作者结论、复现推断和成本估算。

## 安装

把本仓库复制到 Agent 的 skills 目录，让 Agent 能读取根目录的 `SKILL.md` 即可。常见方式是：

```bash
git clone https://github.com/LLYG0102/research-article-report-skill.git
```

然后将仓库目录放到你的 Agent/LLM 平台支持的 skills 路径中。

## 如何调用

上传论文 PDF 后，对 Agent 说：

```text
请使用 research-article-report skill 写一份中文论文阅读报告，逐图到子图，并单独总结计算方法、复现条件、湿实验和成本估计。
```

如果你希望更偏复现，可以补一句：

```text
请特别关注论文披露了哪些复现信息、哪些关键参数缺失、最小复现路径是什么，以及哪些成本是估算。
```

## 输出风格

报告默认使用中文连续段落，保留必要英文术语，例如 `RFdiffusion`、`ProteinMPNN`、`BLI`、`SPR`、`cryo-EM`、`AUC`、`IC50`、`Kd`。它会尽量避免把图注机械翻译成列表，而是解释每个子图在证据链中的作用。

## 项目结构

- `SKILL.md`：Agent 触发后读取的核心工作流。
- `references/`：模范报告风格和复现信息抽取规范。
- `templates/`：报告、逐图解读、计算方法、湿实验成本的写作模板。
- `checklists/`：报告质量、子图定位、成本估计检查清单。
- `examples/`：ProteinMPNN、GPCR miniprotein、PBCNet 类论文的风格片段。
- `scripts/validate_skill_project.py`：轻量项目校验脚本。

## 校验

修改 skill 后可以运行：

```bash
python3 scripts/validate_skill_project.py
```

校验会检查关键文件、核心规则和 README 基本长度，防止项目入口或重要说明缺失。
