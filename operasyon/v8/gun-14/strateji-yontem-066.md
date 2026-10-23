# SYNAPSE V8 Gün 14 — Yöntem 066: Temel otomasyonlar — ücretli bot olmadan
**23.10.2026 | İÇ TASLAK, KAMUYA YAYINLANMADI**
**Güncel konu:** Hukuk ve Uyum İş Akışları; sözleşme maddesi çıkarımı **hukuki görüş değil ön inceleme**. **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**.

## Yönteme özgü karar / üretim
Otomasyon önce kurallar ve insan devri; hukuk örneğinde sadece sentetik kelime taraması yap, kararı otomatikleştirme.

## Karar tablosu ve QA durumu
| Akış | Kural | Sonuç |
|---|---|---|
| İlk soru | hangi madde konuları, rol ve örnek izinleri | yalnız metadatası, gerçek sözleşme YOK |
| Anahtar arama | gizli bilgi/fesih/veri silme | etiket, hukuki hüküm değil |
| Eşleşme yok | otomatik temiz/onay YOK | uzman incelemesi |
| Kimlik/e-posta görünümlü değer | negatif test | DATA_MINIMIZATION_BLOCKED |
| Paylaşım | her platforma ayrı açık onay | bu gün YAPILMADI |
| DM / e-posta scraping | yasak | YAPILMADI |

## Kanıt, sahip, izin
Yerel script `sozlesme_anahtar_kontrol_SENTETIK.py`; test 7/7 OK; UTM taslağı: utm_source=linkedin&utm_medium=organic&utm_campaign=law_scope_preview fakat yayımlanmadı; kullanıcıya özel takip/kimlik kaydı yok.
**Gerçek repo kaynakları:** 23.10.2026 `main` `07040d2ed372df059c6d60d4567c270ad14655e4`, `hizmetler.html`, `sektorler/hukuk.html`, `surec-analizi.html`, `iletisim.html`, `content-manifest.json`, `assets/js/synapse-measurement-v1.js`; `HUKUK_ON_INCELEME_SENTETIK_KANIT_KARTI.md` ve `GUN14_TEKIL_HUNI_KARAR_PANOSU.md`.
**PASS:** bu iç karar/metin ve kaynak dosyası oluşturuldu. **FAIL / AÇIK:** gerçek satış-kaynak eşlemesi ve satıcı/yasal kapı. **BİLİNMİYOR:** gerçek nitelikli inbound/serp gösterimi/kontrat/gelir. **İkinci QA:** görünür içerik, marka, mobil, veri, telif ve hukuk testleri ayrı `GUN14_QA_B_MARKA_HUKUK_UX.md`; canlı panel/render gösterimi sanılmasın.
**Sahip:** SYNAPSE içerik/operasyon, yasal kontrol için hesap sahibi/uzman; **ONAY BEKLİYOR:** ayrıca belirlenmedikçe hiçbir kamuya yayın veya gerçek alıcıya mesaj yetkisi yok. **Dış etki:** sadece taslak branch / draft PR, `main` merge YOK.
