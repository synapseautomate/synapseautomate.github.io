# SYNAPSE Automate | E-ticaret Operasyon Veri Kontrolü
**Durum:** İç taslak; henüz kamuya yayımlanmadı.

## Hedef
Sipariş, stok ve sevkiyat tablolarındaki tutarsızlıkları belirleyip operasyon ekibine önceliklendirilmiş aksiyon listesi sunmak.

## Girdi
CSV/XLSX dışa aktarımları; örnek alanlar: sipariş_kodu, sku, adet, sipariş_tarihi, stok_adedi, sevk_durumu. Gerçek veri kabulünden önce veri işleme ve gizlilik koşulları ayrıca netleştirilecek.

## Teslimat
1. Veri kalite özeti: eksik, yinelenen ve tip hataları.
2. Uyuşmazlık listesi: sipariş adedi > stok, negatif stok, eşleşmeyen SKU, çelişen sevk durumu.
3. Etki ve öncelik matrisi.
4. Yönetici özeti ve önerilen düzeltme adımları.
5. Tek revizyon turu (nihai sözleşme kapsamına bağlı).

## Kapsam dışı
ERP'ye otomatik müdahale, muhasebe denetimi, garantili gelir artışı, canlı sisteme entegrasyon ve güvenlik sertifikasyonu.

## Kabul kriterleri
Her bulgu satır bazlı referans, kural adı ve açıklama içerir; örnek veriyle tekrarlanabilir; kapsam dışı durumlar raporlanır.

## Ticari koşullar
Fiyat, süre, veri hacmi, SLA ve ödeme vadesi keşiften sonra teklif taslağında belirlenir. Şu anda hiçbir fiyat ya da ticari taahhüt ilan edilmez.
