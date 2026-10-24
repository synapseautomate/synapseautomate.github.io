# B2B örnek müşteri sunumu — 1 sayfa
**SYNAPSE Automate | Operasyon Veri Görünürlüğü**
**Durum:** İç taslak. Müşteri referansı veya gerçekleşmiş proje değildir.

## Sorun
Birden çok kanaldan gelen sipariş ve stok tablolarında manuel kontrol, eksik SKU, yinelenen kayıt ve farklı stok zamanları yüzünden operasyonel belirsizlik yaratabilir.

## Yaklaşım
**Keşif (20 dk)** → **veri şeması eşleştirme** → **kontrol kuralları** → **önceliklendirilmiş bulgu raporu** → **ekip değerlendirmesi**.

## Sentetik demo
6 örnek satırda 7 kural eşleşmesi: stok açığı, negatif stok, mükerrer kayıt, eksik SKU ve sevkiyat/stok çelişkisi. Bunlar müşteri sonucu veya finansal tasarruf iddiası değildir.

## Teslimatlar
- Yönetici özeti: risk ve operasyon önceliği
- CSV bulgu listesi: satır, sipariş, SKU, kural ve açıklama
- Kural sözlüğü ve veri kalitesi notları
- Kapsam dahilinde aksiyon önerileri

## Başlangıç için gerekenler
Örnek CSV kolon başlıkları, veri hacmi aralığı, stok zamanlaması, depo ve sipariş statüleri, kabul sorumlusu.

## Güvenlik yaklaşımı
İlk demo tamamen sentetik veriyle yapılır. Gerçek veri için gizlilik, erişim, saklama ve silme koşulları ayrıca kararlaştırılır.

## Sonraki adım
İhtiyaç analizi sonrası kapsam, takvim ve teklif taslağı hazırlanır. Henüz bağlayıcı ticari teklif sunulmamaktadır.
