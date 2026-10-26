# SYNAPSE V8 Gün 17 — QA A: Kaynak, teknik kanıt, olumsuz testler

**Çalışma:** 26 Ekim 2026 · **Plan:** 30 Ekim 2026, Gün 17/30 (numara değiştirilmedi). **Main:** `6de1c4ad10feef1fef37e93d2731dad5e7886574`. **PR:** https://github.com/synapseautomate/synapseautomate.github.io/pull/46 (DRAFT).

## Gerçek yapılan tarama
- GitHub recursive main tree: **428 dosya ve 150 HTML** (önceki 144/389 sayıları artık geçerli değil).
- **150/150 HTML kaynak dosyası** Connector fetch ile açıldı; title, H1 sayısı/metni, canonical, robots, CTA düğme metni örnekleri ve iddia dilinin regex ön elemesi tabloya yazıldı: `150-SAYFA-SEO-IDDA-CTA-ENVANTERI.csv`.
- Bu metaveri taraması, **tüm sayfalarda tam görsel, uluslararası hukuki veya çalışan form testi** değildir.
- Sürüm registry `veri/public-content-version-registry-v1.json`: **27 varlık**, kayıt tarihi `2026-10-13`; 26 kayıt HTML yollarından biriyle eşleşti, tarihleri değiştirilmedi. `scripts/check-public-content-freshness.py` içindeki due/boolean kontrollerinin JS eşdeğeri PASS: 27 current kayıt üzerinden geçmiş due 0, yanlış tipli uzman incelemesi bayrağı 0. **Python betiğinin kendisi çalıştırılmadı.**
- `sitemap.xml`: 131 `<loc>` girdisi ve mevcut `/rehberler/ai-surec-denetimi.html` kaydı; 150 HTML olması tek başına sitemap kusuru kanıtı değildir.
- Statik HTML üzerinden `hizmetler.html` hizmet 09 için eksik rehber bağlantısı saptandı ve draft'a **tek bağlantı** eklendi.
- Rehberde self canonical, tek H1 ve indeks meta korunarak doğruluk/güvenlik/maliyet bölümü eklendi; yeni URL, form, fiyat, ödeme, JS veya sitemap müdahalesi yok.

## Gerçek regresyon sonuçları
16 kontrol **16/16 PASS**; GitHub PR branch kaynak dosyalarına karşı JS assert ile doğrulandı:
(1) rehber tek H1, (2) tek canonical, (3) doğru self canonical, (4) hizmet→rehber, (5) rehber→denetim çözümü, (6) marka adında eğreti slash yok, (7) sentetik uyarı mevcut, (8) hizmet H1 tek, (9) yeni form yok, (10) index robots değişmedi, (11) sonuç yüzdesi uydurulmadı, (12) iç QA/PR notu müşteri metninde yok, (13) altı vaka mevcut, (14) A02 HOLD, (15) A03 STOP, (16) A05 HOLD.

**Sentetik vakalar** gerçek AI inference/müşteri sonucu değildir: A01 PASS, A02/A05/A06 HOLD, A03/A04 STOP. Güvenlik sertifikası veya maliyet tasarrufu iddiasına dönüştürme.

## Kaynaktan çıkan kusur adayları
- **18 noindex HTML:** eski ürün köprüleri, doğrulama ve yardımcı dosyalar aynı sepete alınmadı; noindex içeren kaynakların otomatik indekslenmesi istenmez.
- **H1 yok: 5 HTML**; içlerinden 4'ü noindex ve biri resmî Google doğrulama dosyası; bu sayıyı 5 adet müşteri URL hatası olarak sunma.
- **Canonical meta yok: 3 dosya:** 404.html, `google9226ec2349a9441e.html`, `talep-alindi.html`; özel sayfalar, kesin arama sorunu hükmü YOK.
- **Robots meta belirtilmeyen 4 dosya:** `cozumler/icerik-onay-zinciri.html`, `cozumler/siparis-stok-csv-kontrolu.html`, `google9226ec2349a9441e.html`, `rehberler/kaynak-gosteren-rag-bilgi-tabani-rehberi.html`. Varsayılan indeks davranışı ayrıca kontrol edilmeli.
- **8 ortak canonical grubu:** çoğunlukla `noindex` köprüleri, varsayılan olarak çift indeks sorunu değildir.
- **112 metin parçası iddia dili regex eşleşmesi:** 'müşteri' veya 'garanti değildir' gibi olumsuz/bağlamlı örnekleri de içeriyor; **kanıtsız iddia sayısı BİLİNMİYOR**, 112 kusur ilan edilmedi.
- `SEO-KANONIK-IDDA-KUSUR-DEFTERI.csv` içinde 132 kayıt: ön eleme/inceleme adayları, **kesinleşmiş 132 SEO arızası değil**.

## Test edilmemişler
Gerçek Google kanonik seçimi, HTTP 200/404, 150 URL'nin istemci tarafı tüm linkleri, FormSubmit server cevabı, Safari/Firefox/gerçek cihaz, GSC/GA4, canlı model ve 2026-10-30 saha verileri **TEST EDİLEMEDİ / BİLİNMİYOR**. Bunlar PASS olarak gösterilemez.

Resmî metod kaynakları:
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/appearance/core-web-vitals
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
