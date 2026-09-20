# Yanlış pozitif raporu - sentetik

İlk taslakta `lastmod` alanı olmayan her sayfa "güncellik eksik" sayılıyordu. Bu kural yanlış pozitif üretebilir; çünkü güncellik kanıtı yalnız sitemap `lastmod` ile sınırlı değildir.

Revizyon: kategori, **doğrulanabilir bir güncellik sinyali** arar; sinyalin tek biçimi dayatılmaz. Bu değişiklik sentetik rubric testinde yanlış pozitif riskini düşürür. Gerçek site doğruluğu iddiası değildir.
