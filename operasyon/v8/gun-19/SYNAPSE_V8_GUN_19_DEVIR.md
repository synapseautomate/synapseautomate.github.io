# SYNAPSE AUTOMATE — V8 GÜN 19 / SIFIR BAĞLAMLI OPERATÖR DEVRİ
**Gerçek tarih:** 28.10.2026, Europe/Istanbul. **Plan tarihi:** 01.11.2026 (4 takvim günü erken). **Görev numarası:** Gün 19/30, değiştirilmedi.
**Özgün hizmet:** Sesli Yapay Zekâ ve Çağrı Merkezi: sentetik randevu isteği, açık çağrı yönlendirme, belirsizlikte insan devri.
**Tek karar sorusu:** “Asistan ne zaman randevuyu kesinleştirmemeli, ne zaman bir insana devretmeli?”

## 0. Yetkiler, hesaplar, mali disiplin
- **WEB-G19-20261028: ONAY BEKLİYOR.** Kullanıcının Gün18 PR #48 yayım onayı, Gün19 PR #49 için yetki değildir. Main'e merge YAPILMADI.
- Sosyal: Gün19 kamuya paylaşım kotası YOK; LinkedIn, YouTube, Instagram, X, Threads, TikTok, Pinterest, Facebook, Bluesky için gönderim/planlama **YAPILMADI**, ayrı eylem onayları gerekir.
- Gerçek FormSubmit POST, alıcı inbox erişimi, telefon araması, ses kaydı, gerçek randevu, WhatsApp/DM, hesap/harita/dizin açma, API kullanımı, ödeme **YAPILMADI**. 0 TL peşin.
- KVKK/aydınlatma, FormSubmit üçüncü taraf, fatura/KYC/mesafeli satış ve sesli arama politikası uzman/hesap sahibi teyidine muhtaç. Gerçek para veya müşteri verisi kullanılmadı.

