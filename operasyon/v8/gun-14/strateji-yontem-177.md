# SYNAPSE V8 Gün 14 — Yöntem 177: Erişim çöküşü: yedi kritik kök neden sorusu
**23.10.2026 | İÇ TASLAK, KAMUYA YAYINLANMADI**
**Güncel konu:** Hukuk ve Uyum İş Akışları; sözleşme maddesi çıkarımı **hukuki görüş değil ön inceleme**. **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**.

## Yönteme özgü karar / üretim
Henüz ölçülmüş erişim baz çizgisi yokken 'erişim düştü', 'gölge yasak' deme.

## Karar tablosu ve QA durumu
| Kontrol sorusu | Mevcut kaynak | Bugün hüküm |
|---|---|---|
| 1 Ölçüm/rapor tanımı değişti mi? | GA4 consent kodu | BİLİNMİYOR |
| 2 Hesap/politika/telif uyarısı? | native platform yok | BİLİNMİYOR |
| 3 Hangi yüzey düştü? | GSC/insight yok | BİLİNMİYOR |
| 4 Tek tema mı hepsi mi? | Gün13 paylaşım PASS | BİLİNMİYOR |
| 5 Hedef rol/ülke değişti mi? | hukuk rolü taslak | BİLİNMİYOR |
| 6 Mevsim/rekabet/dış haber? | tarihli karşılaştırma yok | BİLİNMİYOR |
| 7 İçerik vaadi ile fayda ayrımı? | yerel script sadece kelime tarar | PASS: kavramsal etiket |


## Kanıt, sahip, izin
Kök neden hükmü: VERİ YOK, teşhis YOK. İnceleme sırası gerçek platform paneli → teknik politika → mesaj/kitle uyumu → tek değişken. Hesap sil/aç, bot, sahte ziyaret, takipçi satın alma, DM YOK.
**Gerçek repo kaynakları:** 23.10.2026 `main` `07040d2ed372df059c6d60d4567c270ad14655e4`, `hizmetler.html`, `sektorler/hukuk.html`, `surec-analizi.html`, `iletisim.html`, `content-manifest.json`, `assets/js/synapse-measurement-v1.js`; `HUKUK_ON_INCELEME_SENTETIK_KANIT_KARTI.md` ve `GUN14_TEKIL_HUNI_KARAR_PANOSU.md`.
**PASS:** bu iç karar/metin ve kaynak dosyası oluşturuldu. **FAIL / AÇIK:** gerçek satış-kaynak eşlemesi ve satıcı/yasal kapı. **BİLİNMİYOR:** gerçek nitelikli inbound/serp gösterimi/kontrat/gelir. **İkinci QA:** görünür içerik, marka, mobil, veri, telif ve hukuk testleri ayrı `GUN14_QA_B_MARKA_HUKUK_UX.md`; canlı panel/render gösterimi sanılmasın.
**Sahip:** SYNAPSE içerik/operasyon, yasal kontrol için hesap sahibi/uzman; **ONAY BEKLİYOR:** ayrıca belirlenmedikçe hiçbir kamuya yayın veya gerçek alıcıya mesaj yetkisi yok. **Dış etki:** sadece taslak branch / draft PR, `main` merge YOK.
