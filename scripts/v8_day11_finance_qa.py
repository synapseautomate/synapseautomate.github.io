#!/usr/bin/env python3
"""V8 Day11 audit: source repo state only; never implies GSC/live user outcomes."""
from __future__ import annotations
from pathlib import Path
from html.parser import HTMLParser
import csv,json,re,sys,xml.etree.ElementTree as ET
from urllib.parse import urlparse,unquote
from decimal import Decimal
ROOT=Path(__file__).resolve().parents[1]
OUT=Path('/tmp/synapse-v8-day11-evidence')
OUT.mkdir(parents=True,exist_ok=True)
target='cozumler/fatura-on-isleme-mutabakat-kontrolu.html'
prefix='https://synapseautomate.github.io/'
issues=[]
fixture=ROOT/'operasyon/v8/gun-11/fatura-mutabakat-SENTETIK-ornek.csv'
if not fixture.is_file():
    issues.append('synthetic finance fixture missing')
else:
    with fixture.open(newline='',encoding='utf-8') as csvin:
        rows=list(csv.DictReader(csvin))
    bytype={row['source']:row for row in rows}
    try:
        inv=bytype['fatura']
        book=bytype['muhasebe_taslak_kaydi']
        bank=bytype['varsayilan_tek_odeme_satiri']
        assert all(row['synthetic']=='EVET' for row in rows)
        assert len(rows)==3
        assert len({row['reference'] for row in rows})==1
        assert len({row['currency'] for row in rows})==1
        assert Decimal(inv['amount'])==Decimal(book['amount'])
        assert Decimal(inv['amount'])-Decimal(bank['amount'])==Decimal('500')
        # No automatic financial determination: difference is an INCONCLUSIVE human gate.
        assert all(row['decision']=='HUMAN_REVIEW' for row in rows)
    except (AssertionError, KeyError, ValueError, ArithmeticError) as exc:
        issues.append('synthetic finance fixture fails source-reference/currency/500 TL calculation: '+str(exc))
class Tags(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True);self.h1=0;self.h2=0;self.links=[];self.meta=[];self.canon=[];self.title=False;self.images=[];self.breadcrumb=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='h2':self.h2+=1
        if tag=='title':self.title=True
        if tag=='a' and a.get('href'):self.links.append(a['href'])
        if tag=='img':self.images.append(a)
        if tag=='meta':self.meta.append(a)
        if tag=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))
htmls=sorted(x for x in ROOT.rglob('*.html') if not any(part in {'.git','_site','operasyon','node_modules','D01','D02','D03'} for part in x.relative_to(ROOT).parts))
records=[]
for file in htmls:
    rel=file.relative_to(ROOT).as_posix();s=file.read_text(encoding='utf-8')
    scanner=Tags();scanner.feed(s)
    ti=re.search(r'<title[^>]*>(.*?)</title>',s,re.I|re.S)
    title=re.sub(r'<[^>]*>','',ti.group(1)).strip() if ti else ''
    robot=next((a.get('content','') for a in scanner.meta if a.get('name','').lower()=='robots'),'BİLİNMİYOR')
    canonical=scanner.canon[0] if len(scanner.canon)==1 else 'BİLİNMİYOR'
    records.append((rel,title,scanner.h1,scanner.h2,canonical,robot,len(scanner.links),len(scanner.images)))
    if rel==target:
        if scanner.h1!=1:issues.append('target H1 not exactly 1')
        if scanner.h2<3:issues.append('target H2 missing')
        if canonical!=prefix+target:issues.append('target canonical mismatch')
        if 'noindex' in robot.lower():issues.append('target accidentally noindex')
        if not title or 'Fatura' not in title:issues.append('target title missing')
        if not re.search(r'<meta name="description" content="[^"]{50,}',s):issues.append('target description missing')
        if 'SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL' not in s:issues.append('target synthetic disclaimer missing')
        if '12.500' not in s or '12.000' not in s or '500 TL' not in s:issues.append('synthetic comparison unclear')
        for forbidden in ['aggregateRating','"offers"','"price"','"ratingValue"','GÜN 11','CRM API entegrasyonu çalışıyor','garanti edilen']: 
            if forbidden in s:issues.append('forbidden marketing marker: '+forbidden)
        for image in scanner.images:
            if not image.get('alt'):issues.append('target image missing alt')
        for href in scanner.links:
            if href.startswith(('https:','http:','mailto:','tel:','#')):continue
            clean=urlparse(href).path
            loc=(file.parent/unquote(clean)).resolve() if not clean.startswith('/') else (ROOT/clean.lstrip('/')).resolve()
            if not loc.is_relative_to(ROOT) or not loc.exists():issues.append('target local link broken: '+href)
if len(htmls)<146:issues.append('HTML inventory dropped below baseline: '+str(len(htmls)))
with (OUT/'gercek_html_metaanaliz.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['path','title','h1_adet','h2_adet','canonical','robots','link_adet','resim_adet']);w.writerows(records)
maps={}
for name in ['sitemap.xml','sitemap-demand.xml']:
    try:
        root=ET.parse(ROOT/name).getroot()
        locs=[(x.text or '').strip() for x in root.findall('.//{*}loc')]
        maps[name]=locs
    except Exception as exc:issues.append(name+' invalid: '+str(exc));maps[name]=[]
if prefix+target not in maps['sitemap.xml']:issues.append('new indexable page missing sitemap')
if prefix+target in maps['sitemap-demand.xml']:issues.append('target double-listed in demand sitemap')
if len(maps['sitemap.xml'])!=len(set(maps['sitemap.xml'])):issues.append('main sitemap duplicates')
if len(maps['sitemap-demand.xml'])!=len(set(maps['sitemap-demand.xml'])):issues.append('demand sitemap duplicates')
robots=(ROOT/'robots.txt').read_text(encoding='utf-8')
for m in ('sitemap.xml','sitemap-demand.xml'):
    if prefix+m not in robots:issues.append('robots missing sitemap declaration: '+m)
for rel in ['hizmetler.html','sektorler/finans-bankacilik.html']:
    if target not in (ROOT/rel).read_text(encoding='utf-8'):issues.append(rel+' missing source link to target')
if 'sektorler/finans-bankacilik.html' not in (ROOT/'index.html').read_text(encoding='utf-8'):issues.append('home finance sector route missing')
data={'status':'PASS' if not issues else 'FAIL','date':'2026-10-20','real_html_pages_on_branch':len(htmls),'site_maps':{k:len(v) for k,v in maps.items()},'target':target,'routes':['index.html -> sektorler/finans-bankacilik.html -> '+target+' -> araclar/finans-surec-kontrol-listesi.html','hizmetler.html -> '+target], 'issues':issues, 'note':'Source repository only; live GSC and user analytics not accessible; no real form submissions'}
(OUT/'SEO_QA_A_SONUC.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(data,ensure_ascii=False,indent=2))
if issues:sys.exit(1)
