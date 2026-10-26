# AI Sistem İncelemesi — doğruluk, güvenlik, maliyet (eğitim matrisi)
Tarih: 26.10.2026 · Tamamı **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Bu gerçek model çağrısı veya maliyet raporu değildir.

## Tek alıcı sorusu
**Hedef rol:** COO veya BT operasyon sorumlusu. **Problem:** Bir AI asistanının doğru kaynağı kullandığı, kullanıcı yetkisine uyduğu ve ölçümsüz maliyet yaratmadığı nasıl *ön incelemede* anlaşılır? **Ön koşullar:** açık örnek soru, beklenen yetkili belge/sürüm, rol matrisi, insan onayı kararı, sağlayıcı kullanım raporu (varsa).

| Eksen | Minimum kontrol | Kabul sinyali | Kapsam dışı / insan kapısı |
|---|---|---|---|
| Doğruluk | Kaynak kimliği, sürüm, iddia–bölüm eşlemesi | Test vakasıyla ilişkilendirilen dayanak | Yanlış/eksik kaynakta kesin cevap yok |
| Güvenlik | Rol bazlı belge erişimi, dış eylem engeli, talimat manipülasyonu | Yetkisiz içerik gösterilmez | Kapsamlı penetrasyon testi / resmî sertifika verilmez |
| Maliyet | İstek adedi, toplam token, retry/cache, dönem | Gerçek sağlayıcı raporu + yazılı birim fiyat | Kur/komisyon/ROI uydurulmaz |
| İnsan kararı | İstisna sınıfı ve yetkili sorumlu | Durdur/incele/yetkili kabul tutanağı | İş sonucu doğuran kararlar otomatik imzalanmaz |

## Kurgusal vaka testi
A01–A06 sentetik CSV örnekleri. Beklenen güvenli eylemler: A01 PASS; A02/A05/A06 HOLD; A03/A04 STOP. Bu kararlar elle tanımlanmış öğretici politika beklentileridir; **gerçek çalışan AI model testi değildir**.

Maliyet formülü: `tahmini_kullanım_birimi = istek_adedi × (ortalama_girdi_tokenı + ortalama_çıktı_tokenı) × yeniden_deneme_çarpanı`. Fatura maliyeti için doğrulanmış model sağlayıcı tarifesi, input/output ayrımı, önbellek koşulu, kur ve vergiler gerekir; bunlar burada BİLİNMİYOR.

## Örnek teslim/kabul
Teslim: kapsam sayfası, bir test senaryosu tablosu, kaynak/rol matrisi, sınırlamalar, insan onay noktaları ve düzeltme listesi. Kabul: alıcı, her bulgunun kullanılan kaynak ve test koşulunu kontrol eder; yanıltıcı kesinlik yoktur. Entegrasyon, müşteri veri transferi ve otomatik sistem değişimi yok.

Sınır: 6 satırdan evrensel doğruluk, güvenlik veya maliyet kazanımı sonucu çıkarılamaz. Müşteri canlı erişimi ve izinli gerçek veri olmadıkça hiçbir üretim değerlendirmesi tamamlandı sayılamaz.
