# SYNAPSE V8 Gün 01 — sıfır bağlamlı tam devir
**Tarih:** 14.10.2026, UTC+3, Gün 01/30, sapma 0. **İzleyen plan tarihi:** 15.10.2026, Gün 02/30; Gün 02 İŞİ BUGÜN YAPILMADI.

**Tek karar:** Yasal satıcı/fatura yetkisi ve güvenli tahsilat zinciri hesap kanıtıyla kapanmadan **satış hazır HAYIR**. Ödeme kapısı **BİLİNMİYOR**. Ürün test kabul HAYIR, kamu yayın onayı YOK.

**GitHub repo ve SHA:** https://github.com/synapseautomate/synapseautomate.github.io — main baz `bc79409c8f672884a00dcdb89b0b6119cac42f6c` (13.10.2026 14:08:40 TSİ). V6 #10/#11, V7 #12, V8 #13 hepsi açık taslak, merge edilmedi. V6 Gün 01–02 devirleri ve V7/V8 QA dosyaları kendi draft branch'lerinde okunabildi; V8 operasyon klasörü main'de bulunmadı.
**Yeni çalışma dalı:** `audit/v8-gun-01-satis-kapilari-20261014`; yalnız draft PR; `main` MERGE EDİLMEDİ. Canlı URL https://synapseautomate.github.io/ ve LinkedIn https://www.linkedin.com/company/synapseautomate/ (public okuma; panel yok).

**Dosyalar:** `Operasyon-durumu.md`, `metrikler.csv`, `Karar-gunlugu.md`, `blokajlar.md`, `Huni-ve-barindirma-uygunluk-matrisi.md`, `Yetki-ve-onay-listesi.md`, `QA-iki-tur.md`, bu devir ve `SYNAPSE_GUN_01_DEVIR.md` ad uyumluluk kopyası.

**Metrik özeti:** Önceki 27 gün 0 ücretli satış kullanıcı beyanı. Yeni V8 gösterim, nitelikli ziyaret, demo, gönüllü talep, izinli teklif, fonlanan sipariş, tahsilat, iade, net gelir **BİLİNMİYOR**. Açık P0 **6** (sahipler blokajlar.md), P1 **3**. 990/4.900/24.900 TL yalnız TEST. Mağaza API/otomatik stok/ROI garantisi yok.

**Test kanıtı:** web aracı ana sayfa metni okudu. `curl -IL --max-time 12 https://synapseautomate.github.io/` → DNS 000, gerçek HTTP ve 320/375/390/768/1024/1440 render, Lighthouse, form, analytics, checkout **TEST EDİLEMEDİ**. 404 doğrulanmadı; kırık link listesi sonuca bağlanmadı. Yerel dosya paketinde iki ayrı QA kontrolü `python qa_gun01.py` PASS (yalnız belge), `QA-SONUC.txt` kanıtı var. Resmî kaynak tarih/sahipleri `Operasyon-durumu.md` ve huni/hosting matrisinde.

**Yetki:** 0 TL peşin, Shopier ve soğuk temas yok; main merge, canlı web, LinkedIn Services/post, YouTube/Instagram, Upwork katalog incelemesi, MoR ödeme, gerçek müşteri mesajı ve hesap işlemi yapılmadı. Hepsi ayrı açık eylem onayı bekliyor; kimlik/IBAN/vergi sadece hesap sahibinin panelinde.

**Tek sonraki adım (yalnız kullanıcı Gün 02 emri verdiğinde):** Önce bu devir, SHA, açık PR'lar ve yetkili panel erişimini yeniden denetle; V8 PDF'nin yalnız sonraki güne özgü emrini uygula. Arka planda çalışma yok.

Kaynaklar (14.10.2026 erişimi):
- GitHub: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits (güncelleme tarihi gösterilmedi)
- Cloudflare: https://developers.cloudflare.com/pages/platform/limits/ (05.09.2026); https://developers.cloudflare.com/pages/functions/pricing/ (08.09.2026)
- GİB: https://istanbul.gib.gov.tr/mevzuat/kanun/433 (GVK 20/B, kişi/faaliyet teyidi gerekir)
- Ticaret Bakanlığı: https://tuketici.ticaret.gov.tr/yayinlar/tuketici-bilgi-rehberi/mesafeli-sozlesmeler-hakkinda-bilgilendirme (17.08.2026); https://etbis.ticaret.gov.tr/tr/SSS
- KVKK: https://www.kvkk.gov.tr/Icerik/7353/Cerez-Uygulamalari-Hakkinda-Rehber (Temmuz 2025)
- LinkedIn: https://www.linkedin.com/help/linkedin/answer/a7436041 (Company Services koşullu ücretsiz)
