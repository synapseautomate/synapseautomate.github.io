# QA A / 22.10.2026 — kaynak ve teknik negatif test
- Github main SHA 6481fd512a68a844e573a9b0d29d3a0f1e45d008; Gün08 PR #24 dalı Upwork açılmama kararı; Gün09 main devir yolu NOT_FOUND; Gün10/11/12 devirleri okundu.
- main veri/offer-ladder.json: site Süreç Analizi 4.900 TRY / bağımsız 149 USD; pilot 24.900 /750; aylık 14.900 /449. Dar kurulum 4.900 TL TEST ve Upwork fiyatı başka şeydir.
- FormSubmit action site kaynak kodunda görüldü; gerçek teslim NOT_TESTED.
- Resmî Upwork katalog onaydan sonra otomatik aktif olabilir: https://support.upwork.com/hc/en-us/articles/360057397533-How-to-create-a-project-in-Project-Catalog . Platform dışı ödeme/iletişim kısıtı: https://support.upwork.com/hc/en-us/articles/360052511833-Get-to-know-each-other-before-a-contract .
- Yerel python galeri_uret_ve_test.py → PASS: dört farklı sentetik R01-R04 bulgusu ve R05 DEĞERLENDİRİLMEDİ; iki 1200x900 4:3 PNG. Mevcut ticari motor bugünkü test DEĞİL.
- Yerel python /mnt/data/qa_stage13.py → yerel bağımsız HTML için 320/375/390/768/1024/1440 Chromium: 6/6 PASS, tek H1, tek CTA, touch 49.9px, odak, taşma yok. Canlı site testi DEĞİL.
- ffprobe: iki MP4 1080x1920 H264 24 fps 12.0s; ilk render logo kırpılması buldu, ikinci render düzeltildi.
- Gerçek Site HTTP, Safari, Lighthouse, FormSubmit teslimi, GA4/GSC, Upwork panel, ödeme/satış ve hukuk TEST EDİLEMEDİ.
- Binary grafik/video ve QA JSON kanıtları ayrıca sohbet ZIP paketinde; bu PR yalnız metinsel kanıt kayıtları. Kaynak Upwork galeri: https://support.upwork.com/hc/en-us/articles/1500011309082-How-to-add-images-and-video-to-your-Project-Catalog-project .