# QA B — bağımsız okuma, mobil, telif, onay
**Gerçek HTML kontrol:** ilk çalışmada 320/375 px `scrollWidth=380` FAIL; uzun H1 “Kaynağını gösterebilmelisiniz” → “Kaynağı görün” düzeltildi; yeniden 320/375/390/768/1024/1440 **6/6 PASS** (yerel Chromium; GitHub draft HTML'nin Safari eşdeğeri değildir). H1=1, step=5, link-download=2, klavye focus stili var; HTML form/çerez tuzağı yok.
**Kreatif:** ilk kapakta belge resmi logo ile çakışıyordu, grafik alt/sağa taşınıp yeniden PNG+PDF render edildi. Beş PNG'de kullanıcı logosu orantılı, sentetik etiketi, okunabilir mesaj; iç Gün 16/PR/QA notu görünmez. İç QA ayrı klasörde. PDF raster, seçimli metin yok; erişilebilir HTML alternatif var.
**Açık:** gerçek iPhone/Safari, gerçek LinkedIn/Instagram küçültme/crop, canlı 404/FormSubmit/ Lighthouse TEST EDİLEMEDİ. Vergi/fatura/izin kapısı P0 ayrı. Sosyal ve site yayını **ONAY BEKLİYOR**. Yayıma hazır PASS denmedi.



**Kaynaklar:** GitHub main 25.10.2026 `4df7e2e7279c9e3f65c7ad1b1fabeb0fb08ff3d1`; `hizmetler.html`, `kaynaklar.html`, `sablonlar/index.html`, `kanit/teknik-kanit-indeksi.html`, `surec-analizi.html`, `iletisim.html`. Resmî teknik: https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation ; https://developers.google.com/search/docs/crawling-indexing/links-crawlable ; https://www.linkedin.com/help/linkedin/answer/a518909 . **Gerçek RAG motoru veya müşteri kanıtı YOK.** 0 TL yeni peşin harcama. Main ve sosyal yayın ONAY BEKLİYOR.
