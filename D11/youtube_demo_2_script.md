# YouTube demo #2 — 3–6 minute production script

**Working title:** AI Otomasyonda “Bilmiyorum” Neden Bir Özellik? | Structured Extraction Demo

**0:00–0:20 — Hook**
Ekranda aynı sipariş kaydının iki çıktısı. Sol taraf eksik tarihi uyduruyor; sağ taraf `unknown` bırakıp incelemeye yönlendiriyor. Voice: “İki çıktı da düzgün JSON. Sadece biri güvenilir bir iş akışına uygun.”

**0:20–1:15 — Input**
Sentetik sipariş e-postasını göster: sipariş no var, teslim tarihi yok, iade talebi belirsiz. Hassas/veri iddiası yok.

**1:15–2:10 — Structured extraction**
Şema alanlarını göster. Kaynakta olan alanlar doluyor; olmayan alan null. Her alanın `source_ref` izi var.

**2:10–3:00 — Deterministic validator**
Kural: parasal sonuç veya eksik zorunlu kaynak → `HUMAN_REVIEW/HUMAN_APPROVAL`. Modelin prose cevabından bağımsız.

**3:00–3:45 — Human gate**
Onay kartında kaynak, öneri, etki, yetki sahibi, reddetme/geri alma yolu. “AI karar sahibi değil; karar hazırlayıcı.”

**3:45–4:20 — Failure example**
Bozuk/duplicate dosya → fail closed. “Plausible answer üretmek yerine işlem durur.”

**4:20–4:45 — CTA**
“Kendi sürecinizde hangi alan kaynak, hangi karar kural, nerede insan devralıyor? Ücretsiz süreç haritasıyla başlayın.”

**On-screen CTA:** synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html

**Production gate:** gerçek müşteri verisi yok; sentetik etiket görünür; ses/müzik olmadan yayınlanmaz; 9:16 Short türevi ancak uzun demo tamamlandıktan sonra.
