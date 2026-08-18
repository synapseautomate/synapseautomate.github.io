from pathlib import Path
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(".").resolve()
BASE = "https://synapseautomate.github.io"
GUIDE_REL = "rehberler/ai-otomasyonunda-yanlis-baslangiclar.html"
TOOL_REL = "araclar/ai-otomasyon-risk-degerlendirmesi.html"
GUIDE_URL = f"{BASE}/{GUIDE_REL}"
TOOL_URL = f"{BASE}/{TOOL_REL}"

def write_if_changed(path: Path, content: str):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return True

STYLE = r'''
:root{--bg:#06111f;--bg2:#081827;--panel:#10263a;--panel2:#0c1d2e;--line:#284962;--text:#eef7fb;--muted:#a9bbc6;--cyan:#57ded5;--blue:#5ca9ff;--warn:#ffd37a;--good:#7ce3a1}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:linear-gradient(180deg,var(--bg),var(--bg2) 45%,var(--bg));color:var(--text);font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.65}
a{color:#8ee6ef;text-decoration:none}a:hover{text-decoration:underline}.container{width:min(1120px,calc(100% - 32px));margin:auto}
header{position:sticky;top:0;z-index:10;background:rgba(6,17,31,.94);border-bottom:1px solid var(--line);backdrop-filter:blur(10px)}.nav{min-height:72px;display:flex;align-items:center;gap:20px}.brand{font-weight:850;color:#fff;font-size:1.15rem;letter-spacing:.02em}.navlinks{display:flex;gap:18px;margin-left:auto}.cta,.btn{display:inline-flex;align-items:center;justify-content:center;padding:12px 18px;border-radius:999px;background:linear-gradient(90deg,var(--cyan),#38b8dd);color:#03121f;font-weight:850;border:0;cursor:pointer}
.breadcrumb{padding:20px 0;color:var(--muted);font-size:.92rem}.hero{padding:54px 0 34px}.kicker{font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--cyan);font-weight:850}h1{font-size:clamp(2.25rem,5vw,4rem);line-height:1.05;margin:.35em 0}h2{font-size:clamp(1.6rem,3vw,2.4rem);line-height:1.15}h3{line-height:1.25}.lead{font-size:1.15rem;max-width:930px;color:#cedce4}
.section{padding:50px 0}.section-tight{padding:28px 0}.head{display:flex;justify-content:space-between;align-items:end;gap:28px;margin-bottom:22px}.head p{max-width:580px;color:var(--muted)}.grid{display:grid;gap:18px}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}.card{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);border-radius:18px;padding:22px}.card h3{margin-top:0}.tag{display:inline-block;padding:5px 10px;border:1px solid var(--line);border-radius:999px;color:var(--cyan);font-size:.82rem}
.quote{border-left:4px solid var(--cyan);padding:16px 20px;background:rgba(87,222,213,.07);border-radius:0 14px 14px 0}.muted{color:var(--muted)}
.checks{display:grid;gap:12px}.check{display:grid;grid-template-columns:28px 1fr;gap:10px;align-items:start;background:var(--panel2);border:1px solid var(--line);border-radius:14px;padding:14px}.check input{width:20px;height:20px;margin-top:3px}
.scorebox{position:sticky;top:92px;background:linear-gradient(180deg,#12314b,#0d2033);border:1px solid var(--line);border-radius:20px;padding:24px}.score{font-size:3rem;font-weight:900;line-height:1}.result{margin-top:14px;padding:14px;border-radius:14px;background:#0a1a29;border:1px solid var(--line)}.risk{color:var(--warn)}.ready{color:var(--good)}
.band{background:linear-gradient(120deg,#0f2d43,#0b1f31);border:1px solid var(--line);border-radius:22px;padding:28px}.bandrow{display:flex;gap:24px;justify-content:space-between;align-items:center}footer{border-top:1px solid var(--line);padding:38px 0;margin-top:38px;color:var(--muted)}.foot{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
@media(max-width:760px){.navlinks{display:none}.nav{justify-content:space-between}.g2,.g3{grid-template-columns:1fr}.head,.bandrow{display:block}.scorebox{position:static}.cta{font-size:.85rem}.hero{padding-top:34px}}
'''

