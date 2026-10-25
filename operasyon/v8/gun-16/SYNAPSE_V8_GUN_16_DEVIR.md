# SYNAPSE V8 MAX — Gün 16 sıfır bağlamlı tam devir
**Hazırlayan operatör tarihi:** 25.10.2026, Europe/Istanbul. **Plan günü:** 29.10.2026 (4 gün erken), 16/30 numarası değiştirilmedi.
**Gün adı:** Ücretsiz yararlı rehber; **öncelikli konu:** Kuruma Özel Yapay Zekâ ve Bilgi Tabanı / kurumsal kaynak gösteren RAG asistanı. Kullanıcının en üstteki güncel konu bloğu eski CSV/sipariş-stok kreatif örneğinin yerine geçer; satış/kanal/tarih/QA/izin kurallarını değiştirmez.

## A — Tek amaç ve doğrulanmış başlangıç
**Amaç:** Gerçek müşteri verisi istemeden kaynaklı yanıtın *hangi kaynak/sürüm/rol/bölüm/insan kararı* koşuluyla güvenilebileceğini beş adımda öğretmek; pazarlama/gerçek ürün vaadi değil. 
**Repo:** https://github.com/synapseautomate/synapseautomate.github.io 
**Başlangıç main SHA:** `4df7e2e7279c9e3f65c7ad1b1fabeb0fb08ff3d1` (25.10.2026, GitHub commit kaydı).
**Gün16 taslak dal:** `draft/v8-gun-16-rag-kaynakli-bilgi-tabani-20261025`; **PR #43:** https://github.com/synapseautomate/synapseautomate.github.io/pull/43 ; OPEN/DRAFT/MERGED=false. 
**Önceki:** Gün15 CLOSED (19/19 kullanıcı PASS) / iç PR #41 CLOSED, MERGED=false; site PR #42 MERGED. Gün14 PR #39 CLOSED arşiv, #40 MERGED. Mevcut refs üzerinde Gün11 ve Gün14–15 devri okundu; Gün01–10/Gün12–13 devirleri **main'de bulunamadı** ve başka PR/arşiv dallarında ayrıca bulunabilir; bulunmadığı kanıtlanmamış devir içeriği varsayılmadı. Gün01–07 dokunulmadı.
**Sitede gerçekten yazan hizmet:** `hizmetler.html`, “08 Kuruma Özel Yapay Zekâ ve Bilgi Tabanı — Şirketinizin kendi doküman ve bilgi kaynaklarına dayanan yapay zekâ asistanları ile kalite değerlendirme altyapıları kurulur.” Bu bir hizmet tanımıdır, çalışan RAG ürününün müşteri demosu kanıtı değildir.
**Açıklık:** gerçek başarı/satış/benzersiz inbound/kanal kazananı BİLİNMİYOR, Upwork/analitik/ödeme paneli doğrudan erişilmedi.

