#!/usr/bin/env python3
import csv, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
P=ROOT/'D10/regression_30.csv'

def b(v): return str(v).lower()=='true'
def route(r):
    if b(r['adversarial_pattern']): return 'BLOCK_AND_ESCALATE'
    if not b(r['source_verified']): return 'HUMAN_REVIEW'
    if not b(r['input_complete']) or b(r['conflicting_input']): return 'HUMAN_REVIEW'
    if r['risk_level']=='high' or b(r['external_action']): return 'HUMAN_APPROVAL'
    return 'AUTO_PROCEED'
rows=list(csv.DictReader(P.open(encoding='utf-8')))
fails=[]
for r in rows:
    got=route(r)
    if got!=r['expected_route']: fails.append((r['case_id'],r['expected_route'],got))
if fails:
    print('FAIL',fails); raise SystemExit(1)
print(f'PASS: {len(rows)}/{len(rows)} regression cases')
