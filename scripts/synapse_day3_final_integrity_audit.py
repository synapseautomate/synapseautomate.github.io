from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

ROOT = Path(".").resolve()
BASE = "https://synapseautomate.github.io"

REQUIRED = {
    "rehberler/ai-otomasyonunda-yanlis-baslangiclar.html":
        f"{BASE}/rehberler/ai-otomasyonunda-yanlis-baslangiclar.html",
    "araclar/ai-otomasyon-risk-degerlendirmesi.html":
        f"{BASE}/araclar/ai-otomasyon-risk-degerlendirmesi.html",
    "sektorler/finans.html":
        f"{BASE}/sektorler/finans.html",
    "kanit/kilory-yayin-oncesi-kanit-paketi.html":
        f"{BASE}/kanit/kilory-yayin-oncesi-kanit-paketi.html",
    "kaynaklar/ai-otomasyon-otorite-merkezi.html":
        f"{BASE}/kaynaklar/ai-otomasyon-otorite-merkezi.html",
}

errors = []
warnings = []

def err(msg):
    errors.append(msg)

def warn(msg):
    warnings.append(msg)

def normalized_nonempty_lines(text):
    return [line.strip() for line in text.splitlines() if line.strip()]

# 1) Required pages + canonical uniqueness.
canonical_re = re.compile(
    r'<link\b[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\'][^>]*>',
    re.I
)
jsonld_re = re.compile(
    r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.I | re.S
)

for rel, expected_url in REQUIRED.items():
    p = ROOT / rel
    if not p.exists():
        err(f"Required page missing: {rel}")
        continue
    text = p.read_text(encoding="utf-8")
    if "\ufffd" in text or "PASS/Fyapay" in text:
        err(f"Text-integrity marker found in {rel}")

    canonicals = canonical_re.findall(text)
    if len(canonicals) != 1:
        err(f"{rel}: expected exactly 1 canonical tag, found {len(canonicals)}")
    elif canonicals[0] != expected_url:
        err(f"{rel}: canonical mismatch: {canonicals[0]}")

    for raw in jsonld_re.findall(text):
        try:
            json.loads(raw.strip())
        except Exception as exc:
            err(f"{rel}: invalid JSON-LD: {exc}")

# 2) Sitemap: parse + no duplicate loc entries + required URLs exactly once.
sitemap = ROOT / "sitemap.xml"
if not sitemap.exists():
    err("sitemap.xml missing")
else:
    try:
        root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
        locs = []
        for el in root.iter():
            if el.tag.endswith("loc") and el.text:
                locs.append(el.text.strip())
        duplicates = sorted({u for u in locs if locs.count(u) > 1})
        if duplicates:
            err("Duplicate sitemap URLs: " + ", ".join(duplicates))
        for expected in REQUIRED.values():
            c = locs.count(expected)
            if c != 1:
                err(f"Sitemap expected URL exactly once ({c} found): {expected}")
    except Exception as exc:
        err(f"sitemap.xml parse failed: {exc}")

# 3) llms.txt: exact duplicate lines forbidden.
llms = ROOT / "llms.txt"
if not llms.exists():
    warn("llms.txt missing")
else:
    lines = normalized_nonempty_lines(llms.read_text(encoding="utf-8"))
    seen = set()
    dup_lines = []
    for line in lines:
        key = line.casefold()
        if key in seen:
            dup_lines.append(line)
        seen.add(key)
    if dup_lines:
        err("Duplicate llms.txt lines: " + " | ".join(dup_lines))

# 4) Manifest: resource URLs unique.
manifest = ROOT / "content-manifest.json"
if not manifest.exists():
    err("content-manifest.json missing")
else:
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        urls = [
            item.get("url", "").strip()
            for item in data.get("resources", [])
            if isinstance(item, dict) and item.get("url")
        ]
        dup = sorted({u for u in urls if urls.count(u) > 1})
        if dup:
            err("Duplicate manifest resource URLs: " + ", ".join(dup))
    except Exception as exc:
        err(f"content-manifest.json parse failed: {exc}")

# 5) RSS: GUIDs and links unique.
feed = ROOT / "feed.xml"
if not feed.exists():
    err("feed.xml missing")
else:
    try:
        feed_root = ET.fromstring(feed.read_text(encoding="utf-8"))
        guids, links = [], []
        for item in feed_root.iter("item"):
            guid = item.findtext("guid")
            link = item.findtext("link")
            if guid:
                guids.append(guid.strip())
            if link:
                links.append(link.strip())
        dup_guid = sorted({u for u in guids if guids.count(u) > 1})
        dup_link = sorted({u for u in links if links.count(u) > 1})
        if dup_guid:
            err("Duplicate RSS GUIDs: " + ", ".join(dup_guid))
        if dup_link:
            err("Duplicate RSS item links: " + ", ".join(dup_link))
    except Exception as exc:
        err(f"feed.xml parse failed: {exc}")

# 6) robots.txt: sitemap directive should appear at most once.
robots = ROOT / "robots.txt"
if robots.exists():
    lines = normalized_nonempty_lines(robots.read_text(encoding="utf-8"))
    sitemap_lines = [x for x in lines if x.lower().startswith("sitemap:")]
    if len(sitemap_lines) > 1:
        err(f"robots.txt contains {len(sitemap_lines)} Sitemap directives")

# 7) Internal href targets for local .html links on required pages.
href_re = re.compile(r'href=["\']([^"\']+)["\']', re.I)
for rel in REQUIRED:
    p = ROOT / rel
    if not p.exists():
        continue
    text = p.read_text(encoding="utf-8")
    for href in href_re.findall(text):
        href = href.strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "http://", "https://")):
            continue
        href = href.split("#", 1)[0].split("?", 1)[0]
        if not href.endswith(".html"):
            continue
        target = (p.parent / href).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            err(f"{rel}: href escapes repository: {href}")
            continue
        if not target.exists():
            err(f"{rel}: broken internal HTML link: {href}")

# 8) Optional existing text repair guard should be stable/read-only on second run.
guard = ROOT / "scripts" / "synapse_text_repair.py"
if guard.exists():
    import subprocess
    first = subprocess.run([sys.executable, str(guard)], cwd=ROOT, text=True, capture_output=True)
    print(first.stdout)
    if first.returncode != 0:
        err("Existing text integrity guard failed")

print("=== DAY 3 FINAL INTEGRITY AUDIT ===")
for w in warnings:
    print("WARNING:", w)

if errors:
    for e in errors:
        print("ERROR:", e)
    print(f"FINAL AUDIT: FAIL ({len(errors)} error(s))")
    raise SystemExit(1)

print("Duplicate sitemap URLs: 0")
print("Duplicate llms lines: 0")
print("Duplicate manifest resource URLs: 0")
print("Duplicate RSS GUIDs/links: 0")
print("Required canonical mismatches: 0")
print("Broken internal HTML links on audited pages: 0")
print("DAY 3 FINAL INTEGRITY AUDIT: PASS")
