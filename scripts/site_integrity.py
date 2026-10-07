#!/usr/bin/env python3
# trigger: discovery-qa-v1
from __future__ import annotations
import json, re, sys, urllib.parse, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {".git", "_site", "D01", "D02", "D03", "__pycache__"}
PRIMARY = {
    "index.html","hizmetler.html","urunler.html","sektorler.html","kaynaklar.html",
    "guven-merkezi.html","hakkimizda.html","iletisim.html","site-haritasi.html",
    "degisiklikler.html","kanit/teknik-kanit-indeksi.html"
}
DEPRECATED = {
    "urunler/agentready.html":"https://synapseautomate.github.io/urunler.html",
    "urunler/creative.html":"https://synapseautomate.github.io/urunler.html",
    "urunler/magnetflow.html":"https://synapseautomate.github.io/urunler.html",
    "urunler/revenueos.html":"https://synapseautomate.github.io/urunler.html",
    "urunler/vela.html":"https://synapseautomate.github.io/urunler.html",
    "demolar/vela-saha-akisi.html":"https://synapseautomate.github.io/urunler.html",
    "urunler/kilory.html":"https://kilory.fit/",
}
CRITICAL_DISCOVERY = {
    "rehberler/otomasyon-izleme-ve-olay-yonetimi.html",
    "rehberler/kurumsal-ai-otomasyonu-satin-alma-kontrol-listesi.html",
    "kanit/e-ticaret-kontrollu-pilot-ornek-raporu.html",
    "en/proof/ecommerce-controlled-pilot-synthetic-report.html",
    "en/ecommerce-process-analysis.html",
    "rehberler/otomasyon-sablonlari-veri-haklari.html",
    "sablonlar/index.html",
    "degisiklikler.html",
    "guven/versiyonlama-inceleme-politikasi.html",
    "rehberler/7-14-gun-deger-gozden-gecirme.html",
    "kanit/teknik-kanit-indeksi.html",
}
IGNORE_EXT = {".map"}

def all_files():
    out=set()
    for p in ROOT.rglob("*"):
        if not p.is_file(): continue
        rel=p.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts): continue
        out.add(rel.as_posix())
    return out

FILES=all_files()
HTML=sorted(p for p in FILES if p.endswith(".html"))

def meta(content, name):
    pats=[
        rf'<meta[^>]+name=["\']{re.escape(name)}["\'][^>]+content=["\']([^"\']+)',
        rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']{re.escape(name)}["\']',
    ]
    for pat in pats:
        m=re.search(pat,content,re.I)
        if m: return m.group(1).strip()
    return ""

def canonical(content):
    pats=[
        r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)',
        r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']',
    ]
    for pat in pats:
        m=re.search(pat,content,re.I)
        if m: return m.group(1).strip()
    return ""

def title(content):
    m=re.search(r'<title[^>]*>(.*?)</title>',content,re.I|re.S)
    return re.sub(r'\s+',' ',m.group(1)).strip() if m else ""

def resolve(source, raw):
    raw=(raw or "").strip()
    if not raw or raw.startswith("#") or raw.startswith("//"): return None
    if re.match(r'^(https?:|mailto:|tel:|javascript:|data:)', raw, re.I): return None
    u=urllib.parse.urlsplit(raw)
    path=urllib.parse.unquote(u.path)
    if not path: return None
    base=Path(source).parent
    target=(Path(path.lstrip("/")) if path.startswith("/") else base/Path(path))
    parts=[]
    for x in target.parts:
        if x in ("","."): continue
        if x=="..":
            if parts: parts.pop()
        else: parts.append(x)
    s="/".join(parts)
    if path.endswith("/"): s=(s.rstrip("/")+"/index.html").lstrip("/")
    elif not Path(s).suffix: s=(s.rstrip("/")+"/index.html").lstrip("/")
    return s or "index.html"

