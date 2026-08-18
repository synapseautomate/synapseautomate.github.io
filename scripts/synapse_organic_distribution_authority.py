from pathlib import Path
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from html import escape

ROOT = Path(".").resolve()
BASE = "https://synapseautomate.github.io"
HUB_REL = "kaynaklar/ai-otomasyon-otorite-merkezi.html"
HUB_URL = f"{BASE}/{HUB_REL}"
FEED_REL = "feed.xml"
FEED_URL = f"{BASE}/{FEED_REL}"
MANIFEST_REL = "content-manifest.json"
MANIFEST_URL = f"{BASE}/{MANIFEST_REL}"

def write_if_changed(path: Path, content: str):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return True

pages = [
    {"title":"AI Otomasyonunda 7 Yanlış Başlangıç","url":f"{BASE}/rehberler/ai-otomasyonunda-yanlis-baslangiclar.html","type":"thought-leadership","summary":"Süreç, veri, yetki, insan onayı ve ölçüm kurulmadan yapılan yaygın başlangıç hataları."},
    {"title":"AI Otomasyon Risk Değerlendirmesi","url":f"{BASE}/araclar/ai-otomasyon-risk-degerlendirmesi.html","type":"free-tool","summary":"10 kontrol sorusuyla pilot öncesi hazırlık ve risk görünümü."},
    {"title":"Finans ve Bankacılıkta AI Otomasyonu","url":f"{BASE}/sektorler/finans.html","type":"industry","summary":"İnsan denetimli risk ön değerlendirme, anomali sinyalleri, segmentasyon ve raporlama akışları."},
    {"title":"Kilory Yayın Öncesi Kanıt Paketi","url":f"{BASE}/kanit/kilory-yayin-oncesi-kanit-paketi.html","type":"evidence","summary":"Kilory için özellik matrisi, claim sınırları, gizlilik ve yayın kapıları."},
    {"title":"AI Otomasyon Kanıt Metodolojisi","url":f"{BASE}/kanit/ai-otomasyon-kanit-metodolojisi.html","type":"methodology","summary":"İddia, kaynak, ölçüm ve insan onayı arasındaki kanıt yaklaşımı."},
]

STYLE = '''
:root{--bg:#06111f;--bg2:#081827;--panel:#10263a;--panel2:#0c1d2e;--line:#284962;--text:#eef7fb;--muted:#a9bbc6;--cyan:#57ded5}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:linear-gradient(180deg,var(--bg),var(--bg2) 45%,var(--bg));color:var(--text);font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.65}
a{color:#8ee6ef;text-decoration:none}a:hover{text-decoration:underline}.container{width:min(1120px,calc(100% - 32px));margin:auto}
header{position:sticky;top:0;z-index:10;background:rgba(6,17,31,.94);border-bottom:1px solid var(--line);backdrop-filter:blur(10px)}.nav{min-height:72px;display:flex;align-items:center;gap:20px}.brand{font-weight:850;color:#fff;font-size:1.15rem}.navlinks{display:flex;gap:18px;margin-left:auto}.cta{display:inline-flex;padding:12px 18px;border-radius:999px;background:linear-gradient(90deg,var(--cyan),#38b8dd);color:#03121f;font-weight:850}
.breadcrumb{padding:20px 0;color:var(--muted);font-size:.92rem}.hero{padding:54px 0 34px}.kicker{font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--cyan);font-weight:850}h1{font-size:clamp(2.25rem,5vw,4rem);line-height:1.05;margin:.35em 0}h2{font-size:clamp(1.6rem,3vw,2.4rem)}.lead{font-size:1.15rem;max-width:930px;color:#cedce4}
.section{padding:48px 0}.grid{display:grid;gap:18px}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.card{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);border-radius:18px;padding:22px}.card h3{margin-top:0}.tag{display:inline-block;padding:5px 10px;border:1px solid var(--line);border-radius:999px;color:var(--cyan);font-size:.82rem}.muted{color:var(--muted)}.machine{background:#071723;border:1px dashed #3a6077;border-radius:18px;padding:22px}.machine code{word-break:break-all;color:#aeeef3}
footer{border-top:1px solid var(--line);padding:38px 0;margin-top:38px;color:var(--muted)}.foot{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
@media(max-width:760px){.navlinks{display:none}.nav{justify-content:space-between}.g2{grid-template-columns:1fr}.cta{font-size:.85rem}.hero{padding-top:34px}}
'''

