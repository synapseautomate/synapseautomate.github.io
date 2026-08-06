# VELA spec_v1 — saha notundan kontrollü teklif taslağı

## Amaç
Saha çalışanının kısa notunu yapılandırılmış teklif taslağına dönüştürmek; eksik kritik alanı uydurmamak ve dış eylemden önce insan onayı istemek.

## Input
- Serbest metin veya transkript
- Müşteri adı (varsa)
- Kalem/hizmet
- Miktar
- Termin
- Kaynak bilgisi

## Output şeması
`customer`, `item`, `quantity`, `deadline`, `price`, `currency`, `source`, `warnings`, `approval_state`.

## Kurallar
1. Fiyat kaynağı yoksa `price=unknown`.
2. Para birimi belirtilmemişse tahmin edilmez.
3. Miktar sayı değilse insan incelemesine gider.
4. Termin belirsizse netleştirme gerekir.
5. Teklif gönderimi otomatik değildir.
6. Dış e-posta/ödeme/sözleşme insan onayı olmadan yapılmaz.

## Non-goals
- Otonom fiyat belirlemek
- Müşteriye otomatik teklif göndermek
- Vergi/hukuk yorumu yapmak
- Onaysız CRM/ERP yazma işlemi

## Clarification soruları
1. Fiyat hangi onaylı kaynaktan alınacak?
2. Termin kesin tarih mi, yaklaşık ifade mi?
3. Teklifi kim onaylayıp gönderecek?

## 10 edge case
1. Müşteri adı yok
2. İki farklı miktar geçiyor
3. Para birimi yok
4. Fiyat yok
5. “Cuma” tarih bağlamı belirsiz
6. Ses transkriptinde sayı hatası
7. Aynı not iki kez yüklendi
8. Birden fazla hizmet kalemi
9. Uygunsuz/kişisel hassas bilgi
10. Acil ibaresi var fakat yetkili belirtilmemiş

## 5 kesin failure
1. Kaynaksız fiyatı kesin değer olarak üretmek
2. Çelişkili miktarı sessizce seçmek
3. Onaysız dış gönderim yapmak
4. Hassas veriyi gereksiz loglamak
5. Kritik uyarıyı kullanıcıya göstermemek

## Acceptance criteria
### Makinece
- Zorunlu alanlar validate edilir
- Unknown alanlar explicit
- 5/5 failure testi fail-closed
- Teklif gönderim endpoint'i yok

### İnsan rubric
- Kaynak anlaşılır mı?
- Belirsizlik görünür mü?
- Düzeltme kolay mı?
- İnsan devri doğru noktada mı?
- Çıktı müşteriye gönderilmeden önce onaylanabilir mi?
