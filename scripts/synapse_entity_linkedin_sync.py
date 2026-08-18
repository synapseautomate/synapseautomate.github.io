from pathlib import Path
import json
import re

ROOT = Path(".").resolve()
LINKEDIN = "https://www.linkedin.com/company/synapseautomate/"
EXCLUDE = {".git", ".github", "_site", "node_modules", "__pycache__", "D01", "D02"}

SCRIPT_RE = re.compile(
    r'(<script\b[^>]*\btype=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.IGNORECASE | re.DOTALL,
)

def excluded(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return any(part in EXCLUDE for part in rel.parts)

def has_org_type(value) -> bool:
    if value == "Organization":
        return True
    if isinstance(value, list):
        return "Organization" in value
    return False

def sync_org(node):
    changed = False
    found = 0

    if isinstance(node, dict):
        if has_org_type(node.get("@type")):
            found += 1
            same_as = node.get("sameAs", [])
            if isinstance(same_as, str):
                same_as = [same_as]
            elif not isinstance(same_as, list):
                same_as = []

            if LINKEDIN not in same_as:
                same_as.append(LINKEDIN)
                node["sameAs"] = same_as
                changed = True

        for key, value in list(node.items()):
            c, f = sync_org(value)
            changed = changed or c
            found += f

    elif isinstance(node, list):
        for value in node:
            c, f = sync_org(value)
            changed = changed or c
            found += f

    return changed, found

html_files = sorted(
    p for p in ROOT.rglob("*")
    if p.is_file()
    and p.suffix.lower() in {".html", ".htm"}
    and not excluded(p)
)

changed_files = []
org_blocks = 0
org_with_linkedin = 0
invalid_jsonld = []

for path in html_files:
    text = path.read_text(encoding="utf-8")
    file_changed = False

    def repl(match):
        nonlocal_marker = None
        raw = match.group(2).strip()
        try:
            data = json.loads(raw)
        except Exception as exc:
            invalid_jsonld.append((path.relative_to(ROOT).as_posix(), str(exc)))
            return match.group(0)

        changed, found = sync_org(data)
        if found:
            # Count every Organization object after sync.
            def count_linkedin(node):
                total = linked = 0
                if isinstance(node, dict):
                    if has_org_type(node.get("@type")):
                        total += 1
                        same_as = node.get("sameAs", [])
                        if isinstance(same_as, str):
                            same_as = [same_as]
                        if isinstance(same_as, list) and LINKEDIN in same_as:
                            linked += 1
                    for v in node.values():
                        t, l = count_linkedin(v)
                        total += t
                        linked += l
                elif isinstance(node, list):
                    for v in node:
                        t, l = count_linkedin(v)
                        total += t
                        linked += l
                return total, linked

            t, l = count_linkedin(data)
            stats["org"] += t
            stats["linked"] += l

        if not changed:
            return match.group(0)

        stats["changed_here"] = True
        compact = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        return match.group(1) + compact + match.group(3)

    stats = {"org": 0, "linked": 0, "changed_here": False}
    new_text = SCRIPT_RE.sub(repl, text)
    org_blocks += stats["org"]
    org_with_linkedin += stats["linked"]

    # Make the verified LinkedIn property visible on the entity home as well.
    if path.name == "bilgi.html":
        old = '<li><a href="https://github.com/synapseautomate">GitHub</a></li></ul>'
        new = (
            '<li><a href="https://github.com/synapseautomate">GitHub</a></li>'
            '<li><a href="https://www.linkedin.com/company/synapseautomate/">LinkedIn şirket sayfası</a></li></ul>'
        )
        if old in new_text and LINKEDIN not in new_text.split("Resmi dijital varlıklar", 1)[-1]:
            new_text = new_text.replace(old, new, 1)

        note_old = (
            'LinkedIn/YouTube yalnız doğrulanmış kurumsal URL kesinleştiğinde '
            'sameAs listesine eklenir.'
        )
        note_new = (
            'LinkedIn şirket sayfası doğrulanmış resmi kurumsal varlıktır. '
            'YouTube yalnız doğrulanmış kurumsal URL kesinleştiğinde sameAs listesine eklenir.'
        )
        if note_old in new_text:
            new_text = new_text.replace(note_old, note_new, 1)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8", newline="\n")
        changed_files.append(path.relative_to(ROOT).as_posix())

# Add the official LinkedIn URL to llms.txt as a discovery convenience index.
llms = ROOT / "llms.txt"
if llms.exists():
    text = llms.read_text(encoding="utf-8")
    line = f"Official LinkedIn: {LINKEDIN}"
    if line not in text:
        anchor = "Organization profile: https://synapseautomate.github.io/bilgi.html"
        if anchor in text:
            text = text.replace(anchor, anchor + "\n" + line, 1)
        else:
            text = text.rstrip() + "\n" + line + "\n"
        llms.write_text(text, encoding="utf-8", newline="\n")
        changed_files.append("llms.txt")

# Hard QA.
if invalid_jsonld:
    print("Invalid JSON-LD:")
    for rel, err in invalid_jsonld:
        print(f"ERROR {rel}: {err}")
    raise SystemExit(1)

if org_blocks == 0:
    raise SystemExit("No Organization JSON-LD blocks were found.")

if org_with_linkedin != org_blocks:
    raise SystemExit(
        f"Entity sync incomplete: {org_with_linkedin}/{org_blocks} Organization blocks contain LinkedIn."
    )

if llms.exists() and f"Official LinkedIn: {LINKEDIN}" not in llms.read_text(encoding="utf-8"):
    raise SystemExit("llms.txt does not contain the verified LinkedIn URL.")

bilgi = ROOT / "bilgi.html"
if bilgi.exists() and LINKEDIN not in bilgi.read_text(encoding="utf-8"):
    raise SystemExit("bilgi.html does not contain the verified LinkedIn URL.")

changed_files = list(dict.fromkeys(changed_files))
print(f"HTML files scanned: {len(html_files)}")
print(f"Organization objects found: {org_blocks}")
print(f"Organization objects with LinkedIn sameAs: {org_with_linkedin}")
print(f"Files changed: {len(changed_files)}")
for rel in changed_files:
    print("UPDATED:", rel)
print("ENTITY + LINKEDIN SYNC QA: PASS")
