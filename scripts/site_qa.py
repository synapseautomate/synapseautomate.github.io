#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
import json, re, sys, xml.etree.ElementTree as ET, html as htmlmod
ROOT=Path(__file__).resolve().parents[1]
errors=[]
htmls=sorted(ROOT.rglob('*.html'))
minimal={'404.html','site-haritasi.html'}

class Scan(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.visible=[]; self.stack=[]; self.nav_links=[]; self.in_hidden=0; self.in_navfooter=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs); self.stack.append(tag)
        if tag in {'script','style','noscript'}: self.in_hidden+=1
        if tag in {'nav','footer'}: self.in_navfooter+=1
        if tag=='a' and a.get('href'):
            self.links.append(a['href'])
            if self.in_navfooter: self.nav_links.append(a['href'])
    def handle_endtag(self,tag):
        if tag in {'script','style','noscript'} and self.in_hidden: self.in_hidden-=1
        if tag in {'nav','footer'} and self.in_navfooter: self.in_navfooter-=1
        if self.stack: self.stack.pop()
    def handle_data(self,data):
        if not self.in_hidden: self.visible.append(data)

for f in htmls:
    rel=f.relative_to(ROOT).as_posix(); s=f.read_text(encoding='utf-8')
    if rel not in minimal:
        for token in ['<title','name="description"','rel="canonical"','name="viewport"']:
            if token not in s: errors.append(f'{rel} missing {token}')
    for bad in ["{'.join", "for q,a in", 'roof_faq}', 'rev_faq}', '{{', '{%']:
        if bad in s: errors.append(f'{rel} template artifact: {bad}')
    # Validate every JSON-LD block without third-party dependencies.
    for raw in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', s, re.I|re.S):
        try: json.loads(raw)
        except Exception as e: errors.append(f'{rel} invalid JSON-LD: {e}')
    p=Scan(); p.feed(s)
    for href in p.links:
        if href.startswith(('http:','https:','mailto:','tel:','javascript:','#')): continue
        href=href.split('?',1)[0].split('#',1)[0]
        if not href: continue
        target=(f.parent/href).resolve() if not href.startswith('/') else (ROOT/href.lstrip('/')).resolve()
        if target.is_dir(): target=target/'index.html'
        if not target.exists(): errors.append(f'{rel} broken link: {href}')
    for href in p.nav_links:
        if any(href.endswith(x) for x in ['site-haritasi.html','ai-bilgi.html','sitemap.xml','llms.txt']):
            errors.append(f'{rel} exposes technical resource in navigation: {href}')

required=['robots.txt','sitemap.xml','llms.txt','site.webmanifest','assets/styles-v33.css','assets/app-v33.js','assets/og-synapse.png','assets/sitemap.xsl','sektorler.html','hizmetler.html','urunler.html','ai-bilgi.html','site-haritasi.html','kinetra-studios.html']
for r in required:
    if not (ROOT/r).exists(): errors.append('missing '+r)
for old in ['assets/styles.css','assets/app.js']:
    if (ROOT/old).exists(): errors.append('stale cache-prone asset remains '+old)
ET.parse(ROOT/'sitemap.xml'); json.loads((ROOT/'site.webmanifest').read_text(encoding='utf-8'))
site_map=(ROOT/'sitemap.xml').read_text(encoding='utf-8')
for hidden in ['site-haritasi.html','ai-bilgi.html']:
    if hidden in site_map: errors.append('sitemap includes hidden/noindex page '+hidden)

sector_tokens=['Sağlık','Finans & Bankacılık','E-Ticaret','Emlak','Hukuk','Üretim & Lojistik','Eğitim','Gayrimenkul Yönetimi','Ev Hizmetleri / Çatı ve Tadilat']
def visible_text(path):
    p=Scan(); p.feed(Path(path).read_text(encoding='utf-8')); return htmlmod.unescape(' '.join(p.visible))
sectors=visible_text(ROOT/'sektorler.html'); home=visible_text(ROOT/'index.html')
for t in sector_tokens:
    if t not in sectors: errors.append('sector index missing '+t)
    if t not in home: errors.append('homepage sector coverage missing '+t)

