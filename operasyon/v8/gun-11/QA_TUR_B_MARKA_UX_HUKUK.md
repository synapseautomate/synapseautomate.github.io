# QA B — Bağımsız erişilebilirlik/marka/dönüşüm/hukuk

20.10.2026 · Teknik CI gerçek Chromium 320/375/390/768/1024/1440 png üretir; sonuç raporu `SEO_QA_B_TARAYICI.json` Actions artefaktı olarak bulunur.

| Alan | Kaynak/kabul kapısı | Durum |
|---|---|---|
| Resmî logo | `../assets/brand/synapse-logo-clean.png` | KOD_PASS; resim yüklenmesi CI bekliyor |
| Erişilebilirlik | 1 H1, tab skip, CTA yüksekliği >=44, görsel alt, kırpılma | TEST_EDİLEMEDİ → CI |
| 8px ritim ve premium düzen | özgün tipografi/görsel kartlar; UX screenshot incelenmeli | TEST_EDİLEMEDİ |
| Telefon / masaüstü | altı gerçek Chromium viewport; Safari ekranı ayrı | TEST_EDİLEMEDİ |
| Form ve kişisel veri | yeni sayfa form veya veri yükleme sunmaz; CTA mevcut araca gider | KOD_PASS |
| Mevcut araç | gerçek 8 adımlık öz değerlendirme, fatura işleyici değil | KOD_KAYNAK_PASS; browser bekliyor |
| Fiyat ve sahte müşteri | bulunmuyor; sentetik üst etiket var | KOD_PASS |
| Canlı GSC / 404 / Lighthouse / form teslimi | hesap dışı veya yayınlanmamış URL | BİLİNMİYOR |
| Canlı SEO yayın ve hukuk/host uygunluğu | kullanıcı ayrı spesifik yayına onay vermedi | ONAY BEKLİYOR |

## Fiili QA sonucu ek kaydı — 20.10.2026
- İlk gerçek Chromium denemesi 320/375/390 mobil yatay taşma ile **FAIL**; gerçek sonucu sakla. `minmax(0,1fr)`, `min-width:0` sonrası altı viewport, tek H1, görsel yüklenmesi/alt, 44px CTA, klavye skip, iki giriş bağlantısı ve 8 maddelik web aracı `0/8 -> 1/8` **PASS**. Kanıt ve screenshot: https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/39386605289 .
- Screenshotlar 375/390/1440 açılarak gözle incelendi; inceleme yalnız statik Chromium, resmî canlı Safari/Lighthouse veya GSC paneli PASS anlamına gelmez.
- Yasa/hukuk, FormSubmit teslimi, tahsilat/fatura, index ve yayın **AÇIK**. Bu PR hâlâ DRAFT ve yayımlanmadı.
