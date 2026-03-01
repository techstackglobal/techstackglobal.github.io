import os
import re
from playwright.sync_api import sync_playwright

def analyze_page():
    file_path = "posts/shure-sm7b-vs-sm7db.html"
    
    # Word count
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
            text = re.sub(r'<[^>]+>', ' ', html)
            words = text.split()
            print(f"Word count constraint check: {len(words)} words")
            print(f"H1 count: {html.count('<h1')}")
    else:
        print("File not found")

    # Screenshots
    full_path = f"file:///{os.path.abspath(file_path).replace(chr(92), '/')}"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # Desktop
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        page.goto(full_path)
        desktop_path = "C:/.gemini/antigravity/brain/8486ba77-8392-41f5-bf8a-23649803046a/comparison_desktop.png"
        page.screenshot(path=desktop_path, full_page=True)
        print(f"Desktop screenshot saved to {desktop_path}")
        
        # Mobile
        mobile_page = browser.new_page(viewport={'width': 375, 'height': 812})
        mobile_page.goto(full_path)
        mobile_path = "C:/.gemini/antigravity/brain/8486ba77-8392-41f5-bf8a-23649803046a/comparison_mobile.png"
        mobile_page.screenshot(path=mobile_path, full_page=True)
        print(f"Mobile screenshot saved to {mobile_path}")
        
        browser.close()

if __name__ == "__main__":
    analyze_page()
