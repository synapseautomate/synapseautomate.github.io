# V8 Gün 02 — ICP / Problem Brifi (15.10.2026)
**Hipotez:** 1–10 kişilik, CSV dışa aktarabilen Türkiye e-ticaret işletmesi. Kullanıcı operasyon sorumlusu; karar verici işletme sahibi. Sipariş ve stok CSV'lerini günlük/haftalık dışa aktarır; stok anlık değil dosyanın tarih/saatine aittir.

Mevcut Excel/Sheets çözümü: XLOOKUP, COUNTIF ve manuel filtre. Tetikleyici: kampanya sonrası hacim, SKU uyumsuzluğu, yinelenen sipariş, stok dosyası gecikmesi. Birincil vaat: **Sipariş ve stok CSV'lerini mağaza API'si olmadan yerelde karşılaştırıp eksik SKU, mükerrer sipariş ve olası stok yetersizliğini gerekçeli raporla göstermek.**

Yanlış pozitif: varyant, rezervasyon, iptal/iade, bundle, çoklu depo, tarih uyuşmazlığı. Kapsam dışı: otomatik stok değişimi, API, gerçek zamanlı mutabakat, ROI garantisi, müşteri verisini yükleme zorunluluğu. Gerçek talep/ödeme kanıtı BİLİNMİYOR.