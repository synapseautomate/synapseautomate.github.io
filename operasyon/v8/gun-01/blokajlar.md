# V8 Gün 01 — P0/P1/P2, sahip ve durum
**Açık P0: 6; P1: 3; P2: 1 (bu denetimin operasyonel sınıflandırması).**
| ID | Sev. | Gerekçe | Çözüm/eşik | Sahip | Durum |
|---|---|---|---|---|---|
| P0-01 | P0 | Satıcı/vergi/fatura faaliyeti güncel teyit yok | Mali müşavir/GİB + hesap sahibi resmî panel doğrulama | Hesap sahibi/mali müşavir | AÇIK |
| P0-02 | P0 | KYC/ödeme/IBAN/gerçek sandbox ve mali koşullar teyitsiz | Ayrı Upwork/MoR hesap kabulü, komisyon, güvenli ödeme | Hesap sahibi | AÇIK |
| P0-03 | P0 | İki ayrı CSV ile ürün kabul/negatif test kanıtı yok | Gerçek sentetik test ve iki dosya sözleşmesi | Teknik | AÇIK |
| P0-04 | P0 | Teslim/hash/sürüm/iade/SOW kabul kanıtı yok | Test edilmiş dijital teslim ve B2B kabul şartları | Teknik + hesap sahibi | AÇIK |
| P0-05 | P0 | GitHub Pages ticari hosting politikası ve canlı fiyat/CTA ayrımı riski | Checkout Pages'te değil, uygun hosting/metin ve kullanıcı onayı | Teknik + marka | AÇIK RİSK |
| P0-06 | P0 | GA4/FormSubmit çerez ve KVKK canlı izin zinciri denetlenemedi | Aydınlatma/rıza ve gerçek ağ/form testi | Teknik + hukuk | AÇIK RİSK |
| P1-01 | P1 | 320/375/390/768/1024/1440 mobil/desktop gerçek render yok | Gerçek viewport ve accessibility/Lighthouse QA | UX | TEST EDİLEMEDİ |
| P1-02 | P1 | Canlı hizmet fiyatı ile V8 TEST fiyatı karışabilir | Fiyat/CTA kapsamında açık ayrım | Marka | AÇIK |
| P1-03 | P1 | LinkedIn Services/admin analitik belirsiz | Hesap sahibinin panel teyidi | Hesap sahibi | TEST EDİLEMEDİ |
| P2-01 | P2 | İç huni diyagramı görsel değil, matrise döküldü | Daha sonra yalnız izinli iç tasarım | Tasarım | AÇIK |

P0/P1 varken teknik yayına hazır **HAYIR**, ticari satışa hazır **HAYIR**. Eksik kanıt *aktif ihlalin veya ödeme reddinin ispatı değildir*.
