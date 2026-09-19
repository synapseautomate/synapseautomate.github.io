# LinkedIn Company Page — Data Post

**Publish window:** 4–6 hours after the native video.  
**No image required.** The data itself is the post.

## Copy

**100-vaka testinde en pahalı hata “model yanlış cevap verdi” değildi.  
Yetki sınırı yoktu.**

Frozen sentetik regression setindeki candidate baseline 40 kritik mismatch üretti.

Risk Pareto:

**44.9% — authority / egress boundary**  
Write veya dış hedef yetkisi model çıktısından bağımsız değildi.

**35.9% — embedded untrusted instruction**  
Belge/web içeriği ile gerçek instruction sınırı yeterince sert değildi.

**19.2% — stale price / stock source**  
Kaynak doğru olsa bile freshness şartı yoktu.

Çözüm daha uzun prompt olmadı.

1. capability allowlist  
2. instruction/data separation  
3. freshness gate + escalation

Aynı frozen suite root fix sonrası **100/100 expected control state, 0 critical mismatch** verdi.

Sınır önemli: bu production accuracy veya güvenlik garantisi değildir. Sentetik deterministic test kapsamıdır.

Methodology → https://synapseautomate.github.io/kanit/100-vaka-ai-guvenilirlik-regresyon-raporu.html?utm_source=linkedin&utm_medium=organic&utm_campaign=day13_regression&utm_content=data_post

#EnterpriseAI #AISecurity #AIGovernance #Ecommerce
