from bs4 import BeautifulSoup
import re, pathlib, sys

# authoritative mapping
MAPPING = {
  "B0BQSLL3J2": "https://www.amazon.com/dp/B0BQSLL3J2?tag=techstackglob-20",
  "B0DKX5T4XT": "https://www.amazon.com/dp/B0DKX5T4XT?tag=techstackglob-20",
  "B08DWD38VD": "https://www.amazon.com/dp/B08DWD38VD?tag=techstackglob-20",
  "B0B6GHW1SX": "https://www.amazon.com/dp/B0B6GHW1SX?tag=techstackglob-20",
  # add others if needed
}

DP_RE = re.compile(r"/dp/([A-Z0-9]{10})")
GP_RE = re.compile(r"/gp/product/([A-Z0-9]{10})")
ASIN_ANY = re.compile(r"/([A-Z0-9]{10})(?:[/?]|$)")

posts = list(pathlib.Path("posts").glob("*.html"))

def norm_href(href):
    if not href or "amazon." not in href:
        return None
    # try /dp/
    m = DP_RE.search(href)
    if m:
        asin = m.group(1)
    else:
        m = GP_RE.search(href)
        if m:
            asin = m.group(1)
        else:
            m = ASIN_ANY.search(href)
            asin = m.group(1) if m else None
    if not asin:
        return None
    # if we have mapping use it
    if asin in MAPPING:
        return MAPPING[asin]
    # otherwise normalize to dp + site tag
    return f"https://www.amazon.com/dp/{asin}?tag=techstackglob-20"

def process_file(p: pathlib.Path):
    text = p.read_text(encoding="utf-8")
    soup = BeautifulSoup(text, "html.parser")
    changed = False
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "amazon." in href:
            new = norm_href(href)
            if new and new != href:
                a["href"] = new
                # enforce attributes
                a["target"] = "_blank"
                a["rel"] = "nofollow noopener sponsored"
                changed = True
    if changed:
        p.write_text(str(soup), encoding="utf-8")
        print("Updated:", p)
    else:
        print("No change:", p)

if __name__ == "__main__":
    for f in posts:
        process_file(f)
    print("Done. Now run tests (grep/seo_audit).")
