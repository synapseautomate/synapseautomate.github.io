# Süreç madenciliği / bekleme haritası — açık sentetik kanıt

**SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL.**

Bu klasör tek bir soruyu test eder: Olay kaydındaki bekleme sinyali hangi koşulda gerçek bir süreç hatası *sayılmamalı*? Bu Python stdlib betiği yalnızca bu dosyaları okur. Canlı SYNAPSE ürünü veya müşteri verisiyle çalışan entegrasyon değildir.

## Bağımsız tekrar

Python 3.10+ ile depo kökünden:

```bash
python public-proof/process-mining-v1/analyze_process.py public-proof/process-mining-v1/01_temiz.csv
python public-proof/process-mining-v1/analyze_process.py public-proof/process-mining-v1/02_eksik_kolon.csv
python public-proof/process-mining-v1/analyze_process.py public-proof/process-mining-v1/03_cakisma_ve_bekleme.csv --threshold 30
sha256sum public-proof/process-mining-v1/*.csv public-proof/process-mining-v1/analyze_process.py
```

**27 Ekim 2026 yerel çalışma logu:** Ayrı teslim ZIP'i içindeki `tests/test_process.py` için `python -m unittest discover -s tests -v` sonucu **8/8 PASS**; bu testler bu çalışma sırasında yerel olarak çalıştırıldı. GitHub Actions/CI çalışması, müşteri kabul testi veya canlı üretim kaydı olduğu iddia edilmez.

## Üç senaryo ve beklenen çıktı

| Dosya | Çıktı | Kanıt |
|---|---|---|
| 01_temiz.csv | PASS | 2 sentetik vaka, 9 olay; rapor kural listesi boş |
| 02_eksik_kolon.csv | STOP | R1_SCHEMA; `actor` kolonu eksik |
| 03_cakisma_ve_bekleme.csv | REVIEW | R4_WAIT CSV satır 4, 75 dk WARN; R3_DUPLICATE satır 5 HOLD; R5_APPROVAL satır 8 HOLD; R2_ORDER satır 10 HOLD |

Satırlar CSV'de 1-tabanlı başlık dahil satır sayısıdır. Eşik 30 dakika **öğretici varsayım**, doğrulanmış müşteri SLA'sı değildir. Yetki/rol tanımı, tatil/mesai, veri kaynağı, zaman dilimi, mükerrer olayın gerçek nedeni ve onay zorunluluğu insan tarafından incelenmelidir.

## Yerel kanıt dosyalarının SHA-256 (27.10.2026)

```
156a9f2297b66cdb1d1ca4c23d2fa87b19e609161d9fd2cd875f42efe42fb170  analyze_process.py
cebcb48449cefa7d6bd9988238e21b6cc1557667c82d87df689cba7dd5fba3a7  01_temiz.csv
e90f1cf4d78eb126893952b0c1c75a2a24d4c68953765497ee628b96b6b163c5  02_eksik_kolon.csv
a72a02331cfd7e710d655ac365548d3b9e029d2871f82ac9c40c604946276655  03_cakisma_ve_bekleme.csv
```

Bu hash değerleri yerel çalıştırmadan alınmıştır. Repo dosyaları GitHub'dan indirilip `sha256sum` ile ayrıca eşitlenmeden **repo SHA doğrulandı** denemez. `SYNAPSE_G18_SUREC_MADENCILIGI` ZIP paketinde yerel stdout, JSON, beş kanıt kartı, test günlüğü ve iki kısa sentetik anlatım filmi bulunur.

Kapsam dışı: gerçek müşteri, otomatik onay, veri silme, ERP/CRM entegrasyonu, üretim güvenilirliği iddiası, satış veya ROI garantisi.
