#!/usr/bin/env python3
import csv, json, sys
from collections import Counter
from pathlib import Path

def decide(r):
    if r["content_instruction"] != "none": return "STOP_ESCALATE", "untrusted_content_instruction"
    if r["freshness"] == "stale" and r["action_type"] in {"price_update","stock_update","price_publish","stock_adjustment"}: return "STOP_ESCALATE", "stale_commerce_source"
    if r["write_scope"] == "not_granted" or r["data_egress"] == "unapproved_destination": return "STOP_ESCALATE", "authority_boundary"
    if r["source_status"] != "verified": return "HUMAN_REVIEW", "source_review"
    if r["input_quality"] in {"missing","conflicting","partial"}: return "HUMAN_REVIEW", "input:" + r["input_quality"]
    if r["risk_level"] == "high" or r["action_type"] in {"price_publish","refund_prepare","catalog_write","customer_message","stock_adjustment","external_send","price_update","stock_update"}: return "HUMAN_APPROVAL", "consequential_action"
    if r["risk_level"] == "medium": return "HUMAN_REVIEW", "medium_risk_review"
    return "AUTO_PROCEED", "verified_low_risk_read"

def main(path):
    rows=list(csv.DictReader(Path(path).open(encoding="utf-8")))
    failures=[]; states=Counter(); sev=Counter()
    for r in rows:
        s,reason=decide(r); states[s]+=1
        if s != r["expected_state"] or reason != r["expected_reason"]:
            failures.append({"case_id":r["case_id"],"severity":r["severity"],"expected":[r["expected_state"],r["expected_reason"]],"actual":[s,reason]}); sev[r["severity"]]+=1
    out={"suite":"Synapse Automate Reliability Regression v2","cases":len(rows),"passed":len(rows)-len(failures),"failed":len(failures),"critical_failures":sev["critical"],"major_failures":sev["major"],"minor_failures":sev["minor"],"state_counts":dict(states),"failures":failures}
    print(json.dumps(out,ensure_ascii=False,indent=2)); return 1 if failures else 0
if __name__=="__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv)>1 else "cases.csv"))
