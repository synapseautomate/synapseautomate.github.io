# SYNAPSE_GUN_02_DEVIR — 14.10.2026
**Durum:** GÜN 02 / MÜŞTERİ PROBLEMİ ve ÜRÜN KARARI — **CLOSED (iç araştırma)**. SATIŞ/YAYIN **NOT READY**.
**Operatör:** AI · **Sahip:** SYNAPSE Automate · **Ertesi gün:** Gün 03 / 15.10.2026.
**PDF:** V6 MAX 30 Gün; Gün 02 Operasyon (s.11); Gün 03 Operasyon (s.12).

## 1. Kalıcı dosyalar ve bağlantılar
- Site: https://synapseautomate.github.io/ — canlı URL'yi web tarayıcı aracı okumadı; repo kaynak kodu okundu. Ürün veya ödeme yayımlanmadı.
- Repo: https://github.com/synapseautomate/synapseautomate.github.io
- **Gün 01 devir:** https://github.com/synapseautomate/synapseautomate.github.io/blob/audit/gun-01-v6-evidence-20261013/operasyon/gun-01/SYNAPSE_GUN_01_DEVIR.md
- **Gün 01 PR #10:** https://github.com/synapseautomate/synapseautomate.github.io/pull/10 — draft ve main'e merge edilmedi.
- **Gün 02 PR #11:** https://github.com/synapseautomate/synapseautomate.github.io/pull/11 — draft, `main` bazlı ayrı branch `audit/gun-02-v6-icp-fiyat-20261014`. Main'e merge edilmeyecek; kullanıcı açık onay vermedi.
- Gün 02 belgeleri (`operasyon/gun-02/`):
  1. `01-icp-problem-brifi.md`
  2. `02-alici-niyetli-arama-ifadeleri.md`
  3. `03-bes-alternatif-fiyat-kaynaklari.md`
  4. `04-urun-hipotezi-karsilastirma.md`
  5. `05-fiyat-ve-kapsam-varsayimi.md`
  6. `06-metrikler.csv`
  7. `07-onay-kapilari-ve-kusurlar.md`
  8. `08-kalite-ve-kanıt-raporu.md`
  9. `GUN_02_A_H_RAPOR.md`
  10. `SYNAPSE_GUN_02_DEVIR.md`.
