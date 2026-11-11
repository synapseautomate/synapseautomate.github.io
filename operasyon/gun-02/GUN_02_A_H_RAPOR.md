# SYNAPSE AUTOMATE | GÜN 02 KANITLI RAPOR — PDF A–H
**Tarih:** 14.10.2026, İstanbul · **Görev:** Müşteri problemi ve ürün kararı · **Sahip:** SYNAPSE Automate
**Statü:** GÜN 02 ARAŞTIRMA/TASLAK GÖREVİ TAMAMLANDI; ürün/satış/yayın **HAZIR DEĞİL**.
**PR:** https://github.com/synapseautomate/synapseautomate.github.io/pull/11 (draft, main merge yok)
**Gün 01:** https://github.com/synapseautomate/synapseautomate.github.io/pull/10

## A) Bugünün amacı ve gerçek başlangıç bulguları
Hedef: **tek, ödeme ihtimali test edilebilir, dar, tekrarlanan problem**. Gün 01 devir dosyası, karar günlüğü, metrikler ve açık P0'lar GitHub'dan okundu. `main` kaynak `index.html` blob SHA `b188ed7115aa12837d98c05036e85dbf4c012cb9`. Canlı ana sayfayı web tarayıcı aracında doğrudan açma **DisabledError** ile başarısız; canlı HTTP ve mobil test doğrulanamadı. LinkedIn şirket sayfasının kamuya indeksli profili görüldü, yetkili pano verileri bilinmiyor. Yeni dönem ücretli satış, net tahsilat, oturum/CTA **bilinmiyor**. Önceki 27 gün 0 ücretli satış: yalnız kullanıcının bildirdiği önceki dönem tabanı.

**Tek darboğaz:** Tanımlı bir istisna kontrolüne ödeme yapılacağını gösteren gerçek nitelikli müşteri sinyali henüz yok; ayrıca satış öncesinde Gün 01'den devreden hukuki/teknik engeller açık.