forbidden=[r'\bAudit\b',r'\blead\b',r'\bhandoff\b',r'\bKPI\b',r'\bRAG\b',r'AI-native',r'\bCTA\b',r'\bCRM\b',r'TradeOps',r'Founder Pilot',r'human gate',r'human approval',r'\bROI\b',r'\bMVP\b',r'\bSLA\b',r'\bERP\b',r'white-label',r'\bretention\b',r'\bLTV\b',r'\bARR\b',r'\bMRR\b',r'\bB2B\b',r'\bB2C\b',r'self-service',r'\bticket\b',r'\bonboarding\b',r'\binbound\b',r'\bqualification\b',r'\bbooking\b',r'\bworkflow\b',r'\bscoreboard\b',r'\bquiz\b',r'\bcalculator\b',r'\bscorecard\b',r'mini-app',r'\bfunnel\b',r'follow-up',r'Human-in-the-loop',r'\bTraction\b',r'\bFintech\b',r'\bSaaS\b',r'\bConsent\b',r'\bD01\b',r'Gün 1',r'\bQA\b',r'\bsecret\b',r'\bbrief\b',r'\bagentic\b',r'\bmonetization\b',r'\bcohort\b',r'\bGTM\b',r'\bMeasurement\b']
for f in htmls:
    text=visible_text(f).replace('synapseautomate.ai@gmail.com','')
    for pat in forbidden:
        if re.search(pat,text,re.I): errors.append(f'{f.relative_to(ROOT)} unexplained customer jargon: {pat}')

products=visible_text(ROOT/'urunler.html')
for token in ['Müşteri Talebi ve Satış Takibi','$99 başlangıç analizi','Web ve Katalog Hazırlık Sistemi','$149 başlangıç analizi','İçerik Üretim Sistemi','1.250 TL / $99','Etkileşimli Teklif Sistemi','$99 başlangıç paketi','Teklif ve İş Takip Sistemi','ANALİZ İSTE','ÖN İNCELEME İSTE','ÖRNEK İSTE','TANITIM İSTE']:
    if token not in products: errors.append('product architecture missing '+token)
if 'Teknik Araştırma ve Kalite Laboratuvarı' in products: errors.append('internal technical lab exposed as product card')

rev=visible_text(ROOT/'urunler/revenueos.html')
for token in ['Geç cevap','Unutulan takip','Eksik nitelendirme','Onaylı bilgi tabanı','30 SSS','8–12 talep','randevu','yetkili personele aktarım','3 takip mesajı','30 test vakası','9.900 TL','$750','Onaylı kaynak','Minimum veri','İnsan onayı','Açık onay','Süreç Analizi İste']:
    if token not in rev: errors.append('customer/source contract missing '+token)

services=visible_text(ROOT/'hizmetler.html')
for token in ['Yapay Zekâ Destekli Müşteri Asistanı','Satış & Müşteri Talebi ve Satış Takibi','Muhasebe & Finans Otomasyonu','İK & İşe Alım','Pazarlama & İçerik','Hukuk & Uyum','Yapay Zekâ Eğitimi ve Danışmanlık','Kuruma Özel Yapay Zekâ ve Bilgi Tabanı','Yapay Zekâ Sistem İncelemesi ve Optimizasyonu','Süreç Madenciliği','Sesli Yapay Zekâ ve Çağrı Merkezi','Tahmine Dayalı Analitik','Ölçülebilir verimlilik','Bilgi güvenliği yol haritası','Tanımlı servis seviyesi','Şeffaf raporlama']:
    if token not in services: errors.append('service/deck coverage missing '+token)

for f in htmls:
    s=f.read_text(encoding='utf-8')
    for pat in [r'\b%70\b',r'\b%80\b',r'\b%99\b',r'garanti ediyoruz',r'GDPR/KVKK uyumludur',r'Sınırsız Otomasyon']:
        if re.search(pat,s,re.I): errors.append(f'{f.relative_to(ROOT)} risky unsupported claim {pat}')

if errors:
    print('SITE QA: FAIL'); [print('- '+e) for e in errors]; sys.exit(1)
print(f'SITE QA: PASS — {len(htmls)} HTML pages')
print('customer-language scan: PASS')
print('template-artifact scan: PASS')
print('sector coverage: PASS — 9 sector solution entries')
print('product architecture: PASS — source prices retained with plain-language labels')
print('technical resources removed from public navigation: PASS')
print('cache-busted CSS/JS: PASS')
