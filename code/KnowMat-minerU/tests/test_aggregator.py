from knowmat.nodes import aggregator as aggregator_module


def test_aggregate_runs_merges_advanced_quantitative_features(monkeypatch):
    run_payloads = {
        1: {
            "compositions": [
                {
                    "composition": "Alloy-A",
                    "processing_conditions": "LPBF",
                    "characterisation": {"SEM": "cellular structure observed"},
                    "advanced_quantitative_features": {"Cell_Size_avg_um": 5.0},
                    "properties_of_composition": [],
                }
            ]
        },
        2: {
            "compositions": [
                {
                    "composition": "Alloy-A",
                    "processing_conditions": "LPBF + aging",
                    "characterisation": {"TEM": "precipitates observed"},
                    "advanced_quantitative_features": {"Wall_Volume_Fraction_pct": 47.0},
                    "properties_of_composition": [],
                }
            ]
        },
    }

    monkeypatch.setattr(
        aggregator_module,
        "load_run_extraction",
        lambda run: run_payloads[run["run_id"]],
    )

    state = {
        "run_results": [
            {"run_id": 1, "confidence_score": 0.92},
            {"run_id": 2, "confidence_score": 0.88},
        ]
    }

    result = aggregator_module.aggregate_runs(state)
    comp = result["aggregated_data"]["compositions"][0]

    assert comp["characterisation"] == {
        "SEM": "cellular structure observed",
        "TEM": "precipitates observed",
    }
    assert comp["advanced_quantitative_features"] == {
        "Cell_Size_avg_um": 5.0,
        "Wall_Volume_Fraction_pct": 47.0,
    }
