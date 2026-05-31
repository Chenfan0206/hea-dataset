# KnowMat-minerU HEA Public Release

KnowMat-minerU is an extraction pipeline for high-entropy alloy (HEA),
multi-principal-element alloy (MPEA), and complex concentrated alloy (CCA)
literature.

This public release is intentionally scoped to HEA-related workflows. Prompts,
routing logic, and public documentation for unrelated material directions have
been removed.

## Scope

The retained workflow supports:

- PDF/OCR parsing with MinerU or PaddleOCR-compatible pipelines
- HEA/MPEA/CCA paper routing
- structured extraction around Composition -> Processing -> Structure -> Properties
- additive-manufactured HEA process parameter extraction
- HEA microstructure and phase extraction
- HEA mechanical, corrosion, oxidation, thermal, magnetic, and electrochemical property extraction
- quality evaluation, validation, and human review guidance

## Directory Layout

```text
KnowMat-minerU/
├── prompts/       # HEA-scoped prompt templates
├── src/           # extraction pipeline source code
├── scripts/       # utility scripts
├── tests/         # tests for core pipeline behavior
├── configs/       # local configuration placeholders
├── models/        # local model placeholder
├── references/    # local reference placeholder
└── tools/         # developer utilities
```

Historical reports, evaluation outputs, raw example files, feedback folders,
and notebooks are not included in this public release.

## Installation

Python 3.11 is recommended.

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -e .
pip install -r requirements.txt
```

For GPU OCR dependencies, see `requirements-gpu.txt`.

## Configuration

Copy `.env.example` to `.env` and fill in the required local API keys and OCR
configuration.

```bash
cp .env.example .env
```

Do not commit `.env`.

## Prompts

Public prompts are in `prompts/`.

They are HEA-only by design:

- `subfield_detection.yaml` restricts routing to HEA/MPEA/CCA extraction.
- `extraction_system_template.txt` defines the HEA extraction rules.
- `extraction_user_template.txt` defines the HEA extraction workflow.
- `evaluation.yaml`, `validator.yaml`, and `flagging.yaml` support quality control.

## Notes

This directory is part of the `hea-dataset` repository and is intended to
support reproducible HEA dataset construction.
