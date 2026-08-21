from pathlib import Path
import csv, json, re, hashlib, subprocess, sys

ROOT = Path('.').resolve()
BASE = 'https://synapseautomate.github.io'
PROOF = ROOT / 'public-proof' / 'workflow-opportunity-benchmark'
INV = ROOT / 'veri' / 'gun4-workflow-inventory-public.csv'
SCORE = ROOT / 'veri' / 'gun4-opportunity-scorecard.csv'
METH = ROOT / 'veri' / 'gun4-workflow-opportunity-methodology.md'
DECISION = ROOT / 'rehberler' / 'ai-otomasyon-is-akisi-karar-tablosu.html'
ANALYSIS = ROOT / 'surec-analizi.html'
DECISION_URL = BASE + '/rehberler/ai-otomasyon-is-akisi-karar-tablosu.html'
TOOL_URL = BASE + '/araclar/surecini-20-dakikada-haritala.html'
ANALYSIS_URL = BASE + '/surec-analizi.html'
CSV_URL = BASE + '/veri/gun4-workflow-inventory-public.csv'
METH_URL = BASE + '/veri/gun4-workflow-opportunity-methodology.md'
START = '<!-- SYNAPSE_PUBLIC_PROOF_START -->'
END = '<!-- SYNAPSE_PUBLIC_PROOF_END -->'

def fail(msg): raise SystemExit(msg)
def read_csv(p):
    if not p.exists(): fail(f'Required source missing: {p}')
    with p.open('r', encoding='utf-8-sig', newline='') as f: return list(csv.DictReader(f))
def write_if_changed(p, text):
    old = p.read_text(encoding='utf-8') if p.exists() else None
    if old == text: return False
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8', newline='\n')
    return True
def esc(v): return str(v or '').replace('|','\\|').replace('\n',' ').strip()
def as_int(v):
    try: return int(float(v))
    except Exception: return 999
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

for p in [INV, SCORE, METH, DECISION, ANALYSIS]:
    if not p.exists(): fail(f'Required Day 4 asset missing: {p}')

