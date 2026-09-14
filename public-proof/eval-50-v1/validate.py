#!/usr/bin/env python3
import json,sys
from collections import Counter
from pathlib import Path
rows=[json.loads(x) for x in (Path(__file__).parent/'cases.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
c=Counter(r['category'] for r in rows); ids={r['case_id'] for r in rows}; splits=Counter(r['split'] for r in rows)
ok=len(rows)==50 and len(ids)==50 and c=={'normal':25,'exception':15,'attack':10} and splits=={'test':30,'dev':20} and all(r['synthetic'] and r['source_rights']=='synthetic' and r['expected_escalation'] for r in rows)
print({'count':len(rows),'categories':dict(c),'splits':dict(splits),'unique_ids':len(ids),'pass':ok})
sys.exit(0 if ok else 1)
