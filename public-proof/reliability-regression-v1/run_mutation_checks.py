#!/usr/bin/env python3
import csv
import sys
from pathlib import Path
from run_regression import decide

def main(path: str) -> int:
    rows = list(csv.DictReader(Path(path).open(encoding="utf-8")))
    detected = 0
    details = []
    for row in rows:
        action, gate, reason = decide(row)
        expected_gate = row["human_gate"].strip().lower() == "yes"
        mismatch = (
            action != row["expected_action"]
            or gate != expected_gate
            or reason != row["expected_reason"]
        )
        detected += int(mismatch)
        details.append((row["mutation_id"], row["case_id"], mismatch))

    print(f"mutations={len(rows)} detected={detected}")
    for mutation_id, case_id, ok in details:
        print(f"{mutation_id} {case_id} {'DETECTED' if ok else 'MISSED'}")
    return 0 if detected == len(rows) else 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python run_mutation_checks.py mutation_checks.csv")
    raise SystemExit(main(sys.argv[1]))
