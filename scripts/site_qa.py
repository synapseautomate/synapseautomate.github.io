#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
import json, sys, re, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
errors=[]
class P(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.title=False; self.desc=False; self.canonical=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and a.get('href'): self.links.append(a['href'])
        if tag=='link' and a.get('rel')=='canonical': self.canonical=True
        if tag=='meta' and a.get('name')=='description' and a.get('content'): self.desc=True
    def handle_data(self,data):
        pass

for f in ROOT.rglob('*.html'):
    s=f.read_text(encoding='utf-8')
    if '<title>' not in s: errors.append(f'{f}: title missing')
    if 'name="description"' not in s: errors.append(f'{f}: description missing')
    if 'rel="canonical"' not in s: errors.append(f'{f}: canonical missing')
    if 'application/ld+json' not in s: errors.append(f'{f}: JSON-LD missing')
    if 'name="viewport"' not in s: errors.append(f'{f}: viewport missing')
    p=P(); p.feed(s)
    for href in p.links:
        if href.startswith(('http:','https:','mailto:','tel:','javascript:','#')): continue
        href=href.split('?',1)[0].split('#',1)[0]
        if not href: continue
        target=(f.parent/href).resolve()
        if href.startswith('/'): target=(ROOT/href.lstrip('/')).resolve()
        if target.is_dir(): target=target/'index.html'
        if not target.exists(): errors.append(f'{f.relative_to(ROOT)} broken link: {href}')
for required in ['robots.txt','sitemap.xml','llms.txt','site.webmanifest','assets/styles.css','assets/app.js','assets/og-synapse.png']:
    if not (ROOT/required).exists(): errors.append(f'missing {required}')
ET.parse(ROOT/'sitemap.xml')
json.loads((ROOT/'site.webmanifest').read_text(encoding='utf-8'))
for forbidden in [r'\b%70\b',r'\b%80\b',r'\b%99\b',r'8\.000\+',r'\$144M',r'garanti ediyoruz',r'GDPR/KVKK uyumludur']:
    for f in ROOT.rglob('*.html'):
        if re.search(forbidden,f.read_text(encoding='utf-8'),re.I): errors.append(f'{f}: risky unsupported claim {forbidden}')
if errors:
    print('SITE QA: FAIL')
    print('\n'.join('- '+e for e in errors))
    sys.exit(1)
print(f'SITE QA: PASS — {len(list(ROOT.rglob("*.html")))} HTML pages')