## 1. Başlangıç kaynakları
- Ana repo: https://github.com/synapseautomate/synapseautomate.github.io
- Son doğrulanmış yayın `main` SHA: `b2db84e1db00e4acbf0a6882e66c4b55643a113d` (27.10.2026 onaylı Gün18 PR #48).
- Gün19 draft PR: https://github.com/synapseautomate/synapseautomate.github.io/pull/49
- Dal: `draft/v8-gun-19-sesli-ai-talep-yolu-20261028`.
- Gün18 önceki devir okunabildi: `operasyon/v8/gun-18/SYNAPSE_V8_GUN_18_DEVIR.md` Gün18 draft #47. Gün11 devri main'de vardı. Gün01–10,12–17 devirlerinin main dosya yolları bulunmadı; yokluk kendi diğer taslak dal/özel arşivlerinde olmadığı anlamına gelmez. Önceki gün16 RAG/Gün17 AI değerlendirme ve Gün18 süreç madenciliği burada tekrar edilmedi.
- Hizmet #11: `hizmetler.html` — “Sesli Yapay Zekâ ve Çağrı Merkezi / Sesli asistan, çağrı merkezi otomasyonu, sipariş ve randevu akışları.” Bu hizmet açıklaması **gerçek çalışan voicebot** veya çağrı kaydı kanıtı DEĞİL.

## 2. Değişiklikler — sadece draft
1. `cozumler/sesli-yapay-zeka-randevu-insan-devri.html`: tek rol, ön koşul, üç kavramsal sentetik senaryo, human gate, kapsam dışı; canlı bot/ses/CRM/RANDEVU gerçekleşmesi iddia edilmez. Görünür `SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL` etiketi.
2. `hizmetler.html` #11 kartı → yeni konu sayfası; `index.html → hizmetler.html` halihazırda erişilebilir.
3. `iletisim.html`: konu seçeneği “Sesli Yapay Zekâ ve Çağrı Merkezi”; `?konu=sesli-yapay-zeka` gelirse JavaScript ile seçilir, hiçbir veri dışarı otomatik gönderilmez.
4. `surec-analizi.html`: FormSubmit aktarımı için zorunlu checkbox ve gizlilik linki; doğrulanmamış fiyatlar `TEST FİYATI` etiketiyle sınırlandı, `Service.offers` JSON-LD kaldırıldı. Bu, fatura/ödeme uygunluğunun sağlandığı anlamına gelmez; diğer fiyat sayfalarının genel incelemesi açık.
5. `sitemap.xml`: draft yeni konu sayfası ekli; mevcut main sitemap değişmedi.
6. `scripts/v8_gun19_browser_qa.py`, `scripts/v8_gun19_before_after.py`, `scripts/v8_gun19_live_http.py` ve `.github/workflows/v8-gun19-voice-journey-qa.yml`: gerçek CI tarayıcı ve screenshot testleri.
7. `scripts/day1_browser_funnel.mjs`: P1 regresyon düzeltmesi — simüle test formunda yeni zorunlu onay işaretlenir, gerçek FormSubmit'e gönderim hâlâ engellenir.
8. `operasyon/v8/gun-19/` altında 018/019/048/058/070/073/078/089/122/175/237/244 yöntemlerinin gerçek kaynaklı dosyaları, QA A/B, form/404/CTA, yolculuk ve metrik/onay dokümanları var. **İç operasyon klasörünün yanlışlıkla Pages üzerinden yayımlanmaması** için merge öncesi public-only dağıtım süzgeci gerekir; Release Preflight `_site` üretiminde `operasyon/` ve `scripts/` dışlanıyor fakat GitHub Pages yapılandırması ayrıca denetlenmelidir.

## 3. Tamamen gerçek QA ve kaynak
### Tur A — kaynak/veri/teknik
- `python scripts/v8_gun19_browser_qa.py` — GitHub Actions PR checkout üzerinde Playwright Chromium; **6 genişlik (320/375/390/768/1024/1440) × 7 rota = 42/42 PASS**, 42 screenshot, gözlenen pageerror yok. [İş akışı](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659256869), [artefakt](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659256869/artifacts/12803231704). Sonraki teyit: [run 40659965759](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759).
- `python scripts/v8_gun19_before_after.py`: main SHA ile draft gerçek Git kaynakları 320/390/768/1440 width'te karşılaştırıldı, 16 PNG: hizmette yeni href **0→1**, süreç formu zorunlu consent **0→1**. Kanıt [run 40659965759](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759).
- `python scripts/v8_gun19_live_http.py` GitHub runner üzerinden CURRENT LIVE MAIN URL GET testi: ana sayfa, hizmetler, süreç analizi, iletişim, teşekkür ve 404.html **200**; bilinçli olmayan URL **404**; DRAFT sesli AI sayfası hâlen canlıda **404** (beklenen). Hiçbir form POST yok. [Aynı artifact](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759).
- Site Integrity GitHub Actions (en az ilk/ikinci tur) SUCCESS, sitemap eksik 0, orphan 0. Canlı Search Console BİLİNMİYOR.
- Preflight CI ilk yenilemede **FAIL**: önceki gün1 simüle form testinde zorunlu yeni `consent` işaretlenmediğinden redirect bekleme 15sn timeout. Sonraki draft commit `scripts/day1_browser_funnel.mjs` içinde testin kendi sentetik ve dışa çıkmayan onayını işaretleyecek şekilde düzeltildi. **Düzeltme sonrası Preflight sonucunu ayrıca kontrol etmeden PASS yazma.**

### Tur B — tasarım, mobil, erişilebilirlik, hukuk
- 42 PNG gerçek Chromium browser kaydı, yeni sesli AI 390px render incelendi, yatay taşma/H1/alt PASS.
- Yeni sayfa kritik renk çiftlerinde hesaplanan kontrast: 17.45:1, 9.88:1 ve 13.44:1 (normal 4.5:1 üzerinde). CTA CSS 48px, nav 44px; gerçek ekran okuyucu/klavye tam turu/VoiceOver/Safari motoru TEST_EDİLEMEDİ.
- Yerel tarayıcıdan gerçek dışa FormSubmit, GA4/Tag Manager, üçüncü taraf servis ağ çağrısı **bilinçli BLOKE**, gerçek inbox teslimi BİLİNMİYOR.
- Gerçek sesli asistan kaydı, ASR/LLM doğruluk ölçümü, telefon aktarması, rezervasyon doğrulaması, çalışan demo **YOK**. Sentetik görsel ve sözcükler uygulama kanıtı olarak adlandırılmaz.
- Lokal test 404.html statik dosya HTTP 200 (doğal); LIVE bilinçli olmayan URL 404 bulundu (ayrı test). Bu farkları karıştırma.

## 4. Açık P0/P1/P2, düzeltme ve karar
| Kusur | Önlem | Sorumlu | Son durum |
|---|---|---|---|
| P0: gerçek ödeme, fatura, KYC, teslim hukuku yok | CHECKOUT ve satış kapalı | Hesap sahibi/mali müşavir | HOLD |
| P0: canlı bot/gerçek müşteri sonuç iddiası riski | Ürün olarak sunma, sentetik/konsept etiketli sayfa | Operatör | Taslak PASS / gerçek performans kanıtı YOK |
| P1: süreç analizi FormSubmit rızası eksikti | Checkbox ve zorunlu alan eklendi | Operatör | Draft PASS; hukuki yeterlilik dış teyit |
| P1: fiyat/JSON-LD canlı teklif sanılabilir | Genel süreç sayfasında TEST FİYATI, Offers kaldırıldı | Operatör | Draft PASS; diğer fiyat kaynakları açık |
| P1: CI simüle test yeni rızada kırıldı | Sentetik browser test consent seçimini düzeltti | Operatör | Preflight tekrar sonucu bekliyor |
| P1: Safari/VoiceOver/gerçek inbox | İnsan panel testi gerekir | Hesap sahibi / erişilebilirlik QA | TEST EDİLEMEDİ |
| P2: Search Console / GA4 / CRM metrikleri | Yetkili panel doğrulaması | Hesap sahibi | BİLİNMİYOR |

**Teknik yayın:** GitHub draft ve Chromium kaynak QA iyi, ancak CI tam yeşil + Safari/hukuk/gerçek teslim eksik → **WEB yayını HOLD**. **Ticari yayın:** NO-GO. Gün19 CLOSED değil.

## 5. Ölçümler (28.10.2026)
- 42/42 browser kaynağı yerel Chromium PASS; 16 gerçek önce/sonra PNG; canlı main salt-okunur HTTP: 6/6 beklenen 200, draft URL 404, negatif URL 404. Kaynak GitHub Actions logs/artifacts.
- Gün19 kamuya yeni link henüz main'de değil; canlı gerçek ses botu demo izlenme, gönüllü talep, izinli teklif, tahsil edilen satış, sipariş, iade, net gelir, GA4, Search Console **BİLİNMİYOR** (0 demek değil).
- Yeni gerçek müşteri bilgisi kaydı 0, form gönderimi 0, peşin harcama 0 TL, dış post/DM 0.
- Önceki 27 gündeki 0 satış yalnız hesap sahibinin beyanı, bu döneme aktarılmaz.

## 6. SEO ve platform yöntemleri
- 018 GBP / 019 NAP / 070 Apple+Bing / 122 Merchant Center: somut fiziksel müşteri ilişkisi ve/veya gerçek satış ürün/platform kanıtı yok → **NO-GO**, sahte adres/şube/GTIN yok.
- 048 ilgili B2B dizin/medya: yalnız açık erişimli sentetik karar rehberi, dış temas yok.
- 058 fiziksel organik / 073 Snapchat / 078 fiziksel profil / 237 çok şube / 244 fiziksel arıza: B2B sesli AI alıcısı ve doğrulanmış kapasiteye uygun değil → NO-GO.
- 089 zaten site var; sıfır-siteden dönüşüm yerine mevcut web yolu.
- 175 ziyaretçi karar engeli: hizmet → sınır/ön koşul → gönüllü talep / KVKK.

## 7. Kaynaklar ve sonraki tek öncelik
- Repo ve PR: https://github.com/synapseautomate/synapseautomate.github.io/pull/49
- Canlı mevcut hizmet: https://synapseautomate.github.io/hizmetler.html
- Yalnız draft hedef: https://synapseautomate.github.io/cozumler/sesli-yapay-zeka-randevu-insan-devri.html (**şu an 404, henüz yayına alınmadı**).
- KVKK resmî: https://www.kvkk.gov.tr/Icerik/4132/aydinlatma-yukumlulugunun-yerine-getirilmesinde-uyulacak-usul-ve-esaslar-hakkinda-teblig
- Google GBP resmî: https://support.google.com/business/answer/13763036?hl=en
- Google canonical: https://developers.google.com/search/docs/crawling-indexing/canonicalization
- Google crawlable links: https://developers.google.com/search/docs/crawling-indexing/links-crawlable

**Gün20 için TEK ÖNCELİK:** PR #49 güncel son commit'teki Release Preflight ve Day19 browser QA'ları PASS mı kontrol et; açık P1 için gerçek hesap/teslim/Safari gereksinimini yazılı kanıtla kapat. Bu sağlanırsa kullanıcıdan yalnız `WEB-G19-20261028` site yayını için ayrı açık onay iste. Kullanıcıdan Gmail şifresi/IBAN/kimlik/kişisel çağrı kaydı isteme; main'e merge veya sosyal yayın otomatik yapma.


## 28.10.2026 kaynak güncellemesi — CI ve HTTP doğrulaması
- GÜNCEL ve üstün kanıt: GitHub Actions [run 40659965759](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759); [artifact 12802534718](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759/artifacts/12802534718). Gerçek **salt-okunur HTTPS GET main**: ana sayfa, hizmetler, surec-analizi, iletisim, talep-alindi ve 404.html 6/6 **HTTP 200**; bulunmayan URL **404**; **YENİ taslak sesli AI URL canlıda 404 (beklenen)**. Bu testler gerçek FormSubmit POST veya checkout değildir.
- İki sürümden Chromium gerçek render: main-before ↔ draft-after `hizmetler.html` ve `surec-analizi.html`, 320/390/768/1440, **16 gerçek PNG** ve `before-after-summary.json`.
- [Commit e295052](https://github.com/synapseautomate/synapseautomate.github.io/commit/e295052a9476ac433afa828dbc46f48661ca9c6e) sonrası bağımsız CI workflow'ları: Site Integrity, Commercial SEO, Finance SEO, Day12 HR ve **Synapse Release Preflight = SUCCESS**, Gün19 Browser QA = SUCCESS. Önceki Release Preflight FAIL gerçek regresyondu, sonra yerel sentetik consent işaretlemesiyle düzeltildi; gerçek kullanıcı POST'u yok.
- Gün19 canlı yeni sayfa yayımlanmadı. Form başarı/inbox, canlı draft sayfa 200, gerçek Safari ve ödeme hâlâ **TEST EDİLEMEDİ / HOLD**.
