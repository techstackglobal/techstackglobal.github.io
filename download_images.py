import os
import re
import urllib.request
from pathlib import Path

# Setup directories
base_dir = Path(r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog")
assets_dir = base_dir / "assets" / "images" / "products"
assets_dir.mkdir(parents=True, exist_ok=True)

# Regex to find Amazon image URLs
img_regex = re.compile(r'https://m\.media-amazon\.com/images/I/([A-Za-z0-9_\-\.]+?\.jpg)')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def download_image(url, filename):
    filepath = assets_dir / filename
    if not filepath.exists():
        print(f"Downloading {url} to {filepath}")
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download {url}: {e}")
    return filepath

def process_file(html_file):
    print(f"Processing {html_file.name}...")
    content = html_file.read_text(encoding='utf-8')
    matches = img_regex.findall(content)
    if not matches:
        return

    for img_id in set(matches):
        url = f"https://m.media-amazon.com/images/I/{img_id}"
        download_image(url, img_id)
        
        # Calculate relative path
        if html_file.parent.name == "posts":
            rel_path = f"../assets/images/products/{img_id}"
        else:
            rel_path = f"assets/images/products/{img_id}"
            
        print(f"Replacing {url} with {rel_path} in {html_file.name}")
        content = content.replace(url, rel_path)
    
    html_file.write_text(content, encoding='utf-8')

def main():
    # Process root HTML files
    for html_file in base_dir.glob("*.html"):
        process_file(html_file)
        
    # Process posts HTML files
    posts_dir = base_dir / "posts"
    for html_file in posts_dir.glob("*.html"):
        process_file(html_file)
        
    print("Done handling all images globally!")

if __name__ == "__main__":
    main()
