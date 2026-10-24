# V8 Gün 01 — QA: iki bağımsız kontrol alanı
**Tur 1 / teknik veri ve kaynak:** GitHub main SHA, PR #10–13 OPEN/DRAFT/MERGED=false, V6 Gün 01–02 devirleri, V7/V8 QA taslakları, ana site ve e-ticaret kaynak kodu incelendi. Yeni V8 metrikleri BİLİNMİYOR, önceki 0 kullanıcı beyanı. Barındırma platform kaynakları ayrıldı.

**Tur 2 / marka, hukuk, konversiyon, tutarlılık:** Canlı genel hizmet fiyatları V8 TEST fiyatından ayrıldı; GVK 20/B ve MoR yerel vergi muafiyeti varsayılmadı; Company Services paneli aktif denmedi; huni ödeme+teslim hatası ve alt mobil test sınırı açık yazıldı; onaysız yayın yok.

| Kapsam | Tur 1 | Tur 2 | Gerekçe |
|---|---|---|---|
| Belge kaynak/tarih/SHA | GEÇTİ | GEÇTİ | Repo ve resmî URL'ler, bilinmiyor ayrımı |
| Marka / gerçek satış fiyatı | KALDI | KALDI | Sitedeki fiyat-v8 test fiyatı uyumu açıklanmalı |
| 320/375/390/768/1024/1440, klavye, alt, WCAG | TEST EDİLEMEDİ | TEST EDİLEMEDİ | Live render yok |
| Teknik/performans/Lighthouse/HTTP | TEST EDİLEMEDİ | TEST EDİLEMEDİ | DNS 000; ana sayfa web araçça okunmuştu |
| KVKK/çerez/telif | TEST EDİLEMEDİ | KALDI (ticari) | GA4/FormSubmit rıza ve lisans akışı kanıtsız |
| Platform/hukuk | KALDI | KALDI | GitHub Pages ticari risk; KYC/vergi belirsiz |
| Huni ve dönüşüm | KALDI | KALDI | Ödeme/teslim yok |
| 0 TL/yayın/soğuk iletişim yasağı | GEÇTİ (bu oturum) | GEÇTİ | Dış etki, para, mesaj işlemi yok |

**Gerçek komut:** `curl -IL --max-time 12 -sS -o /dev/null -w '%{http_code}' https://synapseautomate.github.io/` → `000`, DNS çözümleme hatası. Bu 404 değildir. Yerel kapsamlı QA ayrıca dosya paketinde `python qa_gun01.py` → iki ayrı veri ve marka/yetki kontrolü PASS; bu PASS **canlı site veya ürün için değildir**.
**Sonuç:** Belge taslağı iki kontrolden geçti, açık **6 P0 / 3 P1** nedeniyle teknik ve ticari yayıma **HAZIR DEĞİL**.
