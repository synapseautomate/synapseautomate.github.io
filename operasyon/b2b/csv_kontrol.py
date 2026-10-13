#!/usr/bin/env python3
"""Sipariş/stok CSV ön inceleme prototipi. Veri yalnız yerel diskte işlenir."""
import argparse
import collections
import csv
import json
from pathlib import Path

REQUIRED = ("siparis_kodu", "sku", "siparis_adedi", "stok_adedi", "sevk_durumu")
OUTPUT = ("satir", "siparis_kodu", "sku", "kural", "aciklama")

def audit(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        missing = set(REQUIRED) - set(fields)
        if missing:
            raise ValueError("Eksik kolonlar: " + ", ".join(sorted(missing)))
        if len(fields) != len(set(fields)):
            raise ValueError("Tekrarlanan kolon başlığı")
        rows = list(reader)
    for line, row in enumerate(rows, start=2):
        if None in row or any(row.get(k) is None for k in REQUIRED):
            raise ValueError(f"Bozuk CSV satırı: {line}")
    counts = collections.Counter(
        (row["siparis_kodu"].strip(), row["sku"].strip()) for row in rows
        if row["siparis_kodu"].strip() and row["sku"].strip()
    )
    issues = []
    for line, row in enumerate(rows, start=2):
        order = row["siparis_kodu"].strip()
        sku = row["sku"].strip()
        def add(rule, message):
            issues.append({"satir": line, "siparis_kodu": order, "sku": sku,
                           "kural": rule, "aciklama": message})
        if not order:
            add("R06", "Sipariş kodu boş")
        if not sku:
            add("R04", "SKU boş")
        if order and sku and counts[(order, sku)] > 1:
            add("R03", "Sipariş+SKU birden fazla satırda")
        try:
            qty = int(row["siparis_adedi"])
            stock = int(row["stok_adedi"])
        except ValueError:
            add("R00", "Adet veya stok tamsayı değil")
            continue
        if qty < 0:
            add("R07", "Sipariş adedi negatif")
        if qty > stock:
            add("R01", "Sipariş adedi stoktan büyük")
        if stock < 0:
            add("R02", "Negatif stok")
        if row["sevk_durumu"].strip() == "sevk_edildi" and stock < 0:
            add("R05", "Sevk edildi ve stok negatif: manuel inceleme")
    return rows, issues

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    parser.add_argument("--out", default="bulgular.csv")
    args = parser.parse_args()
    source = Path(args.csv_file).resolve()
    destination = Path(args.out).resolve()
    if source == destination:
        parser.error("Çıktı dosyası girdi dosyasıyla aynı olamaz")
    try:
        rows, issues = audit(source)
        with open(destination, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=OUTPUT)
            writer.writeheader()
            writer.writerows(issues)
    except (ValueError, OSError, csv.Error) as exc:
        parser.error(str(exc))
    print(json.dumps({"satir_sayisi": len(rows), "bulgu_sayisi": len(issues),
                      "bulgular": str(destination)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
