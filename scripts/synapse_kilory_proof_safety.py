from pathlib import Path
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(".").resolve()
BASE = "https://synapseautomate.github.io"
EVIDENCE_URL = BASE + "/kanit/kilory-yayin-oncesi-kanit-paketi.html"
EVIDENCE_REL = "../kanit/kilory-yayin-oncesi-kanit-paketi.html"
KILORY_URL = BASE + "/urunler/kilory.html"

def write_if_changed(path: Path, content: str):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return True

def replace_many(text, replacements):
    for old, new in replacements:
        text = text.replace(old, new)
    return text

changed = []

# 1) Kilory product page: remove risky/unsupported claims.
kilory = ROOT / "urunler" / "kilory.html"
if not kilory.exists():
    raise SystemExit("urunler/kilory.html was not found.")

text = kilory.read_text(encoding="utf-8")

replacements = [
    ("Kilory | AI Beslenme, Aktivite ve Sosyal Motivasyon Uygulaması",
     "Kilory | AI Destekli Günlük Kayıt ve Motivasyon Deneyimi"),
    ("Kilory; AI öğün analizi, tarif, beslenme ve egzersiz koçluğu, barkod, alışkanlık ve sosyal topluluk özelliklerini birleştiren uygulama.",
     "Kilory; fotoğraf destekli öğün kaydı, tarif fikirleri, günlük aktivite ve alışkanlık notları ile sosyal motivasyonu tek deneyimde birleştirmeyi hedefleyen yayın öncesi üründür."),
    ("Kilory — AI destekli beslenme ve aktivite deneyimi",
     "Kilory — AI destekli günlük kayıt ve motivasyon deneyimi"),
    ("Öğün analizi, tarif, beslenme ve egzersiz koçluğu, barkod, alışkanlık takibi ve sosyal motivasyonu tek ürün deneyiminde birleştiren yayına hazır uygulama.",
     "Fotoğraf destekli öğün kaydı, tarif fikirleri, barkod, günlük aktivite ve alışkanlık notları ile sosyal motivasyonu tek deneyimde birleştirmeyi hedefleyen yayın öncesi ürün."),
    ("Beslenme, hareket ve topluluğu tek akışta birleştiren AI-native ürün.",
     "Günlük kayıt, fikir ve sosyal motivasyonu tek akışta birleştirmeyi hedefleyen AI destekli ürün."),
    ("Kilory, kullanıcı düzenlemesi ve kontrollü kayıt yaklaşımıyla kişiselleştirilmiş günlük deneyim oluşturmayı hedefler.",
     "Kilory, AI çıktısını doğrudan gerçek kabul etmek yerine kullanıcı onayı ve düzeltmesini merkeze alan kontrollü bir günlük kayıt deneyimi hedefler."),
    ("AI fotoğrafla öğün analizi", "Fotoğraf destekli öğün kaydı"),
    ("Kalori, makro ve porsiyon tahmini; kullanıcı düzeltmesiyle kayıt.",
     "Görselden oluşturulan tahmini öğün girdisi; kaydetmeden önce kullanıcı onayı ve düzeltmesi gerekir. Tahmin, ölçüm değildir."),
    ("AI şef ve planlama", "Tarif ve öğün fikri desteği"),
    ("Tarif üretimi, öğün önerisi ve kişiselleştirilmiş planlama.",
     "Kullanıcı tercihlerine göre tarif ve öğün fikri üretimi; tıbbi veya kişiye özel diyet tavsiyesi değildir."),
    ("Barkod & makro", "Barkod & ürün kaydı"),
    ("Paketli ürünleri hızlı ekleme, düzenlenebilir besin kayıtları, su ve makro takibi.",
     "Paketli ürünleri hızlı eklemeyi ve kullanıcı tarafından düzenlenebilir günlük kayıtları desteklemeyi hedefleyen akış."),
    ("Egzersiz koçu", "Aktivite kaydı"),
    ("Kişiselleştirilmiş plan, aktivite takibi ve yakılan kalori görünümü.",
     "Kullanıcının aktivite notlarını ve rutinlerini kendi girdileriyle kaydetmesine yardımcı olmayı hedefleyen akış."),
    ("Türkiye’den başlayıp çok dilli ve küresel dağıtıma uygun ürün mimarisi.",
     "Çok dilli kullanım ve farklı pazarlara uyarlanabilirlik hedefi; yayın öncesi doğrulama kapsamındadır."),
]
text = replace_many(text, replacements)
text = re.sub(r"\byayına hazır uygulama\b", "yayın öncesi doğrulama aşamasındaki ürün", text, flags=re.I)
text = re.sub(r"\bbeslenme ve egzersiz koçluğu\b", "günlük kayıt ve aktivite takibi", text, flags=re.I)

