# Yöntem 116 — Bilgi kazancı

Çoğu genel “RAG nedir?” sayfası yerine **aynı soruda eski v1/güncel v2 kaynak farkı**, kısıtlı rol ve kaynaksız cevap senaryolarını birlikte doğrulanabilir eğitim nesnesi hâline getir. Girdi: 5 kurgusal belge envanteri ve 5 kabul testi. **Üç özgün öğrenim:** (1) eski sürüm kesin cevap veremez; (2) yetkisiz belge doğru görünen yanıtta bile kullanılamaz; (3) “bilmiyorum” güvenli ve kabul edilebilir çıktıdır. Gerçek müşteri vakası ya da RAG model sonuç metriği DEĞİL.

**Kaynak / tarih:** 25.10.2026, main `4df7e2e7279c9e3f65c7ad1b1fabeb0fb08ff3d1`; gerçek hizmet `hizmetler.html` kuruma özel bilgi tabanı kartı; `kaynaklar.html`, `sablonlar/index.html`, `surec-analizi.html`. https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation . **Yalnız sentetik örnek; canlı RAG/gerçek müşteri/satış YOK.** Sorumlu: SYNAPSE operasyon. Gerçek metrik BİLİNMİYOR; yayın WEB-G16-RAG-20261025 ONAY BEKLİYOR.
