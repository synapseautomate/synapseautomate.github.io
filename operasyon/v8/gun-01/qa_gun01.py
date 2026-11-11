#!/usr/bin/env python3
"""Gün 01 arşiv yapısal kontrolü; ürün, canlı URL veya satış testi değildir."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parent
required=["Operasyon-durumu.md","Karar-gunlugu.md","blokajlar.md","Yetki-ve-onay-listesi.md","Huni-ve-barindirma-uygunluk-matrisi.md","QA-iki-tur.md","SYNAPSE_V8_GUN_01_DEVIR.md","metrikler.csv"]
missing=[x for x in required if not (root/x).is_file()]
assert not missing, f"Eksik: {missing}"
with (root/"metrikler.csv").open(encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))
assert rows and all(k in rows[0] for k in ("tarih","kanal","olcu","tanim","deger","birim","kaynak","kanit_guveni"))
print("QA TUR 1: PASS — Gün 01 dosyaları ve metrik başlıkları")
texts="\n".join((root/x).read_text(encoding="utf-8") for x in required if x.endswith(".md"))
assert all(k in texts for k in ("BİLİNMİYOR","P0","TEST EDİLEMEDİ"))
print("QA TUR 2: PASS — belirsizlik ve P0 kayıtları var; ürün/satış/yayın testi değildir")