org_schema = {
    "@context":"https://schema.org","@type":"Organization","@id":f"{BASE}/#organization",
    "name":"Synapse Automate","url":f"{BASE}/",
    "sameAs":["https://github.com/synapseautomate","https://www.linkedin.com/company/synapseautomate/"]
}
collection_schema = {
    "@context":"https://schema.org","@type":"CollectionPage",
    "name":"Synapse Automate AI Otomasyon Otorite Merkezi","url":HUB_URL,
    "about":{"@id":f"{BASE}/#organization"},
    "hasPart":[{"@type":"WebPage","name":p["title"],"url":p["url"]} for p in pages]
}

cards = "\n".join(
    f'<article class="card"><span class="tag">{escape(p["type"])}</span><h3>{escape(p["title"])}</h3><p>{escape(p["summary"])}</p><a href="{escape(p["url"])}">Kaynağı aç →</a></article>'
    for p in pages
)

hub = f'''<!doctype html>
<html lang="tr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>AI Otomasyon Otorite Merkezi | Synapse Automate</title>
<meta name="description" content="Synapse Automate’in AI otomasyonu, insan denetimi, süreç analizi, ücretsiz değerlendirme ve kanıt metodolojisi kaynaklarını tek yerde keşfedin.">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{HUB_URL}">
<link rel="alternate" type="application/rss+xml" title="Synapse Automate Kaynak Akışı" href="{FEED_URL}">
<meta property="og:type" content="website"><meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Synapse Automate"><meta property="og:title" content="AI Otomasyon Otorite Merkezi">
<meta property="og:description" content="Rehberler, ücretsiz araçlar, sektör çerçeveleri ve kanıt sayfaları.">
<meta property="og:url" content="{HUB_URL}"><meta name="theme-color" content="#06111f">
<style>{STYLE}</style>
<script type="application/ld+json">{json.dumps(org_schema,ensure_ascii=False,separators=(",",":"))}</script>
<script type="application/ld+json">{json.dumps(collection_schema,ensure_ascii=False,separators=(",",":"))}</script>
</head><body>
<header><div class="container nav"><a class="brand" href="../index.html">Synapse Automate</a>
<nav class="navlinks"><a href="../hizmetler.html">Hizmetler</a><a href="../urunler.html">Ürünler</a><a href="../sektorler.html">Sektörler</a><a href="../kaynaklar.html">Kaynaklar</a></nav>
<a class="cta" href="../iletisim.html?konu=surec-analizi">Süreç Analizi İste</a></div></header>
<main><div class="container breadcrumb"><a href="../index.html">Ana Sayfa</a> / <a href="../kaynaklar.html">Kaynaklar</a> / Otorite Merkezi</div>
<section class="hero"><div class="container"><div class="kicker">Kurumsal kaynak dizini</div>
<h1>AI otomasyonu hakkında ne söylediğimizi, neyi kanıtladığımızı ve sınırlarımızı tek yerde görün.</h1>
<p class="lead">Bu merkez; Synapse Automate’in insan denetimli AI otomasyonu yaklaşımını, ücretsiz değerlendirme aracını, sektör uygulama çerçevelerini ve kanıt sayfalarını tek bir kurumsal kaynak dizininde toplar.</p></div></section>
<section class="section"><div class="container"><div class="grid g2">{cards}</div></div></section>
<section class="section"><div class="container"><div class="grid g2">
<div class="machine"><h3>Makine-okunur içerik manifesti</h3><p class="muted">Kanonik URL, tür ve kapsam bilgisini JSON olarak yayınlıyoruz.</p><code>{MANIFEST_URL}</code></div>
<div class="machine"><h3>RSS keşif akışı</h3><p class="muted">Yeni ve öncelikli kaynakların standart akış adresi.</p><code>{FEED_URL}</code></div>
</div></div></section>
<section class="section"><div class="container"><div class="card"><h2>Kapsam sınırı</h2><p>Bu kaynaklar arama sıralaması, müşteri sonucu veya finansal/sağlık/hukuk sonucu garantisi vermez. Kanıtlanmamış başarı iddiaları yayınlanmaz; kritik karar ve dış eylemler insan onayıyla ele alınır.</p></div></div></section>
</main><footer><div class="container foot"><span>© 2026 Synapse Automate</span><span>Kaynak, kanıt, insan denetimi.</span></div></footer>
</body></html>'''

manifest = {
    "version":"1.0","generated_at":"2026-08-18",
    "organization":{"name":"Synapse Automate","canonical":f"{BASE}/","linkedin":"https://www.linkedin.com/company/synapseautomate/","github":"https://github.com/synapseautomate"},
    "authority_hub":HUB_URL,
    "discovery":{"sitemap":f"{BASE}/sitemap.xml","rss":FEED_URL,"llms":f"{BASE}/llms.txt"},
    "claim_boundaries":["No ranking guarantee","No financial advice","No autonomous financial transaction claim","No unverified health outcome claim","Critical decisions remain human-controlled where stated"],
    "resources":pages
}
manifest_text = json.dumps(manifest,ensure_ascii=False,indent=2)+"\n"

