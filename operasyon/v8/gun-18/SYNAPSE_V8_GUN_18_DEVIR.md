# SYNAPSE V8 — GÜN 18 / BAĞIMSIZ DEVİR

**Gerçek tarih:** 27.10.2026 Europe/Istanbul. **Plan tarihi:** 31.10.2026; 4 gün erken uygulandı, gün numarası değişmedi. **Özgün konu:** Süreç Madenciliği — darboğaz ve bekleme haritası. **Tek alıcı/karar sorusu:** Operasyon yöneticisi, “Olay kaydındaki 75 dakika bekleme, kesin süreç hatası mıdır?” sorusunu kanıta göre ele alır. Hayır: mesai, sıra, onay, SLA ve zaman damgası kaynağı yetkili insan tarafından incelenmeden kesin hata denemez.

## 1. Başlangıç, gerçek site kaynağı, önceki günler
- Repo: https://github.com/synapseautomate/synapseautomate.github.io
- Bağımsız görülen `main` SHA: `6de1c4ad10feef1fef37e93d2731dad5e7886574` (25.10.2026, değişmişse yeniden doğrula).
- Draft dal: `draft/v8-gun-18-surec-madenciligi-kanit-20261027`; **Draft PR #47**: https://github.com/synapseautomate/synapseautomate.github.io/pull/47 ; merge edilmedi, canlı yayımlanmadı.
- Gün16 ve Gün17 devirleri ilgili taslak dallarından okundu; Gün16 kaynaklı RAG rehberi, Gün17 AI değerlendirmesi ve optimizasyonu — bu günün süreç olay analizi örneği bunları tekrarlamaz. Gün01–15'in bütün devirleri bağımsız ve tek tek okunmuş varsayılmasın.
- Main `hizmetler.html` hizmet #10: “Süreç Madenciliği: Darboğaz tespiti ve otomasyon fırsatlarının haritalanması.” Hizmet açıklaması, çalışan ürün veya canlı müşteri entegrasyonu kanıtı DEĞİL.
- Mevcut `kanit/teknik-kanit-indeksi.html`, `kanit/ai-otomasyon-kanit-metodolojisi.html`, `kanit/e-ticaret-ai-3-sentetik-vaka.html`, `kanit/100-vaka-ai-guvenilirlik-regresyon-raporu.html` incelendi; bunlardaki başka AI benchmark skorları süreç madenciliği testiyle ilişkilendirilmedi.
- Canlı LinkedIn tüm geçmişine ve yöneticinin istatistiğine tam erişim yok. Metricool bağlı marka etiketi `joinkilory`; 14.10–12.11 penceresinde **9 adet** “INTERNAL DUPLICATE — DO NOT PUBLISH” statülü **draft** gördük; bunlar gerçek yayımlanmış gönderiler DEĞİL, hesap etiketinin SYNAPSE ile eşit olduğu varsayılmadı. Bu oturumda paylaşım/planlama/düzenleme yapılmadı.