# Normalize Kilory SoftwareApplication schema.
script_pat = re.compile(
    r'(<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.I | re.S,
)
def jsonld_repl(m):
    raw = m.group(2).strip()
    try:
        data = json.loads(raw)
    except Exception:
        return m.group(0)

    changed_here = False
    nodes = data if isinstance(data, list) else [data]
    for node in nodes:
        if isinstance(node, dict) and node.get("@type") == "SoftwareApplication" and node.get("name") == "Kilory":
            desired_desc = (
                "Fotoğraf destekli öğün kaydı, tarif fikirleri, günlük aktivite ve alışkanlık notları "
                "ile sosyal motivasyonu birleştirmeyi hedefleyen yayın öncesi yaşam tarzı ürünü."
            )
            if node.get("applicationCategory") != "LifestyleApplication":
                node["applicationCategory"] = "LifestyleApplication"
                changed_here = True
            if node.get("description") != desired_desc:
                node["description"] = desired_desc
                changed_here = True
            if node.get("url") != KILORY_URL:
                node["url"] = KILORY_URL
                changed_here = True

    if not changed_here:
        return m.group(0)
    return m.group(1) + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + m.group(3)

text = script_pat.sub(jsonld_repl, text)

if EVIDENCE_REL not in text:
    safety_block = '''<section class="section"><div class="container">
<div class="section-head"><div><div class="kicker">Yayın öncesi doğrulama</div><h2>Önce kanıt, sonra iddia.</h2></div>
<p>Kilory'nin kamuya açık anlatımı ürün kapsamını tarif eder; sağlık sonucu, ölçüm doğruluğu veya tıbbi fayda garantisi vermez.</p></div>
<div class="grid grid-3">
<div class="card"><h3>Tahmin ≠ ölçüm</h3><p>Fotoğraf veya AI çıktısı olası bir taslaktır. Kullanıcı onayı ve düzeltmesi olmadan kesin gerçek olarak sunulmaz.</p></div>
<div class="card"><h3>Tıbbi tavsiye yok</h3><p>Kilory teşhis, tedavi, hastalık önleme, kişiye özel diyet reçetesi veya egzersiz reçetesi sunmayı amaçlamaz.</p></div>
<div class="card"><h3>Veri minimizasyonu</h3><p>Yayın öncesi testlerde gerçek sağlık verisi kullanılmaması; izin, silme ve veri kullanım sınırlarının ürün içinde görünür olması hedeflenir.</p></div>
</div>
<p style="margin-top:24px"><a class="btn btn-secondary" href="../kanit/kilory-yayin-oncesi-kanit-paketi.html">Yayın Öncesi Kanıt Paketini İncele</a></p>
</div></section>'''
    text = text.replace("</main>", safety_block + "</main>", 1)

if write_if_changed(kilory, text):
    changed.append("urunler/kilory.html")

