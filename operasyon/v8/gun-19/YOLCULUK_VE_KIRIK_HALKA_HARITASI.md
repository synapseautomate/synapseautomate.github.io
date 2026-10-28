# Gün 19 | Ziyaretçi → Kapsam → Gönüllü talep
**28.10.2026 (plan 01.11.2026, 4 gün erken)**. Başlangıç SHA `b2db84e1db00e4acbf0a6882e66c4b55643a113d`. Şu an yalnız draft #49.

## Önce / sonra kullanıcı rotası
| Adım | Önce main | Sonra draft | Kanıt |
|---|---|---|---|
| 1 | `index.html` → `hizmetler.html` | Aynı | GitHub kaynak, taranabilir href |
| 2 | Hizmet #11 Sesli AI kartı yeni derin bağlantı içermiyordu | `cozumler/sesli-yapay-zeka-randevu-insan-devri.html` doğrudan hizmet kartından | DRAFT kaynak ve 6 genişlik Chromium |
| 3 | Sesli AI için randevu/human handoff kapsam sayfası yok | 3 kavramsal sentetik durum, gerçek sınırlar, tek CTA | DRAFT sayfa + 6 viewport |
| 4 | İletişim formunda konuyla ilgili seçim yok | `iletisim.html?konu=sesli-yapay-zeka` → konu otomatik seçiliyor | Gerçek yerel browser PASS |
| 5 | Genel süreç formu üçüncü taraf aktarım rızası istemiyordu | Zorunlu checkbox ve gizlilik linki | Gerçek yerel browser PASS |
| 6 | FormSubmit üçüncü taraf, alıcı inbox teslimi belirsiz | Aynı, hiçbir kullanıcı/test datası gönderilmedi | BLOKE / gerçek teslim BİLİNMİYOR |
| 7 | `talep-alindi.html` var ama gerçek submit kanıtı değil | Aynı | Kaynak PASS; gerçek akış BİLİNMİYOR |
| 8 | Fiyat, checkout, fatura, dijital teslim | Resmî teyit eksik | NO-GO; ödeme testi yapılmadı |

## İnsan devri ve ön koşullar
Tek sorun: çağrı operatörü talebin randevu, bölüm yönlendirme ya da hassas istisna olup olmadığını bilsin; otomatik kesinleştirme yapılmasın.
Hedef rol: çağrı merkezi operasyon yöneticisi.
Ön koşul: niyet ağacı, çalışma saatleri, temsilci uygunluğu, takvim yetkisi, KVKK açıklaması, çağrı kaydı hukuku. İnsan onayı: randevu kesinleşmesi, şikâyet, hassas talepler. Kapsam dışı: canlı ses botu / arama API / CRM / gerçek müşteri ses kaydı / sıralama veya doğruluk garantisi.
Üç senaryo: (1) randevu — müsaitlik teyitsiz söz verilmez; (2) destek — departmana yönlendirme önerisi; (3) hassas istek — insana devret.
**SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL.**

## Kırık halkalar
- P0: ticari hazır olma / gerçek ödeme kanıtı yok; işlem kapalı.
- P1: gerçek canlı HTTP ve FormSubmit→inbox→onay zinciri test edilemedi; satış dönüşümü PASS sayılamaz.
- P1: genel süreç analizinde test fiyatları daha önce canlı fiyat gibi görünüyor; draftta TEST FİYATI etiketi ve Offer schema kaldırıldı. Diğer kamu fiyat sayfaları bütünsel denetim bekliyor.
- P2: GA4 rıza akışının gerçek ağ waterfall'u ve Search Console erişimi yok.

## İzleme
Tüm URL'ler ve mevcut kaynaklar GitHub main SHA ile sabitlendi. Ekranlar: GitHub Actions [run 40659256869](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659256869); 42/42 yerel Chromium QA PASS. Canlı 200 ve Safari sonucu için yeni HTTP/önce-sonra denemesi ayrıca gereklidir.
Rollback: taslak yayına alınmadığından canlı geri alma yok. Daha sonra merge onayı verilirse yeni sayfa, hizmet href, iletişim konu seçimi ve sitemap revert edilebilir. Form rıza düzeltmesinin kaldırılması ayrıca gizlilik riski değerlendirmesi ister.