## 2. Oluşturulan gerçek branch/PR ve ulaşım yolu
Draft PR #47 içerisinde 9 değişiklikten oluşan içerik:
1. `kanit/surec-madenciligi-bekleme-haritasi.html` — yepyeni erişilebilir amaçlanan açıklama/3 durum/5 kural/human-gate ve görünür SENTETİK etiketi.
2. `hizmetler.html` #10 hizmet kartı → yeni kanıt sayfası bağlantısı.
3. `kanit/teknik-kanit-indeksi.html` → yeni kanıt sayfası bağlantısı.
4. `sitemap.xml` → taslak yeni URL.
5. `public-proof/process-mining-v1/README.md` — komut, ham dosya, kanıt sınırları.
6-8. `public-proof/process-mining-v1/{01_temiz,02_eksik_kolon,03_cakisma_ve_bekleme}.csv` — satırları etiketli sentetik veriler.
9. `public-proof/process-mining-v1/analyze_process.py` — Python stdlib, giriş/çıktısı bağımsız tekrarlanabilir **kavramsal kontrol**, SYNAPSE üretim motoru olarak sunulmaz.
- **Tasarlanan kullanıcı yolu**: Ana sayfa → Hizmetler → Süreç Madenciliği (#10) → kanıt sayfası → public-proof README/komut ve durumlar. Alternatif: Kanıt indeksi → kanıt sayfası. Linkler draft PR içindedir, **henüz ana sitede görünmez**.

## 3. Beş kural ve üç sentetik senaryo
- 01_temiz.csv: 2 kurgusal vaka, 9 olay, `PASS`.
- 02_eksik_kolon.csv: `actor` eksik; `R1_SCHEMA` CSV satır 1, `STOP`.
- 03_cakisma_ve_bekleme.csv: `R4_WAIT` satır 4 (75dk, 30dk **öğretici** eşik, `WARN`); `R3_DUPLICATE` satır 5 (E402 tekrar, `HOLD`); `R5_APPROVAL` satır 8 (C2 kapanış öncesi onay izi yok, `HOLD`); `R2_ORDER` satır 10 (C3 −1dk, `HOLD`).
- Ön koşul: case/event ID, activity, timezone-aware timestamp, rol, süreç sahibi ve bekleme/SLA takvimi; `actor` kayıp ise dur. Negatifler **kesin müşteri hatası, SLA ihlali veya maddi zarar** kanıtı değil.
- Veri yazma, onay verme, müşteri sistemine bağlanma veya gerçek referans gösterimi yok.

## 4. Gerçek test/log/hash/medya — sohbet teslimi
- Yerel tekrar: `python -m unittest discover -s tests -v` **8/8 PASS**, gerçek log `QA/test_log.txt`. Betik örneği: `python analyze_process.py senaryolar/03_cakisma_ve_bekleme.csv --threshold 30`. Kod/CSV/çıktılar `results/` ve `QA/SHA256SUMS.txt` dosyalarında.
- Yerel `analyze_process.py` SHA256: `156a9f2297b66cdb1d1ca4c23d2fa87b19e609161d9fd2cd875f42efe42fb170`. CSV SHA256: temiz `cebcb48449cefa7d6bd9988238e21b6cc1557667c82d87df689cba7dd5fba3a7`; eksik `e90f1cf4d78eb126893952b0c1c75a2a24d4c68953765497ee628b96b6b163c5`; çakışma `a72a02331cfd7e710d655ac365548d3b9e029d2871f82ac9c40c604946276655`.
- Repo dosyaları GitHub blob olarak tekrar okundu, ama repo indirimi + bağımsız SHA256 eşleştirme bu oturumda ayrıca yapılmadı — **repo hash QA açık**.
- Gerçek oluşturulan medya: *kavramsal sentetik animasyon* 32sn/1920×1080 sessiz MP4 ve 25sn/1080×1920 sessiz MP4, her ikisi kaynak kod/test satırlarına dayalı; **ürün ekran kaydı DEĞİL**. Beş 1920×1080 PNG kural kartı, beş 1080×1350 PNG, 5-sayfalık metin seçilebilir LinkedIn PDF, 2 SRT, 3:45 uzun ekran çekimi storyboard+transkript. **3–5dk gerçek ekran YouTube filmi YOK**: yayımlamak YASAK/HOLD.
- Dokuz platforma özgü yazılı caption/alt metin ve formatlar, 11 yöntem dosyası 017/039/071/072/085/138/189/191/194/198/249, kaynak/SEO/PR/QA/onay/metrik devri ayrıca sohbet ZIP tesliminde `operasyon/v8/gun-18/` altında.
- Kullanıcının paylaştığı marka logosu oran korunarak kullanıldı, özgün film tasarımı yapıldı; hiçbir Nike/Pepsi görseli kopyalanmadı. Müşteri/satış/ROI/fiyat veya canlı entegrasyon iddiası yapılmadı.

## 5. Bağımsız iki QA turu
**Tur A / kaynak, hesap ve test:** 8/8 PASS yerel unittest; kural ve CSV satırları ayrı; sentetik etiket CSV/sayfa/kartta; GitHub kaynak statüsü incelendi. Repo dosyalarıyla tam bağımsız SHA256 tekrarına dair sonuç **TEST EDİLEMEDİ**.
**Tur B / marka, grafik, teknik, erişim ve hukuk:** Yerel HTML **PR HTML ile birebir aynı olmayan preview**, Playwright Chromium `set_content` ile 320/375/390/768/1024/1440 genişliklerinde yatay taşma/tek H1 kontrolü 6/6 PASS. MP4 ffprobe/decode PASS, örnek kare contact sheet görsel QA; ilk filmde metin çizgi çakışması görülüp düzeltilerek yeniden render alındı. PDF 5 sayfa, çıktı PNG boyutları ve seçilebilir metin PASS. **Gerçek GitHub PR HTML renderı, canlı 200/404, mobil Safari, gerçek fiziksel cihaz/crop, ekran okuyucu/klavye/contrast full audit, ses kaydı, platform upload ve satır bazlı tüm animasyon kareleri bağımsız QA TEST EDİLEMEDİ.**
- **Açık P0:** Vergi/fatura/KYC, tüketici, ödeme ve dijital teslim teyitsiz → satış ASLA AÇMA. Gerçek müşteri gibi gösterme riski → sentetik etiketi zorunlu, korundu.
- **Açık P1:** gerçek site URL/CI/6 viewport/keyboard/Safari/Lighthouse, medya crop, platform yükleme ve uzun gerçek CLI demo. **WEB teknik yayım HOLD; ticari/sosyal yayım HOLD**.
- P2: gerçek GA4/GSC, backlink/referral, hesap insights ölçümleri bilinmiyor.
- Yerel logo/promosyon ve tasarım disiplini kanıtı, Nike/Pepsi ile eşdeğer kalite sertifikası DEĞİL.

## 6. Metrikler ve onay kapıları
27.10.2026; lokal kanıtlı test PASS **8 test**, negatif rule türü **5**, sorunlu satır **4**, üretilen açıklayıcı MP4 **2 dosya**, PDF **5 sayfa**. Bu oturumda peşin harcama **0 TL**, dış gönderi/DM/e-posta/yayın/merge **0 eylem**. Gerçek trafik, marka araması, nitelikli ziyaret, gerçek demo izlenme/süre, gönüllü kapsam talebi, izinli teklif, fonlanan platform siparişi, tahsil edilen satış, iade ve net gelir **BİLİNMİYOR**; eski 27 günlük sıfır satış yalnız kullanıcı beyanı.
- `WEB-G18-20261027` → PR #47 site merge/canlı yayın **ONAY BEKLİYOR** (önce P1 çöz).
- `LI-G18 / YT-G18 / YTS-G18 / IG-G18 / TT-G18 / X-G18 / TH-G18 / FB-G18 / PIN-G18` → her tarih/platform ayrı **ONAY BEKLİYOR**; video yüklendi/planlandı iddiası yok.
- `BS-ACCOUNT-G18` → Bluesky hesabını resmi https://bsky.app üzerinden **yalnız kullanıcı** açar; öneri @synapseautomate.bsky.social, uygunluğu bilinmiyor; parola/KYC isteme. `BS-POST-G18` ayrı ONAY BEKLİYOR.
- Ödeme, Upwork/Fiverr katalog aktivasyonu, ücretli reklam, dış iletişim, checkout, FormSubmit hesap değişikliği: **YAPILMADI**, yetki verilmedi.

## 7. Resmî kaynak/izleme ve sonraki tek adım
- GitHub PR #47 ve ana sayfa: https://github.com/synapseautomate/synapseautomate.github.io/pull/47 ; https://synapseautomate.github.io/hizmetler.html
- Google canonical: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Google crawlable links: https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- LinkedIn PDF kuralları: https://www.linkedin.com/help/linkedin/answer/a518909
- LinkedIn video: https://www.linkedin.com/help/linkedin/answer/a1311816
- YouTube format/Shorts: https://support.google.com/youtube/answer/1722171 ; https://support.google.com/youtube/answer/15424877
- Bluesky resmî: https://bsky.app/ ; https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial
- 0 gerçek dış bağlantı işlemi, P0/P1 nedeniyle **GÜN18 CLOSED DEĞİL**.

**Gün19'a tek öncelik:** PR #47'deki gerçek dosyaları temiz checkout ile SHA256 yeniden hesaplayıp 6 viewport, erişilebilirlik, 200/404 ve link akışını doğrula; mevcut P1'leri çöz. *Yalnız bunun sonrasında* kullanıcının özel `WEB-G18-20261027` onayını sor. Main merge/sosyal yayın otomatik yapılmaz.
