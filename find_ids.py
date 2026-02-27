import urllib.request
import re

def get_image_ids(asin):
    url = f"https://www.amazon.com/dp/{asin}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            # Look for image lists in the JSON blob or img tags
            # Common pattern: "hiRes":"https://m.media-amazon.com/images/I/ID.jpg"
            ids = re.findall(r'https://m\.media-amazon\.com/images/I/([A-Za-z0-9_\-]+)\.', html)
            unique_ids = list(dict.fromkeys([i for i in ids if len(i) > 8]))
            print(f"ASIN {asin} found IDs: {unique_ids[:10]}")
    except Exception as e:
        print(f"Error for {asin}: {e}")

if __name__ == "__main__":
    get_image_ids("B0D9R7Q449") # LG
    get_image_ids("B0FBXD383M") # Dell
