# Gün 01 — Kanıt ve iki turlu kalite matrisi
**Tarih:** 2026-10-13 | **Denetleyen:** AI operatörü | **Sahip:** SYNAPSE hesap sahibi
**Kapsam:** Gün 01 raporlarının denetlenmesi; canlı site veya satış sertifikası değildir.

## GitHub main envanteri / doğruluk sınırı
Baz `main` commit: `bc79409c8f672884a00dcdb89b0b6119cac42f6c`, PR #10 baz SHA aynı olarak yeniden doğrulandı (2026-10-13).
| Varlık | SHA / kanıt | Bulgusu |
|---|---|---|
| Ana sayfa | `index.html` SHA `b188ed7115aa12837d98c05036e85dbf4c012cb9` | Marka, H1 ve hizmet bağlantıları kaynak incelemesi. |
| Talep formu | `surec-analizi.html` SHA `0a3fbbb120a77b12b2d5b1646e88e7b02624a4b4` | FormSubmit talep kanalı; ödeme değil. |
| E-ticaret teklif | `teklif/e-ticaret-surec-analizi.html` SHA `63802dec95c17bc2380ad9fc275329f61002a616` | 4.900 TL genel hizmet gösterimi; güncel fiyat teyidi yok. |
| Ölçüm | `assets/js/synapse-measurement-v1.js` SHA `e5bd396eb7225d9aab795af3de00c5cb7d857353` | GA4 yükleme; rıza/çerez kontrolü açık. |
| Sitemap | `sitemap.xml` SHA `8e98a254e69eb1e164f1a7f1b55228ab97a21f6d` | 125 URL yerel paket envanteri. |
| Gizlilik | `gizlilik.html` SHA `cf24ebef6b85df753bc9855f22cfe1ba4b2e1172` | Gizlilik sayfası mevcut; tam KVKK uygunluğu iddiası yok. |
Kaynak bağlantısı: https://github.com/synapseautomate/synapseautomate.github.io/tree/bc79409c8f672884a00dcdb89b0b6119cac42f6c

## Gün 01 QA — bağımsız iki tur
**Tur 1:** Ekteki yerel Gün 01 kanıt paketinde `python testler/test_artefaktlar.py` çalıştırıldı: PASS. 11 zorunlu rapor dosyası, 4 kanal kaydı, metriklerde 'bilinmiyor', tarih/kaynak/sahip ve HTML semantik kontrolleri geçti. Paket içinde ilk 320px rapor taşma/kelime kırma kusuru düzeltilmiş.
**Tur 2:** `python testler/ikinci_tur_kalite.py` ayrı çalıştırıldı: PASS. BS4 semantik, metrik tutarlılığı, altı PNG render genişliği, örnek renk çiftleri ve klavye rapor kayıtları incelendi. Altı PNG genişliği PIL ile yeniden doğrulandı: 320/375/390/768/1024/1440px. Örnek renk çiftlerinin minimum kontrastı 9.74:1 (yerel rapor, bütün canlı site değil).
**Bütünlük:** Yerel `kanit/SHA256SUMS.txt` için `sha256sum -c`: tüm satırlar OK.
**Ek:** Kullanıcının konuşmadaki `SYNAPSE_GUN_01_KANIT_PAKETI.zip` eki; GitHub reposuna tüm PNG/binary kanıtlar yüklenmedi. Yerel kanıtlar sonradan kanıtsız biçimde GitHub'da varmış gibi sunulmaz.

## Kalite karar matrisi
| Denetim alanı | Tur 1 | Tur 2 | Gün 01 durum / yorum |
|---|---|---|---|
| Rapor veri doğruluğu | GEÇTİ | GEÇTİ | Bilinmeyen metrikler 0 yapılmadı; ön dönem 0 yalnız kullanıcı beyanı. |
| Rapor erişilebilirlik ve mobil | GEÇTİ | GEÇTİ | Yalnız yerel Gün 01 HTML özet, canlı site DEĞİL. |
| GitHub statik referansları | GEÇTİ (örneklem) | Kaynak ile kıyaslandı | Önceki pakette 116 yerel referans yol eşleşmesi; canlı HTTP 200/404 taraması YAPILMADI. |
| Canlı site tüm ekranlar / klavye | TEST EDİLEMEDİ | TEST EDİLEMEDİ | Sitede canlı tarayıcı deneyi yok; sayfa testi iddiası yok. |
| Logo hakları / Inter | KISMİ | KISMİ | Inter SIL OFL, logo telif/sahiplik belgesi yok. |
| GA4/KVKK | RİSK BULUNDU | KAYNAK KONTROLÜ | Canlı rıza ve çerez ağ testi yok; satış/yayın risk kapısı açık. |
| Demo/ürün | Prototip PR üzerinde | Ticari teslimat kabulü yok | 990 TL yalnız fiyat hipotezi; satışa hazır ürün değil. |
| Checkout/teslimat | KALDI | TEST EDİLEMEDİ | Ödeme ve otomatik teslimat doğrulanmadı. |
| Vergi/fatura/KVKK sözleşmesi | KALDI | Hesap erişimi yok | Kullanıcı henüz şirket kurmadı, fatura yetkisi yok. |
| PR/main/yayın | Taslak PR | PR metadata doğrulandı | Main değişmedi; PR #10 draft, merged=false. |

## P0 / P1 / P2 sonuçları
**P0 — 4 açık satışa çıkış kapısı:** (1) ticari ürün/kabul paketi henüz son değil; (2) kuruluş-fatura/vergisel uygunluk yok; (3) ödeme doğrulanmadı; (4) teslimat zinciri doğrulanmadı.
**P1:** GA4 opt-in kontrolü, canlı form+mobil/a11y uçtan-uca QA, trafik/satış paneli kanıtı yok.
**P2:** Görsel tasarım token uyumu ve marka varlık sahipliği dosyasını toplama.
**Önce/sonra:** Gün 01'de `main`/canlı siteye değişiklik olmadı. Canlı öncesi/sonrası görsel karşılaştırma uygulanamaz. Yerel raporda 320px düzeltmesi kaydı ayrı kanıt paketinde.

**Gün 01 rapor QA hükmü:** GEÇTİ (belgelenen kapsam). **Canlı ticari satış/yayın hükmü:** KALDI / ONAY BEKLİYOR. Bunlar aynı hüküm değildir.
