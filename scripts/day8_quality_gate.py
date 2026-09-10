#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    "sektorler/e-ticaret.html",
    "rehberler/e-ticaret-ai-otomasyon-satin-alma-rehberi.html",
    "sektorler/uretim-lojistik.html",
    "rehberler/uretim-lojistik-ai-otomasyon-satin-alma-rehberi.html",
    "sektorler/finans.html",
    "rehberler/finans-ai-otomasyon-satin-alma-rehberi.html",
]
NEW_PUBLIC = [
    "rehberler/e-ticaret-ai-otomasyon-satin-alma-rehberi.html",
    "rehberler/uretim-lojistik-ai-otomasyon-satin-alma-rehberi.html",
    "rehberler/finans-ai-otomasyon-satin-alma-rehberi.html",
    "kanit/50-vaka-kaynak-metodolojisi.html",
]
FORBIDDEN_PUBLIC = [
    "day 8",
    "gün 8",
    "public benchmark",
    "v1.0.0",
    "lorem ipsum",
    "synapseautomate.com",
]


def fail(msg):
    print("FAIL:", msg)
    return False


def extract(pattern, text):
    m = re.search(pattern, text, re.I | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def main():
    ok = True
    titles = set()
    h1s = set()

    for rel in PAGES:
        path = ROOT / rel
        if not path.exists():
            ok = fail(f"missing canonical page: {rel}") and ok
            continue
        text = path.read_text(encoding="utf-8")
        low = text.lower()
        canonical = f'https://synapseautomate.github.io/{rel}'
        if f'<link rel="canonical" href="{canonical}"' not in text and f'<link href="{canonical}" rel="canonical"' not in text:
            ok = fail(f"canonical mismatch: {rel}") and ok
        if 'type="application/ld+json"' not in text:
            ok = fail(f"schema missing: {rel}") and ok
        if '<meta name="description"' not in text:
            ok = fail(f"description missing: {rel}") and ok
        title = extract(r"<title>(.*?)</title>", text)
        h1 = extract(r"<h1[^>]*>(.*?)</h1>", text)
        if not title or title in titles:
            ok = fail(f"missing/duplicate title: {rel}") and ok
        titles.add(title)
        if not h1 or h1 in h1s:
            ok = fail(f"missing/duplicate h1: {rel}") and ok
        h1s.add(h1)
        if len(re.sub(r"<[^>]+>", " ", text)) < 1200:
            ok = fail(f"thin content: {rel}") and ok

    for rel in NEW_PUBLIC:
        path = ROOT / rel
        if not path.exists():
            ok = fail(f"missing public asset: {rel}") and ok
            continue
        text = path.read_text(encoding="utf-8")
        low = text.lower()
        for marker in FORBIDDEN_PUBLIC:
            if marker in low:
                ok = fail(f"public/internal marker '{marker}' in {rel}") and ok
        if rel.startswith("rehberler/") and "../araclar/surecini-20-dakikada-haritala.html" not in text:
            ok = fail(f"tool CTA missing: {rel}") and ok

    methodology = ROOT / "kanit/50-vaka-kaynak-metodolojisi.html"
    if methodology.exists():
        text = methodology.read_text(encoding="utf-8")
        for required in ["50 SENTETİK", "Bilinmiyor", "customer_data", "provenance-50-v1"]:
            if required.lower() not in text.lower():
                ok = fail(f"methodology requirement missing: {required}") and ok

    result = subprocess.run(
        [sys.executable, str(ROOT / "public-proof/provenance-50-v1/validate.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    print(result.stdout, end="")
    if result.returncode != 0:
        print(result.stderr, end="")
        ok = fail("50-case provenance validator") and ok

    if ok:
        print("PASS: Day 8 canonical/provenance quality gate")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