org_schema = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": f"{BASE}/#organization",
    "name": "Synapse Automate",
    "url": f"{BASE}/",
    "sameAs": [
        "https://github.com/synapseautomate",
        "https://www.linkedin.com/company/synapseautomate/",
    ],
}

article_schema = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "AI Otomasyonunda En Sık Yapılan 7 Yanlış Başlangıç",
    "description": "AI otomasyon projelerinde veri, süreç, insan onayı, ölçüm ve yetki sınırları kurulmadan yapılan başlangıçların neden riskli olduğunu açıklayan rehber.",
    "mainEntityOfPage": GUIDE_URL,
    "author": {"@id": f"{BASE}/#organization"},
    "publisher": {"@id": f"{BASE}/#organization"},
    "datePublished": "2026-08-18",
    "dateModified": "2026-08-18",
}

guide = f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>AI Otomasyonunda 7 Yanlış Başlangıç | Synapse Automate</title>
<meta name="description" content="AI otomasyonunda süreç, veri, insan onayı, yetki ve ölçüm kurulmadan yapılan 7 yanlış başlangıç. Daha kontrollü bir pilot için uygulanabilir çerçeve.">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{GUIDE_URL}">
<meta property="og:type" content="article">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Synapse Automate">
<meta property="og:title" content="AI Otomasyonunda En Sık Yapılan 7 Yanlış Başlangıç">
<meta property="og:description" content="Daha fazla AI değil; daha görünür süreç, veri, insan onayı ve ölçüm.">
<meta property="og:url" content="{GUIDE_URL}">
<meta name="theme-color" content="#06111f">
<style>{STYLE}</style>
<script type="application/ld+json">{json.dumps(org_schema, ensure_ascii=False, separators=(",", ":"))}</script>
<script type="application/ld+json">{json.dumps(article_schema, ensure_ascii=False, separators=(",", ":"))}</script>
</head>
<body>
<header><div class="container nav">
<a class="brand" href="../index.html">Synapse Automate</a>
<nav class="navlinks"><a href="../hizmetler.html">Hizmetler</a><a href="../urunler.html">Ürünler</a><a href="../sektorler.html">Sektörler</a><a href="../kaynaklar.html">Kaynaklar</a></nav>
<a class="cta" href="../iletisim.html?konu=surec-analizi">Süreç Analizi İste</a>
</div></header>
<main>
<div class="container breadcrumb"><a href="../index.html">Ana Sayfa</a> / <a href="../kaynaklar.html">Kaynaklar</a> / 7 Yanlış Başlangıç</div>

<section class="hero"><div class="container">
<div class="kicker">Thought leadership • operasyon disiplini</div>
<h1>AI otomasyonunda en sık yapılan 7 yanlış başlangıç.</h1>
<p class="lead">Bir iş akışına AI eklemek onu otomatik olarak daha iyi hale getirmez. Süreç, veri, yetki, insan onayı ve ölçüm görünür değilse yalnızca daha hızlı belirsizlik üretebilirsiniz.</p>
<div class="quote"><strong>Temel ilke:</strong> “Ne otomatikleşecek?” sorusundan önce “hangi karar, hangi veriyle, hangi yetki altında ve hangi ölçümle çalışacak?” sorusu cevaplanmalıdır.</div>
</div></section>

