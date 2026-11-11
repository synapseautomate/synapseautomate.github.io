# SYNAPSE Automate | Gün 02 — tek sayfalık durum özeti
**14.10.2026 · Gün 02: Müşteri problemi ve ürün kararı**
**Statü:** GÜN 02 CLOSED (araştırma, kapsam ve karar belgeleri); **SATIŞ/YAYIN NOT READY**.
**Taslak PR:** https://github.com/synapseautomate/synapseautomate.github.io/pull/11 · Ana site **değişmedi**.

## Seçilen tek problem
Küçük e-ticaret işletmesinde CSV sipariş ve stok kayıtlarının karşılaştırılması sırasında boş SKU, tekrar eden sipariş satırı, negatif stok, sipariş-stok açığı ve durum çelişkisi gibi **incelemeye değer** kayıtları görünür kılmak. Hata maliyeti ve sık tekrar ettiği **hipotez**; henüz gerçek müşteriyle kanıtlanmadı.

**Bir cümlelik vaadimiz:** Sipariş ve stok CSV dosyalarındaki stok açığı, negatif stok, boş SKU ve yinelenen kayıt gibi tanımlı tutarsızlıkları yerel olarak işaretleyen kontrol paketi.

## Üç soru / üç net yanıt
1. **Kime?** CSV dışa aktarımı yapabilen küçük e-ticaret işletmesi; kullanıcı operasyon sorumlusu, karar veren sahip/yönetici.
2. **Ne sonuç verir?** Satır/SKU/kural/açıklama bazlı bulgu listesi; otomatik stok güncellemesi, API veya bulut yüklemesi değil.
3. **Neden ödesin?** Tekrarlanabilir kontrol ve insan onaylı inceleme listesi için; **ödemeye razı olduğunu gösteren veri henüz yok**.

## Kanıt sayıları
- **12** aday satın alma niyetli sorgu (arama hacimleri bilinmiyor);
- **6** gerçek alternatifin resmî fiyat/kapsam bağlantısı;
- **3** yalnız **TEST FİYATI:** 990 TL indirilebilir araç, 4.900 TL sınırlı kurulum, 24.900 TL isteğe bağlı B2B pilot.
- **2** alternatif park edildi: haftalık Sheets/Excel otomasyonu, genel sipariş hata kontrolü.
- **4 P0** ticari satışa çıkış engeli açık.
- Yeni dönemde ücretli satış / trafik / CTA / net gelir: **BİLİNMİYOR**, sıfır değildir.

## Kritik risk
Gün 01 Python prototipi birleşik CSV okuyor; Gün 03 PDF planı iki ayrı CSV ister. Ayrıca stok zamanı/depo farkları yanlış pozitif yaratabilir. Şema ve kabul testleri tamamlanmadan 'indirilebilir satış ürünü' denmez.

## İzin ve devir
**YAPILMADI:** canlı site yayını, PR merge, ilan/DM, müşteri teması, fatura, ödeme, ücretli trafik veya hesap başvurusu. Kullanıcının kurumsal B2B tercihi ile PDF indirilebilir birincil ürün önceliği **ayrı kararlar** olarak korundu.
**Gün 03 / 15.10.2026:** çift CSV dosya sözleşmesi, 5 çekirdek kural, 3 sentetik senaryo, falsifiable kabul testleri, veri gizliliği ve 5 adımlı onboarding.

**Kanıtlar:** `01-`…`08-` dosyaları, `GUN_02_A_H_RAPOR.md`, `SYNAPSE_GUN_02_DEVIR.md`. Önceki Gün 01 kaydı: https://github.com/synapseautomate/synapseautomate.github.io/pull/10.
