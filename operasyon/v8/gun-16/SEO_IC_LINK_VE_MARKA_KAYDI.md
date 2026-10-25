# Kaynak, iç bağlantı ve marka kontrolü
**Önce:** `hizmetler.html` Kuruma Özel Yapay Zekâ ve Bilgi Tabanı kartı açıklaması var; yardımcı kaynak linki yok.
**Sonra (yalnız draft):** bu karta `<a class="more" href="rehberler/kaynak-gosteren-rag-bilgi-tabani-rehberi.html">Kaynak gösteren yanıt için 5 kontrolü öğren</a>` eklendi. Zincir: Ana sayfa → Hizmetler → kurumsal bilgi tabanı → rehber → iki CSV. `kaynaklar.html` ve `kanit/teknik-kanit-indeksi.html` farklı sorulara cevap veriyor; yeni rehber kaynak/sürüm/yetki özelinde ve kopya sayfa değil.
**Yerel HTML:** Chromium `qa_test.py` ile 320/375/390/768/1024/1440 6/6 PASS; ilk sürüm 320/375 H1 taşma FAIL ve başlık kısaltılıp düzeltildi. `main` canlı HTTP/Safari/Lighthouse TEST EDİLEMEDİ. User-provided logo karelerde ölçek oranı korunmuş; gerçek RAG arayüzü yok; marka isminde slash yok. İndir URL'si yayın olana kadar canlı değildir.
**Google:** Düz `<a href>` iç link kullanımı resmî öneriyle uyumlu, `Dataset` JSON-LD eklenmedi; Rich Results/indeksleme garanti yok.



**Kaynaklar:** GitHub main 25.10.2026 `4df7e2e7279c9e3f65c7ad1b1fabeb0fb08ff3d1`; `hizmetler.html`, `kaynaklar.html`, `sablonlar/index.html`, `kanit/teknik-kanit-indeksi.html`, `surec-analizi.html`, `iletisim.html`. Resmî teknik: https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation ; https://developers.google.com/search/docs/crawling-indexing/links-crawlable ; https://www.linkedin.com/help/linkedin/answer/a518909 . **Gerçek RAG motoru veya müşteri kanıtı YOK.** 0 TL yeni peşin harcama. Main ve sosyal yayın ONAY BEKLİYOR.
