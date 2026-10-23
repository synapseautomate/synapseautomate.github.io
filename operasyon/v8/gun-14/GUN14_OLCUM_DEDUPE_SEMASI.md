# Gün 14 anonim tekil talep/olay sözleşmesi
| Kaynak olayı | Asgari kayıt | Sayım koşulu | ASLA aynı şey sayma |
|---|---|---|---|
| LinkedIn gösterimi | anonim günlük toplam panel ekranı | görüntüleme | lead |
| GSC organik tıklama | sorgu/sayfa/gün aggregate | tıklama | benzersiz kişi |
| GA4 consentli ziyaret | UTM/sayfa/time aggregated | consent izinli rapor | FormSubmit teslimi |
| Sentetik örnek görüntüsü | gerçek event paneli | görüldüyse demo | satış |
| Site FormSubmit | yetkili teslim id'si ve izinli veri | gerçekten teslim edildi | sadece butona basıldı |
| Services inbound | platform talebi | mesaj gerçek ve gönüllü | soğuk outreach |
| Teklif | kullanıcı izinli yazılı belge | teklif durumu | funded |
| Fonlanan | platform escrow/kontrat makbuzu | funds kanıtı | tahsilat |
| Tahsilat | platform settlement/banka kaydı | net ödeme belgesi | kâr |
| İade | platform veya banka ters işlem | iade dekontu | yeni sipariş |
**Sentetik deduplikasyon negatif testi:** Kurgusal ID `SYN-T-001`: LinkedIn Services ve site FormSubmit iki kanaldan görülürse tek lead olarak say, `first_touch` ve `last_touch` metadata ayrı saklanabilir; gerçek kimlik/parola/API/ödeme detaylarını CSV'ye koyma. Kullanıcı izni ve KVKK sözleşmesi olmadan çapraz-kanal eşleme İŞLETİLMEZ. Gelen gerçek vaka YOK.
**Boş metrik:** HİÇBİRİ otomatik 0 doldurulmaz; panel yoksa `BİLİNMİYOR`, sıfır sadece ekran üzerinden doğrulanmış sıfırsa 0. A sütunundan E'ye kaynak/kanıt güvenini kaydet.
