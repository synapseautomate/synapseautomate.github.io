from pathlib import Path
from html.parser import HTMLParser
import html
import json
import re
import unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(".").resolve()
EXCLUDE = {".git", ".github", "_site", "node_modules", "__pycache__", "D01", "D02", "D03"}
SUFFIXES = {".html", ".htm", ".txt", ".xml", ".json", ".js", ".css", ".svg", ".md", ".csv", ".webmanifest"}

TR_LETTER = "A-Za-z\u00c7\u011e\u0130\u00d6\u015e\u00dc\u00e7\u011f\u0131\u00f6\u015f\u00fc"
EMBEDDED_AI = re.compile(
    rf"(?P<left>[{TR_LETTER}])yapay\s+zek(?:\u00e2|a)(?P<right>[{TR_LETTER}])",
    re.IGNORECASE,
)

KNOWN = {
    "PASS/Fyapay zek\u00e2L": "PASS/FAIL",
    "PASS/Fyapay zekaL": "PASS/FAIL",
    "Teknoloji Yap\u0131s\u0131u": "Teknoloji Yap\u0131s\u0131",
    "Teknoloji Yap\u0131s\u0131\u00fc": "Teknoloji Yap\u0131s\u0131",
    "Teknoloji Yap\u0131s\u0131\u0131": "Teknoloji Yap\u0131s\u0131",
    "Teknoloji Yap\u0131s\u0131i": "Teknoloji Yap\u0131s\u0131",
    "Teknoloji Yap\u0131s\u0131\u0131n": "Teknoloji Yap\u0131s\u0131n\u0131n",
    "Teknoloji Yap\u0131s\u0131in": "Teknoloji Yap\u0131s\u0131n\u0131n",
    "Teknoloji Yap\u0131s\u0131a": "Teknoloji Yap\u0131s\u0131na",
    "Teknoloji Yap\u0131s\u0131e": "Teknoloji Yap\u0131s\u0131na",
    "Teknoloji Yap\u0131s\u0131da": "Teknoloji Yap\u0131s\u0131nda",
    "Teknoloji Yap\u0131s\u0131de": "Teknoloji Yap\u0131s\u0131nda",
    "Teknoloji Yap\u0131s\u0131dan": "Teknoloji Yap\u0131s\u0131ndan",
    "Teknoloji Yap\u0131s\u0131den": "Teknoloji Yap\u0131s\u0131ndan",
}

MOJIBAKE = {
    "\u00c3\u00a7": "\u00e7",
    "\u00c4\u0178": "\u011f",
    "\u00c4\u00b1": "\u0131",
    "\u00c4\u00b0": "\u0130",
    "\u00c3\u00b6": "\u00f6",
    "\u00c3\u00bc": "\u00fc",
    "\u00c5\u0178": "\u015f",
    "\u00e2\u20ac\u2122": "\u2019",
    "\u00e2\u20ac\u201c": "\u2014",
    "\u00e2\u20ac\u00a6": "\u2026",
    "\u00c2\u00a0": " ",
}

MOJIBAKE_MARKERS = ("\u00c3", "\u00c4", "\u00c5", "\u00e2\u20ac", "\u00c2")
ZERO_WIDTH = ("\u200b", "\u200c", "\u200d", "\u2060", "\ufeff")

def candidate(path):
    if not path.is_file():
        return False
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDE for part in rel.parts):
        return False
    if path.suffix.lower() not in SUFFIXES:
        return False
    if re.fullmatch(r"google[a-z0-9_-]+\.html", path.name.lower()):
        return False
    return True

def repair_text(text):
    text = unicodedata.normalize("NFC", text)
    for ch in ZERO_WIDTH:
        text = text.replace(ch, "")
    for bad, good in MOJIBAKE.items():
        text = text.replace(bad, good)
    for bad, good in KNOWN.items():
        text = text.replace(bad, good)
    for _ in range(20):
        new = EMBEDDED_AI.sub(
            lambda m: m.group("left")
            + ("AI" if m.group("left").isupper() and m.group("right").isupper() else "ai")
            + m.group("right"),
            text,
        )
        if new == text:
            break
        text = new
    return unicodedata.normalize("NFC", text)

class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() in {"script", "style"}:
            self.skip += 1

    def handle_endtag(self, tag):
        if tag.lower() in {"script", "style"} and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

files = sorted(p for p in ROOT.rglob("*") if candidate(p))
if not files:
    raise SystemExit("No public text-bearing files found.")

changed = []
decode_errors = []

for path in files:
    raw = path.read_bytes()
    try:
        original = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        decode_errors.append((path, str(exc)))
        continue
    repaired = repair_text(original)
    if repaired != original:
        path.write_text(repaired, encoding="utf-8", newline="\n")
        changed.append(path.relative_to(ROOT).as_posix())

hard = []

def add_issue(path, line, kind, context=""):
    rel = path.relative_to(ROOT).as_posix()
    context = " ".join(str(context).split())[:220]
    hard.append((rel, line, kind, context))

for path, exc in decode_errors:
    add_issue(path, 1, "not valid UTF-8", exc)

for path in files:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    for n, line in enumerate(text.splitlines() or [""], 1):
        if "\ufffd" in line:
            add_issue(path, n, "Unicode replacement character", line)
        if any(ch in line for ch in ZERO_WIDTH):
            add_issue(path, n, "zero-width character", line)
        if EMBEDDED_AI.search(line):
            add_issue(path, n, "AI bulk replacement still embedded in a word", line)
        if any(marker in line for marker in MOJIBAKE_MARKERS):
            add_issue(path, n, "possible mojibake or encoding corruption", line)
        if "&amp;amp;" in line or "&#65533;" in line:
            add_issue(path, n, "broken or double HTML entity", line)

    suffix = path.suffix.lower()
    if suffix in {".html", ".htm"}:
        parser = VisibleText()
        try:
            parser.feed(text)
            visible = html.unescape(" ".join(parser.parts))
        except Exception as exc:
            add_issue(path, 1, "HTML parser failure", exc)
            visible = ""
        for marker in ("[object Object]", "undefined undefined", "\ufffd"):
            if marker in visible:
                add_issue(path, 1, "visible runtime or text artifact", marker)

    if suffix in {".json", ".webmanifest"}:
        try:
            json.loads(text)
        except Exception as exc:
            add_issue(path, 1, "invalid JSON", exc)

    if suffix in {".xml", ".svg"}:
        try:
            ET.fromstring(text)
        except Exception as exc:
            add_issue(path, 1, "invalid XML or SVG", exc)

hard = list(dict.fromkeys(hard))

print("Files scanned:", len(files))
print("Files repaired:", len(changed))
for rel in changed:
    print("REPAIRED:", rel)

if hard:
    print("Unresolved hard issues:", len(hard))
    for rel, line, kind, context in hard[:100]:
        print(f"ERROR {rel}:{line} | {kind} | {context}")
    raise SystemExit(1)

print("TEXT INTEGRITY QA: PASS")