<section class="section-tight"><div class="container">
<div class="grid g2">
<div class="card"><span class="tag">1</span><h3>Problemi değil aracı seçerek başlamak</h3><p>“Chatbot yapalım”, “agent kuralım” veya “AI ekleyelim” başlangıç noktası değildir. Önce tekrar eden iş, gecikme, hata ve karar noktası tanımlanmalıdır.</p></div>
<div class="card"><span class="tag">2</span><h3>Kaynağı görünmez bırakmak</h3><p>AI çıktısının hangi veri, belge veya kurala dayandığı bilinmiyorsa kullanıcı doğru ile tahmini ayıramaz. Kaynak ve güven seviyesi görünür olmalıdır.</p></div>
<div class="card"><span class="tag">3</span><h3>İnsan onayını sonradan eklemek</h3><p>Finansal etki, müşteri iletişimi, fiyatlama, sağlık, hukuk veya itibar riski taşıyan adımlarda insan onayı tasarımın başından itibaren yer almalıdır.</p></div>
<div class="card"><span class="tag">4</span><h3>“Unknown” ile uydurma değeri ayırmamak</h3><p>Eksik bilgi varsa sistem bunu açıkça söylemelidir. Uydurma bir değer üretmek, eksik veriyle çalışmaktan daha tehlikelidir.</p></div>
<div class="card"><span class="tag">5</span><h3>Baz çizgi olmadan başarı ilan etmek</h3><p>Başlangıçtaki süre, hata, tekrar işleme veya müdahale oranı ölçülmeden pilot sonrası iyileşme iddiası güvenilir değildir.</p></div>
<div class="card"><span class="tag">6</span><h3>Yetki ile erişimi karıştırmak</h3><p>Bir sisteme erişebilmek, o sistem adına karar verme yetkisi olduğu anlamına gelmez. Okuma, önerme, yazma ve dış eylem yetkileri ayrı ele alınmalıdır.</p></div>
<div class="card"><span class="tag">7</span><h3>Pilotu geniş kapsamla başlatmak</h3><p>İlk pilot tek, ölçülebilir ve geri alınabilir bir akışta başlamalıdır. Küçük ama kanıtlanabilir kapsam, büyük ve belirsiz kapsamdan daha değerlidir.</p></div>
<div class="card"><span class="tag">Kontrol</span><h3>Doğru başlangıç neye benzer?</h3><p>Girdi → doğrulama → kaynak → AI taslağı → kural kapısı → insan onayı → kayıtlı çıktı. Her adımın sahibi ve ölçümü bellidir.</p></div>
</div>
</div></section>

<section class="section"><div class="container">
<div class="head"><div><div class="kicker">Kendini test et</div><h2>Süreciniz bu hatalardan kaçına açık?</h2></div><p>Ücretsiz değerlendirme aracı 10 kontrol sorusuyla sürecinizin risk ve hazırlık görünümünü verir. Sonuç teşhis değildir; pilot öncesi konuşmayı yapılandırır.</p></div>
<div class="band"><div class="bandrow"><div><h3>AI Otomasyon Risk Değerlendirmesi</h3><p class="muted">Kaynak, yetki, insan onayı, veri minimizasyonu ve ölçüm hazırlığını kontrol edin.</p></div><a class="btn" href="../araclar/ai-otomasyon-risk-degerlendirmesi.html">Ücretsiz Değerlendirmeyi Aç</a></div></div>
</div></section>

