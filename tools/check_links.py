from bs4 import BeautifulSoup
import pathlib, requests, sys, re

files = list(pathlib.Path("posts").glob("*.html"))
bad = []
for f in files:
    s = f.read_text(encoding="utf-8")
    soup = BeautifulSoup(s, "html.parser")
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("http"):
            try:
                r = requests.head(href, allow_redirects=True, timeout=10)
                code = r.status_code
            except Exception as e:
                code = None
            if code != 200:
                bad.append((str(f), href, code))
for b in bad:
    print("BROKEN:", b)
if not bad:
    print("All external links returned 200 (or were untested).")
