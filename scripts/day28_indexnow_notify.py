#!/usr/bin/env python3
"""Notify IndexNow ONLY after a successful Pages deployment. Never commits or deploys."""
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

BASE="https://synapseautomate.github.io/"
KEY="b92e13eb5417ef94e6aa9a04c7d7333a"
ROOT=Path(__file__).resolve().parents[1]

def changed_html():
    try:
        res=subprocess.check_output(["git","show","--pretty=format:","--name-only","--diff-filter=AM",os.environ["RELEASE_SHA"]],text=True)
        return sorted({n.strip() for n in res.splitlines() if n.strip().endswith(".html")})
    except (subprocess.CalledProcessError,KeyError):
        raise SystemExit("Release commit inspection unavailable; aborting IndexNow")

def eligible(path):
    if path.startswith((".github/","D01/","D02/","D03/")) or path in ("404.html","talep-alindi.html"):
        return False
    file=ROOT/path
    if not file.is_file() or ".." in Path(path).parts:
        return False
    html=file.read_text("utf-8")
    tags=re.findall(r"<meta\b[^>]*>",html,re.I)
    if any(re.search(r'name\s*=\s*["\']robots["\']',t,re.I) and re.search(r'noindex',t,re.I) for t in tags):
        return False
    return True

def main():
    urls=[BASE if n=="index.html" else BASE+n for n in changed_html() if eligible(n)]
    if not urls:
        print("IndexNow: no changed indexable HTML pages; skipped")
        return
    keyfile=ROOT/(KEY+".txt")
    if not keyfile.is_file() or keyfile.read_text("utf-8").strip()!=KEY:
        raise SystemExit("IndexNow: static ownership file invalid")
    with urllib.request.urlopen(BASE+KEY+".txt",timeout=20) as r:
        if r.read().decode("utf-8").strip()!=KEY:
            raise SystemExit("IndexNow: live ownership key mismatch")
    payload=json.dumps({"host":"synapseautomate.github.io","key":KEY,"keyLocation":BASE+KEY+".txt","urlList":urls}).encode("utf-8")
    req=urllib.request.Request("https://api.indexnow.org/indexnow",data=payload,headers={"Content-Type":"application/json; charset=utf-8"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=30) as r:
            code=r.status
    except urllib.error.HTTPError as e:
        raise SystemExit("IndexNow: notification rejected HTTP "+str(e.code))
    if code not in (200,202):
        raise SystemExit("IndexNow: unexpected response "+str(code))
    print("IndexNow accepted "+str(len(urls))+" changed indexable URLs, HTTP "+str(code)+". No indexing guarantee.")

if __name__=="__main__":
    main()
