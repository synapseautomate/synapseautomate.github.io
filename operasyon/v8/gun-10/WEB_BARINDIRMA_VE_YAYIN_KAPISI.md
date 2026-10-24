# Web yayın koşulları / kaynaklı karar
- PR #28: https://github.com/synapseautomate/synapseautomate.github.io/pull/28
- Staging CI: https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/39237109324 3/3 PASS; prod canlı HTTP/Safari/Lighthouse kanıtı değildir.
- GitHub Pages resmî kullanım sınırı: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits . Ticari işlemi esas alan ve çevrimiçi işletme işleten barındırma amaçlarına izin verilmiyor. Mevcut sitede FormSubmit ve ücretli teklif anlatısı olduğundan uygunluk hesabın sahibi/GitHub destek ile teyit edilmeli; P0 AÇIK.
- Ücretsiz statik barındırmaya uygun araştırma yolu: https://developers.cloudflare.com/pages/framework-guides/deploy-anything/ ; https://developers.cloudflare.com/pages/platform/limits/ . Bu, hesabın açıldığı veya kabul edildiği anlamına gelmez.
- Hesap sahibi yalnız resmî panelde Cloudflare Pages > Create > Pages > Import GitHub, kart/abonelik talebi varsa DUR; production branch ve build output gözden geçir.
- Çalışma yayın dizininde .git, .github, operasyon, scripts, docs, iç QA, kişisel veriler bulunmamalı. Önce preview yayımlanıp kendi URL'sinde 320/375/390/768/1024/1440, klavye, HTTP, FormSubmit ve consent testi yapılmalı.
- Gerçek yayın için doğru *.pages.dev domaini panelden alınır; URL icat edilmez. GitHub Pages main merge ile canlıya geçme bu koşullar kapanmadan yapılmaz.
- Rollback: GitHub revert veya sağlayıcının önceki deployment rollback özelliği. Harcama 0 TL, satış aktivasyonu yok.

## Önemli URL/canonical koşulu
Cloudflare Pages ücretsiz .pages.dev alt alanı açılırsa bu, mevcut `synapseautomate.github.io` alan adını **taşımaz**. Mevcut statik ZIP'deki canonical, OG, sitemap, JSON-LD, FormSubmit `_next` ve mutlak iç/harici dönüş URL'leri GitHub adresini kullanır. Gerçek .pages.dev proje adresi bilinmeden topluca yeni site yayını yapılamaz.
Cloudflare Pages girişleri hesap sahibince yapılmalı; doğrulanan proje URL'si sonrası bu alanlar güvenli şekilde yeniden yazılıp, kayıtlı mutlak URL'lerin 200/redirect/canonical testleri tekrar edilmeli. Yeni alan adının SEO'da eskiyle eş olduğu iddia edilmez.
Mevcut paket yalnız **test edilmiş statik yayın adayı**; Cloudflare'a doğrudan atılıp doğru üretim çıktısı sayılmaz. Kısa vadede orijinal GitHub sayfası salt proje gösterimi ve ticari işlem barındırma ayrımı resmî uygunluk değerlendirmesine tabidir.
