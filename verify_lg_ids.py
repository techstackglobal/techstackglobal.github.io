import urllib.request

def verify_ids(asin, ids):
    print(f"Verifying IDs for {asin}:")
    for img_id in ids:
        url = f"https://m.media-amazon.com/images/I/{img_id}._AC_SL1500_.jpg"
        try:
            req = urllib.request.Request(url, method='HEAD')
            with urllib.request.urlopen(req) as resp:
                if resp.status == 200:
                    size = resp.getheader('Content-Length')
                    print(f"ID: {img_id}, URL: {url}, Size: {size}")
        except:
            pass

if __name__ == "__main__":
    # LG IDs I found
    lg_ids = ['61xJcNKKLXL', '517f0agMn-L', '51waPb-h-9L'] # Filtering for ones that look like real IDs
    verify_ids("B0D9R7Q449", lg_ids)
    
    # Dell IDs - let's try some common ones if I can't find them from the script
    # User said previous was invisible. Let's try to find the actual primary ID.
    dell_ids = ['61FBXD383M', '71FBXD383M'] # Generic guesses
    verify_ids("B0FBXD383M", dell_ids)
