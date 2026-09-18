#!/usr/bin/env python3
from decimal import Decimal, InvalidOperation

ALLOWED_CURRENCY={"TRY","USD","EUR","GBP"}
CONSEQUENTIAL={"refund","payment","price_override","external_publish","delete"}

def decide(case):
    # R1 Mandatory + source provenance.
    mandatory=("source_id","action_type","currency","quantity","term")
    missing=[k for k in mandatory if case.get(k) in (None,"")]
    if missing or not case.get("source_verified"):
        return "STOP_ESCALATE"
    # R2 Currency allow-list.
    if case["currency"] not in ALLOWED_CURRENCY:
        return "HUMAN_REVIEW"
    # R3 Quantity positive numeric.
    try:
        q=Decimal(str(case["quantity"]))
    except (InvalidOperation, ValueError):
        return "HUMAN_REVIEW"
    if q <= 0:
        return "HUMAN_REVIEW"
    # R4 Duplicate/conflict visibility.
    if case.get("conflict"):
        return "STOP_ESCALATE"
    if case.get("duplicate"):
        return "HUMAN_REVIEW"
    # R5 Consequential actions require authorized human approval.
    if case["action_type"] in CONSEQUENTIAL:
        return "HUMAN_APPROVAL"
    return "AUTO_PROCEED"

BASE={"source_id":"SRC-1","action_type":"classify","currency":"TRY","quantity":2,"term":"net30","source_verified":True}
TESTS=[
 ("R1-positive",{},"AUTO_PROCEED"),
 ("R1-negative",{"source_verified":False},"STOP_ESCALATE"),
 ("R2-positive",{"currency":"EUR"},"AUTO_PROCEED"),
 ("R2-negative",{"currency":"JPY"},"HUMAN_REVIEW"),
 ("R3-positive",{"quantity":"3.5"},"AUTO_PROCEED"),
 ("R3-negative",{"quantity":0},"HUMAN_REVIEW"),
 ("R4-positive",{"duplicate":False,"conflict":False},"AUTO_PROCEED"),
 ("R4-negative",{"duplicate":True},"HUMAN_REVIEW"),
 ("R5-positive",{"action_type":"summarize"},"AUTO_PROCEED"),
 ("R5-negative",{"action_type":"refund"},"HUMAN_APPROVAL"),
]

def main():
    failures=[]
    for name,patch,expected in TESTS:
        c=dict(BASE); c.update(patch)
        got=decide(c)
        if got!=expected: failures.append((name,got,expected))
    if failures: raise SystemExit(f"FAIL {failures}")
    print("PASS 10/10 deterministic cases")
    print("PASS 5/5 critical rule families with positive + negative coverage")
if __name__=="__main__": main()
