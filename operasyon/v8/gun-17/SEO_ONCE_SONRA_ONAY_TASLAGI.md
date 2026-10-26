# Gün 17 — Önce/sonra ve yayın öncesi onay taslağı
**Tarih:** 26.10.2026 · **PR:** https://github.com/synapseautomate/synapseautomate.github.io/pull/46 — DRAFT / main merge YOK.

| Konum | Önce (doğrulanan main) | Sonra (draft PR) | Kullanıcı niyeti |
|---|---|---|---|
| `hizmetler.html` kart 09 | 'Yapay Zekâ Sistem İncelemesi ve Optimizasyonu' hizmet açıklaması, **ilgili rehbere link yok** | Aynı kartın altında mevcut `rehberler/ai-surec-denetimi.html` bağlantısı, 'Doğruluk, güvenlik ve maliyet kontrolünü incele' | hizmet → somut eğitim yolu |
| `rehberler/ai-surec-denetimi.html` | Genel 'AI process audit hangi soruları cevaplamalı?' tanıtımı ve 3 kart | aynı URL/title/meta yenileme; 3 ayrı ölçüt (kaynak sürümü, rol yetkisi, maliyet kapsamı), 2 sentetik vaka | karar sorusuna somut yanıt |
| Canonical | https://synapseautomate.github.io/rehberler/ai-surec-denetimi.html | DEĞİŞMEDİ | çakışan yeni sayfa yok |
| Birincil mevcut CTA | Ücretsiz Hazırlık Taraması | KORUNDU | gereksiz yeni form yok |
| Fiyat, ödeme, analitik, sitemap | mevcut | DOKUNULMADI | güvenli küçük diff |

### İddia sınırı
SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL. Gerçek AI doğruluk testi, canlı güvenlik penetrasyon testi, oran, KYC veya finansal kazanım iddiası yok.

### Kanıt ve ön şart
Statik kaynak assert **16/16 PASS**; altı gerçek viewport, mobile Safari, keyboard, HTTP 200/404, FormSubmit ve GSC **TEST EDİLEMEDİ**. Bu sebeple P1 kapısı açık ve 'yayına hazır' değildir. Ayrı **WEB-G17-SEO-001** kullanıcı onayı ve canlı release kapısı beklenir.

### Rollback
Yanlış bir güncelleme yapılırsa PR diff'i geri alınır; eski sürüm `main@6de1c4ad10feef1fef37e93d2731dad5e7886574`. Main'e force push veya otomatik merge YOK.
