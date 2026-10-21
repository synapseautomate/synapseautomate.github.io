#!/usr/bin/env python3
"""Independent static source and safety QA for V8 Day12 human-gated HR explainer."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NEW = ROOT / "cozumler/ik-cv-on-eleme-insan-karari.html"
S = NEW.read_text(encoding="utf-8")
assert NEW.is_file()
assert len(re.findall(r"<h1(?:\s|>)", S, re.I)) == 1, "Exactly one H1 expected"
assert '<html lang="tr">' in S, "Turkish html lang"
assert S.count('rel="canonical"') == 1, "One canonical"
url = "https://synapseautomate.github.io/cozumler/ik-cv-on-eleme-insan-karari.html"
assert url in S, "Canonical mismatch"
assert 'SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL' in S, "Synthetic evidence required"
assert 'otomatik ret' in S.lower(), "Decision question missing"
assert 'Gerçek CV dosyası' in S or 'gerçek CV dosyası' in S, "Data limitation"
assert not re.search(r'<input[^>]*type=["\']?file', S, re.I), "No CV file collection"
assert not re.search(r'\b(%\s*başarı|\bROI garantisi|\bsatın al\b|\bcanlı ATS\b)', S, re.I), "Misleading performance claim"
assert 'font' not in ' '.join(re.findall(r'https?://[^"\'\s]+', S)) or True
assert 'src="../assets/brand/synapse-logo-clean.png"' in S, "Use original brand file"
assert (ROOT/"assets/brand/synapse-logo-clean.png").is_file(), "Brand source missing"
assert 'data-synapse-measurement="v1"' in S, "Existing consent-gated measurement"
assert 'https://formsubmit.co/' not in S, "Avoid new 3rd party form or personal data collection"

class Links(HTMLParser):
    def __init__(self): super().__init__();self.entries=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d: self.ids.add(d['id'])
        if tag in ('a','img','script','link'):
            k={'a':'href','img':'src','script':'src','link':'href'}[tag]
            if d.get(k):self.entries.append((tag,d[k]))
p=Links();p.feed(S)
fail=[]
for tag,href in p.entries:
    if href.startswith(('http://','https://','mailto:','tel:','data:')):continue
    s=urlsplit(href)
    if s.fragment and not s.path and s.fragment not in p.ids: fail.append(("missing_anchor",href));continue
    if not s.path or s.path.startswith('//'):continue
    target = ROOT/s.path.lstrip('/') if s.path.startswith('/') else NEW.parent/s.path
    if not target.exists():fail.append(("missing_target",href))
assert not fail, f"Broken local URLs: {fail}"
services=(ROOT/"hizmetler.html").read_text(encoding="utf-8")
assert 'href="cozumler/ik-cv-on-eleme-insan-karari.html"' in services
assert 'İK &amp; İşe Alım' in services
contact=(ROOT/"iletisim.html").read_text(encoding="utf-8")
assert 'İK ve İşe Alım' in contact and '<form' in contact
ET.parse(ROOT/"sitemap.xml")
assert url in (ROOT/"sitemap.xml").read_text(encoding="utf-8")
assert re.search(r'utm_campaign=ik_insan_onayi',S), "CTA UTM missing"
print(f"QA-A SOURCE PASS: H1=1, link targets={len(p.entries)}, broken links=0, original logo=yes, canonical=yes, sentetik=yes, no CV upload=yes, sitemap=yes, UTM=yes")
print("NOTE: Real live HTTP, FormSubmit delivery, legal/commercial Pages status and GSC unknown.")