<section class="section-tight"><div class="container">
<div class="grid g2">
<div class="card"><h3>Finans ve bankacılıkta örnek</h3><p>Finansal kararların kendisini değil, karar öncesi kontrol ve inceleme akışını otomatikleştirmek daha güvenli başlangıçtır.</p><p><a href="../sektorler/finans.html">Finans &amp; Bankacılık süreç çerçevesini incele →</a></p></div>
<div class="card"><h3>Tek sonraki adım</h3><p>Bir süreci seçin. Girdi, karar, çıktı, risk, yetki ve ölçümünü birlikte haritalayalım.</p><p><a href="../iletisim.html?konu=surec-analizi">Süreç Analizi İste →</a></p></div>
</div>
</div></section>
</main>
<footer><div class="container foot"><span>© 2026 Synapse Automate</span><span>İnsan denetimli, ölçülebilir AI otomasyonu.</span></div></footer>
</body></html>'''

tool_schema = {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "AI Otomasyon Risk Değerlendirmesi",
    "url": TOOL_URL,
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "provider": {"@id": f"{BASE}/#organization"},
    "description": "AI otomasyon pilotu öncesinde süreç, veri, yetki, insan onayı ve ölçüm hazırlığını 10 soruda değerlendiren ücretsiz araç.",
}

checks = [
    "Süreç tek cümlede ve ölçülebilir biçimde tanımlı.",
    "Girdi verisinin kaynağı ve sahibi belli.",
    "Eksik bilgi olduğunda sistemin 'unknown' diyebilmesi planlandı.",
    "AI çıktısının hangi kaynağa dayandığı kullanıcıya gösterilecek.",
    "Kritik karar veya dış eylem için insan onayı var.",
    "Okuma, önerme, yazma ve dış eylem yetkileri ayrı tanımlandı.",
    "Yalnız gerekli veri kullanılacak; veri minimizasyonu yapıldı.",
    "Başlangıç baz çizgisi (süre/hata/müdahale vb.) ölçüldü.",
    "Pilot geri alınabilir ve tek bir sınırlı akışta başlayacak.",
    "Başarı kriteri ve pilot sonrası karşılaştırma yöntemi belli.",
]
checks_html = "\n".join(
    f'<label class="check"><input type="checkbox" data-weight="10"><span><strong>{i+1}.</strong> {text}</span></label>'
    for i, text in enumerate(checks)
)

tool = f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>AI Otomasyon Risk Değerlendirmesi | Synapse Automate</title>
<meta name="description" content="AI otomasyon pilotu öncesi süreç, veri, yetki, insan onayı ve ölçüm hazırlığını 10 soruda ücretsiz değerlendirin.">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{TOOL_URL}">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Synapse Automate">
<meta property="og:title" content="AI Otomasyon Risk Değerlendirmesi">
<meta property="og:description" content="10 kontrol sorusuyla pilot öncesi hazırlık ve risk görünümü.">
<meta property="og:url" content="{TOOL_URL}">
<meta name="theme-color" content="#06111f">
<style>{STYLE}</style>
<script type="application/ld+json">{json.dumps(org_schema, ensure_ascii=False, separators=(",", ":"))}</script>
<script type="application/ld+json">{json.dumps(tool_schema, ensure_ascii=False, separators=(",", ":"))}</script>
</head>
<body>
<header><div class="container nav">
<a class="brand" href="../index.html">Synapse Automate</a>
<nav class="navlinks"><a href="../hizmetler.html">Hizmetler</a><a href="../sektorler.html">Sektörler</a><a href="../kaynaklar.html">Kaynaklar</a></nav>
<a class="cta" href="../iletisim.html?konu=surec-analizi">Süreç Analizi İste</a>
</div></header>
<main>
<div class="container breadcrumb"><a href="../index.html">Ana Sayfa</a> / <a href="../kaynaklar.html">Kaynaklar</a> / AI Otomasyon Risk Değerlendirmesi</div>
<section class="hero"><div class="container">
<div class="kicker">Ücretsiz araç • 10 kontrol noktası</div>
<h1>AI otomasyon pilotunuz ne kadar hazır?</h1>
<p class="lead">Bu araç satış skoru vermez. Süreç, kaynak, veri, yetki, insan onayı ve ölçüm alanlarında hangi temel kontrollerin eksik olduğunu görünür hale getirir.</p>
</div></section>

<section class="section-tight"><div class="container">
<div class="grid g2">
<div><div class="checks">{checks_html}</div></div>
<div>
<div class="scorebox">
<div class="kicker">Hazırlık skoru</div>
<div class="score"><span id="score">0</span>/100</div>
<div id="result" class="result"><strong>Başlangıç:</strong> Kutuları işaretledikçe sonuç güncellenir.</div>
<p class="muted">Bu skor profesyonel güvenlik, hukuk, finans veya sağlık değerlendirmesi değildir. Pilot öncesi süreç konuşmasını yapılandırır.</p>
<p><a class="btn" href="../iletisim.html?konu=ai-otomasyon-risk-degerlendirmesi">Sonucu Süreç Analizine Taşı</a></p>
</div>
</div>
</div>
</div></section>

<section class="section"><div class="container">
<div class="head"><div><div class="kicker">Skoru nasıl yorumlamalı?</div><h2>Eksik kontrol sayısı, otomasyonun riskini görünür kılar.</h2></div></div>
<div class="grid g3">
<div class="card"><h3 class="risk">0–40 • Önce temel</h3><p>Süreç, veri veya yetki sınırları yeterince görünür değil. Pilot kurmadan önce kontrol noktalarını tamamlayın.</p></div>
<div class="card"><h3>50–70 • Pilot adayı</h3><p>Sınırlı kapsamlı, geri alınabilir bir pilot mümkün olabilir; eksik alanları insan onayıyla kapatın.</p></div>
<div class="card"><h3 class="ready">80–100 • Daha kontrollü başlangıç</h3><p>Temel hazırlık güçlü görünüyor. Yine de gerçek sistem, veri ve risk koşulları ayrıca doğrulanmalıdır.</p></div>
</div>
</div></section>

<section class="section-tight"><div class="container">
<div class="grid g2">
<div class="card"><h3>Neden bu 10 soru?</h3><p>AI otomasyonunda en sık yaşanan sorunların önemli kısmı model seçiminin dışında; süreç tanımı, veri kaynağı, yetki, insan onayı ve ölçüm eksiklerinde ortaya çıkar.</p><p><a href="../rehberler/ai-otomasyonunda-yanlis-baslangiclar.html">7 yanlış başlangıç rehberini oku →</a></p></div>
<div class="card"><h3>Finansal süreç mi?</h3><p>Finans ve bankacılıkta kredi, fiyatlama, ödeme veya benzeri maddi kararları otonomlaştırmadan önce insan yetkisi ve kontrol kapıları ayrıca tanımlanmalıdır.</p><p><a href="../sektorler/finans.html">Finans &amp; Bankacılık çerçevesi →</a></p></div>
</div>
</div></section>
</main>
<footer><div class="container foot"><span>© 2026 Synapse Automate</span><span>Ücretsiz değerlendirme • veri sunucuya gönderilmez.</span></div></footer>
<script>
(function(){{
  const boxes=[...document.querySelectorAll('input[type="checkbox"][data-weight]')];
  const scoreEl=document.getElementById('score');
  const result=document.getElementById('result');
  function update(){{
    const score=boxes.filter(b=>b.checked).reduce((s,b)=>s+Number(b.dataset.weight||0),0);
    scoreEl.textContent=score;
    if(score<=40){{
      result.innerHTML='<strong class="risk">Önce temel kontrolleri tamamlayın.</strong><br>Süreç, veri, yetki veya ölçüm alanlarında kritik boşluklar var.';
    }} else if(score<=70){{
      result.innerHTML='<strong>Pilot adayı.</strong><br>Sınırlı ve geri alınabilir bir pilot düşünülebilir; eksik kontrolleri insan onayıyla kapatın.';
    }} else {{
      result.innerHTML='<strong class="ready">Daha kontrollü başlangıç.</strong><br>Temel hazırlık güçlü; yine de gerçek veri, entegrasyon ve risk koşullarını pilotta doğrulayın.';
    }}
  }}
  boxes.forEach(b=>b.addEventListener('change',update));
  update();
}})();
</script>
</body></html>'''

