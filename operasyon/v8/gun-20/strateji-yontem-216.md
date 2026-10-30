# SYNAPSE AUTOMATE · V8 GÜN 20 · 30.10.2026
**Planlanan gün:** 02.11.2026. **Fiilî çalışma:** 30.10.2026 (3 gün erken), görev numarası değişmedi.
**Hizmet #12:** Tahmine Dayalı Analitik — Talep tahmini, müşteri kaybı analizi, fiyat karar desteği, tedarik projeksiyonları. Kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/hizmetler.html).
**İşlem sınırı:** 0 TL peşin. Yalnız DRAFT; dış yayın, merge, kullanıcıya gönderi, insan verisi, ödeme veya yeni hesap yok.
**Kanıt sınıfı:** Hizmet açıklaması gerçek; burada geliştirilen 3 veri ön koşulu örneği KAVRAMSAL/SENTETİK. Gerçek çalışan tahmin motoru, müşteri verisi, doğruluk yüzdesi veya canlı bağlantı kanıtı yok.
## Yöntem / karar: Geçişi kolaylaştırma
**Sahip:** SYNAPSE operasyon, hesap yetkisi kullanıcıda. **Durum:** DRAFT / NO EXTERNAL ACTION.
**Karar ve uygunluk:** Excel'den tahmin için veri taşıma ancak doğru kolon, tarih/kimlik eşlemesi ve geri alma planıyla güvenlidir; canlı araç yok.
**Somut Gün20 üretimi:** Boş CSV gereksinimleri: tarih, ürün_id, satış_adedi, stok_müsait, kampanya; saat dilimi/para birimi ve iptal durumları ayrıca tanımlanır. Satış 0 iken stok 0 ise gerçek talep bilinmeyebilir. Dışa verme ve müşteri CRM/API erişimi yok. Kontrol listesi taslağı, bir tık geçiş iddiası değil.
| Kabul | Gözlem |
|---|---|
| Hizmet gerçekliği | Kaynak hizmet #12 GitHub main, PASS |
| İddia/kanıt | Sentetik kavramsal, gerçek tahmin motoru veya alıcı verisi YOK |
| Gerçek hesap/panel | BİLİNMİYOR, kişisel temas YAPILMADI |
| Peşin maliyet | 0 TL (işlem günlüğü) |
| Kullanıcı yayın izni | AYRI ONAY BEKLİYOR, sosyal kota 0 |
| Bağımsız test | Sadece FAQ için browser QA, diğer yöntemde implementasyon/performans kanıtı yok |
**Geri alma:** Gün20 tek FAQ yeniden kaldırılır; önerilen yöntemler canlı kod üretmediğinden ek rollback yok.

## Denetlenebilir kaynaklar
- **GitHub main:** 05bd1f2a31d36fe92134e756e485a104337fbe9f; https://github.com/synapseautomate/synapseautomate.github.io/pull/52 yalnız DRAFT.
- [Hizmet #12 (main)](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/hizmetler.html).
- [Teklif merdiveni (main)](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/veri/offer-ladder.json): 4.900 TL / 24.900 TL / 14.900 TL aylık (güncel hesap/fatura için kesin fiyat değildir); USD 149/750/449 bağımsız USD liste sayıları.
- [Fiyat rehberi](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/rehberler/ai-otomasyon-fiyatlari.html); [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/surec-analizi.html); [e-ticaret teklifi](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/teklif/e-ticaret-surec-analizi.html); [ana sayfa](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/index.html).
- [Tahmin değerlendirmenin kör noktaları / rolling-origin](https://link.springer.com/article/10.1007/s10618-022-00894-5); [stokta bulunmama, satışın talebi eksik göstermesi](https://www.sciencedirect.com/science/article/pii/S0169207023000961).
- [Nike, Rip the Script (2026)](https://about.nike.com/en/newsroom/releases/nike-debuts-rip-the-script-a-step-inside-the-universe-of-nike-football); [Pepsi Football Nation (2026)](https://www.pepsico.com/en/newsroom/press-releases/2026/pepsi-recruits-global-stars-to-create-the-pepsi-football-nation-where-fans-define-the-rules). Yalnız yaratıcı yaklaşım kıyası, görsel veya fikrî mülkiyet kopyalanmadı.
