#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
import json, sys, re, html, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]; errors=[]
class P(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a' and a.get('href'): self.links.append(a['href'])
for f in ROOT.rglob('*.html'):
 s=f.read_text(encoding='utf-8')
 for token in ['<title>','name="description"','rel="canonical"','application/ld+json','name="viewport"']:
  if token not in s: errors.append(f'{f.relative_to(ROOT)} missing {token}')
 for bad in ["{''.join(",'.join(f','roof_faq','rev_faq','for q,a in']:
  if bad in s: errors.append(f'{f.relative_to(ROOT)} template artifact: {bad}')
 p=P(); p.feed(s)
 for href in p.links:
  if href.startswith(('http:','https:','mailto:','tel:','javascript:','#')): continue
  href=href.split('?',1)[0].split('#',1)[0]
  if not href: continue
  target=(f.parent/href).resolve() if not href.startswith('/') else (ROOT/href.lstrip('/')).resolve()
  if target.is_dir(): target=target/'index.html'
  if not target.exists(): errors.append(f'{f.relative_to(ROOT)} broken link: {href}')
for r in ['robots.txt','sitemap.xml','llms.txt','site.webmanifest','assets/styles.css','assets/app.js','assets/og-synapse.png','assets/sitemap.xsl','sektorler.html','ai-bilgi.html','site-haritasi.html','kinetra-studios.html']:
 if not (ROOT/r).exists(): errors.append('missing '+r)
for r in ['saglik','finans','e-ticaret','emlak','hukuk','uretim-lojistik','egitim','gayrimenkul-yonetimi']:
 if not (ROOT/f'sektorler/{r}.html').exists(): errors.append('missing sector '+r)
for r in ['revenueos','agentready','creative','magnetflow','vela','kilory']:
 if not (ROOT/f'urunler/{r}.html').exists(): errors.append('missing product '+r)
ET.parse(ROOT/'sitemap.xml'); json.loads((ROOT/'site.webmanifest').read_text(encoding='utf-8'))
products=(ROOT/'urunler.html').read_text(encoding='utf-8')
for token in ['RevenueOS','$99 audit','AgentReady','$149 audit','Creative','1.250 TL / $99','MagnetFlow','$99 starter','VELA','AUDIT İSTE','SCAN İSTE','ÖRNEK İSTE','DEMO İSTE']:
 if token not in products: errors.append('product architecture missing '+token)
sectors=(ROOT/'sektorler.html').read_text(encoding='utf-8')
for token in ['Sağlık','Finans & Bankacılık','E-Ticaret','Emlak','Hukuk','Üretim & Lojistik','Eğitim','Gayrimenkul Yönetimi','Ev Hizmetleri / Roofing']:
 if token not in sectors: errors.append('sector index missing '+token)
llms=(ROOT/'llms.txt').read_text(encoding='utf-8')
if 'Active vertical:' in llms: errors.append('llms.txt must not declare an exclusive active vertical')
if 'Home Services / Roofing is one documented RevenueOS implementation pattern' not in llms: errors.append('llms.txt roofing implementation context missing')
for f in ROOT.rglob('*.html'):
 s=f.read_text(encoding='utf-8')
 for forbidden in [r'\b%70\b',r'\b%80\b',r'\b%99\b',r'garanti ediyoruz',r'GDPR/KVKK uyumludur',r'Sınırsız Otomasyon']:
  if re.search(forbidden,s,re.I): errors.append(f'{f.relative_to(ROOT)} risky unsupported claim {forbidden}')
 if 'href="llms.txt">LLM Bilgi Dosyası' in s or 'href="sitemap.xml">Site Haritası' in s or 'href="../llms.txt">LLM Bilgi Dosyası' in s or 'href="../sitemap.xml">Site Haritası' in s:
  errors.append(f'{f.relative_to(ROOT)} exposes raw technical resource in footer')

# Corporate homepage must show the complete sector set, not a single active vertical.
home=html.unescape((ROOT/'index.html').read_text(encoding='utf-8'))
for token in ['Sağlık','Finans & Bankacılık','E-Ticaret','Emlak','Hukuk','Üretim & Lojistik','Eğitim','Gayrimenkul Yönetimi','Ev Hizmetleri / Roofing']:
 if token not in home: errors.append('homepage sector coverage missing '+token)
for bad in ['Aktif sektör','Bugünün odak nişi','tek aktif sektör']:
 if bad.lower() in home.lower(): errors.append('homepage must not present an exclusive active sector: '+bad)

# RevenueOS page must satisfy the source PDF site contract end-to-end.
rev=html.unescape((ROOT/'urunler/revenueos.html').read_text(encoding='utf-8'))
for token in ['Geç cevap','Unutulan takip','Eksik nitelendirme','Onaylı knowledge base','30 SSS','8–12 niyet','Lead score','Booking + human handoff','3 takip mesajı','Lead board','30 test vakası','RevenueOS','AgentReady','Creative','MagnetFlow','VELA','9.900 TL','global alternatif $750','%50 ön ödeme','Onaylı kaynak','Minimum veri','Human gate','Consent & silme','24 Saat Audit İste']:
 if token not in rev: errors.append('RevenueOS source contract missing '+token)

# Source-deck service and sector coverage.
services=html.unescape((ROOT/'hizmetler.html').read_text(encoding='utf-8'))
for token in ['AI Chatbot & Müşteri Hizmetleri','Satış & Lead Generation','Muhasebe & Finans Otomasyonu','İK & İşe Alım','Pazarlama & İçerik','Hukuk & Uyum','AI Eğitim & Danışmanlık','Özel AI / RAG & Evals','AI Denetimi & Optimizasyon','Süreç Madenciliği','Sesli AI & Çağrı Merkezi','Tahmine Dayalı Analitik','Ölçülebilir verimlilik','Bilgi güvenliği yol haritası','Tanımlı servis seviyesi','Şeffaf raporlama']:
 if token not in services: errors.append('service/deck coverage missing '+token)


# Investor-deck coverage: products, studio, group and investor framing.
kilory=html.unescape((ROOT/'urunler/kilory.html').read_text(encoding='utf-8'))
for token in ['AI fotoğrafla öğün analizi','AI şef & tarif akışı','Barkod tarama','Sosyal akış','Egzersiz planlama','Su, makro & hedefler','Freemium + Premium abonelik','AI Beslenme Asistanı Pro','B2B kurumsal wellness lisansı','İzin ve uyum esaslı araştırma iş birlikleri','uygulama içi reklam']:
 if token not in kilory: errors.append('Kilory source/deck coverage missing '+token)
studio=html.unescape((ROOT/'kinetra-studios.html').read_text(encoding='utf-8'))
for token in ['Fikir','Tasarım','Geliştirme','Test','Lansman','48–72 saat','Sağlık & İyi Yaşam','Finans & Fintech','E-Ticaret & Perakende','Eğitim & Üretkenlik','Sosyal & Yaşam Tarzı','B2B & SaaS','Hızlı pazara çıkış','Sermaye verimliliği','Çok katmanlı gelir','Veri & öğrenme döngüsü','Global dağıtım','Portföy + IP + gelirleşme']:
 if token not in studio: errors.append('Kinetra Studios source/deck coverage missing '+token)
group=html.unescape((ROOT/'kinetra-group.html').read_text(encoding='utf-8'))
for token in ['Kinetra Studios','Synapse Automate','Kilory','AI Ventures','AI Academy','Infrastructure','Marketplace','B2C + B2B çift motor','Yeniden kullanılabilir IP']:
 if token not in group: errors.append('Kinetra Group source/deck coverage missing '+token)
invest=html.unescape((ROOT/'yatirimcilar.html').read_text(encoding='utf-8'))
for token in ['2026','2027','2028','2029','2030','yönetim senaryosudur','gerçekleşmiş gelir','Kinetra Studios','Synapse Automate','$2.6–4.4T','%88','$644B','%33']:
 if token not in invest: errors.append('investor source/deck coverage missing '+token)

if errors:
 print('SITE QA: FAIL'); [print('- '+e) for e in errors]; sys.exit(1)
print(f'SITE QA: PASS — {len(list(ROOT.rglob("*.html")))} HTML pages')
print('template-artifact scan: PASS')
print('sector coverage: PASS — 9 sector solution entries')
print('product architecture: PASS — 5 source products with entry price + CTA')
print('raw technical resources removed from user-facing footer: PASS')
