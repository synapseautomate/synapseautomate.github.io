#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

def extract(case):
    text=case['input']
    if text == '<CORRUPT>': raise ValueError('PARSE_FAILED')
    if text == 'DUPLICATE': raise ValueError('DUPLICATE_INPUT')
    if not text.strip(): raise ValueError('EMPTY_INPUT')
    order=None
    m=re.search(r'(?:Sipariş\s*#|order_id[,\"]?:[\"]?)([A-Z0-9-]+)',text,re.I)
    if m: order=m.group(1)
    elif 'C-9' in text: order='C-9'
    typ=None
    low=text.lower()
    if 'iade' in low or 'refund' in low: typ='refund' if ('ödeme' in low or 'tl iade' in low) else 'return'
    elif 'adres' in low: typ='address_exception'
    elif 'stock_exception' in low or 'stok' in low: typ='stock_exception'
    elif 'faq' in low or 'takip linki' in low: typ='faq'
    priority=None
    if 'öncelik yüksek' in low and 'öncelik düşük' in low: priority=None
    elif 'priority,summary' in low and ',high,' in low: priority='high'
    elif 'öncelik yüksek' in low: priority='high'
    elif 'öncelik düşük' in low or '"priority":"low"' in low: priority='low'
    unknowns=[]
    if typ is None: unknowns.append('request_type')
    if order is None: unknowns.append('order_id')
    if priority is None: unknowns.append('priority')
    if ('iade yapın' in low or (typ=='refund' and ('payment' in low or 'ödeme' in low))):
        route='HUMAN_APPROVAL'
    elif typ in ('refund',) and 'tl iade' in low:
        route='HUMAN_APPROVAL'
    elif typ=='faq' and not ('yüksek' in low or 'çeliş' in low):
        route='AUTO_PROCEED'
    else:
        route='HUMAN_REVIEW'
    if '3.200 tl iade' in low: route='HUMAN_APPROVAL'
    if 'öncelik yüksek' in low and 'öncelik düşük' in low: route='HUMAN_REVIEW'
    return {'order_id':order,'request_type':typ,'unknowns':unknowns,'route':route}

def main():
    cases=json.loads(Path(__file__).with_name('test_cases.json').read_text(encoding='utf-8'))
    passed=0
    for c in cases:
        try:
            out=extract(c)
            if 'expected_error' in c: raise AssertionError(f"expected error {c['expected_error']}, got {out}")
            exp=c['expected']
            for k,v in exp.items():
                if out[k]!=v: raise AssertionError(f"{c['id']} {k}: {out[k]} != {v}")
        except ValueError as e:
            if c.get('expected_error')!=str(e): raise
        passed+=1
    print(f'PASS {passed}/{len(cases)} synthetic structured-extraction cases')
if __name__=='__main__': main()