# 2) Claim-safe copy on other prominent Kilory surfaces.
targets = {
    "index.html": [
        ("AI destekli beslenme, aktivite, tarif, alışkanlık ve sosyal motivasyon deneyimini birleştiren yayına hazır ürün.",
         "Fotoğraf destekli öğün kaydı, tarif fikirleri, günlük aktivite ve alışkanlık notları ile sosyal motivasyonu birleştirmeyi hedefleyen yayın öncesi ürün."),
    ],
    "urunler.html": [
        ("Yayına hazır uygulama", "Yayın öncesi ürün"),
        ("AI öğün analizi, tarif, beslenme ve egzersiz koçluğu, barkod, alışkanlık ve sosyal topluluk katmanını birleştirir.",
         "Fotoğraf destekli öğün kaydı, tarif fikirleri, barkod, günlük aktivite ve alışkanlık notları ile sosyal motivasyon katmanını birleştirmeyi hedefler."),
    ],
    "kinetra-group.html": [
        ("Kinetra Studios’un AI destekli beslenme, aktivite ve sosyal motivasyon ürünü.",
         "Kinetra Studios portföyünde, günlük kayıt ve sosyal motivasyon deneyimi olarak yayın öncesi doğrulanan ürün."),
    ],
}
for rel, reps in targets.items():
    p = ROOT / rel
    if not p.exists():
        continue
    old = p.read_text(encoding="utf-8")
    new = replace_many(old, reps)
    new = re.sub(r"\byayına hazır uygulama\b", "yayın öncesi ürün", new, flags=re.I)
    if write_if_changed(p, new):
        changed.append(rel)

# 3) llms.txt: descriptive only, no ranking claims.
llms = ROOT / "llms.txt"
if llms.exists():
    old = llms.read_text(encoding="utf-8")
    new = old.replace(
        "Kilory — AI nutrition, activity and social motivation application",
        "Kilory — pre-release lifestyle product concept for assisted meal logging, daily activity/habit notes and social motivation; no medical claims",
    )
    line = "- Kilory pre-release evidence: " + EVIDENCE_URL
    if line not in new:
        new = new.rstrip() + "\n" + line + "\n"
    if write_if_changed(llms, new):
        changed.append("llms.txt")

