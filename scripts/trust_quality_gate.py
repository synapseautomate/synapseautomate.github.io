#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
import json, re, subprocess, sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = [
    "guven-merkezi.html",
    "gizlilik.html",
    "surec-analizi.html",
    "iletisim.html",
    "kaynaklar.html",
    "sektorler/gayrimenkul-yonetimi.html",
    "kanit/risk-yetki-matrisi.html",
    "kanit/ornek-insan-onay-karti.html",
]
FORBIDDEN = [("day" + " 9"), ("gün" + " 9"), "lorem ipsum", "synapseautomate.com", "public benchmark", "v1.0.0"]
entity = json.loads((ROOT / "veri/public-entity.json").read_text(encoding="utf-8"))
ok = True

class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.canonical = 0
        self.schema = 0
        self.details = 0
        self.hrefs = []
        self.ids = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "h1": self.h1 += 1
        if tag == "link" and "canonical" in (d.get("rel") or "").split(): self.canonical += 1
        if tag == "script" and d.get("type") == "application/ld+json": self.schema += 1
        if tag == "details": self.details += 1
        if tag == "a" and d.get("href"): self.hrefs.append(d["href"])
        if d.get("id"): self.ids.append(d["id"])

def fail(msg):
    global ok
    ok = False
    print("FAIL:", msg)

for rel in PUBLIC:
    p = ROOT / rel
    if not p.exists():
        fail("missing " + rel)
        continue
    t = p.read_text(encoding="utf-8")
    low = t.lower()
    scan = Scan(); scan.feed(t)
    if scan.h1 != 1: fail(f"h1 count {rel}: {scan.h1}")
    if scan.canonical != 1: fail(f"canonical count {rel}: {scan.canonical}")
    if scan.schema < 1: fail("schema missing " + rel)
    if len(scan.ids) != len(set(scan.ids)): fail("duplicate id " + rel)
    for marker in FORBIDDEN:
        if marker in low: fail(f"public marker {marker}: {rel}")
    base = p.parent
    for href in scan.hrefs:
        clean = urlsplit(href)
        if clean.scheme or href.startswith(("mailto:", "tel:", "javascript:", "/", "#")):
            continue
        path = clean.path
        if not path: continue
        target = (base / path).resolve()
        if ROOT.resolve() not in target.parents and target != ROOT.resolve():
            continue
        if not target.exists(): fail(f"broken link {rel} -> {href}")

# Trust-center required language.
t = (ROOT / "guven-merkezi.html").read_text(encoding="utf-8").lower()
for term in ["veri minimizasyonu", "saklama", "olay yönetimi", "bilinmiyor", "sözleşme", "fatura", "kabul kriteri", "insan onayı"]:
    if term not in t: fail("trust center term " + term)

# Gayrimenkul requirements.
g = (ROOT / "sektorler/gayrimenkul-yonetimi.html").read_text(encoding="utf-8")
gscan = Scan(); gscan.feed(g)
if gscan.details != 12: fail(f"gayrimenkul FAQ != 12 ({gscan.details})")
if "Süreç Analizi İste" not in g: fail("gayrimenkul CTA")

# Form sensitivity and routing clarity.
s = (ROOT / "surec-analizi.html").read_text(encoding="utf-8").lower()
for term in ["hassas", "formsubmit", "süreç metadatası"]:
    if term not in s: fail("process form trust copy " + term)

# Sitemap.
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
for rel in ["guven-merkezi.html", "kanit/risk-yetki-matrisi.html", "kanit/ornek-insan-onay-karti.html"]:
    if rel not in sm: fail("sitemap " + rel)

# Public entity consistency on core trust surfaces.
for rel in ["guven-merkezi.html", "gizlilik.html"]:
    t = (ROOT / rel).read_text(encoding="utf-8")
    if entity["email"] not in t or entity["telephone"] not in t:
        fail("entity contact mismatch " + rel)

# Dataset validators.
for v in ["public-proof/workflow-output-schema-v2/validate.py", "public-proof/eval-50-v1/validate.py"]:
    r = subprocess.run([sys.executable, str(ROOT / v)], cwd=ROOT, text=True, capture_output=True)
    print(r.stdout, end="")
    if r.returncode:
        print(r.stderr, end="")
        fail("validator " + v)

print("PASS: trust quality gate" if ok else "FAIL: trust quality gate")
sys.exit(0 if ok else 1)