changed = []
if write_if_changed(ROOT / GUIDE_REL, guide):
    changed.append(GUIDE_REL)
if write_if_changed(ROOT / TOOL_REL, tool):
    changed.append(TOOL_REL)

sitemap = ROOT / "sitemap.xml"
if sitemap.exists():
    st = sitemap.read_text(encoding="utf-8")
    for url in [GUIDE_URL, TOOL_URL]:
        if url not in st:
            st = st.replace("</urlset>", f'  <url><loc>{url}</loc><lastmod>2026-08-18</lastmod></url>\n</urlset>')
    if write_if_changed(sitemap, st):
        changed.append("sitemap.xml")
    ET.fromstring(sitemap.read_text(encoding="utf-8"))

llms = ROOT / "llms.txt"
if llms.exists():
    old = llms.read_text(encoding="utf-8")
    new = old
    for line in [
        f"- AI automation thought-leadership guide: {GUIDE_URL}",
        f"- Free AI automation risk assessment: {TOOL_URL}",
    ]:
        if line not in new:
            new = new.rstrip() + "\n" + line + "\n"
    if write_if_changed(llms, new):
        changed.append("llms.txt")

resources = ROOT / "kaynaklar.html"
if resources.exists():
    old = resources.read_text(encoding="utf-8")
    new = old
    if "rehberler/ai-otomasyonunda-yanlis-baslangiclar.html" not in new and "</main>" in new:
        block = '''
<section class="section"><div class="container">
<div class="section-head"><div><div class="kicker">Yeni kaynaklar</div><h2>AI otomasyonuna daha kontrollü başlayın.</h2></div></div>
<div class="grid grid-2">
<div class="card"><h3>AI Otomasyonunda 7 Yanlış Başlangıç</h3><p>Süreç, veri, yetki, insan onayı ve ölçüm kurulmadan yapılan en yaygın başlangıç hataları.</p><a class="btn btn-secondary" href="rehberler/ai-otomasyonunda-yanlis-baslangiclar.html">Rehberi Oku</a></div>
<div class="card"><h3>AI Otomasyon Risk Değerlendirmesi</h3><p>10 kontrol sorusuyla pilot öncesi hazırlık ve risk görünümünü ücretsiz değerlendirin.</p><a class="btn btn-secondary" href="araclar/ai-otomasyon-risk-degerlendirmesi.html">Ücretsiz Aracı Aç</a></div>
</div></div></section>
'''
        new = new.replace("</main>", block + "</main>", 1)
    if write_if_changed(resources, new):
        changed.append("kaynaklar.html")

