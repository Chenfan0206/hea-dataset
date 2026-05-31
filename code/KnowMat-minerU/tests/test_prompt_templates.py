from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_system_prompt_contains_specimen_boundary_guardrails():
    prompt = (ROOT / "prompts" / "extraction_system_template.txt").read_text(encoding="utf-8")

    assert "Do NOT automatically split every screening composition" in prompt
    assert "Do NOT split into a new item for test temperature" in prompt
    assert "comparison row/value/caption/legend entry" in prompt
    assert "process-state or recycle-state matrix" in prompt
    assert "broad literature landscape plots" in prompt
    assert "distinct benchmark labels/states were not collapsed" in prompt


def test_user_prompt_contains_targeted_examples_for_reference_and_over_split():
    prompt = (ROOT / "prompts" / "extraction_user_template.txt").read_text(encoding="utf-8")

    assert "Screening route should keep only retained upstream endpoints" in prompt
    assert "Never convert a test-condition matrix into extra items" in prompt
    assert "Figure-only benchmark labels still count as Reference items" in prompt
    assert "Powder-recycling matrices must stay expanded" in prompt
    assert "Do not invent precursor references from mechanism discussion" in prompt
    assert "Literature landscape plot does not license one Reference per historical point" in prompt
    assert "Do not collapse many benchmark labels into one umbrella reference" in prompt
