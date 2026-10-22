# SYNAPSE V8 GÜN13 | Yöntem taslağı

**Yalnız iç çalışma • 22.10.2026 • Plan 26.10.2026 • İzin olmadan yayın yok.**

## 222 — Negatif güven taahhüdü

## Önce / sonra ve karar engeli
**Mevcut önce:** surec-analizi.html ilk H1 “Önce doğru süreci seçin. Sonra otomasyonu kurun.”, iletisim.html “Bir iş akışını birlikte haritalayalım.”, e-ticaret teklif sayfası “Sipariş, iade ve müşteri takibi kimde bekliyor?”. CSV incelemesinin dosya ve kapsam sınırı ilk cümlede net değil. FormSubmit action kaynakta var, teslim doğrulanmadı.

**Sadece taslak sonra:** “Sipariş ve stok CSV’lerinde tutarsızlıkları görünür kılın. Bir sipariş.csv + bir stok.csv; eksik SKU, tekrar, SKU/depo farkı, negatif stok. R05 stok yeterliliği yalnız yeterli tarih/depo/rezervasyon bilgisiyle, aksi halde DEĞERLENDİRİLMEDİ.” Ardından “SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL” notu; metin gerçek müşteri vaka veya mevcut ürün performansı olarak sunulmaz. **Tek CTA (yalnız site):** “Kapsam uyumluluğunu sor” → surec-analizi.html. Kesin fiyat/kur/fatura/süre, API, otomatik stok değiştirme, garanti yok. **320/390/768/1440 CTA:** yalnız yeni prototip PASS; canlı site TEST_EDİLEMEDİ. **Form yönü:** kaynak kod FormSubmit; gerçek POST/Inbox TEST_EDİLEMEDİ.

**Kendine özgü itiraz:** İspatı olmayan gizli ücret/veri silme/garanti sözlerini yayınlama tehlikesi.

**Uygulama / karar:** Beş risk/denetim: sürpriz ücret—onaylı değişiklik kaydı; kişisel veri—ilk formda gizli CSV yok; gizli abonelik—tek teslim ile aylık servisi ayır; sahte stok—canlı değişiklik yok ve R05 koşullu; yanlış ROI/telif—müşteri vakası uydurma ve özgün sentetik örnek. Alıcı denetim yolları: kapsam tutanağı, form metni, servis listesi, rapor kural kaydı, örnek etiketi. İşleyen operasyon denetimi henüz doğrulanmadıysa kesin politika olarak iddia edilmez.

## Kaynak / iki QA turu / onay
**Repo kaynakları:** https://github.com/synapseautomate/synapseautomate.github.io/blob/main/surec-analizi.html ; https://github.com/synapseautomate/synapseautomate.github.io/blob/main/iletisim.html ; https://github.com/synapseautomate/synapseautomate.github.io/blob/main/teklif/e-ticaret-surec-analizi.html ; https://github.com/synapseautomate/synapseautomate.github.io/blob/main/cozumler/siparis-stok-csv-kontrolu.html .

**QA A kaynak+teknik:** repo metnindeki CTA hedefi, FormSubmit ve fiyatlar okunabildi; form gerçek gönderimi yapılmadı. **QA B bağımsız tasarım:** Yeni iç prototip Chromium 320/375/390/768/1024/1440: altı genişlikte tek CTA, yatay taşma yok, 44px ve klavye odağı PASS. Canlı üretim sitesi bu görüntülerle test edilmedi; Safari, canlı form teslimi, 404, Lighthouse, Upwork paneli TEST_EDİLEMEDİ. Font/telif/gerçek ürün ekranı için ayrı kanıt gerekir. **Yayın:** ONAY BEKLİYOR. **Sorumlu:** SYNAPSE hesap sahibi.
