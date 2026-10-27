# SYNAPSE V8 Gün 11 — YouTube Shorts üretim ve yayın öncesi devir

**Tarih:** 20.10.2026 · Gün 11, plan tarihi 24.10.2026 · **KULLANICI İSTEĞİ:** YouTube gönderisi 1920×1080 yatay değil **1080×1920 Shorts** olacak. Yayın yetkisi verilmedi, hesap sahibinin ayrı onayı şart.

## Gerçek oluşturulan kullanıcı teslimi (bu PR'a video binary taşınmadı)
1. `SYNAPSE_SHORTS_A_500TL_KARAR_KAPISI_1080x1920.mp4`: 27,005 sn, 24 fps, H.264/AAC stereo, 500 TL sentetik mutabakat farkının karar olmaması.
2. `SYNAPSE_SHORTS_B_GERCEK_FINANS_ARACI_1080x1920.mp4`: 24,009 sn, 24 fps, H.264/AAC stereo, gerçek mevcut finans web aracındaki sentetik 0/8→8/8 adımlarının tarayıcı ekranından belgelenmiş işaretlemeleri.
3. Her iki Shorts için resmî logo kullanılan dikey PNG kapak (1080×1920), ayrı hazır YouTube başlık/açıklama metni, Türkçe SRT içerik transkripti.
4. `SYNAPSE_GUN11_SHORTS_TAM_YAYIN_TASLAGI.zip`: kullanıcının bu sohbetindeki dosya teslimi; içeride PUBLIC_ASSETS ve INTERNAL_OPERATIONS ayrı.

## Kaynak ve ürün doğruluğu
- Resmî logo: `assets/brand/synapse-logo-clean.png` — orijinal görüntü, deformasyon YOK; Inter font yerel sistemden OFL esaslı raster çıktıya işlendi, font dosyası pakete eklenmedi.
- Çalışan gerçek araç: https://synapseautomate.github.io/araclar/finans-surec-kontrol-listesi.html . PR #33'ün kaynak Playwright kontrolü 8 gerçek checkbox durumunu doğrular. Gerçek işlem, banka, fatura programı veya ERP entegrasyonu değildir.
- Fatura bilgisi sayfası: https://synapseautomate.github.io/cozumler/fatura-on-isleme-mutabakat-kontrolu.html ; örnek 12.500 − 12.000 = 500 TL fark tamamen SENTETİK.
- Her sahnede `SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL` görünür, gerçek müşteri gösterilmez.

## QA A — Dosya/doğruluk
- Her iki gerçek MP4: 1080×1920, 24 fps, H.264, yuv420p, AAC stereo, `ffmpeg -xerror -i VIDEO -f null -` **EXIT 0**.
- Ses yalnız yerel sentez; başka markaların lisanslı müziği, stok sahne veya yapay müşteri/ürün ekranı yok.
- A maksimum ses: -11,1 dBFS; B: -11,5 dBFS; kırpılma >0 dBFS YOK.
- Her video, logo, kapak ayrı gerçek dosya. Zip `testzip()` PASS.
- HTML sayfa/sitemap/CTA ölçüm güncellemesi ayrı `main` PR32/34 ile yapılmıştı; bu medya PR'ı bunları tekrar merge etmez.

## QA B — Görsel/motion
- 20 farklı video zamanında kare açılıp yan yana incelendi.
- İlk B UI kesitinde uzun Türkçe soru ve başlıklar **KESİLİYORDU (FAIL)**. Kaynağın gerçek checkbox kutu koordinatlarına göre 8 ayrı soru dikdörtgeni tekrar crop edilerek **DÜZELTİLDİ**; son ekran örnekleri tam soru metnini ve gerçek checkbox durumunu koruyor.
- Native 1080×1920 cover/son fotoğraflar ve küçültülmüş 270×480 inceleme oluşturuldu. Resmî logo orantısı, CTA, Türkçe karakterler, sentetik açıklama gözle denetlendi.
- **NOT TESTED:** Fiziksel telefon üzerinde Shorts arayüz bindirmesi / nihai YouTube platformu canlı oynatım / kullanıcı cihazı ses deneyimi ve izinli yayın. Bunları PASS olarak yazma.

## Benchmark
- B2B ürün görsel hiyerarşisi için Linear'ın kaynakla belgelenen 2026 tasarım yaklaşımı incelendi: https://linear.app/now/behind-the-latest-design-refresh .
- Resmî Shorts biçimi: https://support.google.com/youtube/answer/12779649 .
- Nike/Red Bull/Linear eşit kalitedeyiz sonucu iddia edilmez, kimlikleri kopyalanmadı.

## Yayın durumu / devir
**YouTube SHORTS A: ONAY BEKLİYOR, B: ONAY BEKLİYOR.** `main`e PR33 merge YOK; YouTube/Facebook/Instagram'a otomatik post YOK.
**Gün 12 tek sonraki adım:** Hesap sahibi onay verirse her Shorts'un YouTube uygulaması içinde kapak safe-area, açıklama URL, ilk 2 saniye, altyazı ve ses kontrolünü yapıp ayrı yayın kararı almak. Google gerçek gösterim, tıklama, müşteri/satış metrikleri BİLİNMİYOR.
