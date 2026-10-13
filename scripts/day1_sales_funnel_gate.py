#!/usr/bin/env python3
"""Revenue Day 1: assert exactly one primary intake path. No live submission."""
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[1]
home=(ROOT/'index.html').read_text('utf-8')
solution=(ROOT/'cozumler/e-ticaret-operasyon-otomasyonu.html').read_text('utf-8')
offer=(ROOT/'teklif/e-ticaret-surec-analizi.html').read_text('utf-8')
intake=(ROOT/'surec-analizi.html').read_text('utf-8')
thanks=(ROOT/'talep-alindi.html').read_text('utf-8')
tracker=(ROOT/'assets/js/synapse-measurement-v1.js').read_text('utf-8')

ecommerce_sector=(ROOT/'sektorler/e-ticaret.html').read_text('utf-8')
ecommerce_guide=(ROOT/'rehberler/e-ticaret-ai-otomasyon-satin-alma-rehberi.html').read_text('utf-8')
solutions_hub=(ROOT/'urunler.html').read_text('utf-8')
errors=[]
def check(ok,msg):
    if not ok: errors.append(msg)
check('href="teklif/e-ticaret-surec-analizi.html"' in home,'Home primary offer link missing')
sector_offer='../teklif/e-ticaret-surec-analizi.html'
for name,html in [('Ecommerce sector',ecommerce_sector),('Buyer guide',ecommerce_guide)]:
    check(sector_offer in html,name+' has no direct offer link')
    check('href="../surec-analizi.html?src=ecommerce-' not in html,name+' bypasses offer and sends buyer straight to intake')
check('href="teklif/e-ticaret-surec-analizi.html"' in solutions_hub,'Solutions hub has no e-commerce offer path')
check('href="../teklif/e-ticaret-surec-analizi.html"' in solution,'Sector offer link missing')
check(not re.search(r'<form\b',solution,re.I),'Duplicate E-commerce FormSubmit form still present')
check('href="../surec-analizi.html?' in offer,'Offer to central intake link missing')
check('4.900 TL' in offer and '$149' in offer,'Price list missing')
check('kur dönüşümü değildir' in offer,'Independent USD/TRY boundary missing')
check(len(re.findall(r'<form\b',intake,re.I))==1,'Expected exactly one central form')
check('data-synapse-lead="process_analysis"' in intake,'Lead event marker missing')
check('submitted=process_analysis' in intake,'Form redirect marker missing')
check('data-synapse-success="process_analysis"' in thanks,'Return marker mismatch')
check('noindex,follow' in thanks,'Thank-you page not noindex')
check("emit('generate_lead'" in tracker,'GA4 lead signal missing; admin key-event still requires human setup')
print('Revenue Day1 sales-funnel static gate:', 'PASS' if not errors else 'FAIL')
for problem in errors: print(' -',problem)
sys.exit(1 if errors else 0)
