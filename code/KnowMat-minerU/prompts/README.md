# HEA Prompt Templates

This directory stores the public prompt templates used by KnowMat-minerU for
high-entropy alloy (HEA), multi-principal-element alloy (MPEA), and complex
concentrated alloy (CCA) extraction.

The public repository is intentionally scoped to HEA-related prompts only.
Prompts for unrelated material directions are not retained here.

## Files

- `extraction_system_template.txt`: HEA extraction agent system prompt.
- `extraction_user_template.txt`: HEA extraction user prompt.
- `subfield_detection.yaml`: HEA-only routing and classification prompt.
- `evaluation.yaml`: extraction quality evaluation prompt.
- `validator.yaml`: aggregation validation prompt.
- `flagging.yaml`: final quality flagging prompt.

## Editing Rules

- Keep prompts HEA/MPEA/CCA scoped.
- Do not add routing examples for unrelated material directions.
- Keep placeholders such as `{paper_text}` and `{routing_supplements}` intact.
- Run prompt syntax checks after editing.
