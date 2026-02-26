import requests
import os

images = {
    "https://m.media-amazon.com/images/I/61-oTP1X4rL._AC_SL1500_.jpg": "assets/images/macbook_hero.jpg",
    "https://m.media-amazon.com/images/I/61F6Ng0di0L._AC_SL1500_.jpg": "assets/images/macbook_internal.jpg"
}

os.makedirs("assets/images", exist_ok=True)

for url, path in images.items():
    print(f"Downloading {url} to {path}...")
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Success")
        else:
            print(f"Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
