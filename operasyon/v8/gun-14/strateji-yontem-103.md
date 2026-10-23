# SYNAPSE V8 Gün 14 — Yöntem 103: Reklam dışı görünürlük fırsatları
**23.10.2026 | İÇ TASLAK, KAMUYA YAYINLANMADI**
**Güncel konu:** Hukuk ve Uyum İş Akışları; sözleşme maddesi çıkarımı **hukuki görüş değil ön inceleme**. **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**.

## Yönteme özgü karar / üretim
Yeni içerik üretiminden önce temel sitenin marka, doğru hukuk sınırı, iç link ve güvenli form erişimi denetlenir.

## Karar tablosu ve QA durumu
| Katman | Repo kanıtı | Açık kontrol |
|---|---|---|
| Marka | main index.html, hizmetler.html | PASS kaynak; canlı browser TEST_EDİLEMEDİ |
| Hukuk açıklaması | sektörler/hukuk.html | PASS metin sınırları |
| Site araması | sitemap.xml | indekslenme BİLİNMİYOR, GSC yok |
| CTA | iletisim.html#contact-form | form id var, teslim BİLİNMİYOR |
| Sosyal | Gün13 kullanıcı PASS | permalink+insight BİLİNMİYOR |
| İzinli kanıt | yerel sentetik kelime tarama 7/7 | kamuya henüz onay yok |

## Kanıt, sahip, izin
Gerçek fotoğraf/vaka, doğrulanmamış firma belgesi, yerel harita veya kamu rozetleri yok. CRO tek niyet sorusu: “Ön inceleme kapsamına girer mi?”; dosya göndermeye zorlama YOK.
**Gerçek repo kaynakları:** 23.10.2026 `main` `07040d2ed372df059c6d60d4567c270ad14655e4`, `hizmetler.html`, `sektorler/hukuk.html`, `surec-analizi.html`, `iletisim.html`, `content-manifest.json`, `assets/js/synapse-measurement-v1.js`; `HUKUK_ON_INCELEME_SENTETIK_KANIT_KARTI.md` ve `GUN14_TEKIL_HUNI_KARAR_PANOSU.md`.
**PASS:** bu iç karar/metin ve kaynak dosyası oluşturuldu. **FAIL / AÇIK:** gerçek satış-kaynak eşlemesi ve satıcı/yasal kapı. **BİLİNMİYOR:** gerçek nitelikli inbound/serp gösterimi/kontrat/gelir. **İkinci QA:** görünür içerik, marka, mobil, veri, telif ve hukuk testleri ayrı `GUN14_QA_B_MARKA_HUKUK_UX.md`; canlı panel/render gösterimi sanılmasın.
**Sahip:** SYNAPSE içerik/operasyon, yasal kontrol için hesap sahibi/uzman; **ONAY BEKLİYOR:** ayrıca belirlenmedikçe hiçbir kamuya yayın veya gerçek alıcıya mesaj yetkisi yok. **Dış etki:** sadece taslak branch / draft PR, `main` merge YOK.