errors=[]
warnings=[]
inbound={p:0 for p in HTML}
data={}
for p in HTML:
    c=(ROOT/p).read_text("utf-8",errors="replace")
    robots=meta(c,"robots").lower()
    idx="noindex" not in robots
    can=canonical(c)
    links=re.findall(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']',c,re.I)
    broken=[]
    internal=[]
    for raw in links:
        q=resolve(p,raw)
        if not q: continue
        if Path(q).suffix.lower() in IGNORE_EXT: continue
        internal.append(q)
        if q not in FILES:
            broken.append((raw,q))
        if q in inbound: inbound[q]+=1
    data[p]={"indexable":idx,"robots":robots,"canonical":can,"title":title(c),"links":internal}
    if broken:
        errors.append({"type":"broken_local_reference","page":p,"items":broken[:20]})
    if idx and p!="404.html":
        if not can:
            errors.append({"type":"missing_canonical","page":p})
        elif not can.startswith("https://"):
            errors.append({"type":"non_absolute_canonical","page":p,"canonical":can})
        if not data[p]["title"]:
            errors.append({"type":"missing_title","page":p})

for p,target in DEPRECATED.items():
    d=data.get(p)
    if not d:
        errors.append({"type":"missing_deprecated_route","page":p}); continue
    if d["indexable"]:
        errors.append({"type":"deprecated_must_noindex","page":p})
    if d["canonical"]!=target:
        errors.append({"type":"deprecated_bad_canonical","page":p,"got":d["canonical"],"want":target})

for p in PRIMARY:
    d=data.get(p)
    if not d:
        errors.append({"type":"missing_primary_page","page":p}); continue
    if not d["indexable"] and p!="404.html":
        errors.append({"type":"primary_noindex","page":p})
    if p!="404.html":
        c=(ROOT/p).read_text("utf-8",errors="replace")
        if "assets/synapse-logo.png" in c:
            warnings.append({"type":"legacy_logo_on_primary","page":p})

# Visible discovery requirement for critical recent assets.
hub_links=set(data.get("kaynaklar.html",{}).get("links",[])) | set(data.get("guven-merkezi.html",{}).get("links",[])) | set(data.get("site-haritasi.html",{}).get("links",[]))
for p in sorted(CRITICAL_DISCOVERY):
    if p not in hub_links:
        errors.append({"type":"critical_asset_not_discoverable","page":p})

# Sitemap integrity.
sitemap=ROOT/"sitemap.xml"
if not sitemap.exists():
    errors.append({"type":"missing_sitemap"})
    sitemap_paths=set()
else:
    try:
        root=ET.parse(sitemap).getroot()
        ns="{http://www.sitemaps.org/schemas/sitemap/0.9}"
        locs=[e.text.strip() for e in root.findall(f".//{ns}loc") if e.text]
        sitemap_paths=set()
        for url in locs:
            if not url.startswith("https://synapseautomate.github.io/"):
                warnings.append({"type":"foreign_sitemap_url","url":url}); continue
            p=url.removeprefix("https://synapseautomate.github.io/")
            p="index.html" if p=="" else (p+"index.html" if p.endswith("/") else p)
            sitemap_paths.add(p)
            if p not in FILES:
                errors.append({"type":"sitemap_missing_file","page":p})
            elif p in data and not data[p]["indexable"]:
                errors.append({"type":"noindex_in_sitemap","page":p})
        for p in DEPRECATED:
            if p in sitemap_paths:
                errors.append({"type":"deprecated_in_sitemap","page":p})
    except Exception as e:
        errors.append({"type":"invalid_sitemap_xml","error":str(e)})
        sitemap_paths=set()

# Report all indexable orphans and sitemap omissions, but don't fail solely for old archive-like pages.
orphans=[p for p,d in data.items() if d["indexable"] and p!="index.html" and inbound.get(p,0)==0]
missing_sitemap=[p for p,d in data.items() if d["indexable"] and p not in sitemap_paths and p not in {"404.html","talep-alindi.html"}]
for p in sorted(orphans):
    warnings.append({"type":"indexable_orphan","page":p})
for p in sorted(missing_sitemap):
    warnings.append({"type":"indexable_missing_sitemap","page":p})

report={
    "html_pages":len(HTML),
    "files":len(FILES),
    "errors":errors,
    "warnings":warnings,
    "orphan_count":len(orphans),
    "missing_sitemap_count":len(missing_sitemap),
}
print(json.dumps(report,ensure_ascii=False,indent=2))
Path("/tmp/site-integrity-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),"utf-8")
if errors:
    print(f"SITE INTEGRITY: FAIL ({len(errors)} errors)",file=sys.stderr)
    sys.exit(1)
print(f"SITE INTEGRITY: PASS | HTML={len(HTML)} | orphans={len(orphans)} | sitemap_missing={len(missing_sitemap)}")
