# SYNAPSE AUTOMATE · V8 GÜN 20 · 30.10.2026
**Planlanan gün:** 02.11.2026. **Fiilî çalışma:** 30.10.2026 (3 gün erken), görev numarası değişmedi.
**Hizmet #12:** Tahmine Dayalı Analitik — Talep tahmini, müşteri kaybı analizi, fiyat karar desteği, tedarik projeksiyonları. Kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/hizmetler.html).
**İşlem sınırı:** 0 TL peşin. Yalnız DRAFT; dış yayın, merge, kullanıcıya gönderi, insan verisi, ödeme veya yeni hesap yok.
**Kanıt sınıfı:** Hizmet açıklaması gerçek; burada geliştirilen 3 veri ön koşulu örneği KAVRAMSAL/SENTETİK. Gerçek çalışan tahmin motoru, müşteri verisi, doğruluk yüzdesi veya canlı bağlantı kanıtı yok.
## Gerçek kaynak karşılaştırması (ana dal)
| Sayfa / veri | Görünen fiyat ve iddia | Teslim / CTA | Kanıt ve risk |
|---|---|---|---|
| `veri/offer-ladder.json` | 4.900 TRY / $149 süreç; 24.900 TRY / $750 pilot; 14.900 TRY / $449 aylık; `billing` one_time/one_time/monthly | Süreç: 3–10 bulgu, gözlem, öncelik, 7 günlük plan; Pilot: kontrollü tek akış; aylık: izleme/rapor | Sayılar kaynakta GERÇEK; satışa onaylı olduğu doğrulanmadı, TEST FİYATI olarak kalmalı |
| `index.html` | “Süreç Analizi 4.900 TL; pilot gerekirse 24.900 TL başlangıç fiyatıyla” | `surec-analizi.html` ve ücretsiz tarama CTA | Sitede test niteliği aynı görünür bağlamda açık değil; mevcut P1 |
| `surec-analizi.html` | 4.900 TL test fiyatı uyarısı ve $149 örneği; ayrıca diğer fiyatlar | Üçüncü taraf FormSubmit, consent kutusu | Kapsam/form mevcut, gerçek teslim TEST_EDİLEMEDİ |
| `teklif/e-ticaret-surec-analizi.html` | Meta description “4.900 TL başlangıçlı” ve sayfada 4.900/$149 | Form yoluna giden süreç analizi teklifi | TEST FİYATI ayrımı meta/ekran bütünlüğünde henüz tamamlanmadı; mevcut P1 |
| `rehberler/ai-otomasyon-fiyatlari.html` | Fiyatlar 4.900/24.900/14.900 TL ve USD karşılık olmayan liste; JSON-LD FAQ’da “başlangıç fiyatları” | Fiyat açıklama ve gönüllü analiz CTA | Gün20 taslakta yeni tek FAQ test niteliğini ve talep tahmini koşullarını açıklar; fakat eski snippet/FAQ schema farklılığı açık P1 |

## Fiyat, teslim ve hukuki tutarlılık kararı
**Uygulanabilir tek değişiklik:** yalnız fiyat rehberine 1 yeni FAQ. Diğer P1'lar sessizce düzeltilmiş gösterilmedi; sonraki gün için backlog. Gün20 canlı fiyat veya tahsilat değiştirilmedi. Sipariş, otomatik stok, checkout, kişisel IBAN, vergi/fatura yetkisi, KDV ve iade koşulları doğrulanmadıkça satışa geçiş YOK.
**Kullanıcının varsayımsal testi:** test fiyatları gerçek müşteri/satış garantisi değildir. Mevcut durum = BİLİNMİYOR; 0 olarak raporlanmaz.

## Denetlenebilir kaynaklar
- **GitHub main:** 05bd1f2a31d36fe92134e756e485a104337fbe9f; https://github.com/synapseautomate/synapseautomate.github.io/pull/52 yalnız DRAFT.
- [Hizmet #12 (main)](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/hizmetler.html).
- [Teklif merdiveni (main)](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/veri/offer-ladder.json): 4.900 TL / 24.900 TL / 14.900 TL aylık (güncel hesap/fatura için kesin fiyat değildir); USD 149/750/449 bağımsız USD liste sayıları.
- [Fiyat rehberi](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/rehberler/ai-otomasyon-fiyatlari.html); [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/surec-analizi.html); [e-ticaret teklifi](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/teklif/e-ticaret-surec-analizi.html); [ana sayfa](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/index.html).
- [Tahmin değerlendirmenin kör noktaları / rolling-origin](https://link.springer.com/article/10.1007/s10618-022-00894-5); [stokta bulunmama, satışın talebi eksik göstermesi](https://www.sciencedirect.com/science/article/pii/S0169207023000961).
- [Nike, Rip the Script (2026)](https://about.nike.com/en/newsroom/releases/nike-debuts-rip-the-script-a-step-inside-the-universe-of-nike-football); [Pepsi Football Nation (2026)](https://www.pepsico.com/en/newsroom/press-releases/2026/pepsi-recruits-global-stars-to-create-the-pepsi-football-nation-where-fans-define-the-rules). Yalnız yaratıcı yaklaşım kıyası, görsel veya fikrî mülkiyet kopyalanmadı.
