#!/usr/bin/env python3
"""Sentetik veya izinli CSV dosyasında operasyon kontrolü. Yalnız Python standart kütüphanesi."""
import argparse, csv, collections, json
from pathlib import Path
REQUIRED=("siparis_kodu","sku","siparis_adedi","stok_adedi","sevk_durumu")
def audit(path):
    with open(path,encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        missing=set(REQUIRED)-set(reader.fieldnames or [])
        if missing: raise ValueError("Eksik kolonlar: "+", ".join(sorted(missing)))
        rows=list(reader)
    counts=collections.Counter((r["siparis_kodu"].strip(),r["sku"].strip()) for r in rows)
    issues=[]
    for index,row in enumerate(rows,start=2):
        order=row["siparis_kodu"].strip(); sku=row["sku"].strip()
        def add(rule,detail): issues.append({"satir":index,"siparis_kodu":order,"sku":sku,"kural":rule,"aciklama":detail})
        if not sku: add("R04","SKU boş")
        if counts[(order,sku)]>1: add("R03","Sipariş+SKU birden fazla satırda")
        try:
            qty=int(row["siparis_adedi"]); stock=int(row["stok_adedi"])
        except ValueError:
            add("R00","Adet veya stok tamsayı değil"); continue
        if qty>stock: add("R01","Sipariş adedi stoktan büyük")
        if stock<0: add("R02","Negatif stok")
        if row["sevk_durumu"].strip()=="sevk_edildi" and stock<0: add("R05","Sevk edildi ve stok negatif: manuel inceleme")
    return rows,issues
def main():
    p=argparse.ArgumentParser();p.add_argument("csv_file");p.add_argument("--out",default="bulgular.csv");args=p.parse_args()
    rows,issues=audit(args.csv_file)
    with open(args.out,"w",encoding="utf-8-sig",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=["satir","siparis_kodu","sku","kural","aciklama"]);writer.writeheader();writer.writerows(issues)
    print(json.dumps({"satir_sayisi":len(rows),"bulgu_sayisi":len(issues),"bulgular":args.out},ensure_ascii=False))
if __name__=="__main__":main()
