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
    "sektorler/finans-bankacilik.html",
    "rehberler/finans-ai-otomasyon-satin-alma-rehberi.html",
]
NEW_PUBLIC = [
    "rehberler/e-ticaret-ai-otomasyon-satin-alma-rehberi.html",
    "rehberler/uretim-lojistik-ai-otomasyon-satin-alma-rehberi.html",
    "rehberler/finans-ai-otomasyon-satin-alma-rehberi.html",
    "kanit/50-vaka-kaynak-metodolojisi.html",
    "kaynaklar.html",
]
DISCOVERABLE = [
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


def canonical_href(text):
    return (
        extract(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', text)
        or extract(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', text)
    )


def robots_value(text):
    return (
        extract(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)', text)
        or extract(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']robots["\']', text)
    ).lower()


def local_path_from_canonical(url):
    prefix = "https://synapseautomate.github.io/"
    if not url.startswith(prefix):
        return None
    rel = url[len(prefix):]
    return rel or "index.html"


def main():
    ok = True
    titles = set()
    h1s = set()
    sitemap = ROOT / "sitemap.xml"
    sitemap_text = sitemap.read_text(encoding="utf-8") if sitemap.exists() else ""

    for rel in PAGES:
        path = ROOT / rel
        if not path.exists():
            ok = fail(f"missing canonical page: {rel}") and ok
            continue
        text = path.read_text(encoding="utf-8")
        expected_canonical = f"https://synapseautomate.github.io/{rel}"
        actual_canonical = canonical_href(text)
        robots = robots_value(text)
        is_deprecated_bridge = "noindex" in robots and actual_canonical and actual_canonical != expected_canonical

        if is_deprecated_bridge:
            target_rel = local_path_from_canonical(actual_canonical)
            if not target_rel:
                ok = fail(f"deprecated bridge canonical must stay on canonical site: {rel}") and ok
            elif not (ROOT / target_rel).exists():
                ok = fail(f"deprecated bridge target missing: {rel} -> {target_rel}") and ok
            if expected_canonical in sitemap_text:
                ok = fail(f"deprecated bridge must not be in sitemap: {rel}") and ok
            if actual_canonical not in sitemap_text:
                ok = fail(f"deprecated bridge canonical target missing from sitemap: {rel}") and ok
            if "follow" not in robots:
                ok = fail(f"deprecated bridge must remain followable: {rel}") and ok
        else:
            if actual_canonical != expected_canonical:
                ok = fail(f"canonical mismatch: {rel}") and ok
            if 'type="application/ld+json"' not in text:
                ok = fail(f"schema missing: {rel}") and ok
            if len(re.sub(r"<[^>]+>", " ", text)) < 1200:
                ok = fail(f"thin content: {rel}") and ok

        if '<meta name="description"' not in text and 'name="description"' not in text:
            ok = fail(f"description missing: {rel}") and ok
        title = extract(r"<title>(.*?)</title>", text)
        h1 = extract(r"<h1[^>]*>(.*?)</h1>", text)
        if not title or title in titles:
            ok = fail(f"missing/duplicate title: {rel}") and ok
        titles.add(title)
        if not h1 or h1 in h1s:
            ok = fail(f"missing/duplicate h1: {rel}") and ok
        h1s.add(h1)

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

    hub = ROOT / "kaynaklar.html"
    if not hub.exists():
        ok = fail("resources hub missing") and ok
    else:
        hub_text = hub.read_text(encoding="utf-8")
        for rel in DISCOVERABLE:
            if rel not in hub_text:
                ok = fail(f"not discoverable from resources hub: {rel}") and ok

    if not sitemap.exists():
        ok = fail("sitemap missing") and ok
    else:
        sitemap_text = sitemap.read_text(encoding="utf-8")
        for rel in DISCOVERABLE:
            url = f"https://synapseautomate.github.io/{rel}"
            if url not in sitemap_text:
                ok = fail(f"missing sitemap URL: {rel}") and ok

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
        print("PASS: Day 8 canonical/provenance/discoverability quality gate")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