# 4) Evidence page: feature matrix + claim limits + privacy + store copy + screen flow.
evidence = ROOT / "kanit" / "kilory-yayin-oncesi-kanit-paketi.html"
evidence_html = '''<!doctype html>
<html lang="tr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Kilory Yayın Öncesi Kanıt Paketi | Synapse Automate</title>
<meta name="description" content="Kilory için özellik matrisi, iddia sınırları, gizlilik prensipleri, mağaza metni, ekran akışı ve yayın kapıları. Sağlık sonucu garantisi veya tıbbi tavsiye içermez.">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="https://synapseautomate.github.io/kanit/kilory-yayin-oncesi-kanit-paketi.html">
<meta property="og:type" content="article">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Synapse Automate">
<meta property="og:title" content="Kilory Yayın Öncesi Kanıt Paketi">
<meta property="og:description" content="Özellik matrisi, iddia sınırları, gizlilik, mağaza metni, ekran akışı ve yayın kapıları.">
<meta property="og:url" content="https://synapseautomate.github.io/kanit/kilory-yayin-oncesi-kanit-paketi.html">
<meta property="og:image" content="https://synapseautomate.github.io/assets/og-synapse.png">
<meta name="theme-color" content="#06111f">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/styles.css">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"Kilory Yayın Öncesi Kanıt Paketi","url":"https://synapseautomate.github.io/kanit/kilory-yayin-oncesi-kanit-paketi.html","about":{"@type":"SoftwareApplication","name":"Kilory","applicationCategory":"LifestyleApplication","url":"https://synapseautomate.github.io/urunler/kilory.html"}}</script>
</head>
<body>
<a class="skip" href="#main">İçeriğe geç</a>
<header class="site-header"><div class="container nav">
<a class="brand" href="../index.html" aria-label="Synapse Automate ana sayfa"><img src="../assets/synapse-logo.png" alt="Synapse Automate"></a>
<button class="menu-button" aria-label="Menüyü aç" aria-expanded="false">☰</button>
<nav class="nav-links" aria-label="Ana menü"><a href="../hizmetler.html">Hizmetler</a><a href="../urunler.html">Ürünler</a><a href="../hakkimizda.html">Hakkımızda</a><a href="../iletisim.html">İletişim</a></nav>
<a class="nav-cta" href="../urunler/kilory.html">Kilory'ye Dön</a>
</div></header>

<main id="main">
<div class="container breadcrumb"><a href="../index.html">Ana Sayfa</a> / <a href="../urunler/kilory.html">Kilory</a> / <span>Yayın Öncesi Kanıt Paketi</span></div>

<section class="page-hero"><div class="container">
<div class="kicker">Kilory • yayın öncesi kanıt</div>
<h1>Önce kapsamı ve sınırı kanıtla; sonra mağaza iddiasını yayınla.</h1>
<p class="lead">Bu sayfa Kilory'nin yayın öncesi ürün iddialarını sınırlamak için hazırlanmış kanıt çerçevesidir. Mevcut ürün anlatımı tıbbi fayda, kesin kalori/makro doğruluğu, hastalık yönetimi, kişiye özel diyet veya egzersiz reçetesi vaat etmez.</p>
</div></section>

<section class="section-tight"><div class="container">
<div class="section-head"><div><div class="kicker">1. Özellik matrisi</div><h2>Ürün kapsamı ≠ doğrulanmış sonuç.</h2></div><p>Aşağıdaki satırlar özellik niyetini tarif eder. Canlı test, mağaza yayını ve kullanıcı doğrulaması ayrı kapılardır.</p></div>
<div class="table-wrap"><table>
<thead><tr><th>Alan</th><th>Yayın öncesi kapsam</th><th>Kullanıcı kontrolü</th><th>İzin verilen iddia</th><th>Yayın kanıtı</th></tr></thead>
<tbody>
<tr><td>Fotoğraf destekli öğün kaydı</td><td>Görselden tahmini kayıt taslağı</td><td>Onay / düzeltme zorunlu</td><td>“Tahmini kayıt taslağı oluşturur”</td><td>UI testi + hata örnekleri</td></tr>
<tr><td>Tarif fikirleri</td><td>Tercihlere göre tarif fikri</td><td>Kullanıcı seçer</td><td>“Tarif fikri üretir”</td><td>İçerik güvenlik testi</td></tr>
<tr><td>Barkod / ürün kaydı</td><td>Paketli ürün girişi</td><td>Kaynak veriyi kullanıcı doğrular</td><td>“Kayıt girişini hızlandırmayı hedefler”</td><td>Veri kaynağı + fallback testi</td></tr>
<tr><td>Aktivite / alışkanlık notları</td><td>Kullanıcı girdisiyle günlük kayıt</td><td>Kullanıcı düzenler / siler</td><td>“Günlük kayıt tutmaya yardımcı olur”</td><td>CRUD + silme testi</td></tr>
<tr><td>Sosyal motivasyon</td><td>Paylaşım / grup / meydan okuma kapsamı</td><td>Paylaşım kullanıcı seçimine bağlı</td><td>“Sosyal motivasyon özellikleri hedefler”</td><td>Moderasyon + gizlilik testi</td></tr>
</tbody></table></div>
</div></section>

<section class="section"><div class="container">
<div class="section-head"><div><div class="kicker">2. Claim sınırları</div><h2>Mağaza metninde kullanma / kullan.</h2></div></div>
<div class="grid grid-2">
<div class="card"><h3>Kullanma</h3><ul>
<li>“Kaloriyi doğru ölçer”, “makroyu kesin hesaplar”</li>
<li>“Kilo verdirir”, “sağlığınızı iyileştirir”, “hastalığı önler”</li>
<li>“Diyetisyen yerine geçer”, “kişiye özel diyet verir”</li>
<li>“Egzersiz reçetesi verir”, “tedaviye yardımcı olur”</li>
<li>Kanıt yokken “en doğru”, “en iyi”, “garantili”</li>
</ul></div>
<div class="card"><h3>Kullan</h3><ul>
<li>“Tahmini öğün kaydı taslağı”</li>
<li>“Kullanıcı onayı ve düzenlemesiyle kayıt”</li>
<li>“Tarif fikirleri ve günlük kayıt desteği”</li>
<li>“Aktivite ve alışkanlık notlarını tek yerde düzenleme”</li>
<li>“Tıbbi tavsiye değildir”</li>
</ul></div>
</div>
</div></section>

<section class="section-tight"><div class="container">
<div class="section-head"><div><div class="kicker">3. Gizlilik ve veri sınırı</div><h2>Yayın öncesi minimum güven kapısı.</h2></div></div>
<div class="grid grid-3">
<div class="card"><h3>İzin</h3><p>Fotoğraf, kamera veya hassas nitelikte olabilecek kullanıcı verisi işlenmeden önce amaç ve izin açık olmalıdır.</p></div>
<div class="card"><h3>Minimizasyon</h3><p>Gerekmeyen veri toplanmaz. Demo ve public testlerde gerçek sağlık verisi kullanılmaz.</p></div>
<div class="card"><h3>Kontrol</h3><p>Kullanıcı verisini görme, düzenleme ve silme yolu ürün içinde anlaşılır biçimde bulunmalıdır.</p></div>
</div>
</div></section>

<section class="section"><div class="container">
<div class="section-head"><div><div class="kicker">4. Mağaza metni</div><h2>Claim-safe kısa açıklama.</h2></div></div>
<div class="card"><p><strong>Kilory</strong>, öğünlerinizi ve günlük alışkanlıklarınızı kaydetmeye, tarif fikirleri keşfetmeye, aktivite notlarınızı düzenlemeye ve sosyal motivasyon özelliklerini tek yerde kullanmaya yardımcı olmayı hedefleyen bir yaşam tarzı uygulamasıdır. Fotoğraf destekli AI çıktıları tahmini taslaklardır ve kullanıcı onayı/düzeltmesi gerektirir. Kilory tıbbi teşhis, tedavi, hastalık önleme, kişiye özel diyet veya egzersiz reçetesi sunmaz.</p></div>
</div></section>

<section class="section-tight"><div class="container">
<div class="section-head"><div><div class="kicker">5. Ekran akışı</div><h2>Yayın öncesi minimum 10 ekran.</h2></div></div>
<ol class="steps">
<li><strong>Karşılama:</strong> ürün kapsamı ve “tıbbi tavsiye değildir” sınırı.</li>
<li><strong>İzin:</strong> kamera/fotoğraf ve veri kullanım amacı.</li>
<li><strong>Tercihler:</strong> kullanıcı tarafından değiştirilebilir tercih ve hedefler.</li>
<li><strong>Ana ekran:</strong> günlük kayıtların özeti; kesin sağlık sonucu dili yok.</li>
<li><strong>Öğün ekle:</strong> manuel, fotoğraf veya ürün girişi.</li>
<li><strong>AI taslak:</strong> tahmin + confidence/warning + kaynak türü.</li>
<li><strong>Kullanıcı onayı:</strong> düzenle / kabul et / iptal et.</li>
<li><strong>Aktivite & alışkanlık:</strong> kullanıcının kendi girdileri.</li>
<li><strong>Sosyal alan:</strong> paylaşım ayarı + moderasyon/şikâyet yolu.</li>
<li><strong>Gizlilik & hesap:</strong> izinler, veri kontrolü, silme/export yolu.</li>
</ol>
</div></section>

<section class="section"><div class="container">
<div class="section-head"><div><div class="kicker">6. Yayın kapısı</div><h2>PASS olmadan mağaza iddiası büyütülmez.</h2></div></div>
<div class="grid grid-2">
<div class="card"><h3>Makine / test kapısı</h3><ul>
<li>Fotoğraf taslağı kullanıcı onayı olmadan kaydedilmiyor.</li>
<li>Eksik / düşük güvenli çıktı warning üretiyor.</li>
<li>Silme ve düzenleme çalışıyor.</li>
<li>İzin reddedildiğinde güvenli fallback var.</li>
<li>Gerçek sağlık verisi public testte kullanılmıyor.</li>
</ul></div>
<div class="card"><h3>İnsan / yayın kapısı</h3><ul>
<li>Mağaza metnindeki her iddia ürün içinde görülebiliyor.</li>
<li>Ekran görüntüsü gerçek UI ile eşleşiyor.</li>
<li>Gizlilik ve izin metni anlaşılır.</li>
<li>Sağlık sonucu veya doğruluk garantisi yok.</li>
<li>Yaş derecelendirmesi ve mağaza politikası ayrıca kontrol edildi.</li>
</ul></div>
</div>
</div></section>

<section class="section-tight"><div class="container"><div class="band"><div class="band-grid">
<div><div class="kicker">Kanıt seviyesi</div><h2>Bu paket ürün spesifikasyonu ve yayın kapısıdır; canlı müşteri sonucu değildir.</h2><p>Son güncelleme: 18 Ağustos 2026. Bir iddia gerçek kullanıcı verisi veya kontrollü test ile doğrulanmadan başarı sonucu olarak pazarlanmaz.</p></div>
<a class="btn btn-primary" href="../urunler/kilory.html">Kilory Ürün Sayfası</a>
</div></div></div></section>
</main>

<footer class="footer"><div class="container">
<div class="footer-grid">
<div><a class="brand" href="../index.html"><img src="../assets/synapse-logo.png" alt="Synapse Automate"></a><p style="color:#8fa8b8;max-width:370px">Kurumsal AI otomasyonu, AI-native ürünler ve insan denetimli dijital operasyon sistemleri.</p></div>
<div><h4>Çözümler</h4><a href="../urunler/revenueos.html">RevenueOS</a><a href="../urunler/kilory.html">Kilory</a><a href="../hizmetler.html">Kurumsal Hizmetler</a></div>
<div><h4>Kurumsal</h4><a href="../hakkimizda.html">Hakkımızda</a><a href="../iletisim.html">İletişim</a></div>
<div><h4>Kaynak</h4><a href="../sitemap.xml">Site Haritası</a></div>
</div>
<div class="copyright"><span>© 2026 Synapse Automate. Tüm hakları saklıdır.</span><span>Kilory yayın öncesi claim-safe kanıt çerçevesi.</span></div>
</div></footer>
<script defer src="../assets/app.js"></script>
</body></html>
'''
if write_if_changed(evidence, evidence_html):
    changed.append("kanit/kilory-yayin-oncesi-kanit-paketi.html")

