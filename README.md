# HEA Dataset

本仓库整理了材料文献解析、结构化抽取与多模态对齐数据集的提交材料。仓库包含两部分核心内容：

1. 解析后的数据集及标准数据集下载入口
2. KnowMat-minerU 高熵合金公开版数据抽取与解析代码

## 仓库结构

```text
hea-dataset/
├── dataset/
│   └── organized_75papers_dataset/
│       ├── README.md
│       ├── manifest.csv
│       ├── manifest.json
│       └── papers/
└── code/
    └── KnowMat-minerU/
        ├── README.md
        ├── README_zh.md
        ├── src/
        ├── scripts/
        ├── prompts/
        ├── configs/
        └── tests/
```

## 数据集说明

数据集位于 `dataset/organized_75papers_dataset/`，每篇论文对应 `papers/序号__论文题目/` 下的一个独立文件夹。

每篇论文目录内包含三类内容：

- `01_extracted_content/`：原始 PDF、解析结果 `extracted.json`、人工标注 `human_annotation.json`
- `02_images/`：论文图片资源
- `03_multimodal_alignment/`：图文多模态对齐结果，以及每张图 top5 文本候选的 JSONL/CSV 展开

数据集规模：

- 标准数据集合计覆盖 2000 余篇材料论文，包含大规模结构化抽取条目与多模态图文资源
- 当前仓库内提供 75 篇论文的解析后数据子集，便于快速查看目录结构、字段组织和图文对齐格式
- 当前仓库内数据子集包含图片记录数：836
- 当前仓库内数据子集包含图文候选对数：4180

索引文件：

- `dataset/organized_75papers_dataset/manifest.csv`
- `dataset/organized_75papers_dataset/manifest.json`

## 标准数据集下载

额外的标准数据集文件存放在百度网盘，合计覆盖 2000 余篇论文，数据规模更大、条目更丰富：

- 文件名：标准数据集
- 链接：[https://pan.baidu.com/s/17iJz7eHSg5BGGYWHZaarTA?pwd=8ujw](https://pan.baidu.com/s/17iJz7eHSg5BGGYWHZaarTA?pwd=8ujw)
- 提取码：`8ujw`

## 代码说明

代码位于 `code/KnowMat-minerU/`。

KnowMat-minerU 是面向高熵合金（HEA）、多主元合金（MPEA）和复杂浓缩合金（CCA）文献的数据抽取流水线，支持从 PDF/TXT 文献中抽取结构化合金数据，并结合 OCR、LLM、多代理抽取、质量评估与人工复核标记生成机器可读结果。

主要能力包括：

- 批量处理 PDF/TXT 文献
- 支持 MinerU API、PaddleOCR API 或本地 OCR
- 抽取高熵合金成分、工艺条件、表征信息和性能数据
- 生成结构化 JSON、解析报告和质量评估结果
- 支持大规模并行处理与断点恢复

代码的详细安装和运行方式见：

- `code/KnowMat-minerU/README_zh.md`
- `code/KnowMat-minerU/README.md`

## 整体流程

本仓库对应的数据构建流程如下：

1. 论文收集

   收集高温结构材料相关论文，形成待解析 PDF 文献集合。

2. 文献解析

   使用 KnowMat-minerU 对论文进行 OCR 与版面解析，提取正文、表格、公式、图片及元信息。

3. 结构化抽取

   基于材料科学抽取提示词和多代理流水线，从解析文本中抽取材料成分、制备工艺、组织结构、测试条件和性能指标等结构化字段。

4. 图片与文本整理

   汇总论文图片、图注、正文候选片段和解析文本，为后续图文对齐准备统一的数据结构。

5. 多模态对齐

   对论文图片与相关文本片段进行匹配，形成每张图对应的 top5 文本候选，并导出 JSONL/CSV 格式的对齐结果。

6. 人工复核与质量控制

   结合自动质量评估结果与人工标注，对抽取结果、图文对齐关系和异常样本进行复核。

7. 数据集组织

   按论文粒度统一组织为 `papers/序号__论文题目/` 目录，并生成 `manifest.csv` 与 `manifest.json` 作为全局索引。

## 快速查看

查看数据集索引：

```bash
cd dataset/organized_75papers_dataset
python -m json.tool manifest.json | head
```

查看代码运行说明：

```bash
cd code/KnowMat-minerU
cat README_zh.md
```

## 来源文件

本仓库由以下素材包整理得到：

- `GitHub的素材/organized_75papers_dataset_new.zip`
- `GitHub的素材/KnowMat-minerU.zip`
- 百度网盘标准数据集：链接 [https://pan.baidu.com/s/17iJz7eHSg5BGGYWHZaarTA?pwd=8ujw](https://pan.baidu.com/s/17iJz7eHSg5BGGYWHZaarTA?pwd=8ujw)，提取码 `8ujw`
