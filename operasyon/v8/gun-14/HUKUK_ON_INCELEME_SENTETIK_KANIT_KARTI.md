# Hukuk ve Uyum — sözleşme maddesi çıkarımı: ön inceleme
**SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**
**B2B hedef rol:** hukuk operasyon sorumlusu / sözleşme koordinatörü. **Tek karar sorusu:** “4 örnek maddede gizlilik, fesih ve veri silme ifadeleri nerede geçiyor; hangi kayıt uzman incelemesine gitmeli?” **Hukuki yorum değil.**
**Gerçek kaynak:** main `hizmetler.html` “Hukuk & Uyum: sözleşme ön inceleme, madde çıkarımı, doküman sınıflandırma ve insan onayı”; `sektorler/hukuk.html` insan denetimli kontrollü hukuk iş akışları; `rehberler/ai-otomasyonunda-insan-onayi.html`. Bunlar mevcut çalışan ticari sözleşme motoru kanıtı değildir.
**Ön koşullar:** İçerik hak sahibi izni; kişisel veri/gizli gerçek sözleşme yok; sözleşme tipi ve uzman onay rolü yazılı tanımlı; PDF imza/ek/tablolar ve OCR bu sentetik metin taramasının kapsamı DIŞINDA.
**Sentetik iş akışı:** 4 uydurma madde → yalnız anahtar kelime eşleşmesi → referans madde ID + anahtar etiket → **UZMAN_INCELEMESI_GEREKLI** → avukat/hukuk birimi yorumlar → yayın, sözleşme bağlayıcılığı, imza veya otomatik onay YOK.
| İcat edilmiş satır | Basit işaret | İnsan kararı |
|---|---|---|
| M-01 “gizli bilgi” | GIZLILIK_IFADESI | gerekli |
| M-02 “fesih” | FESIH_IFADESI | gerekli |
| M-03 “veri silme talebi” | VERI_SILME_IFADESI | gerekli |
| M-04 eşleşmeyen diğer şart | bayrak YOK (uygun anlamına gelmez) | gerekli |
**Gerçek sentetik test:** `python -m unittest -v test_sozlesme_anahtar_kontrol_SENTETIK.py` → 7/7 OK 23.10.2026. Pozitif demo `python sozlesme_anahtar_kontrol_SENTETIK.py` → 4 kayıt ve her kayıt `legal_conclusion:null`; e-posta ve 11 haneli kimlik görünümlü değer negatif testte bloklandı. CLI/Python gerçek ticari ürüne ait değil; yalnız bu günün iç prototipi.
**Kapsam dışı:** hukuki danışmanlık, geçerlilik/uygunluk skoru, imza, önerilen sözleşme dili, yargılama, dava tahmini, özel veri, real-time DMS/CRM entegrasyonu, otomatik sözleşme onayı, ROI.
**Telif/gizlilik:** özgün sentetik Türkçe metin, gerçek şirket/müşteri/sözleşme yok. KVKK veri minimizasyonu kaynağı: https://www.kvkk.gov.tr/Icerik/4189/Kisisel-Verilerin-Islenmesine-Iliskin-Temel-Ilkeler .
**Tek CTA taslağı (yayınlanmadı):** “Ön inceleme kapsamının uygunluğunu sorun” → var olan `iletisim.html#contact-form`; gizli sözleşme göndermeyin.
