from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / "veri/offer-ladder.json").read_text(encoding="utf-8"))

analysis = ROOT / "surec-analizi.html"
pricing = ROOT / "rehberler/ai-otomasyon-fiyatlari.html"
legal = ROOT / "sektorler/hukuk.html"

pages = {
    "surec-analizi.html": analysis,
    "rehberler/ai-otomasyon-fiyatlari.html": pricing,
    "sektorler/hukuk.html": legal,
}

errors = []
texts = {}
for name, path in pages.items():
    if not path.exists():
        errors.append(f"missing page: {name}")
        continue
    text = path.read_text(encoding="utf-8")
    texts[name] = text
    if '<meta name="viewport"' not in text:
        errors.append(f"missing viewport: {name}")
    if "overflow-x:hidden" not in text:
        errors.append(f"missing horizontal overflow guard: {name}")

for offer in config["offers"]:
    tr = f'{offer["price_try"]:,}'.replace(",", ".") + " TL"
    usd = f'${offer["price_usd"]}'
    for name in ["surec-analizi.html", "rehberler/ai-otomasyon-fiyatlari.html"]:
        text = texts.get(name, "")
        if tr not in text or usd not in text:
            errors.append(f"price mismatch for {offer['id']} on {name}: expected {tr} / {usd}")

# Legal page must show the analysis entry price and defer broader pricing to the guide.
if "4.900 TL" not in texts.get("sektorler/hukuk.html", "") or "$149" not in texts.get("sektorler/hukuk.html", ""):
    errors.append("legal page missing Process Analysis starting price")
if "ai-otomasyon-fiyatlari.html" not in texts.get("sektorler/hukuk.html", ""):
    errors.append("legal page missing pricing guide link")

forbidden = [
    "Day 6",
    "DAY 6",
    "Gün 6",
    "GÜN 6",
    "public scoreboard",
    "Public scoreboard",
    "PUBLIC REGRESSION",
    "Public regression",
]
for name, text in texts.items():
    for token in forbidden:
        if token in text:
            errors.append(f"internal/public workflow label found on {name}: {token}")

# High-impact boundaries must remain explicit.
for required in ["hukuki tavsiye", "nihai", "insan"]:
    if required.lower() not in texts.get("sektorler/hukuk.html", "").lower():
        errors.append(f"legal boundary missing term: {required}")

if errors:
    print("QA FAIL")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("QA PASS")
print("- canonical offer ladder matches public pricing surfaces")
print("- viewport and horizontal overflow guards present")
print("- forbidden internal workflow labels absent")
print("- legal human-approval boundary present")
