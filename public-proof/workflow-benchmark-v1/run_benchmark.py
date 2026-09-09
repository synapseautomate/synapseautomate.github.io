#!/usr/bin/env python3
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATASET = ROOT.parent / "reliability-regression-v1" / "test_cases.csv"
SUMMARY_CSV = ROOT / "benchmark_summary.generated.csv"
SUMMARY_JSON = ROOT / "benchmark_result.generated.json"


def baseline_action(row):
    """Approach A: naive baseline that always continues automatically."""
    return "AUTO_PROCEED"


def gated_action(row):
    """Approach B: deterministic source/input/risk/human-gate policy."""
    if row["adversarial_type"] != "none":
        return "BLOCK_AND_ESCALATE"
    if row["source_status"] != "verified":
        return "HUMAN_REVIEW"
    if row["input_quality"] in {"missing", "conflicting"}:
        return "HUMAN_REVIEW"
    if row["risk_level"] == "high":
        return "HUMAN_APPROVAL"
    if row["scenario_type"] == "external_action":
        return "HUMAN_APPROVAL"
    if row["risk_level"] == "medium" and row["scenario_type"] == "recommendation_support":
        return "HUMAN_REVIEW"
    return "AUTO_PROCEED"


def evaluate(name, fn, rows):
    predictions = [fn(r) for r in rows]
    matches = sum(p == r["expected_action"] for p, r in zip(predictions, rows))
    human_expected = [i for i, r in enumerate(rows) if r["human_gate"] == "yes"]
    human_captured = sum(predictions[i] != "AUTO_PROCEED" for i in human_expected)
    adversarial = [i for i, r in enumerate(rows) if r["adversarial_type"] != "none"]
    adversarial_blocked = sum(predictions[i] == "BLOCK_AND_ESCALATE" for i in adversarial)
    counts = Counter(predictions)
    return {
        "approach": name,
        "cases": len(rows),
        "policy_matches": matches,
        "policy_mismatches": len(rows) - matches,
        "human_gate_expected": len(human_expected),
        "human_gate_captured": human_captured,
        "adversarial_cases": len(adversarial),
        "adversarial_blocked": adversarial_blocked,
        "auto_proceed": counts["AUTO_PROCEED"],
        "human_review": counts["HUMAN_REVIEW"],
        "human_approval": counts["HUMAN_APPROVAL"],
        "block_and_escalate": counts["BLOCK_AND_ESCALATE"],
    }


def main():
    with DATASET.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    if len(rows) != 100:
        raise SystemExit(f"Expected pinned v1 dataset of 100 cases, got {len(rows)}")

    results = [
        evaluate("A_ALWAYS_PROCEED", baseline_action, rows),
        evaluate("B_RISK_GATED", gated_action, rows),
    ]

    a, b = results
    # Pinned v1 reproducibility gates. A version bump is required if the dataset changes.
    assert a["policy_matches"] == 36
    assert a["policy_mismatches"] == 64
    assert a["human_gate_captured"] == 0
    assert a["adversarial_blocked"] == 0
    assert b["policy_matches"] == 100
    assert b["policy_mismatches"] == 0
    assert b["human_gate_captured"] == 64
    assert b["adversarial_blocked"] == 15

    fields = list(results[0].keys())
    with SUMMARY_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    payload = {
        "version": "1.0.0",
        "date": "2026-09-09",
        "dataset": "../reliability-regression-v1/test_cases.csv",
        "synthetic_non_sensitive": True,
        "comparison_type": "decision-strategy benchmark; not an LLM model-quality benchmark",
        "results": results,
        "limits": [
            "synthetic deterministic policy test",
            "not production accuracy",
            "not ROI evidence",
            "not legal, medical, financial or compliance assurance",
            "latency and cost were not measured in this benchmark",
        ],
    }
    SUMMARY_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
