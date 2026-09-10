#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES = ROOT / "cases.csv"
EXPECTED_UNKNOWN = "unknown_or_unverified_never_autofilled"
VALID_ROUTES = {"AUTO_PROCEED", "HUMAN_REVIEW", "HUMAN_APPROVAL", "BLOCK_AND_ESCALATE"}
VALID_CLUSTERS = {"e_ticaret", "uretim_lojistik", "finans_operasyon"}


def as_bool(value: str) -> bool:
    return str(value).strip().lower() == "true"


def route(row):
    if as_bool(row["adversarial_pattern"]):
        return "BLOCK_AND_ESCALATE"
    if not as_bool(row["source_verified"]):
        return "HUMAN_REVIEW"
    if not as_bool(row["input_complete"]) or as_bool(row["conflicting_input"]):
        return "HUMAN_REVIEW"
    if row["risk_level"] == "high" or as_bool(row["external_action"]):
        return "HUMAN_APPROVAL"
    return "AUTO_PROCEED"


def main():
    with CASES.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    failures = []
    if len(rows) != 50:
        failures.append(f"expected 50 rows, found {len(rows)}")

    ids = [row["case_id"] for row in rows]
    if len(set(ids)) != len(ids):
        failures.append("duplicate case_id")

    for row in rows:
        cid = row["case_id"]
        if row["cluster"] not in VALID_CLUSTERS:
            failures.append(f"{cid}: invalid cluster")
        if row["unknown_rule"] != EXPECTED_UNKNOWN:
            failures.append(f"{cid}: unknown rule changed")
        if row["provenance_dataset"] != "synthetic" or as_bool(row["customer_data"]):
            failures.append(f"{cid}: provenance/customer-data invariant failed")
        if row["expected_route"] not in VALID_ROUTES:
            failures.append(f"{cid}: invalid expected route")
        actual = route(row)
        if actual != row["expected_route"]:
            failures.append(f"{cid}: expected {row['expected_route']}, got {actual}")

    if failures:
        print("FAIL")
        for item in failures:
            print("-", item)
        raise SystemExit(1)

    distribution = {}
    for row in rows:
        distribution[row["expected_route"]] = distribution.get(row["expected_route"], 0) + 1
    print("PASS: 50/50 synthetic provenance cases")
    print("customer_data=false for 50/50")
    print("unknown rule invariant: PASS")
    print("route distribution:", distribution)


if __name__ == "__main__":
    main()
