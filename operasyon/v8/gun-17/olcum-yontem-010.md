# Yöntem 010 / Core Web Vitals ve kullanıcı deneyimi
**Tarih:** 2026-10-26 · **Marka:** SYNAPSE Automate · **Sahip:** Ölçüm sorumlusu / hesap sahibi.
**Ana kaynak:** https://developers.google.com/search/docs/appearance/core-web-vitals
**Repo:** https://github.com/synapseautomate/synapseautomate.github.io/tree/main
**Statü:** Dahili karar/taslak; canlı hesap eylemi YOK. Resmî platform özelliği, mevcut repo kanıtı ve editoryal hipotez ayrı tutulur.

## Gün 17'ye özgü uygulanabilir karar
Gerçek kullanıcı CWV ölçümü GSC/CrUX panelinden; pageview veya JS olayları CWV değildir. Referans iyi sınırlar LCP ≤2,5s, INP ≤200ms, CLS ≤0,1.

## Kontrol ve kabul girdileri
1. `cwv_lcp_field`: saniye, p75 / gerçek CrUX veya izinli RUM
2.  `cwv_inp_field`: milisaniye, p75 / gerçek CrUX veya izinli RUM
3. `cwv_cls_field`: skor, p75 / gerçek CrUX veya izinli RUM
4. `cta_click`: tıklama, gerçek teslim değildir
5. `form_submit_verified`: FormSubmit sunucu kabulü, tıklamadan farklı

## Gerçeklik sınırı ve dosyaya dönüşen çıktı
Gerçek panel BİLİNMİYOR; sentetik örnek event yalnız tanım. Test URL: https://synapseautomate.github.io/rehberler/ai-surec-denetimi.html?utm_source=linkedin&utm_medium=organic&utm_campaign=ai_system_review (dışarı gönderilmedi). Gerçek kişisel iz/UTM/log saklanmaz; KVKK ve çerez onayı ayrıca denetlenir. Yeni JS dağıtımı YOK.

## Karar, sorumlu, kanıt seviyesi
GO: sorgu önce kullanıcı görevi ve erişilebilirlik; gerçek saha ölçümü olmadan hız kazancı iddia edilmez. Rollback: yeni ölçüm kodu olmadığı için yok; gelecekte olay eklenirse consent flag kapalıyken gönderimi negatif test et.
GSC/GA4/gerçek inbound/gerçek ödeme metrikleri, kullanıcı resmî paneli gösterene kadar **BİLİNMİYOR**. Kullanıcıdan şifre, IBAN, kimlik istenmez. Yeni dış işlem ayrı izin gerektirir.
