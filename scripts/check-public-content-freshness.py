#!/usr/bin/env python3
from pathlib import Path
from datetime import date
import json, sys

path=Path(__file__).resolve().parents[1]/"veri/public-content-version-registry-v1.json"
data=json.loads(path.read_text(encoding="utf-8"))
today=date.today()
errors=[]
for a in data.get("assets",[]):
    due=date.fromisoformat(a["review_due_at"])
    if a.get("status")=="current" and due < today:
        errors.append(f"STALE current asset: {a['url']} review_due_at={due.isoformat()}")
    if a.get("external_expert_reviewed") not in (False, True):
        errors.append(f"Invalid expert-review flag: {a['url']}")
if errors:
    print("\n".join(errors))
    sys.exit(2)
print(f"PUBLIC CONTENT FRESHNESS: PASS ({len(data.get('assets',[]))} assets checked; {today.isoformat()})")