## B) Tamamlanan işler, gerçek bağlantılar ve dosyalar
1. `01-icp-problem-brifi.md`: küçük e-ticaret ICP, veri biçimi, acı/karar/satın alma motivasyonu ve 3 alıcı sorusuna yanıt.
2. `02-alici-niyetli-arama-ifadeleri.md`: **12 aday sorgu** (Q01–Q12). Arama hacmi veya dönüşüm ölçülmedi.
3. `03-bes-alternatif-fiyat-kaynaklari.md`: **6 gerçek alternatif**; üretici fiyat, kapsam, kaynak URL ve 14.10.2026 doğrulama tarihi.
4. `04-urun-hipotezi-karsilastirma.md`: yalnız sipariş/stok CSV kontrolü **H1 birincil**, haftalık Excel/Sheets ve genel sipariş hata kontrolü park edildi.
5. `05-fiyat-ve-kapsam-varsayimi.md`: **990 / 4.900 / 24.900 TL** üçü de **TEST FİYATI**, ürün/kurulum/pilot sınırları ve geçerleme planı.
6. `06-metrikler.csv`: verisi erişilemeyen metrikler **bilinmiyor**, rapor sayaçları ve kaynak/sahip.
7. `07-onay-kapilari-ve-kusurlar.md`: P0/P1/P2 ve tek tek açık onay kapıları.
8. `08-kalite-ve-kanıt-raporu.md`: iki tur doküman QA, kaynak çapraz kontrolü, PDF QA ve yapı/test sınırları.
9. `SYNAPSE_GUN_02_DEVIR.md`: Gün 03 operatörüne kanıt ve açık engel devri.
10. Tek sayfalık A4 PDF: `SYNAPSE_GUN_02_ICP_PROBLEM_BRIFI.pdf` (konuşma dosyası; henüz GitHub'a ikili olarak yüklenmedi).
**Dosya kökü:** `operasyon/gun-02/` — PR #11 içinde.

## C) P0/P1/P2 kusurlar ve tamir yolu
**P0'lar (dört açık, ticari yayın/satış engelleri):** (1) nihai ürün kabulü; (2) kuruluş, vergi/fatura ve sözleşmesel uygunluk; (3) ödeme/kimlik/tahsilat; (4) teslim ve kabul akışı.
**P1:** PDF Gün 03 iki ayrı CSV isterken mevcut prototip birleşik CSV kullanıyor; stok zaman/depo semantiği yanlış pozitif doğurabilir; canlı GA4 opt-in/mobil/form ölçümleri ve gerçek alıcı niyeti yok.
**P2:** Tasarım tokenları, ikon/telif kaydı, SEO mikro metin revizyonu. **Bugün bu kusurlar “kapatıldı” denmez.**

## D) Marka / UX / içerik / telif / politika / test kalite matrisi
| Alan | İç Gün 02 taslakları | Canlı yayın / gerçek satış |
|---|---|---|
| Marka / dil / açıklık | GEÇTİ: tek cümle vaat, net sınırlamalar | Canlı marka karşılaştırması TEST EDİLEMEDİ |
| ICP / teklif / doğruluk | GEÇTİ: yalnız doğrulanabilir semantik ve fiyat hipotezi | Ödeme/satın alma kanıtı YOK |
| Rakip / telif / kaynak | GEÇTİ: altı resmî URL, yalnız kısa olgusal özetler | Yetkisiz rakip görsel/kopya kullanılmadı |
| Veri / KVKK | GEÇTİ: ürün yerelde işleme hedefi, PII yükleme zorunlu değil | Hukuk + gerçek uygulama akışı TEST EDİLEMEDİ |
| HTML / mobil / klavye | İç doküman ve A4 PDF render kontrolü GEÇTİ | Canlı altı viewport ve klavye TEST EDİLEMEDİ |
| Ölçüm / fiyat / CTA | Fiyat etiketleri TEST, metrikler doğru ayrıldı | Canlı CTA, form ve checkout KALDI / doğrulanmadı |
| İki tur QA | Doküman yapı/çapraz kaynak ve PDF testi GEÇTİ | Canlı uçtan uca PASS **verilmedi** |
Ayrıntılı kanıt: `08-kalite-ve-kanıt-raporu.md`.

## E) Rakamlar ve kaynak
| Metrik | Bugün | Veri türü |
|---|---|---|
| Birincil ürün hipotezi | **1** | Gün 02 karar dosyası |
| İkinci ürün başlatma | **0** | H2/H3 park edildi |
| Aday alıcı sorgusu | **12** | Sorgu taslağı; arama verisi değil |
| Doğrulanabilir rakip karşılaştırması | **6** | Resmî üretici fiyat sayfaları |
| Yanıtlanan alıcı sorusu | **3** | ICP brifi |
| Deneysel fiyat | **3** | PDF fiyat hipotezleri |
| Yeni dönem ücretli satış / trafik / CTA / gelir | **Bilinmiyor** | Yetkili paneller yok |
| Satış için açık P0 | **4** | Gün 01 devri + Gün 02 kusur kaydı |

**Fiyat kanıtları (14.10.2026 resmî sayfalar):** Dopigo Pazaryeri 24.999 TL/yıl, StockMount stok+sipariş kampanyası 25.000 TL/yıl, Workspace Starter yıllık fiyat görünümü 71,20 TL/ay/kullanıcı, Microsoft 365 İş Temel 7 USD/ay/kullanıcı yıllık, Airtable Free ve Team 20 USD/kullanıcı/ay yıllık, Coupler.io Free ve Starter 32 USD/ay aylık. Bu ürünlerin fiyatları SYNAPSE'ın test fiyatına pazar kabul kanıtı oluşturmaz.

## F) Kullanıma hazır iç taslaklar ve **ONAY BEKLEYEN** eylemler
**Ürün vaadi:** “Sipariş ve stok CSV dosyalarındaki stok açığı, negatif stok, boş SKU ve yinelenen kayıt gibi tanımlı tutarsızlıkları yerel olarak işaretleyen kontrol paketi.”
**Temel kapsam dışı:** mağaza/ERP bağlantısı, otomatik stok güncelleme, sonuç garantisi ve zorunlu kişisel veri yükleme **yok**.
**Tek tek onaylanacak işler:** (A01) PR main merge ve canlı yayın, (A02) fiyatlı ürün/CTA/ilan/LinkedIn yayını, (A03) müşteri iletişimi, (A04) satıcı/kimlik/fatura/ödeme, (A05) gerçek veri ve GA4/form uçtan uca doğrulaması. Bugün **hiçbiri yapılmadı**.

## G) Eksikler ve yalnız kullanıcının yapabileceği adımlar
**Şimdi kullanıcıdan herhangi bir bilgi veya izin gerekli değil.** Henüz vergi/fatura/tüzel statü, satıcı onboarding, banka/IBAN, ödeme uygunluğu ve resmî hesap panelleri ancak hesap sahibi tarafından güvenli ve izinli süreçte tamamlanabilir. Kimlik/kart/parola paylaşılması istenmez. Pazarın fiyatı kabulü ve alıcı sorun sıklığı, gönüllü gerçek sinyal olmadan **belirlenemez**.

## H) Ertesi güne tam devir
`SYNAPSE_GUN_02_DEVIR.md`: GitHub dosyaları, seçilen H1, altı rakip kanıtı, fiyat hipotezleri, üç alıcı sorusu, iki QA turu, 4 P0 ve P1, açık kullanıcı onayları. **Gün 03 / 15.10.2026 — Teklif ve kabul kriteri mimarisi**: iki CSV veri sözleşmesi, beş çekirdek kural, üç sentetik senaryo, kural kabul testi, gizlilik/README/onboarding. **Gün 02 kapanışı satış onayı değildir.**

**Gün 02 karar kapısı:** üç alıcı sorusu yanıtlandı, ≥5 (6) kaynaklı alternatif, tek cümle vaat tamam. **Görev araştırma safhası CLOSED / ticari yayın NOT READY.**
