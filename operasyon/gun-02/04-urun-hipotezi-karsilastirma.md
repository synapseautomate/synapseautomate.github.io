# GÜN 02 | Tek dar ürün hipotezi ve alternatif seçim kararı
**Tarih:** 2026-10-14 · **Durum:** ÜRÜN HİPOTEZİ SEÇİLDİ / TALEP ve SATIŞ DOĞRULANMADI
**Kaynak:** V6 MAX Gün 02; önceki devir: https://github.com/synapseautomate/synapseautomate.github.io/pull/10

## Bir cümle (onay öncesi)
**Sipariş ve stok CSV dosyalarındaki stok açığı, negatif stok, boş SKU ve yinelenen sipariş-SKU satırları gibi tanımlı tutarsızlıkları cihazda işaretleyen kontrol paketi.**

## Seçim tablosu (göstergeler yalnız mantıksal hipotez, ölçülmüş pazar verisi değil)
| Ürün hipotezi | Daraltılabilir ve test edilebilir sorun | Veri/gizlilik | Tekrar edilebilirlik | Bağlı maliyet ve teslimat | Karar |
|---|---|---|---|---|---|
| **H1 Sipariş/stok CSV uyuşmazlığı** | Boş SKU, yinelenen satır, negatif stok, sipariş>stok ve durum uyumsuzluğu için satır bazlı kural/çıktı | Yerel çalışacak tasarım; gerçek veri izinsiz alınmaz | Deterministik CSV kontrol ve sentetik test örneği var (Gün 01 PR) | Tam ürün UX/onboarding ve iki-CSV şema sözleşmesi henüz yok | **TEK BİRİNCİL HİPOTEZ** |
| H2 Haftalık Excel/Sheets rapor otomasyonu | Belirsiz kaynak/ölçümler, daha geniş kapsam | Genellikle hesap bağlantısı veya bulut izni gerekir | Müşteriye göre değişir | API/kurulum ve bakım ihtiyacı olası | PARK ET — yeni ürün yok |
| H3 Genel sipariş hata kontrolü | Sorun ve hata taksonomisi H1'e kıyasla geniş | Sipariş kişisel veri içerebilir | Kural seti henüz dar değil | Yanlış pozitif ve hassas veri riski | PARK ET — yeni ürün yok |

## Başlangıç kapsamı (ürün sözleşmesi Gün 03'te dondurulacak)
- Minimum kullanıcı girdisi: CSV UTF-8 / UTF-8 BOM; uygun başlıklar; mümkün olduğunca kimliksiz/sentetik test.
- Hata raporu alanları: satır no, sipariş kodu, SKU, kural kodu, açıklama.
- **Kontrol adayları:** R01 sipariş adedi > stok adedi, R02 stok < 0, R03 aynı sipariş kodu + SKU tekrar, R04 SKU boş, R05 sevk edilmiş + negatif stok (inceleme işareti), R00 sayısal tip bozuk, R06 sipariş kodu boş, R07 sipariş adedi negatif.
- **Semantik risk:** Stok adedi sipariş öncesi/sonrası olabilir; depo birimi ve zaman penceresi farkı yanlış pozitife yol açabilir. Uyarı = kesin hata/parasız zarar değildir.
- **Şema açıklığı:** PDF Gün 03 iki CSV (sipariş ve stok), Gün 01 prototipi birleşik tek CSV kabul ediyor. **P1 ürün gereksinimi uyumsuzluğu**: Day03 veri eşleme tasarımında çözülmeden dosya “indirilebilir satış ürünü” olamaz.

## Kesin kapsam dışı
- Mağaza, pazaryeri, ERP, ödeme, e-fatura veya envanter API bağlantısı **YOK**.
- Sisteme otomatik stok değişikliği, iptal, sevk etme veya fiyat müdahalesi **YOK**.
- Finansal tasarruf, hata yakalama yüzdesi, “tüm siparişleri doğru analiz eder” ve satış artışı garantisi **YOK**.
- Gerçek kişi verisi sisteme veya üçüncü taraflara gönderilmek zorunda **DEĞİL**.
- SLA, büyük hacim, özelleştirilmiş iş kuralı, uzaktan kurulum, veri göçü ve destek **temel ürünün otomatik parçası değil**.

## Ürün mimarisi ve B2B sapmasının kaydı
**PDF önceliği:** 1) indirilebilir yerel araç; 2) yalnız müşteri talebiyle dar kurulum; 3) isteğe ve uygunluk kapılarına bağlı analiz/pilot.
**Hesap sahibinin önceki tercihi:** Kurumsal B2B hizmeti birincil satış kanalı olarak konumlamak. Bu tercih iptal edilmedi; PDF'nin indirilebilir ürünü ile **çelişen ticari öncelikler** olarak şeffaf biçimde birlikte kaydedildi. Teknik temel aynı kural motoru olabilir; bugün müşteri veya ürün satışı yapılmaz.
**Bir sonraki karar:** Gün 03 iki kaynak CSV sözleşmesini ve 5 çekirdek kuralı doğrulanabilir kabul testine bağlayacak. Ürünün ticari sunulma şekli satış öncesi ayrıca hesap sahibinin kararı ve yasal uygunlukla netleşecek.
