# Gün 17 — QA TUR B: bağımsız okunabilirlik, marka, UX, hukuk ve yayım
**Tarih:** 26.10.2026 · **Kamu yayını:** YAPILMADI.

| Alan | Statü | Gerçek gözlem / engel |
|---|---|---|
| İçerik doğruluğu | PASS (editoryal kontrol) | Sentetik A01–A06 kapsamı, kaynak/sürüm/rol/tavan anlamları tutarlı; üretim performansı sonucu yok |
| Marka doğruluğu | PASS (kaynak kontrolü) | Ana CSS token'ları ve logo path'i değiştirilmedi; hiçbir rakip/sertifika rozeti eklenmedi |
| UX, H1/H2 ve tek eylem | PASS (statik kaynak) | tek H1; CTA mevcut, yeni bölümde bir bağlamsal link, yanıltıcı checkout yok |
| Mobil: 320/375/390/768/1024/1440 px | **TEST EDİLEMEDİ** | gerçek branch HTML tarayıcı renderı yapılmadı |
| Klavye/screen reader/touch target | **TEST EDİLEMEDİ** | cihaz, erişilebilirlik ağacı ve forma etkileşim yok |
| Lighthouse / CWV saha | **TEST EDİLEMEDİ** | gerçek CrUX/GSC/yerel Lighthouse raporu yok |
| URL HTTP 200 ve kırık dış bağlantılar | **TEST EDİLEMEDİ** | canlı GitHub Pages erişimi bu ortamda engellendi |
| Statik rehber canonical | PASS (kaynak) | self canonical bozulmadı |
| Telif / fotoğraf | PASS (yalnız bu metin) | yeni görsel, müzik veya font eklenmedi |
| KVKK / kişisel veri | PASS (yeni değişiklik) | yeni form, dosya yükleme, veri aktarma veya çerez eklenmedi |
| Platform/hukuk | HOLD | hizmet vaadi ve fiyat/teslim için hesap sahibi + uzman kontrolü gerekli; satış açılmadı |
| Dönüşüm ve gerçek talep | BİLİNMİYOR | yetkili analitik veya FormSubmit teslim kaydı yok |
| Gönderi / ödeme / main merge | YAPILMADI | ayrı açık kullanıcı onayı yok |

**P1 açığı / sahibi: QA sorumlusu:** Gerçek altı viewport render, klavye ve URL/http deneyimi olmadan 'teknik yayına hazır' denemez. Bu, *bulunmuş bir mobil kusur* değil, gerekli testin eksik olmasıdır.

**P0:** Dar taslakta kontrol edilen kritik alanlarda saptanmış P0 yok; sitenin tümünde P0=0 veya satışa uygunluk kanıtlanmadı.
**P2:** Metinsel başlık düzenlemesinin gerçek CTR etkisi bilinmiyor; A/B üstünlük iddiası yok.

**İkinci tur spesifik kırmızı çizgiler:** Yanlış test fiyatı, sahte AI model çıktısı, otomatik onay, logo değişimi, veri sızıntısı, sentetik etiket eksikliği, Upwork dışı ödeme CTA'sı, kopya SEO sayfası ve iç QA notunun müşteri metnine sızması. Bu değişiklikler statik kaynakta tespit edilmedi.

**Yayım kararı:** Teknik statik taslak = oluşturuldu. Ticari satış = HOLD. Canlı site = ONAY BEKLİYOR, bunun öncesinde gerçek viewport/keyboard/HTTP testleri istenir. Sosyal = yeni gönderi YOK. 
