# Veri Akışı ve Roller v1

## Referans veri akışı

`Onaylı kaynak -> minimum veri hazırlığı -> model/kural değerlendirmesi -> doğrulama kapısı -> insan yetki kapısı -> yetkili eylem -> karar/kanıt kaydı`

Bu kamuya açık bir referans modelidir; her projenin aynı sistemleri kullandığı anlamına gelmez. Proje özelindeki sistemler, alanlar, saklama ve erişim SOW/onboarding sırasında tanımlanır.

## Roller

| Rol | Sorumluluk | Yetki sınırı |
|---|---|---|
| İş sahibi | Hedef, iş sonucu, kapsam önceliği | İş hedefini ve kabul kriterini onaylar |
| Veri sahibi | Kaynak, izin, hassasiyet, kullanım sınırı | Veri erişimi/paylaşımını onaylar |
| Süreç sahibi | Kurallar, istisnalar, mevcut adımlar | Operasyonel kural ve istisnayı onaylar |
| Yetkili onay sahibi | Yüksek etkili veya geri dönüşü zor kararlar | Onay / ret / durdurma |
| Synapse Automate | Kapsam içi tasarım, test, ölçüm ve işletim | Kapsam dışı veya müşteri adına nihai yetki üstlenmez |

## Minimum veri kuralı

Kamuya açık talep formu süreç metadatası ister; sır veya müşteri seviyesinde hassas veri istemez. Parola, API anahtarı, ödeme verisi ve gizli müşteri dosyaları kamu formlarına gönderilmemelidir.
