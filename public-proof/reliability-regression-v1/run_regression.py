#!/usr/bin/env python3
"""
Synapse Automate - Day 5 reliability regression v1
Deterministic policy regression over synthetic, non-sensitive test cases.

Usage:
    python run_regression.py test_cases.csv
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

def decide(row: dict) -> tuple[str, bool, str]:
    adversarial = row["adversarial_type"]
    source_status = row["source_status"]
    input_quality = row["input_quality"]
    risk = row["risk_level"]
    scenario = row["scenario_type"]

    if adversarial != "none":
        return "BLOCK_AND_ESCALATE", True, f"adversarial:{adversarial}"
    if source_status != "verified":
        return "HUMAN_REVIEW", True, f"source:{source_status}"
    if input_quality in {"missing", "conflicting"}:
        return "HUMAN_REVIEW", True, f"input:{input_quality}"
    if risk == "high":
        return "HUMAN_APPROVAL", True, "high_risk"
    if scenario == "external_action":
        return "HUMAN_APPROVAL", True, "external_action"
    if risk == "medium" and scenario == "recommendation_support":
        return "HUMAN_REVIEW", True, "medium_risk_recommendation"
    return "AUTO_PROCEED", False, "low_risk_verified"

def main(path: str) -> int:
    rows = list(csv.DictReader(Path(path).open(encoding="utf-8")))
    failures = []
    actual_counts = Counter()
    gated = 0

    for row in rows:
        actual_action, actual_gate, actual_reason = decide(row)
        actual_counts[actual_action] += 1
        gated += int(actual_gate)

        expected_gate = row["human_gate"].strip().lower() == "yes"
        if (
            actual_action != row["expected_action"]
            or actual_gate != expected_gate
            or actual_reason != row["expected_reason"]
        ):
            failures.append({
                "case_id": row["case_id"],
                "expected": {
                    "action": row["expected_action"],
                    "human_gate": expected_gate,
                    "reason": row["expected_reason"],
                },
                "actual": {
                    "action": actual_action,
                    "human_gate": actual_gate,
                    "reason": actual_reason,
                },
            })

    summary = {
        "suite": "Synapse Automate Day 5 Reliability Regression v1",
        "cases": len(rows),
        "passed": len(rows) - len(failures),
        "failed": len(failures),
        "pass_rate": round((len(rows) - len(failures)) / max(len(rows), 1), 4),
        "human_gated_cases": gated,
        "action_counts": dict(sorted(actual_counts.items())),
        "failures": failures,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if failures else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python run_regression.py test_cases.csv")
    raise SystemExit(main(sys.argv[1]))
