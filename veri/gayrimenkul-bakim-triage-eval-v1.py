#!/usr/bin/env python3
import csv
from pathlib import Path

path = Path(__file__).with_name('gayrimenkul-bakim-triage-spec-v1.csv')
rows = list(csv.DictReader(path.open(encoding='utf-8')))

def yes(v):
    return str(v).strip().lower() == 'yes'

before_match = sum(yes(r['baseline_match']) for r in rows)
after_match = sum(yes(r['controlled_match']) for r in rows)
before_critical_miss = sum(
    yes(r['critical_if_missed']) and r['baseline_state'] == 'AUTO_PROCEED'
    for r in rows
)
after_critical_miss = sum(
    yes(r['critical_if_missed']) and r['controlled_state'] == 'AUTO_PROCEED'
    for r in rows
)
routine = [r for r in rows if r['expected_state'] == 'AUTO_PROCEED']
before_routine = sum(r['baseline_state'] == 'AUTO_PROCEED' for r in routine)
after_routine = sum(r['controlled_state'] == 'AUTO_PROCEED' for r in routine)

print(f'cases={len(rows)}')
print(f'before_match={before_match}/{len(rows)}')
print(f'controlled_match={after_match}/{len(rows)}')
print(f'critical_miss={before_critical_miss}->{after_critical_miss}')
print(f'routine_auto={before_routine}/{len(routine)}->{after_routine}/{len(routine)}')
