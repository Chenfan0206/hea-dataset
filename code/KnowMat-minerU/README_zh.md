# KnowMat-minerU 高熵合金公开版

KnowMat-minerU 是面向高熵合金（HEA）、多主元合金（MPEA）和复杂浓缩合金（CCA）文献的数据抽取流水线。

本公开版本仅保留高熵合金相关流程。与其他材料方向相关的提示词、路由说明、过程输出、历史评测材料和杂项文件已删除。

## 范围

当前保留的能力包括：

- 基于 MinerU 或 PaddleOCR 兼容流程的 PDF/OCR 解析
- HEA/MPEA/CCA 文献路由
- 围绕“成分 -> 工艺 -> 组织结构 -> 性能”的结构化抽取
- 增材制造高熵合金工艺参数抽取
- 高熵合金相结构、析出相、晶粒、胞状/枝晶结构、偏析等组织信息抽取
- 高熵合金力学、腐蚀、氧化、热学、磁学、电化学等性能抽取
- 抽取质量评估、聚合验证和人工复核提示

## 目录结构

```text
KnowMat-minerU/
├── prompts/       # HEA 范围内的提示词模板
├── src/           # 抽取流水线源码
├── scripts/       # 工具脚本
├── tests/         # 核心行为测试
├── configs/       # 本地配置占位目录
├── models/        # 本地模型占位目录
├── references/    # 本地参考资料占位目录
└── tools/         # 开发辅助工具
```

本公开版本不包含历史报告、评测输出、原始示例数据、反馈文件夹和 notebook 中间材料。

## 安装

推荐使用 Python 3.11。

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -e .
pip install -r requirements.txt
```

如需 GPU OCR 依赖，可参考 `requirements-gpu.txt`。

## 配置

复制 `.env.example` 为 `.env`，并填写本地 API Key 和 OCR 配置。

```bash
cp .env.example .env
```

不要提交 `.env`。

## 提示词

公开提示词位于 `prompts/`，并已限制为 HEA 范围：

- `subfield_detection.yaml`：HEA/MPEA/CCA 路由提示词
- `extraction_system_template.txt`：HEA 抽取系统提示词
- `extraction_user_template.txt`：HEA 抽取用户提示词
- `evaluation.yaml`、`validator.yaml`、`flagging.yaml`：质量控制提示词

## 说明

本目录属于 `hea-dataset` 仓库，用于支撑高熵合金数据集构建流程复现。