- Ek teslim: `SYNAPSE_GUN_02_ICP_PROBLEM_BRIFI.pdf` (tek sayfalık yerel PDF; konuşma eki; GitHub'da PDF dosyası yok).

## 2. Gün 02 net kararları
**H1 — TEK BİRİNCİL HİPOTEZ:** Küçük e-ticaret işletmeleri için sipariş/stok CSV uyuşmazlık kontrol paketi.
**Tek cümle vaat:** “Sipariş ve stok CSV dosyalarındaki stok açığı, negatif stok, boş SKU ve yinelenen kayıt gibi tanımlı tutarsızlıkları yerel olarak işaretleyen kontrol paketi.”
**Park edilenler:** H2 haftalık Excel/Sheets rapor otomasyonu; H3 genel sipariş hata kontrolü. Her ikisine de yeni ürün geliştirme başlatılmadı.
**ICP:** CSV çıkarabilen küçük e-ticaret işletmesi; operasyondaki günlük kullanıcı ve sahibi/operasyon yöneticisi karar verici.
**Üç alıcı sorusu:** (i) tekrar eden sorun? (ii) erişilebilir veri/çıktı? (iii) niçin ödemeye değecek? Dosyada yanıtlar yalnız hipotezdir.
**Ticari mimari:** PDF önce indirilebilir araç, talep halinde sınırlı kurulum, uygunluk sonrası analiz/pilot ister. Hesap sahibinin önceki **kurumsal B2B satış tercihi** korunur; model önceliği çatışması **açık karar konusu**, sessizce değiştirilmez.
**Kapsam dışı:** ERP/mağaza/API entegrasyonu, otomatik stok/fiyat müdahalesi, gerçek ROI iddiası, PII yükleme zorunluluğu.
**Deneysel fiyatlar:** 990 TL / indirilebilir P1; 4.900 TL / P2 kurulum; 24.900 TL / P3 pilot. **Üçü de TEST FİYATI.** Vergi/KDV/destek/teslim kapsamı ve satış uygunluğu henüz belirlenmedi.

## 3. Pazar kanıtları ve gerçek metrikler
- 12 aday alıcı araması Q01–Q12. Arama hacmi, Search Console sırası, tıklama ve dönüşüm verisi **yok**.
- 6 resmî kaynaklı alternatif: Dopigo, StockMount, Google Workspace/Sheets, Microsoft 365/Excel, Airtable, Coupler.io. Her birinin fiyat türü, para birimi, teslim/kapsam ve 14.10.2026 doğrulama URL'si `03-bes-alternatif-fiyat-kaynaklari.md` içindedir.
- Yeni dönem sipariş, ücretli satış, gelir, iade, net tahsilat, reklam, site/LinkedIn ziyaret/CTA **BİLİNMİYOR**; önceden bildirilmiş 0 satış yalnız önceki 27 günün kullanıcı beyanıdır.
- GitHub main `index.html` blob SHA `b188ed7115aa12837d98c05036e85dbf4c012cb9` doğrulandı. Yetkili satış/analitik hesapları okunmadı.

## 4. Kusurlar / iki tur QA
- **4 satış P0 açık:** (1) ticari ürün/nihai test paketi, (2) şirket-vergi-fatura ve sözleşmesel uygunluk, (3) ödeme/checkout, (4) dijital teslim/B2B kabul.
- **P1 kritik ürün semantiği:** PDF Gün 03 ayrı sipariş.csv + stok.csv dosyaları ister; Gün 01 Python prototipi **tek birleşik CSV** okuyor. Karışık stok zamanlaması/depo kırılımı için sessiz yanlış hata riski mevcut. Şema, eşleme ve kabul testleri olmadan 'satılabilir ürün' deme.
- **P1 diğer:** Gerçek kullanıcı sorunu/ödeme talebi yok; GA4 çerez izin ve canlı altı viewport/klavye/form testleri yapılmadı.
- **Tur 1:** 7 ilk dosyanın GitHub’dan varlığı ve içerikleri; 12 Q, 6 alternatif, 3 soru, 3 fiyat, 14 metrik kayıt doğrulandı.
- **Tur 2:** altı üretici URL/fiyatı, bağlam ve para birimi/abonelik farkı, açık kapsam dışı öğeler, park edilen 2 hipotez, `main` değişmemesi kontrol edildi. Yerel tek sayfa PDF PyMuPDF ile bir sayfa ve metin çıkarma testi, PNG olarak görsel kontrol PASS. Canlı site QA **TEST EDİLEMEDİ**.
- Ayrıntı: `08-kalite-ve-kanıt-raporu.md`.

## 5. Mutlak sınırlar ve kullanıcı onayı
0 TL peşin işlem, 0 istenmeyen temas. Shopier dışlandı; bu karara geri dönme. Henüz şirket/fatura yok; şirket logosu/ünvanı veya ödeme/satış açık iddiası kurma. Hiçbir müşteriye yazılmadı, para/ödeme harcanmadı, PR main’e birleştirilmedi, site/ilan/post değiştirilmedi.
**ONAY BEKLEYEN:** PR merge/yayın, ürün/CTA/fiyat değişikliği, kanal ilanı, müşteri iletişimi, satış/ödeme, gerçek veri ve analitik testleri; her eylem tek tek açık onay gerektirir. Kullanıcıdan bu aşamada bilgi istemek zorunlu değil.

## 6. Gün 03 / 15 Ekim 2026 — PDF görevi
**Adı:** Teklif ve kabul kriteri mimarisi. Şu sırayı izle:
1. İndirilebilir paket dosya sözleşmesi: README, `ornek_siparis.csv`, `ornek_stok.csv`, yerel kontrol aracı/şablon, çıktı CSV, kural sözlüğü.
2. Beş çekirdek kural: SKU eşleme, boş/mükerrer satır, stok eksiği, eşleşmeyen SKU, toplam sipariş miktarı.
3. Üç tamamen **SENTETİK** test seti: temiz, eksik kolon, bozuk veri/çakışma; beklenen kural/satır çıktıları.
4. Satır/kural bazlı yalancı olgular (falsifiable) ve negatif testler; belirsiz stok zamanı varsayımı sessizce hata sayılmaz.
5. Dosyalar müşteri cihazında kalmalı; buluta gönderim veya izinli kişisel veri gerekmemeli.
6. Lisans, sistem gereksinimi, revizyon/sürüm, destek/iade/teslimat taslak koşulları.
7. 5 adımlı ilk 5 dakika onboarding ve açık hata mesajları.
**Gün 03 teslimi:** ürün gereksinimleri/kabul test matrisi, v0.1 dosya sözleşmesi, onboarding iskeleti. Gün 03'e geçmeden müşteriye satış veya yayın yapma.

**DURUM:** Gün 02 belge, müşteri problemi ve tek hipotez kararı CLOSED; gerçek ticari ürün, sözleşme ve ödeme NOT READY.
