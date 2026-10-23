# Gün 14 — Kullanıcı/panel gerekli asgari adımlar ve eylem izinleri
**Dış işlemlerden hiçbiri bu oturumda yapılmadı.** Peşin ücretli harcama 0 TL. Dört ayrı gerçeklik sınıfı:
1. **Kaynak kod gerçekliği**: GitHub dosya/PR/CI okunabilir; mevcut hukuki otomasyon motoru veya gerçek müşteri iş akışı değildir.
2. **Kullanıcı beyanı**: Gün13 sosyal/Story B ve site PASS; spesifik post permalink/time/Insights paneli bağımsız değil.
3. **İzinli gelen alıcı**: resmî şirket LinkedIn Services inbox, FormSubmit e-posta, Upwork panel gibi kendi hesap alanlarından yalnız anonimleştirilmiş sayı ve tarih özeti; hesap erişimi yoksa BİLİNMİYOR.
4. **Ödeme/hukuk**: yalnız hesap sahibi + yetkili uzman teyidi. Parola, kimlik, IBAN, gerçek müşteri sözleşmesi isteme.
## Eylem bazlı bağımsız onaylar (hepsi ONAY BEKLİYOR)
| Kod | Eylem | Durum |
|---|---|---|
| `WEB-CTA-TEKDEGISKEN-20261023` | Mevcut süreç analizi sayfasında tek CTA A/B taslağını canlıya almak | ONAY BEKLİYOR, önkoşul/ölçüm de açık |
| `LI-COMPANY-SERVICES-20261023` | LinkedIn Company Services aktivasyon | ONAY BEKLİYOR; kullanıcı hesabında şirket büyüklüğü ve yetki teyit |
| `WEB-HUKUK-BILGI-20261023` | Hukuk bilgi sayfası eklemek (bu gün üretilmedi) | ONAY BEKLİYOR |
| `LI-HUKUK-KART-20261023` | İleride özgün hukuk kanıt kartını LinkedIn şirket hesabından yayımlamak | ONAY BEKLİYOR |
| `YT-HUKUK-A-20261023` | Kavramsal hukuk Shorts storyboard A'dan sonra gerçek medya üretim/yayın | ONAY BEKLİYOR |
| `YT-HUKUK-B-20261023` | Kavramsal hukuk Shorts storyboard B'den sonra gerçek medya üretim/yayın | ONAY BEKLİYOR |
| `CUSTOMER-H14-20261023` | Gerçek gönüllü alıcıya yanıt | ayrıca spesifik içerik/alıcı onayı |
| `MAIN-MERGE-H14-20261023` | Bu günün iç dosyalarını main'e alma | ONAY BEKLİYOR; **varsayılan YAPMA** |
**Önkoşul:** P0 satıcı/fatura/KVKK/gerçek hukuk uzmanı ve platform şartı teyit olmadan ticari iddia YOK. FormSubmit delivered email, GA4/GSC/LinkedIn paneli gerçek belge türü ve tarihle doğrulanmalı. ≥5 doğrulanmış benzersiz inbound kanıtı yoksa dönüşüm oranına başarı etiketi koyma.
