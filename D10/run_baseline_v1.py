#!/usr/bin/env python3
import csv, time, statistics, pathlib, json
ROOT=pathlib.Path(__file__).resolve().parents[1]
CASES=ROOT/'public-proof/provenance-50-v1/cases.csv'
rows=list(csv.DictReader(CASES.open(encoding='utf-8')))

def b(v): return str(v).lower()=='true'

def A(r):
    # Minimal single-step baseline: reacts only to explicit external action/high risk.
    if b(r['external_action']) or r['risk_level']=='high': return 'HUMAN_APPROVAL'
    return 'AUTO_PROCEED'

def B(r):
    # Structured context baseline: provenance + completeness + action gates, but no adversarial hard-stop.
    if not b(r['source_verified']) or not b(r['input_complete']) or b(r['conflicting_input']): return 'HUMAN_REVIEW'
    if r['risk_level']=='high' or b(r['external_action']): return 'HUMAN_APPROVAL'
    return 'AUTO_PROCEED'

def C(r):
    # Segmented + validator route: explicit adversarial block, provenance gate, then risk/authority gate.
    if b(r['adversarial_pattern']): return 'BLOCK_AND_ESCALATE'
    if not b(r['source_verified']): return 'HUMAN_REVIEW'
    if not b(r['input_complete']) or b(r['conflicting_input']): return 'HUMAN_REVIEW'
    if r['risk_level']=='high' or b(r['external_action']): return 'HUMAN_APPROVAL'
    return 'AUTO_PROCEED'

configs=[('A_single_step',A,1),('B_structured_context',B,2),('C_segmented_validator',C,3)]
out=[]; detail=[]
for name,fn,complexity in configs:
    timings=[]; correct=0; corrections=0
    for r in rows:
        st=time.perf_counter_ns(); pred=fn(r); timings.append((time.perf_counter_ns()-st)/1e6)
        ok=pred==r['expected_route']; correct+=ok; corrections += (not ok)
        detail.append({'config':name,'case_id':r['case_id'],'predicted_route':pred,'expected_route':r['expected_route'],'match':str(ok).lower()})
    out.append({
        'config':name,'cases':len(rows),'exact_matches':correct,'exact_match_rate':f'{correct/len(rows):.1%}',
        'corrections_needed':corrections,'median_runtime_ms':f'{statistics.median(timings):.6f}',
        'estimated_external_model_cost_per_case_usd':'0.000000','complexity_index':complexity,
        'cost_note':'Deterministic local harness only; LLM/API spend not measured.'
    })
with (ROOT/'D10/baseline_report_v1.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)
with (ROOT/'D10/baseline_case_results_v1.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=detail[0].keys()); w.writeheader(); w.writerows(detail)
# winner: simplest config with >=98% if any, else best accuracy then lowest complexity
eligible=[x for x in out if float(x['exact_match_rate'].strip('%'))>=98]
win=min(eligible,key=lambda x:x['complexity_index']) if eligible else sorted(out,key=lambda x:(-x['exact_matches'],x['complexity_index']))[0]
(ROOT/'D10/baseline_report_v1.md').write_text(f'''# Baseline Report v1\n\nSame 50 synthetic cases, same expected-route rubric. Prediction functions never read `expected_route`; evaluation compares only after prediction.\n\n| Config | Exact | Corrections | Complexity |\n|---|---:|---:|---:|\n'''+''.join(f"| {x['config']} | {x['exact_matches']}/50 ({x['exact_match_rate']}) | {x['corrections_needed']} | {x['complexity_index']} |\n" for x in out)+f'''\n**Selected:** `{win['config']}`. Selection rule: prefer the simplest configuration that reaches at least 98% exact-route agreement; otherwise choose best accuracy, then lowest complexity.\n\n**Cost caveat:** this is a deterministic local routing harness. External model/API cost was not measured, so no LLM cost claim is made.\n''',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
