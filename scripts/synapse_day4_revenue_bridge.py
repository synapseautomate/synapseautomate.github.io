from pathlib import Path
import csv
import io
import re
import json
import sys
import subprocess
import xml.etree.ElementTree as ET
from html import escape

ROOT = Path(".").resolve()
BASE = "https://synapseautomate.github.io"

INVENTORY = ROOT / "veri" / "gun4-workflow-inventory.csv"
SCORECARD = ROOT / "veri" / "gun4-opportunity-scorecard.csv"

DECISION_REL = "rehberler/ai-otomasyon-is-akisi-karar-tablosu.html"
DECISION_URL = f"{BASE}/{DECISION_REL}"
AUDIT_REL = "surec-analizi.html"
AUDIT_URL = f"{BASE}/{AUDIT_REL}"

def write_if_changed(path: Path, content: str):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return True

def load_csv(path):
    if not path.exists():
        raise SystemExit(f"Required Day 4 asset missing: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

inventory = load_csv(INVENTORY)
scorecard = load_csv(SCORECARD)

if len(inventory) != 30:
    raise SystemExit(f"Expected 30 inventory rows, got {len(inventory)}")
if len(scorecard) < 10:
    raise SystemExit("Opportunity scorecard must contain at least 10 rows.")

required_inv = ["kategori","is_akisi","girdi","karar","cikti","ekonomik_sonuc","owner","human_gate"]
for key in required_inv:
    if key not in inventory[0]:
        raise SystemExit("Missing inventory column: " + key)

public_buf = io.StringIO()
writer = csv.DictWriter(public_buf, fieldnames=required_inv, lineterminator="\n")
writer.writeheader()
for row in inventory:
    writer.writerow({k: row.get(k, "") for k in required_inv})
public_csv = public_buf.getvalue()

methodology = """# Synapse Automate - Workflow Opportunity Scoring Methodology

Status: public methodology, synthetic/redacted workflow inventory.

## Purpose
This rubric prioritizes repeated operational workflows before choosing a model, agent, or UI.

## Scoring inputs
Each workflow is scored from 1-5 on:
- pain / operational friction
- frequency
- money proximity
- data accessibility
- measurability
- fragmentation
- risk
- sales-cycle friction

## Weighting
Opportunity Score =
pain + frequency + (2 x money proximity) + (2 x data accessibility)
+ measurability + fragmentation - risk - sales-cycle friction

Money proximity and data accessibility receive double weight.
Risk and long sales cycles reduce the score.

## Safety boundary
The score is not an ROI guarantee. It only ranks discovery priority.
Price, payment, customer commitments, legal/medical/financial advice,
and other critical external actions remain human-controlled.

## Evidence boundary
The current 30-row inventory is synthetic and workflow-level.
It is not presented as customer performance data or a case study.

Canonical decision page:
https://synapseautomate.github.io/rehberler/ai-otomasyon-is-akisi-karar-tablosu.html
"""

def intish(v, default=999):
    try:
        return int(float(v))
    except Exception:
        return default

top10 = sorted(scorecard, key=lambda r: intish(r.get("rank")))[:10]

ecom_inventory = [r for r in inventory if r.get("kategori","").strip().casefold() == "e-ticaret".casefold()]
ecom_names = {r["is_akisi"] for r in ecom_inventory}
ecom_top = [r for r in top10 if r.get("is_akisi") in ecom_names]
if not ecom_top:
    ecom_top = [{"is_akisi": r["is_akisi"], "score": "—"} for r in ecom_inventory[:5]]

STYLE = """
:root{--bg:#06111f;--bg2:#0a1b2c;--panel:#10263a;--panel2:#0b1d2e;--line:#29485f;--txt:#eff7fb;--muted:#a9bbc6;--cyan:#58e6d6;--blue:#58a8ff;--green:#79e5a0}
*{box-sizing:border-box}body{margin:0;background:linear-gradient(180deg,var(--bg),var(--bg2) 48%,var(--bg));color:var(--txt);font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.65}
a{color:#8ee6ef}.container{width:min(1120px,calc(100% - 32px));margin:auto}header{position:sticky;top:0;z-index:10;background:rgba(6,17,31,.95);border-bottom:1px solid var(--line)}.nav{min-height:72px;display:flex;align-items:center;gap:18px}.brand{font-weight:850;color:#fff;text-decoration:none}.navlinks{display:flex;gap:18px;margin-left:auto}.hero{padding:58px 0 34px}.kicker{color:var(--cyan);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;font-weight:850}h1{font-size:clamp(2.15rem,5vw,4rem);line-height:1.06;margin:.3em 0}.lead{max-width:900px;color:#d1dee6;font-size:1.13rem}.section{padding:44px 0}.grid{display:grid;gap:18px}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}.card{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);border-radius:18px;padding:22px}.card h2,.card h3{margin-top:0}.tag{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:4px 9px;color:var(--cyan);font-size:.8rem}.muted{color:var(--muted)}.btn{display:inline-flex;padding:12px 18px;border-radius:999px;background:linear-gradient(90deg,var(--cyan),#3cc1df);color:#04121e;text-decoration:none;font-weight:850;border:0;cursor:pointer}.btn2{background:transparent;color:#b8f2f1;border:1px solid #3e687d}.tablewrap{overflow:auto;border:1px solid var(--line);border-radius:16px}table{width:100%;border-collapse:collapse;min-width:760px;background:#0c1e2f}th,td{text-align:left;padding:13px 14px;border-bottom:1px solid #203c52;vertical-align:top}th{color:var(--cyan);font-size:.84rem}td{color:#dbe7ee}.notice{border-left:4px solid var(--green);padding:14px 16px;background:#0b2530;border-radius:10px}.price{font-size:2rem;font-weight:900;color:var(--cyan)}label{font-weight:750}input,textarea{width:100%;margin-top:6px;padding:13px;border-radius:12px;border:1px solid var(--line);background:#071724;color:#fff;font:inherit}textarea{min-height:115px}.field{margin-bottom:16px}.small{font-size:.9rem;color:var(--muted)}footer{border-top:1px solid var(--line);padding:35px 0;color:var(--muted)}@media(max-width:760px){.navlinks{display:none}.g2,.g3{grid-template-columns:1fr}}
"""

top_rows = "".join(
    f"<tr><td>{escape(str(r.get('rank','')))}</td><td>{escape(r.get('is_akisi',''))}</td><td>{escape(r.get('kategori',''))}</td><td>{escape(str(r.get('score','')))}</td><td>{escape(r.get('human_gate',''))}</td></tr>"
    for r in top10
)
ecom_rows = "".join(
    f"<li>{escape(r.get('is_akisi',''))}{(' - puan: ' + escape(str(r.get('score','')))) if r.get('score') else ''}</li>"
    for r in ecom_top
)

decision = f"""<!doctype html><html lang="tr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>AI Otomasyon İş Akışı Karar Tablosu | Synapse Automate</title>
<meta name="description" content="30 tekrarlı iş akışını para yakınlığı, veri erişimi, ölçülebilirlik, risk ve insan onayıyla değerlendiren Synapse Automate karar tablosu.">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="canonical" href="{DECISION_URL}">
<style>{STYLE}</style>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"TechArticle","headline":"AI Otomasyon İş Akışı Karar Tablosu","url":DECISION_URL,"author":{"@type":"Organization","name":"Synapse Automate","url":BASE+"/"}},ensure_ascii=False,separators=(",",":"))}</script>
</head><body>
<header><div class="container nav"><a class="brand" href="../index.html">Synapse Automate</a><nav class="navlinks"><a href="../sektorler.html">Sektörler</a><a href="../kaynaklar.html">Kaynaklar</a><a href="../araclar/surecini-20-dakikada-haritala.html">Ücretsiz Araç</a></nav></div></header>
<main>
<section class="hero"><div class="container"><div class="kicker">Karar tablosu · kamu kanıtı</div><h1>AI projesine model seçerek değil, iş akışı seçerek başlayın.</h1><p class="lead">30 sentetik ama gerçekçi operasyon iş akışı; para yakınlığı, veri erişimi, sıklık, ölçülebilirlik, dağınıklık, risk ve satış çevrimiyle aynı çerçevede değerlendirildi. Bu bir müşteri başarı hikâyesi veya ROI garantisi değildir.</p><p><a class="btn" href="../araclar/surecini-20-dakikada-haritala.html">Sürecini 20 Dakikada Haritala</a></p></div></section>

<section class="section"><div class="container"><h2>İlk 10 fırsat</h2><div class="tablewrap"><table>
<thead><tr><th>Sıra</th><th>İş akışı</th><th>Kategori</th><th>Puan</th><th>İnsan kapısı</th></tr></thead><tbody>{top_rows}</tbody>
</table></div><p class="small">Puan yalnız keşif önceliğini belirler; otomatik ROI veya başarı iddiası değildir.</p></div></section>

<section class="section"><div class="container"><h2>İlk üç ticari küme</h2><div class="grid g3">
<div class="card"><span class="tag">Öncelik 1</span><h3>E-Ticaret & Perakende</h3><p>Mevcut 30 satırlık envanterde doğrudan temsil edilen ve puanlanan kümedir.</p><ul>{ecom_rows}</ul></div>
<div class="card"><span class="tag">Öncelik 2</span><h3>Gayrimenkul Yönetimi + Emlak</h3><p>Talep önceliklendirme, bakım, kiracı iletişimi ve sözleşme akışları ticari hipotezdir. Mevcut 30 satırlık veri setinde puanlanmış müşteri kanıtı olarak sunulmaz; inbound verisiyle doğrulanacaktır.</p></div>
<div class="card"><span class="tag">Öncelik 3</span><h3>Ev Hizmetleri / Roofing</h3><p>Hızlı yanıt, hizmet uygunluğu, teklif ve takip akışları ticari hipotezdir. Mevcut envanterden müşteri sonucu türetilmez; gerçek talep gelene kadar kanıt statüsü “hipotez”dir.</p></div>
</div></div></section>

<section class="section"><div class="container"><div class="grid g2">
<div class="card"><h2>Metodoloji</h2><p><b>Opportunity Score</b> = acı + sıklık + 2×para yakınlığı + 2×veri erişimi + ölçülebilirlik + dağınıklık - risk - satış çevrimi.</p><p><a href="../veri/gun4-workflow-opportunity-methodology.md">Metodolojiyi aç</a> · <a href="../veri/gun4-workflow-inventory-public.csv">Public CSV'yi indir</a></p></div>
<div class="card"><h2>Güven sınırı</h2><p>Fiyat, ödeme, müşteri taahhüdü ve diğer kritik dış eylemler insan onayında kalır. Eksik bilgi uydurulmaz. Sentetik veri müşteri vakası gibi sunulmaz.</p></div>
</div></div></section>

<section class="section"><div class="container"><div class="card"><h2>Bir sonraki adım</h2><p>İş akışınızı 20 dakikada haritaladıktan sonra, uygun görünüyorsa ücretli Süreç Analizi ile 3-10 bulgu, kanıt, öncelik ve 7 günlük uygulama planına geçebilirsiniz.</p><p class="price">4.900 TL / $149</p><p><a class="btn" href="../surec-analizi.html">Süreç Analizi İste</a></p></div></div></section>
</main><footer><div class="container">© 2026 Synapse Automate · Kanıt, insan denetimi, ölçülebilir süreçler.</div></footer></body></html>"""

audit = f"""<!doctype html><html lang="tr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Süreç Analizi İste | Synapse Automate</title>
<meta name="description" content="Tekrarlayan iş akışınız için 3 alanla ücretli Synapse Automate Süreç Analizi talebi oluşturun.">
<meta name="robots" content="index,follow"><link rel="canonical" href="{AUDIT_URL}">
<style>{STYLE}</style></head><body>
<header><div class="container nav"><a class="brand" href="index.html">Synapse Automate</a><nav class="navlinks"><a href="rehberler/ai-otomasyon-is-akisi-karar-tablosu.html">Karar Tablosu</a><a href="araclar/surecini-20-dakikada-haritala.html">Ücretsiz Araç</a></nav></div></header>
<main><section class="hero"><div class="container"><div class="kicker">Tek ücretli sonraki adım</div><h1>Süreç Analizi</h1><p class="lead">Tekrarlayan bir iş akışını; darboğaz, veri, insan onayı ve ekonomik sonuç açısından yapılandırılmış biçimde inceler. Özel geliştirme başlamadan önce neyin yapılmaya değer olduğunu netleştirir.</p><div class="notice"><b>Başlangıç fiyatı: 4.900 TL / $149.</b> Ödeme/fatura kanalı ve kapsam sipariş öncesi gerçek durumla doğrulanır. Sonuç veya ROI garantisi verilmez.</div></div></section>
<section class="section"><div class="container"><div class="grid g2">
<div class="card"><h2>Talep oluştur</h2>
<form id="requestForm">
<div class="field"><label for="volume">1. Hacim / sıklık</label><textarea id="volume" required placeholder="Örn. Günde 80-120 sipariş; haftada 5-6 saat manuel kontrol."></textarea></div>
<div class="field"><label for="loss">2. Ana kayıp / darboğaz</label><textarea id="loss" required placeholder="Örn. Feed hataları geç fark ediliyor; ürünler yayından düşüyor ve ekip tek tek kontrol ediyor."></textarea></div>
<div class="field"><label for="owner">3. Karar sahibi</label><input id="owner" required placeholder="Örn. E-ticaret operasyon yöneticisi"></div>
<button class="btn" type="submit">Talebi E-posta ile Hazırla</button>
</form>
<p class="small">Form sunucuya veri kaydetmez. Gönder düğmesi cihazınızdaki e-posta uygulamasını açar. Kişisel veri, müşteri adı, kimlik bilgisi veya ticari sır girmeyin.</p>
</div>
<div class="card"><h2>Standart çıktı</h2><ul><li>3-10 somut bulgu</li><li>Bulgu başına kanıt / gözlem</li><li>Öncelik sırası</li><li>Maliyet/etki değerlendirmesi</li><li>7 günlük uygulama planı</li></ul><p><b>Hedef teslim:</b> kapsam ve ödeme doğrulandıktan sonra 24 saat. Kapasite veya kapsam farklıysa başlangıçta açıkça belirtilir.</p><p><a href="araclar/surecini-20-dakikada-haritala.html">Önce ücretsiz süreç haritasını kullan →</a></p></div>
</div></div></section></main>
<footer><div class="container">© 2026 Synapse Automate · Kritik kararlar insan onayında.</div></footer>
<script>
(function(){{
 const f=document.getElementById('requestForm');
 f.addEventListener('submit',function(e){{
   e.preventDefault();
   const v=document.getElementById('volume').value.trim();
   const l=document.getElementById('loss').value.trim();
   const o=document.getElementById('owner').value.trim();
   if(!v||!l||!o) return;
   const body='SYNAPSE AUTOMATE - SÜREÇ ANALİZİ TALEBİ\\n\\nHacim / sıklık:\\n'+v+'\\n\\nAna kayıp / darboğaz:\\n'+l+'\\n\\nKarar sahibi:\\n'+o+'\\n\\nKaynak: web formu';
   location.href='mailto:synapseautomate.ai@gmail.com?subject='+encodeURIComponent('Süreç Analizi Talebi')+'&body='+encodeURIComponent(body);
 }});
}})();
</script></body></html>"""

changed = []
for rel, content in [
    ("veri/gun4-workflow-inventory-public.csv", public_csv),
    ("veri/gun4-workflow-opportunity-methodology.md", methodology),
    (DECISION_REL, decision),
    (AUDIT_REL, audit),
]:
    if write_if_changed(ROOT / rel, content):
        changed.append(rel)

tool = ROOT / "araclar" / "surecini-20-dakikada-haritala.html"
if tool.exists():
    t = tool.read_text(encoding="utf-8")
    marker = "day4-revenue-bridge"
    if marker not in t and "</main>" in t:
        bridge = f"""<section id="{marker}" class="section"><div class="container"><div class="card">
<h2>Süreç haritanız netleştiyse</h2><p>Bir sonraki ücretli adım, 3-10 bulgu + kanıt + öncelik + 7 günlük plan içeren Süreç Analizi'dir.</p>
<p><strong>Başlangıç fiyatı: 4.900 TL / $149</strong></p><p><a class="btn" href="../surec-analizi.html">Süreç Analizi İste</a></p>
</div></div></section>"""
        t = t.replace("</main>", bridge + "</main>", 1)
        if write_if_changed(tool, t):
            changed.append("araclar/surecini-20-dakikada-haritala.html")

resources = ROOT / "kaynaklar.html"
if resources.exists():
    t = resources.read_text(encoding="utf-8")
    if DECISION_REL not in t and "</main>" in t:
        block = f"""<section class="section"><div class="container"><div class="card">
<h3>AI Otomasyon İş Akışı Karar Tablosu</h3><p>30 tekrarlı iş akışının puanlama metodolojisi, ilk 10 fırsatı ve üç ticari küme için karar çerçevesi.</p>
<a class="btn btn-secondary" href="{DECISION_REL}">Karar Tablosunu Aç</a></div></div></section>"""
        t = t.replace("</main>", block + "</main>", 1)
        if write_if_changed(resources, t):
            changed.append("kaynaklar.html")

sitemap = ROOT / "sitemap.xml"
if sitemap.exists():
    t = sitemap.read_text(encoding="utf-8")
    for u in [DECISION_URL, AUDIT_URL]:
        if u not in t:
            t = t.replace("</urlset>", f'  <url><loc>{u}</loc><lastmod>2026-08-19</lastmod></url>\n</urlset>')
    if write_if_changed(sitemap, t):
        changed.append("sitemap.xml")
    ET.fromstring(sitemap.read_text(encoding="utf-8"))

llms = ROOT / "llms.txt"
if llms.exists():
    t = llms.read_text(encoding="utf-8")
    for line in [
        f"- Workflow opportunity decision table: {DECISION_URL}",
        f"- Paid process analysis request: {AUDIT_URL}",
        f"- Public workflow inventory: {BASE}/veri/gun4-workflow-inventory-public.csv",
    ]:
        if line not in t:
            t = t.rstrip() + "\n" + line + "\n"
    if write_if_changed(llms, t):
        changed.append("llms.txt")

for rel, canonical in [(DECISION_REL, DECISION_URL),(AUDIT_REL, AUDIT_URL)]:
    text = (ROOT / rel).read_text(encoding="utf-8")
    if text.count('rel="canonical"') != 1 or canonical not in text:
        raise SystemExit("Canonical QA failed: " + rel)
    if "\ufffd" in text or "PASS/Fyapay" in text:
        raise SystemExit("Text integrity failed: " + rel)

pub_rows = list(csv.DictReader(io.StringIO((ROOT/"veri/gun4-workflow-inventory-public.csv").read_text(encoding="utf-8"))))
if len(pub_rows) != 30:
    raise SystemExit("Public inventory row count must be 30.")

public_text = (ROOT/"veri/gun4-workflow-inventory-public.csv").read_text(encoding="utf-8")
if re.search(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', public_text):
    raise SystemExit("Email detected in public inventory.")
if re.search(r'\b(?:\+?90)?0?5\d{9}\b', public_text.replace(" ","")):
    raise SystemExit("Phone-like data detected in public inventory.")

if sitemap.exists():
    root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
    locs = [e.text.strip() for e in root.iter() if e.tag.endswith("loc") and e.text]
    dups = sorted({u for u in locs if locs.count(u) > 1})
    if dups:
        raise SystemExit("Duplicate sitemap URLs: " + ", ".join(dups))

guard = ROOT / "scripts" / "synapse_text_repair.py"
if guard.exists():
    r = subprocess.run([sys.executable, str(guard)], cwd=ROOT, text=True, capture_output=True)
    print(r.stdout)
    if r.returncode != 0:
        print(r.stderr)
        raise SystemExit("Existing text integrity guard failed.")

changed = list(dict.fromkeys(changed))
print("Files changed:", len(changed))
for rel in changed:
    print("UPDATED:", rel)
print("Public inventory rows: 30")
print("Process-analysis form fields: 3")
print("New product features: 0")
print("DAY 4 REVENUE BRIDGE QA: PASS")
