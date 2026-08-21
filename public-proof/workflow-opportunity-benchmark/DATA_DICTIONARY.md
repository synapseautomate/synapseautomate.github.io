# Data Dictionary

`veri/gun4-workflow-inventory-public.csv` alanları:

| Alan | Anlamı | Public güvenlik kuralı |
|---|---|---|
| `kategori` | Operasyon alanı | Kişi/şirket adı içermez |
| `is_akisi` | Tekrarlı sürecin adı | Müşteri vakası gibi sunulmaz |
| `girdi` | Karar öncesi bilgi/olay | Hassas veri örneği içermez |
| `karar` | Verilecek operasyon kararı | Otonom kritik karar iddiası yok |
| `cikti` | Karar sonrası çıktı | Sonuç garantisi değildir |
| `ekonomik_sonuc` | Ekonomik etkinin yönü | ROI rakamı/garantisi değildir |
| `owner` | Süreç/karar sahibinin rolü | Gerçek kişi adı içermez |
| `human_gate` | İnsan onayı gereken nokta | Kritik eylem insanda kalır |

## Evidence boundary

Bu veri seti sentetik ve iş-akışı seviyesindedir; gerçek müşteri performansı değildir, kişisel veri/iletişim bilgisi içermez ve satış/ROI garantisi vermez.
