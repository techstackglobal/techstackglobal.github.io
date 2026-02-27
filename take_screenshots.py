import os
from playwright.sync_api import sync_playwright

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Desktop
        context_desktop = browser.new_context(viewport={'width': 1280, 'height': 800})
        page_desktop = context_desktop.new_page()
        
        # Mobile
        iphone_13 = p.devices['iPhone 13']
        context_mobile = browser.new_context(**iphone_13)
        page_mobile = context_mobile.new_page()

        urls = {
            'homepage': 'https://techstackglobal.github.io/',
            'macbook': 'https://techstackglobal.github.io/posts/apple-macbook-pro-m4-pro-review.html'
        }

        output_dir = 'c:/Users/PMLS/.gemini/antigravity/brain/8acb5e45-297b-4c05-ae50-1d7cdeac50b0/'

        for name, url in urls.items():
            print(f"Navigating to {url} (Desktop)...")
            page_desktop.goto(url)
            page_desktop.screenshot(path=os.path.join(output_dir, f"{name}_desktop.png"), full_page=True)

            print(f"Navigating to {url} (Mobile)...")
            page_mobile.goto(url)
            page_mobile.screenshot(path=os.path.join(output_dir, f"{name}_mobile.png"), full_page=True)
            
        print("Screenshots captured successfully.")
        browser.close()

if __name__ == '__main__':
    capture_screenshots()