rss_items = "".join(
    f'<item><title>{escape(p["title"])}</title><link>{escape(p["url"])}</link><guid isPermaLink="true">{escape(p["url"])}</guid><description>{escape(p["summary"])}</description><pubDate>Tue, 18 Aug 2026 12:00:00 GMT</pubDate></item>'
    for p in pages
)
feed = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
<title>Synapse Automate Kaynak Akışı</title><link>{BASE}/</link>
<description>AI otomasyonu, insan denetimi, süreç analizi, ücretsiz araçlar ve kanıt kaynakları.</description>
<language>tr-tr</language><lastBuildDate>Tue, 18 Aug 2026 12:00:00 GMT</lastBuildDate>
{rss_items}
</channel></rss>'''

changed = []
for rel, content in [(HUB_REL,hub),(MANIFEST_REL,manifest_text),(FEED_REL,feed)]:
    if write_if_changed(ROOT/rel, content):
        changed.append(rel)

sitemap = ROOT/"sitemap.xml"
if sitemap.exists():
    st=sitemap.read_text(encoding="utf-8")
    if HUB_URL not in st:
        st=st.replace("</urlset>",f'  <url><loc>{HUB_URL}</loc><lastmod>2026-08-18</lastmod></url>\n</urlset>')
    if write_if_changed(sitemap,st):
        changed.append("sitemap.xml")
    ET.fromstring(sitemap.read_text(encoding="utf-8"))

llms=ROOT/"llms.txt"
if llms.exists():
    new=llms.read_text(encoding="utf-8")
    for line in [f"- AI automation authority hub: {HUB_URL}",f"- Machine-readable content manifest: {MANIFEST_URL}",f"- RSS resource feed: {FEED_URL}"]:
        if line not in new:
            new=new.rstrip()+"\n"+line+"\n"
    if write_if_changed(llms,new):
        changed.append("llms.txt")

robots=ROOT/"robots.txt"
if robots.exists():
    new=robots.read_text(encoding="utf-8")
    sitemap_line=f"Sitemap: {BASE}/sitemap.xml"
    if sitemap_line not in new:
        new=new.rstrip()+"\n\n"+sitemap_line+"\n"
    if write_if_changed(robots,new):
        changed.append("robots.txt")

for rel in ["index.html","kaynaklar.html"]:
    p=ROOT/rel
    if not p.exists():
        continue
    new=p.read_text(encoding="utf-8")
    rss_tag=f'<link rel="alternate" type="application/rss+xml" title="Synapse Automate Kaynak Akışı" href="{FEED_URL}">'
    if rss_tag not in new and "</head>" in new:
        new=new.replace("</head>",rss_tag+"\n</head>",1)
    if rel=="kaynaklar.html" and HUB_REL not in new and "</main>" in new:
        block=f'''<section class="section"><div class="container"><div class="section-head"><div><div class="kicker">Otorite merkezi</div><h2>Tüm AI otomasyon kaynaklarını tek dizinde keşfedin.</h2></div></div><div class="card"><h3>AI Otomasyon Otorite Merkezi</h3><p>Rehberler, ücretsiz araçlar, sektör çerçeveleri ve kanıt sayfalarını tek yerde toplar.</p><a class="btn btn-secondary" href="{HUB_REL}">Otorite Merkezini Aç</a></div></div></section>'''
        new=new.replace("</main>",block+"</main>",1)
    if write_if_changed(p,new):
        changed.append(rel)

json.loads((ROOT/MANIFEST_REL).read_text(encoding="utf-8"))
ET.fromstring((ROOT/FEED_REL).read_text(encoding="utf-8"))
hub_text=(ROOT/HUB_REL).read_text(encoding="utf-8")
pat=re.compile(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',re.I|re.S)
for raw in pat.findall(hub_text):
    json.loads(raw.strip())

for required in [FEED_URL,MANIFEST_URL]:
    if required not in hub_text:
        raise SystemExit("Authority hub missing discovery reference: "+required)

if sitemap.exists() and HUB_URL not in sitemap.read_text(encoding="utf-8"):
    raise SystemExit("Authority hub missing from sitemap.")

guard=ROOT/"scripts"/"synapse_text_repair.py"
if guard.exists():
    r=subprocess.run([sys.executable,str(guard)],cwd=ROOT,text=True,capture_output=True)
    print(r.stdout)
    if r.returncode!=0:
        print(r.stderr)
        raise SystemExit("Text integrity guard failed.")

changed=list(dict.fromkeys(changed))
print("Files changed:",len(changed))
for rel in changed:
    print("UPDATED:",rel)
print("ORGANIC DISTRIBUTION + AUTHORITY DISCOVERY QA: PASS")
