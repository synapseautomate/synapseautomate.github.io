#!/usr/bin/env python3
from pathlib import Path
import re, csv, subprocess, sys, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
required=[
'D10/baseline_report_v1.md','D10/baseline_report_v1.csv','D10/threat_model_v1.md','D10/risk_register.csv','D10/partner_one_pager.md',
'D10/finance_readiness.csv','D10/regression_30.csv','D10/regression_sop_v2.md','D10/ai_query_benchmark_v1.csv','D10/cluster_ranking.md','D10/cross_sell_map.md',
'cozumler/roofing-ev-hizmetleri.html','teklif/e-ticaret-surec-analizi.html','kanit/e-ticaret-agentic-commerce-karsilastirma.html','surec-analizi.html','sektorler/e-ticaret.html']
errors=[]
for p in required:
    if not (ROOT/p).exists(): errors.append(f'missing {p}')
# customer-facing pages: no internal day labels, no wrong .com
pages=['cozumler/roofing-ev-hizmetleri.html','teklif/e-ticaret-surec-analizi.html','kanit/e-ticaret-agentic-commerce-karsilastirma.html','sektorler/e-ticaret.html','surec-analizi.html']
for p in pages:
    text=(ROOT/p).read_text(encoding='utf-8')
    low=text.lower()
    for bad in ['day 10','gün 10','public benchmark','v1.0.0','synapseautomate.com']:
        if bad in low: errors.append(f'{p}: internal/wrong-domain marker {bad}')
    if 'https://synapseautomate.github.io/' not in text: errors.append(f'{p}: canonical domain missing')
# Roofing requirements
roof=(ROOT/'cozumler/roofing-ev-hizmetleri.html').read_text(encoding='utf-8')
if roof.count('<details>')<12: errors.append('roofing: fewer than 12 FAQ')
if '4.900 TL / $149' not in roof: errors.append('roofing: price CTA missing')
# exact comparison claims must match baseline report
with (ROOT/'D10/baseline_report_v1.csv').open(encoding='utf-8') as f: rows=list(csv.DictReader(f))
if [r['exact_matches'] for r in rows] != ['22','47','50']: errors.append('baseline unexpected')
# AI query coverage
with (ROOT/'D10/ai_query_benchmark_v1.csv').open(encoding='utf-8') as f: q=list(csv.DictReader(f))
if len(q)!=100 or any(r['local_file_exists']!='true' for r in q): errors.append('100-query local canonical coverage failed')
# validators
for cmd in [[sys.executable,str(ROOT/'D10/run_baseline_v1.py')],[sys.executable,str(ROOT/'D10/run_regression_30.py')],[sys.executable,str(ROOT/'public-proof/provenance-50-v1/validate.py')],[sys.executable,str(ROOT/'public-proof/workflow-output-schema-v2/validate.py')]]:
    cp=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    if cp.returncode: errors.append('validator failed: '+' '.join(cmd)+'\n'+cp.stdout+'\n'+cp.stderr)
# sitemap valid + new URLs included
try: s=ET.parse(ROOT/'sitemap.xml')
except Exception as e: errors.append(f'sitemap invalid: {e}')
sm=(ROOT/'sitemap.xml').read_text(encoding='utf-8')
for url in ['teklif/e-ticaret-surec-analizi.html','kanit/e-ticaret-agentic-commerce-karsilastirma.html']:
    if url not in sm: errors.append(f'sitemap missing {url}')
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    raise SystemExit(1)
print('PASS: Day 10 full quality gate')
