import urllib.request
import re

def get_all_image_data(asin):
    url = f"https://www.amazon.com/dp/{asin}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            # Look for the 'colorImages' JSON which usually contains high-res images
            matches = re.findall(r'https://m\.media-amazon\.com/images/I/([A-Za-z0-9_\-]+)\.', html)
            unique_ids = []
            seen = set()
            for i in matches:
                if len(i) > 8 and i not in seen:
                    unique_ids.append(i)
                    seen.add(i)
            print(f"ASIN {asin} discovered IDs: {unique_ids}")
    except Exception as e:
        print(f"Error for {asin}: {e}")

if __name__ == "__main__":
    get_all_image_data("B0FBXD383M") # Dell
    get_all_image_data("B0D9R7Q449") # LG