## B — Üretilen gerçek artefaktlar, önce/sonra
**Kamuya yönelik yalnız TASLAK dosyalar:**
1. `hizmetler.html`: mevcut Kuruma Özel Yapay Zekâ ve Bilgi Tabanı kartına yalnız `rehberler/kaynak-gosteren-rag-bilgi-tabani-rehberi.html` linki eklendi. Başlık/açıklama/fiyat/diğer CTA ve form değişmedi.
2. `rehberler/kaynak-gosteren-rag-bilgi-tabani-rehberi.html`: 5 adım, tek gerçek alıcı problemi, sentetik kaynaklı cevap, “bilinmiyor”, ücretsiz dosyalar, kimler için değil, gizlilik ve kaynak URL.
3. `veri/rag_ornek_kaynak_envanteri.csv`: 5 sentetik kaynak satırı; şema `kaynak_id;surum;gecerli_tarih;erisim;durum;sahip;bolum;baslik;metin;ornek_etiketi` (UTF-8 BOM, `;` ayraç). Eski v1, güncel v2, genel ekip ve kısıtlı İK ayrımı.
4. `veri/rag_beklenen_kontrol_sonuclari.csv`: beş kurgusal soru/gerekçe/kaynak/karar; noktalı virgül içeren metin CSV alıntısı düzeltildi, gönderilen satırın şeması bozulmaz.
5. `veri/validate_rag_example.py`: gerçek Python stdlib ile kaynak/rol/sürüm negatif test; **RAG asistanı değil**, model/indeks yok.
**İç çalışma:** `operasyon/v8/gun-16/` 12 yöntem dosyası: 044,053,059,087,116,129,160,196,213,217,240,247; ayrıca kapsam kabul matrisi, ücretsiz–hizmet link matrisi, sosyal caption/alt metin, SEO/iç bağlantı, QA A, QA B ve bu devir.
**Gerçek medya (sohbet paketi, GitHub'da binary YOK):** `SYNAPSE_RAG_5_ADIM_LINKEDIN.pdf` = 5 gerçek PDF sayfası; `SYNAPSE_RAG_KAYNAKLI_YANIT_01..05_1080x1350.png` = 5 farklı özgün kare; 320px thumbnail/yan-yana contact sheet; `PUBLIC_ASSETS/kaynak-gosteren-rag-bilgi-tabani-rehberi.html` yerel eşdeğer; iki CSV, Python testi ve QA script'i.
**Marka:** yalnız kullanıcı tarafından sağlanan orijinal SYNAPSE logo varlığı (orantılı); dış fotoğraf/müzik/ücretli font YOK. Her görselde `SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL`; iç PR/gün/QA notları kreatifin üzerinde YOK. Bu bir sahte RAG UI ekranı veya müşteri vakası değildir.

## C — P0/P1/P2 risk, önlem ve teknik/ticari yayın kapısı
| Öncelik | Açık madde | Önlem / sahip | Son durum |
|---|---|---|---|
| P0 | KYC/vergi/fatura/dijital teslim/gizlilik ve gerçek ödeme kanıtı bağımsız yok | hesap sahibi + yetkili hukuk/mali uzman | SATIŞA AÇMA YOK |
| P0 | RAG gerçek ürün/müşteri demosu olmadığı halde varmış gibi iddia riski | operatör: sentetik/kavramsal açık etiket | YANILTICI İDDİA ÖNLENDİ |
| P1 | Gerçek HTTP/404, tam site responsive, Safari, Lighthouse, FormSubmit | teknik QA / hesap sahibi | TEST EDİLEMEDİ |
| P1 | LinkedIn iPhone gerçek PDF kabulü, Instagram gerçek crop ve alt metin paneli | hesap sahibi | TEST EDİLEMEDİ |
| P1 | Yetkili GA4/GSC/FormSubmit/veri izni ve nitelikli talep kaynakları | hesap sahibi | BİLİNMİYOR |
| P2 | Raster PDF'de seçilebilir metin yok | erişilebilir HTML alternatif dosyası | ALTERNATİF VAR |
**Karar:** iç metin/medya teknik üretim tamamlandı. Kamu yayını ve gerçek ticari işlem **ONAY BEKLİYOR; P0/P1 nedeniyle “yayına hazır” etiketi YOK.**

## D — İki bağımsız QA
**Tur A / gerçek komut ve sonuç:**
- `python build.py`: 2 CSV, tek erişilebilir HTML, 5 adet 1080×1350 PNG ve PDF oluşturuldu.
- `python PUBLIC_ASSETS/validate_rag_example.py`: **5/5 PASS** (güncel v2, eski v1 hariç, İK kapalı, olmayan bilgi→BİLİNMİYOR, kaynak içi talimat→insan incelemesi). Canlı retrieval/LLM **ÇALIŞTIRILMADI**.
- `python qa_test.py`: PDF fitz 5 sayfa, her sayfa 540×675 pt ve render 1080×1350; PNG sayısı 5 ve boyutları doğru. Kaynak H1=1, 5 adım, 2 indirme ve form yok. GitHub compare #43 5 kamu dosyası ve 12 yöntem dosyası, istenmeyen fiyat/analytics JS değişikliği yok.
**Tur B / gerçek düzeltme ve sınırlı render:**
- İlk 320/375 px yerel HTML kontrolünde uzun H1 `scrollWidth=380` FAIL. Metin “Kaynağı görün” şeklinde düzenlendi; **320/375/390/768/1024/1440 6/6 PASS** (Playwright/Chromium `page.set_content`, dosya URL politika nedeniyle yerel file:// engelli).
- İlk yaratıcı kapakta logo/belge üst üste biniyordu; grafik kaydırılıp yeniden gerçek PNG/PDF üretildi. Beş orijinal sayfada etiket/lisans kontrolü yapıldı, bütünleşik kare gösterimi `INTERNAL_QA/5_SAYFA_YAN_YANA.png`. Yerel editoryal marka PASS, gerçek sosyal arayüz testi YOK.
- **Sınır:** GitHub PR HTML, aynı kullanıcı mesajı/içerik ve CSS mantığına göre daha kompakt kardeş sürümdür; 6 viewport birebir PR HTML renderı diye yanlış iddia edilmez. PR dosyası kaynak/href/H1/adım/etiket statik doğrulamasından geçmiştir. Gerçek Safari, screen reader, Lighthouse ve sosyal upload TEST EDİLEMEDİ.
**Resmî kaynak (25.10.2026):**
- RAG / retrieval, erişim ve hallucination sınırları: https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation (Microsoft)
- SEO iç link: https://developers.google.com/search/docs/crawling-indexing/links-crawlable (Google)
- PDF LinkedIn biçimi: https://www.linkedin.com/help/linkedin/answer/a518909 (LinkedIn)
- Google Dataset koşulları: https://developers.google.com/search/docs/appearance/structured-data/dataset ; `Dataset` JSON-LD canlı veri yayını olmadığı için eklenmedi
- KVKK ilkeler: https://www.aile.gov.tr/kvkk/mevzuat/ (T.C. Bakanlık).

## E — Metrik sözlüğü, kaynak ve güven düzeyi
| Tarih/kanal | Tanım | Değer/birim | Kaynak/güven |
|---|---|---|---|
| 25.10 içerik | doğru kabul kontrol adımı | 5 adım | yerel HTML + deterministik Python yüksek |
| 25.10 test | negatif örnek test | 5/5 PASS | stdlib/yerel log yüksek |
| 25.10 PDF | gerçek LinkedIn PDF sayfası | 5 sayfa | fitz orta-yüksek |
| 25.10 site/rehber | yeni draft dosya yolu, canlı indirme | 1 draft HTML, **canlı indirme YOK** | GitHub PR, yüksek |
| Site organik | rehber açılışı/indirimi | BİLİNMİYOR olay | panel yok |
| LinkedIn/Instagram | gösterim, kaydetme, ilgili soru | BİLİNMİYOR olay | panel yok |
| Funnel | tekil nitelikli gönüllü talep | BİLİNMİYOR kişi | form ve kanal paneli yok |
| B2B işlem | izinli teklif/funded sipariş/banka tahsilatı/iade/net gelir | BİLİNMİYOR işlem/TRY | belge/panel yok |
| Bu oturum | peşin harcama ve gerçek dış platform gönderimi | 0 TL, 0 gönderi | bu oturum eylem günlüğü |
**0 ≠ BİLİNMİYOR.** GitHub taslak açılması görüntülenme/lead değildir. Sentetik test satırları gerçek kullanıcı, sipariş veya ticari sonuç değildir.

## F — Dosya ve ayrı kullanıcı eylem onayı
**Doğrudan indirilebilir sohbet dosyaları:** kullanıcıya gösterilen `SYNAPSE_V8_GUN16_RAG_TUM_DOSYALAR.zip` (üretildiğinde), `SYNAPSE_RAG_5_ADIM_LINKEDIN.pdf`, beş PNG ve rehber HTML. GitHub PR kamu URL'si **draft**, canlı site linki gibi gösterilmez.
- `WEB-G16-RAG-20261025` — yalnız yeni rehber + iki CSV + bir test script'i + hizmet kartı iç linki için **ONAY BEKLİYOR**.
- `LI-G16-RAG-20261025` — LinkedIn Company PDF paylaşımı **ONAY BEKLİYOR**.
- `IG-G16-RAG-20261025` — Instagram 5 PNG paylaşımı **ONAY BEKLİYOR**; hesabın uygunluğu da teyitsiz.
Gönderi/ticari talep/ödeme/alan adı/hesap aktivasyonu izni ayrı; Metricool bağlantısı diğer hesapları kapsadığından kullanılmadı.

## G — Engeller ve asgari insan adımları
Asıl kullanıcı hesabında yayın öncesi final kreatif/kanal yükleme kontrolü ve GitHub PR #43 için ayrıca **belirli** site yayın izni. Gerçek satış veya KYC/fatura açma onayı yok. Panel verisi talep edilirse yalnız kişisiz/toplam metrik; parola/IBAN/kimlik/gerçek müşteri dosyası isteme.
**Rollback (ileride yayınlanırsa):** hizmet kartından yeni `<a class="more" ...>` öğesini kaldır, yeni rehber/örnek dosyaları ayrı commit ile çıkar; `main` şu an aynen korunmaktadır.

## H — Sonraki gün için tek öncelik
**Gün17 öncesi önce gerçek kanalın nitelikli inbound/araç açılış durumunu yetkili panelden yeniden doğrula; erişilemiyorsa BİLİNMİYOR yaz.** Gün16 sentetik RAG rehberini canlı ürün gibi genişletme, üçüncü ürün veya yeni platform açma. Sadece kullanıcı eylem bazlı onay verirse PR #43 main, LinkedIn PDF ve Instagram ayrı ayrı ele alınabilir. **GÜN 16 = DRAFT; CLOSED DEĞİL.**


---
## Son QA düzeltmesi — sentetik CSV etiketinin dosya düzeyinde açık olması
**25.10.2026 — ikinci QA düzeltmesi:** İlk CSV tesliminde zorunlu `SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL` ibaresi dosyanın her satırında yoktu. Her iki GitHub CSV'ye `ornek_etiketi` sütunu eklendi, 5'er kurgusal satırın her birine açık etiket yazıldı, noktalı virgül geçen tek alan çift tırnakla doğru CSV sütununda tutuldu. **Gerçek çıktı:** yerel Python csv.DictReader iki dosyada 5 satır/5 etiket PASS, `python qa_test.py` tekrar QA_A=true ve QA_B=true. Bu yalnız teknik sentetik veri paket kontrolüdür, çalışan RAG/gerçek kişisel veri yetki testi değildir. Yeni GitHub değişiklikleri `90c0473b2533e693d9c599fe571ed7f785ef57d0` ve `a7b7f66067eb195492ca98227ec8fe1517ad623e` kaynak/sonuç CSV etiket düzeltmeleridir.