for rel in [GUIDE_REL, TOOL_REL]:
    p = ROOT / rel
    if not p.exists():
        raise SystemExit(f"Missing required page: {rel}")
    text = p.read_text(encoding="utf-8")
    if "PASS/Fyapay" in text or "\ufffd" in text:
        raise SystemExit(f"Text integrity issue in {rel}")
    pat = re.compile(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.I | re.S)
    for raw in pat.findall(text):
        json.loads(raw.strip())

tool_text = (ROOT / TOOL_REL).read_text(encoding="utf-8")
if tool_text.count('data-weight="10"') != 10:
    raise SystemExit("Risk assessment must contain exactly 10 weighted checks.")
if "Ücretsiz Değerlendirmeyi Aç" not in (ROOT / GUIDE_REL).read_text(encoding="utf-8"):
    raise SystemExit("Guide does not link to assessment tool.")

guard = ROOT / "scripts" / "synapse_text_repair.py"
if guard.exists():
    r = subprocess.run([sys.executable, str(guard)], cwd=ROOT, text=True, capture_output=True)
    print(r.stdout)
    if r.returncode != 0:
        print(r.stderr)
        raise SystemExit("Text integrity guard failed.")

changed = list(dict.fromkeys(changed))
print("Files changed:", len(changed))
for rel in changed:
    print("UPDATED:", rel)
print("THOUGHT LEADERSHIP + FREE EVAL CLUSTER QA: PASS")
