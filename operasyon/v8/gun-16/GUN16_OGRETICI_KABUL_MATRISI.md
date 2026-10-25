# Kaynak gösteren yanıt — öğrenilebilir örnek matrisi
**Kitle:** kurumsal bilgi yönetimi/operasyon sorumlusu. **Tek problem:** farklı sürüm veya rol erişimi yüzünden aynı soruya dayanağı belirsiz cevap.
| Adım | Kurgusal girdi | Kabul kriteri | Hatalı durum |
|---|---|---|---|
| 1 Kaynak | KB-OPS-01 | ID/sahip/bölüm tanımlı | yalnız dosya adı |
| 2 Sürüm | v1 ve v2 | güncel v2 | v1 üzerinden karar |
| 3 Yetki | EKIP/KISITLI | İK belgesi genel role kapalı | gizli metin alıntısı |
| 4 Alıntı | KB-OPS-01@v2#3.2 | kritik iddia bölüme dayanır | kaynaksız kesinlik |
| 5 İnsan | çelişki/boş kaynak | BILINMIYOR/INSAN_INCELEMESI | uydurma karar |
**Test komutu:** `python veri/validate_rag_example.py`; repo source test taslağı 5 denetim. **Yerel çalıştırılan ayrı test:** `python PUBLIC_ASSETS/validate_rag_example.py` = 5/5 PASS. Çalışan LLM/retrieval yok. Örnek ücretsiz; şahsi veri/ödeme/form YOK.



**Kaynaklar:** GitHub main 25.10.2026 `4df7e2e7279c9e3f65c7ad1b1fabeb0fb08ff3d1`; `hizmetler.html`, `kaynaklar.html`, `sablonlar/index.html`, `kanit/teknik-kanit-indeksi.html`, `surec-analizi.html`, `iletisim.html`. Resmî teknik: https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation ; https://developers.google.com/search/docs/crawling-indexing/links-crawlable ; https://www.linkedin.com/help/linkedin/answer/a518909 . **Gerçek RAG motoru veya müşteri kanıtı YOK.** 0 TL yeni peşin harcama. Main ve sosyal yayın ONAY BEKLİYOR.
