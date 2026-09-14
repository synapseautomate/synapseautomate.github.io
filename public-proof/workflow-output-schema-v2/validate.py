#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).parent
cases=json.loads((R/'test-cases.json').read_text(encoding='utf-8'))
ok=0
for c in cases:
    required={'case_id','decision','evidence','unknowns','human_gate'}
    good=required <= c.keys() and c['evidence'] and all(e.get('source_ref') and e.get('source_rights') in {'synthetic','public','customer-authorized'} for e in c['evidence'])
    if c['decision']!='AUTO_PROCEED': good=good and c['human_gate']['required'] is True
    if good: ok+=1
print(f'{ok}/{len(cases)} PASS')
sys.exit(0 if ok==len(cases)==10 else 1)
