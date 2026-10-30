# SYNAPSE AUTOMATE · V8 GÜN 20 · 30.10.2026
**Planlanan gün:** 02.11.2026. **Fiilî çalışma:** 30.10.2026 (3 gün erken), görev numarası değişmedi.
**Hizmet #12:** Tahmine Dayalı Analitik — Talep tahmini, müşteri kaybı analizi, fiyat karar desteği, tedarik projeksiyonları. Kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/hizmetler.html).
**İşlem sınırı:** 0 TL peşin. Yalnız DRAFT; dış yayın, merge, kullanıcıya gönderi, insan verisi, ödeme veya yeni hesap yok.
**Kanıt sınıfı:** Hizmet açıklaması gerçek; burada geliştirilen 3 veri ön koşulu örneği KAVRAMSAL/SENTETİK. Gerçek çalışan tahmin motoru, müşteri verisi, doğruluk yüzdesi veya canlı bağlantı kanıtı yok.
## Tur A · 30.10.2026 · Veri ve teknik kaynak kontrolü
1. Kaynak main SHA ve fiyat eşleşmesi: GitHub API ile `index.html`, `surec-analizi.html`, `teklif/e-ticaret-surec-analizi.html`, `rehberler/ai-otomasyon-fiyatlari.html`, `veri/offer-ladder.json` incelendi: PASS (kaynak okuma), P1 fiyat iması açık.
2. Yalnız bir kamuya dönük değişken: Yeni `<details><summary>Talep tahmini için görünen fiyat kesin mi?</summary>...</details>`; JSON-LD, form, CTA ve diğer sayfalar DEĞİŞTİRİLMEDİ. PASS (kod diff).
3. Kapsam: hizmet #12 gerçek hizmet açıklamasıdır, çalışan model kanıtı değildir. Metinde kesin tahmin oranı, ROI, fiyat tahsilatı, mağaza API veya müşteri vaka sonucu bulunmaz. PASS (kaynak iddiası kontrolü).
4. Yanlış pozitif senaryosu: stokta yokluk dönemindeki satış 0 ise talep 0 olduğunu iddia etmemek; eksik zaman damgası varsa model vaadi vermemek. Senaryo kavramsal, hesaplama yapılmadı.
5. Gerçek finans/veri paneli/deney ataması yok: CTR, CTA→lead, gerçek yedi günlük tereddüt, satış, iade, net gelir BİLİNMİYOR. 0 yazma.
6. Test komutu: `python scripts/v8_g20_faq_browser_qa.py` ve GitHub Actions `V8 Day20 Single FAQ Chromium + Before After QA`. İlk çalışmada 12 rotadan 10 normal PASS, 320px'te main ve draft aynı **27px P1 taşma** tespit. Yeni FAQ taşma farkı 0; test karşılaştırma revize edildi; tam sonuç son iş kaydından kontrol edilecek.
7. Canlı HTTP doğrudan bu oturum web erişiminden alınamadı; GitHub kaynak başarı canlı 200 sayılmaz. Dış HTTP bağımsız GET yeteneği varsa ayrıca incele. Form POST asla yapma.
8. Güvenlik: form action, KYC, çerez, IBAN veya ödeme eylemi değişmedi. Peşin harcama 0, dış post 0.
**Teknik GO:** QA tur B, ek P1 ve gerçek tarayıcı sonucu kapısı açık olduğundan HOLD.

## Denetlenebilir kaynaklar
- **GitHub main:** 05bd1f2a31d36fe92134e756e485a104337fbe9f; https://github.com/synapseautomate/synapseautomate.github.io/pull/52 yalnız DRAFT.
- [Hizmet #12 (main)](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/hizmetler.html).
- [Teklif merdiveni (main)](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/veri/offer-ladder.json): 4.900 TL / 24.900 TL / 14.900 TL aylık (güncel hesap/fatura için kesin fiyat değildir); USD 149/750/449 bağımsız USD liste sayıları.
- [Fiyat rehberi](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/rehberler/ai-otomasyon-fiyatlari.html); [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/surec-analizi.html); [e-ticaret teklifi](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/teklif/e-ticaret-surec-analizi.html); [ana sayfa](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/index.html).
- [Tahmin değerlendirmenin kör noktaları / rolling-origin](https://link.springer.com/article/10.1007/s10618-022-00894-5); [stokta bulunmama, satışın talebi eksik göstermesi](https://www.sciencedirect.com/science/article/pii/S0169207023000961).
- [Nike, Rip the Script (2026)](https://about.nike.com/en/newsroom/releases/nike-debuts-rip-the-script-a-step-inside-the-universe-of-nike-football); [Pepsi Football Nation (2026)](https://www.pepsico.com/en/newsroom/press-releases/2026/pepsi-recruits-global-stars-to-create-the-pepsi-football-nation-where-fans-define-the-rules). Yalnız yaratıcı yaklaşım kıyası, görsel veya fikrî mülkiyet kopyalanmadı.


## Gün 20 nihai koşu sonucu — 30.10.2026
- [Gün20 gerçek Chromium browser karşılaştırması run 41033820118](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/41033820118); [12 PNG + JSON kanıt paketi artifact 12967440538](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/41033820118/artifacts/12967440538).
- Komut: `python scripts/v8_g20_faq_browser_qa.py`. **12 render: 10 PASS, 2 BASELINE_P1, 0 yeni başarısız regresyon.** 320px görünümde main ve PR her ikisi de 347px scrollWidth => 27px mevcut yatay taşma. Diğer 375/390/768/1024/1440 genişlikler 10/10 normal PASS. H1=1, eksik img alt=0, gözlenen JS pageerror=0. FAQ mouse click/keyboard Enter testleri ayrıca uygulandı. 320px için **mobil PASS ilan etmiyoruz**.
- [Site Integrity run 41033820097](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/41033820097) SUCCESS; [Release Preflight run 41033820108](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/41033820108) SUCCESS.
- Özgün yeni 3D art'ın ilk sürümünde kompozisyon/kırpma kusuru tespit edilip yeniden render edildi; iki çıktının gerçek boyutları **1920×1080, 1080×1350** ve son SHA-256 sırasıyla **ed705e8c04dcc81d1ae6213ec90f43c9920b6a6bfde6b915ab4e0b53aefc590c** ile **e9f1ef15256e24d2d9763830d5d483714b591d23a24dd1aeff2510020471e3bd**. Yerel dosyalar `/mnt/data/gun20_talep_tahmini/`; GitHub'da public siteye eklenmedi. Resmî marka logo dosyası bu yerel rendera işlenmediği için nihai logolu kreatif/kanal QA HOLD.
- Canlı HTTPS / Safari / gerçek FormSubmit / GA4 / gerçek talep ve satış paneli TEST EDİLEMEDİ / BİLİNMİYOR. Son 7 gün için metrik veya A/B lift çıkarılmadı. Yalnız DRAFT PR #52, dış gönderi yok, ödeme yok.
