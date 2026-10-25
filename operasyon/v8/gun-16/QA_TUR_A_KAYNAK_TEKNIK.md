# QA A — teknik + veri negatif test
**Fiilen yürütülen:** `python build.py`, `python PUBLIC_ASSETS/validate_rag_example.py`, `python qa_test.py` (yerel kanıt ZIP içinde). İlk komut dosyaları üretti; 5/5 deterministik test PASS; beş PNG 1080×1350; PDF 5 sayfa/540×675pt ve PDF tekrar render 1080×1350 gerçek test. Canlı RAG retrieval/LLM testi **YAPILMADI**.
**Negatifler:** (T01) güncel v2 var; (T02) eski v1 dışarıda; (T03) KISITLI İK belge ekip rolünden hariç; (T04) kaynak yoksa BİLİNMİYOR; (T05) kaynak içeriğinden komut yürütme yok/insan incelemesi.
**İddia ve platform:** `hizmetler.html` gerçek hizmet tanımı; müşteri kurulumu/gelir/ISO/ROI/otomatik hukuk kararı yok; Microsoft RAG belgesi yalnız mimari ve risk düzeyi. LinkedIn 5 sayfa, 0.8 MB civarı, resmî 100 MB/300 sayfa sınırında. Gerçek LinkedIn yükleme kabul testi **YAPILMADI**. 
**Kaynak QA sonucu:** yerel materyal teknik üretim PASS; gerçek model, canlı ödeme/KVKK ve kanal paneli TEST EDİLEMEDİ.



**Kaynaklar:** GitHub main 25.10.2026 `4df7e2e7279c9e3f65c7ad1b1fabeb0fb08ff3d1`; `hizmetler.html`, `kaynaklar.html`, `sablonlar/index.html`, `kanit/teknik-kanit-indeksi.html`, `surec-analizi.html`, `iletisim.html`. Resmî teknik: https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation ; https://developers.google.com/search/docs/crawling-indexing/links-crawlable ; https://www.linkedin.com/help/linkedin/answer/a518909 . **Gerçek RAG motoru veya müşteri kanıtı YOK.** 0 TL yeni peşin harcama. Main ve sosyal yayın ONAY BEKLİYOR.