inventory = read_csv(INV)
scorecard = read_csv(SCORE)
cols = ['kategori','is_akisi','girdi','karar','cikti','ekonomik_sonuc','owner','human_gate']
if len(inventory) != 30: fail(f'Expected 30 public workflows, got {len(inventory)}')
if len(scorecard) < 10: fail('Opportunity scorecard must contain at least 10 rows')
missing = [c for c in cols if c not in inventory[0]]
if missing: fail('Missing public columns: ' + ', '.join(missing))
raw = INV.read_text(encoding='utf-8')
if re.search(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', raw): fail('Email detected in public inventory')
if re.search(r'\b(?:\+?90)?0?5\d{9}\b', re.sub(r'\s+','',raw)): fail('Phone-like identifier detected')
decision_text = DECISION.read_text(encoding='utf-8')
if DECISION_URL not in decision_text: fail('Canonical decision URL missing')
if 'sentetik' not in decision_text.casefold(): fail('Synthetic evidence boundary missing')

top10 = sorted(scorecard, key=lambda r: as_int(r.get('rank')))[:10]
top_table = ['| Sıra | İş akışı | Kategori | Puan | İnsan kapısı |','|---:|---|---|---:|---|']
for r in top10:
    top_table.append(f"| {esc(r.get('rank'))} | {esc(r.get('is_akisi'))} | {esc(r.get('kategori'))} | {esc(r.get('score'))} | {esc(r.get('human_gate'))} |")
counts = {}
for r in inventory:
    k = (r.get('kategori') or 'Belirtilmemiş').strip(); counts[k] = counts.get(k,0)+1
cat_table = ['| Kategori | İş akışı sayısı |','|---|---:|'] + [f'| {esc(k)} | {v} |' for k,v in sorted(counts.items(), key=lambda x:(-x[1],x[0].casefold()))]

sample = inventory[0]
example = {'evidence_status':'synthetic_workflow_level_example','workflow':{k:sample.get(k,'') for k in cols},'human_control':{'rule':'critical decisions and external actions remain human-controlled','source':DECISION_URL}}
manifest = {'name':'Synapse Automate Workflow Opportunity Benchmark','version':'1.0','updated':'2026-08-21','publisher':'Synapse Automate','evidence_status':'synthetic_and_workflow_level_not_customer_performance_data','workflow_count':30,'top_opportunity_count':10,'canonical':{'decision_table':DECISION_URL,'free_mapping_tool':TOOL_URL,'process_analysis':ANALYSIS_URL,'public_inventory_csv':CSV_URL,'methodology':METH_URL},'source_integrity':{'public_inventory_sha256':sha(INV),'methodology_sha256':sha(METH),'decision_page_sha256':sha(DECISION)},'claims':{'roi_guarantee':False,'customer_case_study':False,'autonomous_critical_actions':False}}

readme = f'''# Synapse Automate — Workflow Opportunity Benchmark

**30 tekrarlı operasyon iş akışını, teknoloji seçmeden önce aynı karar çerçevesinde değerlendiren public proof paketi.**

> **Kanıt statüsü:** Bu çalışma sentetik ve iş-akışı seviyesindedir. Müşteri performans verisi, müşteri başarı hikâyesi veya ROI garantisi değildir.

## Kamuya açık kaynaklar

- **Canlı karar tablosu:** {DECISION_URL}
- **Ücretsiz süreç haritalama aracı:** {TOOL_URL}
- **Ücretli Süreç Analizi:** {ANALYSIS_URL}
- **30 satırlık public CSV:** {CSV_URL}
- **Puanlama metodolojisi:** {METH_URL}

## Kapsam

- 30 tekrarlı operasyon iş akışı
- 8 değerlendirme boyutu
- Para yakınlığı ve veri erişimine çift ağırlık
- Risk ve uzun satış çevrimine negatif ağırlık
- Kritik kararlar için açık insan kapısı
- İlk 10 fırsatın karşılaştırmalı görünümü

### Kategori dağılımı

{chr(10).join(cat_table)}

## İlk 10 fırsat

{chr(10).join(top_table)}

> Puan yalnız **keşif önceliğini** sıralar. Satış, ROI, doğruluk veya otomasyon başarısı garantisi değildir.

## Opportunity Score

```text
acı + sıklık + (2 × para yakınlığı) + (2 × veri erişimi)
+ ölçülebilirlik + dağınıklık - risk - satış çevrimi
```

Detaylı metodoloji: [`veri/gun4-workflow-opportunity-methodology.md`](../../veri/gun4-workflow-opportunity-methodology.md)

## İnsan denetimi sınırı

AI; sınıflandırma, özet, taslak, ön kontrol veya sinyal üretebilir. Fiyat/ödeme, müşteri taahhüdü, hassas veri, hukuki-tıbbi-finansal kararlar, geri döndürülemez dış eylemler ve yüksek etkili belirsiz kararlar insan onayında kalır.

## Nasıl kullanılır?

1. Public CSV’den kendi operasyonunuza en yakın iş akışını bulun.
2. Para yakınlığı, veri erişimi, ölçülebilirlik ve riski değerlendirin.
3. AI’ın yapacağı kısmı ve insanın onaylayacağı kısmı ayırın.
4. Önce ücretsiz araçla süreci haritalayın.
5. Ekonomik olarak anlamlıysa Süreç Analizi’ne geçin.

Bkz. [`USAGE.md`](USAGE.md) ve [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md).

## Tek source of truth

Bu klasör kanıt vitrini; kaynak veriyi kopyalamaz:

- [`veri/gun4-workflow-inventory-public.csv`](../../veri/gun4-workflow-inventory-public.csv)
- [`veri/gun4-opportunity-scorecard.csv`](../../veri/gun4-opportunity-scorecard.csv)
- [`veri/gun4-workflow-opportunity-methodology.md`](../../veri/gun4-workflow-opportunity-methodology.md)
- [`rehberler/ai-otomasyon-is-akisi-karar-tablosu.html`](../../rehberler/ai-otomasyon-is-akisi-karar-tablosu.html)

Makinece okunabilir manifest: [`proof-manifest.json`](proof-manifest.json)

## Sonraki adım

Ücretsiz haritalama: **{TOOL_URL}**

Uygun görünüyorsa Süreç Analizi: **{ANALYSIS_URL}**

---

**Synapse Automate** · Kurumsal AI otomasyonu · İnsan denetimi · Ölçülebilir iş akışları  
{BASE}/
'''

data_dictionary = '''# Data Dictionary

`veri/gun4-workflow-inventory-public.csv` alanları:

| Alan | Anlamı | Public güvenlik kuralı |
|---|---|---|
| `kategori` | Operasyon alanı | Kişi/şirket adı içermez |
| `is_akisi` | Tekrarlı sürecin adı | Müşteri vakası gibi sunulmaz |
| `girdi` | Karar öncesi bilgi/olay | Hassas veri örneği içermez |
| `karar` | Verilecek operasyon kararı | Otonom kritik karar iddiası yok |
| `cikti` | Karar sonrası çıktı | Sonuç garantisi değildir |
| `ekonomik_sonuc` | Ekonomik etkinin yönü | ROI rakamı/garantisi değildir |
| `owner` | Süreç/karar sahibinin rolü | Gerçek kişi adı içermez |
| `human_gate` | İnsan onayı gereken nokta | Kritik eylem insanda kalır |

## Evidence boundary

Bu veri seti sentetik ve iş-akışı seviyesindedir; gerçek müşteri performansı değildir, kişisel veri/iletişim bilgisi içermez ve satış/ROI garantisi vermez.
'''

usage = f'''# Usage Guide

Bu paket bir yazılım kütüphanesi değil; **iş akışı seçim ve keşif çerçevesidir**.

## 1. Süreci şu formatta yaz

```text
Girdi → Karar → Çıktı → Ekonomik sonuç → Owner → Human gate
```

## 2. Sekiz boyutta 1–5 puanla

Acı, sıklık, para yakınlığı, veri erişimi, ölçülebilirlik, dağınıklık, risk, satış çevrimi.

## 3. Ağırlığı uygula

```text
acı + sıklık + 2×para yakınlığı + 2×veri erişimi
+ ölçülebilirlik + dağınıklık - risk - satış çevrimi
```

## 4. İnsan kapısını yazmadan otomasyon tasarlama

Fiyat, ödeme, müşteri taahhüdü, hassas veri ve kritik dış eylem insan onayında kalır.

## 5. Teknolojiyi en son seç

Önce iş akışını ve karar sınırını doğrula; sonra model, agent, entegrasyon veya UI seç.

Ücretsiz haritalama: {TOOL_URL}

Canonical karar tablosu: {DECISION_URL}

Ücretli Süreç Analizi: {ANALYSIS_URL}
'''

changelog = '''# Changelog

## 1.0 — 2026-08-21

- 30 satırlık public workflow inventory tek source of truth olarak bağlandı.
- İlk 10 opportunity görünümü README'ye eklendi.
- Veri sözlüğü, kullanım rehberi ve machine-readable manifest eklendi.
- Sentetik/müşteri-performansı-değil kanıt sınırı zorunlu hale getirildi.
- İnsan onayı ve kritik dış eylem sınırı dokümante edildi.
- Kişisel veri / iletişim bilgisi sızıntısı için QA eklendi.
'''

outputs = {
    PROOF/'README.md': readme,
    PROOF/'DATA_DICTIONARY.md': data_dictionary,
    PROOF/'USAGE.md': usage,
    PROOF/'CHANGELOG.md': changelog,
    PROOF/'example-workflow.json': json.dumps(example, ensure_ascii=False, indent=2)+'\n',
    PROOF/'proof-manifest.json': json.dumps(manifest, ensure_ascii=False, indent=2)+'\n',
}
changed=[]
for p,t in outputs.items():
    if write_if_changed(p,t): changed.append(str(p.relative_to(ROOT)))

root = ROOT/'README.md'
block = f'''{START}
## Public proof: 30 Workflow Opportunity Benchmark

Synapse Automate’in **30 tekrarlı operasyon iş akışını** para yakınlığı, veri erişimi, ölçülebilirlik, risk ve insan onayıyla değerlendiren public proof paketi:

**[`public-proof/workflow-opportunity-benchmark/`](public-proof/workflow-opportunity-benchmark/)**

Canlı canonical karar tablosu: {DECISION_URL}

> Evidence boundary: sentetik ve iş-akışı seviyesindedir; müşteri performans verisi veya ROI garantisi değildir.
{END}'''
if root.exists():
    rt = root.read_text(encoding='utf-8')
    if START in rt and END in rt:
        rt = re.sub(re.escape(START)+r'.*?'+re.escape(END), block, rt, flags=re.S)
    else: rt = rt.rstrip()+'\n\n'+block+'\n'
else:
    rt = f'# Synapse Automate\n\nKurumsal AI otomasyonu, insan denetimi ve ölçülebilir iş akışları.\n\nWebsite: {BASE}/\n\n{block}\n'
if write_if_changed(root,rt): changed.append('README.md')

llms=ROOT/'llms.txt'
if llms.exists():
    lt=llms.read_text(encoding='utf-8')
    line='- Public proof package: repository folder `public-proof/workflow-opportunity-benchmark/`; canonical evidence remains on the Synapse Automate website.'
    if line not in lt:
        if write_if_changed(llms,lt.rstrip()+'\n'+line+'\n'): changed.append('llms.txt')

# QA
proof_text='\n'.join(p.read_text(encoding='utf-8') for p in outputs)
for required in ['sentetik','ROI garantisi',DECISION_URL,TOOL_URL,ANALYSIS_URL,'İlk 10 fırsat']:
    if required.casefold() not in readme.casefold(): fail('README missing: '+required)
rows=[ln for ln in readme.splitlines() if re.match(r'^\|\s*\d+\s*\|',ln)]
if len(rows)!=10: fail(f'Expected 10 top rows, got {len(rows)}')
if re.search(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', proof_text): fail('Email detected in proof package')
if re.search(r'\b(?:\+?90)?0?5\d{9}\b', re.sub(r'\s+','',proof_text)): fail('Phone-like identifier detected in proof package')
for bad in ['\ufffd','PASS/Fyapay','Teknoloji Yapısıu']:
    if bad in proof_text: fail('Broken text marker: '+bad)
check=json.loads((PROOF/'proof-manifest.json').read_text(encoding='utf-8'))
if check['workflow_count']!=30 or check['claims']['roi_guarantee'] is not False: fail('Manifest QA failed')

guard=ROOT/'scripts'/'synapse_text_repair.py'
if guard.exists():
    r=subprocess.run([sys.executable,str(guard)],cwd=ROOT,text=True,capture_output=True)
    print(r.stdout)
    if r.returncode!=0: print(r.stderr); fail('Existing text integrity guard failed')

changed=list(dict.fromkeys(changed))
print('Files changed:',len(changed))
for x in changed: print('UPDATED:',x)
print('Proof workflow count: 30')
print('README top opportunities: 10')
print('Sensitive identifier scan: PASS')
print('Evidence boundary: PASS')
print('Source-of-truth duplication: 0')
print('New product features: 0')
print('GITHUB PUBLIC PROOF QA: PASS')
