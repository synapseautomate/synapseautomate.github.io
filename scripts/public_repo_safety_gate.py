#!/usr/bin/env python3
"""Pre-publication guard. Fails closed on obvious internal sources or secrets.

This is a limited automated check, not a full secret audit or human approval.
"""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
banned_dirs = ("operasyon/", ".github/internal/", "internal/", "private/", "secrets/")
private_methods = {"kinetra-studios/opportunity-scorecard.md", "kinetra-studios/returnops-prompts-v1.md", "kinetra-studios/returnops-bakeoff-v1.csv"}
text_suffixes = {".html", ".js", ".mjs", ".md", ".txt", ".json", ".jsonl", ".csv", ".xml", ".yml", ".yaml", ".py", ".srt"}
secret_rules = [
    re.compile(r"ghp_[A-Za-z0-9]{25,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{25,}"),
    re.compile(r"sk-[A-Za-z0-9]{24,}"),
    re.compile(r"AKIA[A-Z0-9]{16}"),
    re.compile(r"AIza[A-Za-z0-9_-]{30,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
html_only = [
    re.compile(r"ChatGPT\s+dosya\s+indirme", re.I),
    re.compile(r"SIFIR[\s_-]*BA[ĞG]LAMLI\s+(?:OPERAT[ÖO]R\s+)?DEV[İI]R", re.I),
]
for p in root.rglob("*"):
    if not p.is_file():
        continue
    rel = p.relative_to(root).as_posix()
    if any(part in {".git", "_site", "node_modules", "__pycache__"} for part in p.relative_to(root).parts):
        continue
    if rel.startswith(banned_dirs) or rel in private_methods or "/.env" in "/" + rel or rel == ".env" or re.search(r"\.(?:pem|p12|pfx|key)$", rel, re.I):
        errors.append(f"Private source path in public repository: {rel}")
        continue
    if p.suffix.lower() not in text_suffixes:
        continue
    try:
        content = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"Text source cannot be audited: {rel}")
        continue
    for pattern in secret_rules:
        if pattern.search(content):
            errors.append(f"Potential credential in: {rel}")
    if p.suffix.lower() == ".html":
        for pattern in html_only:
            if pattern.search(content):
                errors.append(f"Customer-facing internal note in: {rel}")
if errors:
    print("PUBLIC SOURCE SAFETY GATE: FAIL")
    for item in sorted(set(errors)):
        print("- " + item)
    sys.exit(1)
print("PUBLIC SOURCE SAFETY GATE: PASS (limited automated checks only)")
