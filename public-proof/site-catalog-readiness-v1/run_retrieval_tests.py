import json, pathlib
P=pathlib.Path(__file__).parent
store={x["source_id"]:x for x in json.loads((P/"context_store_v1.json").read_text())}
tests=json.loads((P/"retrieval_tests.json").read_text())
def decide(t):
    candidates=[store[x] for x in t["available"] if x in store and store[x]["topic"]==t["query_topic"]]
    if not candidates:return ("ESCALATE",None)
    if any(x["status"]=="conflict" for x in candidates):return ("ESCALATE",None)
    current=[x for x in candidates if x["status"]=="current"]
    if len(current)==1:return ("USE",current[0]["source_id"])
    return ("ESCALATE",None)
passn=0
for t in tests:
    got=decide(t); exp=(t["expected"],t["source"])
    ok=got==exp; passn+=ok; print(t["id"],"PASS" if ok else "FAIL",got)
print(f"{passn}/{len(tests)} PASS")
raise SystemExit(0 if passn==len(tests) else 1)
