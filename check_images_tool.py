import sys
import urllib.request
import re

def check_asin_images(asin):
    print(f"Checking images for ASIN: {asin}")
    # Try the standard ASIN-based URL pattern first
    for i in range(1, 10):
        v = f"{i:02d}"
        url = f"https://images-na.ssl-images-amazon.com/images/P/{asin}.{v}._SCLZZZZZZZ_.jpg"
        try:
            req = urllib.request.Request(url, method='HEAD')
            with urllib.request.urlopen(req) as resp:
                if resp.status == 200:
                    content_length = resp.getheader('Content-Length')
                    if content_length and int(content_length) > 5000:
                        print(f"VALID: {url} (Size: {content_length})")
                    else:
                        print(f"INVALID (small/empty): {url}")
        except Exception as e:
            # print(f"ERROR: {url} - {e}")
            pass

if __name__ == "__main__":
    asins = ["B0D9R7Q449", "B0FBXD383M"]
    for asin in asins:
        check_asin_images(asin)
