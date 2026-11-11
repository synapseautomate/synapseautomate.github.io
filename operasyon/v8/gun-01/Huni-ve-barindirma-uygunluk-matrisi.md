# V8 Gün 01 — Huni ve barındırma matrisi
| Halka | Gerçek kaynak | Masaüstü kanıt | Mobil kanıt | Karar |
|---|---|---|---|---|
| Demo | https://synapseautomate.github.io/ ücretsiz genel tarama CTA | Kamu metni okundu; iki CSV ürün demo kanıtı YOK | 320/375/390 render TEST EDİLEMEDİ | V8 demo satış kanıtı değil |
| Kapsam | main `teklif/e-ticaret-surec-analizi.html` | Bir akış/insan onayı/3–10 bulgu kaynakta var | 768/1024 render TEST EDİLEMEDİ | Genel B2B hizmet, yerel CSV ile karıştırma |
| Fiyat | main `index.html` + e-ticaret teklif sayfası | 4.900 TL süreç analizi; 24.900 TL pilot başlangıç yazısı | 1440 render TEST EDİLEMEDİ | V8 990/4.900/24.900 yalnız TEST |
| Güvenli ödeme | Yetkili Upwork/MoR paneli | KYC/checkout kanıtı YOK | End-to-end TEST EDİLEMEDİ | BİLİNMİYOR, satış HAYIR |
| Teslim | V6 birleşik CSV taslağı, V8 iki CSV sözleşmesi | Hash/sürüm/teslim kanıtı YOK | İndirme TEST EDİLEMEDİ | Açık P0 |

**HTTP gerçeği:** web aracı ana sayfayı okuyabildi; container `curl -IL --max-time 12 https://synapseautomate.github.io/` DNS çözümleyemedi (000). Alt site URL'lerin HTTP 200/404 testi yapılmadı. Kırık link tespit listesi **kanıtlanmış öğe yok; test tamamlanmadı**; görüntü/ekran görüntüsü PASSED yok.

| Ölçüt | GitHub Pages | Cloudflare Pages Free |
|---|---|---|
| Statik marka vitrini | Mevcut ana sayfa erişilebilir, ticari amaç sınırı var | 0 TL koşullu statik aday; hesap açılmadı |
| E-ticaret/checkout | Resmî 'not intended for or allowed' hükmü; kullanılmaz | Statik hosting checkout/MoR değildir; yasal ve hesap uygunluğu ayrı |
| Ücretsiz kota | GitHub Pages limitleri ve ticari kısıtlar | 500 build/ay, 1 paralel, 20.000 dosya, 25 MiB/file (05.09.2026); statik asset ücretsiz ve sınırsız (08.09.2026) |
| Functions ve gizli işlem | Pages'te kredi kartı/şifre istenmez | Functions Workers kotasına bağlı, plansız faturalama/negatif bakiye kabul edilmez |
| Yayın | Main değişmedi | Yalnız araştırma, DEPLOY YOK |

**Ayrık satın alma yolları:** Upwork Project Catalog *hizmet* platform içi fonlama/sipariş; Paddle ilk MoR dijital ürün incelemesi, Lemon Squeezy yazılım yedeği, Payhip+iyzico kart/komisyon riski varsa dışarıda; Shopier dışarıda. Bu yol ve teslimlerin hiçbirinde satıcı/ödeme/teslim kanıtı yok.

Kaynaklar (14.10.2026 erişimi):
- GitHub: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits (güncelleme tarihi gösterilmedi)
- Cloudflare: https://developers.cloudflare.com/pages/platform/limits/ (05.09.2026); https://developers.cloudflare.com/pages/functions/pricing/ (08.09.2026)
- GİB: https://istanbul.gib.gov.tr/mevzuat/kanun/433 (GVK 20/B, kişi/faaliyet teyidi gerekir)
- Ticaret Bakanlığı: https://tuketici.ticaret.gov.tr/yayinlar/tuketici-bilgi-rehberi/mesafeli-sozlesmeler-hakkinda-bilgilendirme (17.08.2026); https://etbis.ticaret.gov.tr/tr/SSS
- KVKK: https://www.kvkk.gov.tr/Icerik/7353/Cerez-Uygulamalari-Hakkinda-Rehber (Temmuz 2025)
- LinkedIn: https://www.linkedin.com/help/linkedin/answer/a7436041 (Company Services koşullu ücretsiz)
