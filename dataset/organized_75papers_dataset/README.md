# Organized 75 Papers Dataset

每篇论文对应 `papers/序号__论文题目/` 一个文件夹，内部固定为三部分：

- `01_extracted_content/`：原始 PDF、`extracted.json`、`human_annotation.json`
- `02_images/`：原始图片 `figures/`
- `03_multimodal_alignment/`：多模图文对齐文件，以及每张图 top5 文本的 JSONL/CSV 展开

## 统计

- 论文总数：75
- 匹配到多模对齐的论文数：74
- 未匹配多模对齐的论文数：1
- 图片记录数：836
- 图文候选对数：4180

## 索引文件

- `manifest.csv`
- `manifest.json`

## 未匹配多模对齐的论文

- 022：Multiscale modeling of hydrogen diffusion in iron: Effect of applied stresses and dislocations（方向：增材）
