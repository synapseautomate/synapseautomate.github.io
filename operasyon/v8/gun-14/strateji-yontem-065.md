# SYNAPSE V8 Gün 14 — Yöntem 065: Ücretsiz araç kutusu ve gerçek sınırlar
**23.10.2026 | İÇ TASLAK, KAMUYA YAYINLANMADI**
**Güncel konu:** Hukuk ve Uyum İş Akışları; sözleşme maddesi çıkarımı **hukuki görüş değil ön inceleme**. **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**.

## Yönteme özgü karar / üretim
Arama/ölçüm araçlarını ancak hesap yetkisi varsa veri kaynağı kabul et. Yerel script tam metin hukuki anlaşmazlık çözmez.

## Karar tablosu ve QA durumu
| Araç | Sunulan işlev | Sahiplik / koşul | Durum |
|---|---|---|---|
| GSC | sorgu ve tıklama performansı | site ownership gerekli | BİLİNMİYOR |
| GA4 | consentli oturum | rıza + doğru etiket + yetkili panel | KOD PASS; panel BİLİNMİYOR |
| LinkedIn native analytics | şirket gösterimi/talep | admin account | BİLİNMİYOR |
| Python standard library unittest | tamamen sentetik madde tarama | yerel, üçüncü taraf veri yok | 7/7 PASS |
| PageSpeed/Rich Results | kamuya açık URL testleri | HTTP erişimi gerek | TEST EDİLEMEDİ |
| Ücretli editörler / API | zorunlu değil | kart/abonelik riski | KAPSAM DIŞI |

## Kanıt, sahip, izin
Sorumlu teknik operatör ve hesap sahibi; Google/LinkedIn resmi linkleri kanal dokümanında. Ücretsiz plan sınırsız/sıfır veri maliyeti iddiası değil; hiçbir gizli müşteri belgesi online AI'ya yüklenmeyecek.
**Gerçek repo kaynakları:** 23.10.2026 `main` `07040d2ed372df059c6d60d4567c270ad14655e4`, `hizmetler.html`, `sektorler/hukuk.html`, `surec-analizi.html`, `iletisim.html`, `content-manifest.json`, `assets/js/synapse-measurement-v1.js`; `HUKUK_ON_INCELEME_SENTETIK_KANIT_KARTI.md` ve `GUN14_TEKIL_HUNI_KARAR_PANOSU.md`.
**PASS:** bu iç karar/metin ve kaynak dosyası oluşturuldu. **FAIL / AÇIK:** gerçek satış-kaynak eşlemesi ve satıcı/yasal kapı. **BİLİNMİYOR:** gerçek nitelikli inbound/serp gösterimi/kontrat/gelir. **İkinci QA:** görünür içerik, marka, mobil, veri, telif ve hukuk testleri ayrı `GUN14_QA_B_MARKA_HUKUK_UX.md`; canlı panel/render gösterimi sanılmasın.
**Sahip:** SYNAPSE içerik/operasyon, yasal kontrol için hesap sahibi/uzman; **ONAY BEKLİYOR:** ayrıca belirlenmedikçe hiçbir kamuya yayın veya gerçek alıcıya mesaj yetkisi yok. **Dış etki:** sadece taslak branch / draft PR, `main` merge YOK.
