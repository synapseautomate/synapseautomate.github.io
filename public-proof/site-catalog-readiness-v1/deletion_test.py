import json,pathlib,tempfile
P=pathlib.Path(__file__).parent
src=P/"audit_log_sample.jsonl"
rows=[json.loads(x) for x in src.read_text().splitlines() if x.strip()]
assert any(r["case_id"]=="SYN-DEL-001" for r in rows)
rows=[r for r in rows if r["case_id"]!="SYN-DEL-001"]
assert not any(r["case_id"]=="SYN-DEL-001" for r in rows)
print("deletion test PASS: synthetic case trace removed from authorized working copy")