# 5) Sitemap.
sitemap = ROOT / "sitemap.xml"
if sitemap.exists():
    st = sitemap.read_text(encoding="utf-8")
    if EVIDENCE_URL not in st:
        entry = "\n  <url><loc>" + EVIDENCE_URL + "</loc><lastmod>2026-08-18</lastmod></url>\n"
        st = st.replace("</urlset>", entry + "</urlset>")
        sitemap.write_text(st, encoding="utf-8", newline="\n")
        changed.append("sitemap.xml")

# 6) Hard QA.
kilory_text = kilory.read_text(encoding="utf-8")
for phrase in [
    "yayına hazır uygulama",
    "Egzersiz koçu",
    "Kişiselleştirilmiş plan, aktivite takibi ve yakılan kalori görünümü.",
    "Kalori, makro ve porsiyon tahmini; kullanıcı düzeltmesiyle kayıt.",
]:
    if phrase.lower() in kilory_text.lower():
        raise SystemExit("Unsafe Kilory phrase remains: " + phrase)

if EVIDENCE_REL not in kilory_text:
    raise SystemExit("Kilory page does not link to evidence page.")

if sitemap.exists() and EVIDENCE_URL not in sitemap.read_text(encoding="utf-8"):
    raise SystemExit("Evidence page missing from sitemap.")

for rel_asset in ["assets/styles.css", "assets/app.js", "assets/synapse-logo.png"]:
    if not (ROOT / rel_asset).exists():
        raise SystemExit("Required asset missing: " + rel_asset)

jsonld_pat = re.compile(
    r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.I | re.S,
)
for p in [kilory, evidence]:
    for raw in jsonld_pat.findall(p.read_text(encoding="utf-8")):
        json.loads(raw.strip())

if sitemap.exists():
    ET.fromstring(sitemap.read_text(encoding="utf-8"))

guard = ROOT / "scripts" / "synapse_text_repair.py"
if guard.exists():
    result = subprocess.run([sys.executable, str(guard)], cwd=ROOT, text=True, capture_output=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise SystemExit("Text integrity guard failed after Kilory patch.")

changed = list(dict.fromkeys(changed))
print("Files changed:", len(changed))
for rel in changed:
    print("UPDATED:", rel)
print("KILORY PRE-RELEASE PROOF + CLAIM SAFETY QA: PASS")
