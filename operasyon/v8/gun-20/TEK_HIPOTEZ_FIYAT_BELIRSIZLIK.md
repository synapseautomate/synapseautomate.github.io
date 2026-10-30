# SYNAPSE AUTOMATE · V8 GÜN 20 · 30.10.2026
**Planlanan gün:** 02.11.2026. **Fiilî çalışma:** 30.10.2026 (3 gün erken), görev numarası değişmedi.
**Hizmet #12:** Tahmine Dayalı Analitik — Talep tahmini, müşteri kaybı analizi, fiyat karar desteği, tedarik projeksiyonları. Kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/hizmetler.html).
**İşlem sınırı:** 0 TL peşin. Yalnız DRAFT; dış yayın, merge, kullanıcıya gönderi, insan verisi, ödeme veya yeni hesap yok.
**Kanıt sınıfı:** Hizmet açıklaması gerçek; burada geliştirilen 3 veri ön koşulu örneği KAVRAMSAL/SENTETİK. Gerçek çalışan tahmin motoru, müşteri verisi, doğruluk yüzdesi veya canlı bağlantı kanıtı yok.
## Bir değişken / tek itiraz
**Alıcı rolü:** E-ticaret talep planlama sorumlusu. **Tek karar sorusu:** “Tahmine dayalı analiz için görünen fiyat kesin mi ve veri yetersizse ne olur?”
**Tereddüt sınıfı:** “Fiyat kesin mi?” — gelen gerçek müşteri itirazı DEĞİL, uzman değerlendirmesi hipotezidir. Son 7 gün panel kanıtı yok; test süresinde kullanıcı, form, gelir verisi BİLİNMİYOR.
**Kontrol:** 05bd1f2a31d36fe92134e756e485a104337fbe9f üzerindeki fiyat rehberi FAQ. **Tek değişken:** yalnız mevcut fiyat rehberindeki FAQ listesine **bir** yeni <details> ekle; başka sayfa, CTA, fiyat, form alanı veya tasarım değiştirme.
**Önce:** “Talep tahmini için görünen fiyat kesin mi?” sorusu görünür FAQ bölümünde yok.
**Sonra / doğrudan kamu metni:**
> **Talep tahmini için görünen fiyat kesin mi?**
>
> Hayır. Sitedeki 4.900 TL süreç analizi, 24.900 TL pilot ve 14.900 TL/ay operasyon tutarları yalnız **TEST FİYATI** örnekleridir; kesin satış teklifi, açık ödeme veya kabul edilmiş teslim koşulu değildir. Tahminin kapsamından önce tarihli gerçek talep geçmişi, stokta bulunmama günleri, promosyon ve kampanya dönemleri, iade/iptal ayrımı, eksik veriler ve tahmin ufku değerlendirilir. Yeterli veri yoksa tahmin güvencesi verilmez. Belirsizlik aralığı ve basit bir referans yöntemle kıyaslama tasarlanır; stok/tedarik kararı yetkili insanda kalır. Kapsam, vergi, fatura ve ödeme uygunluğu ayrıca yazılı doğrulanmadan satış başlamaz.

**Ön koşullar:** zaman damgalı gözlem, ürün/birim/kanal tanımı, stokta yokluk etiketleri, promosyon ve olay takvimi, yeterli geçmiş dönemi, hedef tahmin ufku, model dışı test ve dürüst belirsizlik raporu.
**Sentetik iş akışı:** veri sahibinin dönem tablosu → missing/stockout kontrolü → naif baz model → rolling-origin karşılaştırma ve tahmin aralığı → insan onayı → gerekirse gönüllü kapsam talebi. Ürün/entegrasyon yapıldığı iddiası YOK.
**Kapsam dışı:** otomatik sipariş/stok güncelleme, kesin tahmin doğruluğu, getiri garantisi, canlı mağaza API, üçüncü taraf müşteri verisi, kesin fiyat/ödeme.
**Ölçüt hipotezi:** panel erişilirse FAQ sayfasından gönüllü nitelikli talep geçişi; şimdilik BİLİNMİYOR, A/B istatistiği veya uplift YOK.
**Rollback:** yalnız yeni <details>...</details> bloğunu çıkar; görsel fiyatlar, schema, CTA ve form aynı kalır. Diff tek kamu değişkenidir.
**Onay:** WEB-G20-20261030 = ONAY BEKLİYOR; kullanıcının Gün19 onayı Gün20 onayı sayılmaz.

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
