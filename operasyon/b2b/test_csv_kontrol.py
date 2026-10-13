"""CSV prototipi için standart kütüphane unittest senaryoları."""
import csv
import tempfile
import unittest
from pathlib import Path
from csv_kontrol import audit

FIELDS=["siparis_kodu","sku","siparis_adedi","stok_adedi","sevk_durumu"]
class CsvKontrolTest(unittest.TestCase):
    def check(self,rows):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"input.csv"
            with p.open("w",encoding="utf-8",newline="") as f:
                w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
            return audit(p)
    def row(self,**overrides):
        r=dict(zip(FIELDS,["A","SKU", "2","5","bekliyor"]))
        r.update(overrides);return r
    def test_clean(self):
        rows,issues=self.check([self.row()])
        self.assertEqual(len(rows),1);self.assertEqual(issues,[])
    def test_shortage(self):
        _,issues=self.check([self.row(siparis_adedi="7",stok_adedi="3")])
        self.assertEqual([i["kural"] for i in issues],["R01"])
    def test_negative_shipped(self):
        _,issues=self.check([self.row(stok_adedi="-2",sevk_durumu="sevk_edildi")])
        self.assertEqual({i["kural"] for i in issues},{"R01","R02","R05"})
    def test_duplicate(self):
        _,issues=self.check([self.row(),self.row()])
        self.assertEqual([i["kural"] for i in issues],["R03","R03"])
    def test_missing_sku(self):
        _,issues=self.check([self.row(sku="")])
        self.assertEqual([i["kural"] for i in issues],["R04"])
    def test_invalid_quantity(self):
        _,issues=self.check([self.row(siparis_adedi="abc")])
        self.assertEqual([i["kural"] for i in issues],["R00"])
    def test_missing_header(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"bad.csv";p.write_text("sku,stok_adedi\nSKU,5\n",encoding="utf-8")
            with self.assertRaises(ValueError):audit(p)
if __name__=="__main__":unittest.main()
