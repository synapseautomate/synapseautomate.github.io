#!/usr/bin/env python3
"""Fail-closed static release checks; no external dependencies."""
from __future__ import annotations
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://synapseautomate.github.io/"
KEY = "b92e13eb5417ef94e6aa9a04c7d7333a"
CORE = (
    "index.html",
    "kaynaklar.html",
    "surec-analizi.html",
    "rehberler/ai-otomasyon-fiyatlari.html",
    "sektorler/finans-bankacilik.html",
    "cozumler/roofing-ev-hizmetleri.html",
    "guven-merkezi.html",
    "talep-alindi.html",
    "kanit/ev-hizmetleri-talep-yonlendirme-ornek-akis.html",
    "teklif/ev-hizmetleri-surec-analizi.html",
)
class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = []
        self.links = []
        self.jsonld = []
        self._ld = False
        self._parts = []
        self.has_title = False
    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag == "meta":
            self.meta.append(attr)
        if tag == "link":
            self.links.append(attr)
        if tag == "title":
            self.has_title = True
        if tag == "script" and attr.get("type","").lower() == "application/ld+json":
            self._ld = True
            self._parts = []
    def handle_data(self, data):
        if self._ld:
            self._parts.append(data)
    def handle_endtag(self, tag):
        if tag == "script" and self._ld:
            self.jsonld.append("".join(self._parts))
            self._ld = False

def check(root: Path, artifact: bool) -> list[str]:
    issues = []
    def bad(message: str):
        issues.append(message)
    keyfile = root / (KEY + ".txt")
    if not keyfile.is_file() or keyfile.read_text("utf-8").strip() != KEY:
        bad("IndexNow ownership file absent/invalid in release artifact")
    urls = set()
    sitemap = root / "sitemap.xml"
    if not sitemap.is_file():
        bad("missing sitemap.xml")
    else:
        try:
            xroot = ET.parse(sitemap).getroot()
            found = [n.text.strip() for n in xroot.iter() if n.tag.endswith("}loc") and n.text]
            for url in found:
                if not url.startswith(BASE):
                    bad("off-domain sitemap location: " + url[:120])
                if url in urls:
                    bad("duplicate sitemap location: " + url[:120])
                urls.add(url)
        except (ET.ParseError, ValueError) as e:
            bad("invalid sitemap: " + str(e))
    for path in CORE:
        f = root / path
        if not f.is_file():
            bad("missing public page: " + path)
            continue
        raw = f.read_text("utf-8")
        if "\ufffd" in raw or any(t in raw for t in ("Ã¼","Ã§","Ä±","Ã–","Ãœ")):
            bad("broken Turkish Unicode encoding: " + path)
        p = Scan()
        try:
            p.feed(raw)
        except Exception as e:
            bad("invalid HTML parsing: " + path + ": " + str(e))
            continue
        if not p.has_title:
            bad("missing HTML title: " + path)
        if not any(m.get("name","").lower() == "viewport" and "width=device-width" in m.get("content","") for m in p.meta):
            bad("missing mobile viewport: " + path)
        robots = " ".join(m.get("content","").lower() for m in p.meta if m.get("name","").lower() == "robots")
        can = [x.get("href","") for x in p.links if x.get("rel","").lower() == "canonical"]
        if path == "talep-alindi.html":
            if "noindex" not in robots or BASE + path in urls:
                bad("thank-you route must be noindex and absent from sitemap")
        elif "noindex" not in robots:
            expected = BASE if path == "index.html" else BASE + path
            if can != [expected]:
                bad("canonical mismatch: " + path + " got " + str(can))
            if expected not in urls:
                bad("indexable core page omitted from sitemap: " + path)
        for ld in p.jsonld:
            try:
                json.loads(ld)
            except json.JSONDecodeError as e:
                bad("invalid JSON-LD on " + path + ": " + str(e))
    if artifact:
        forbidden_suffixes = {".zip",".py",".pyc",".sqlite",".db",".sha256"}
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            r = p.relative_to(root)
            if any(x in {".git",".github","__pycache__","D01","D02","D03"} for x in r.parts) or p.suffix.lower() in forbidden_suffixes or p.name.startswith(".env"):
                bad("internal file in public artifact: " + str(r))
                if len(issues) > 100:
                    break
    return issues

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact", default=None, help="staged Pages artifact directory")
    args = ap.parse_args()
    root = Path(args.artifact).resolve() if args.artifact else ROOT
    issues = check(root, bool(args.artifact))
    print(json.dumps({"gate":"Day28 Release Integrity","mode":"artifact" if args.artifact else "source","status":"PASS" if not issues else "FAIL","issues":issues},ensure_ascii=False,indent=2))
    return 1 if issues else 0

if __name__ == "__main__":
    sys.exit(main())
