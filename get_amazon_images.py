from playwright.sync_api import sync_playwright
import re

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        url = "https://www.amazon.com/dp/B0D9R7Q449"
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)
        content = page.content()
        matches = re.findall(r'https://m\.media-amazon\.com/images/I/([A-Za-z0-9_\-]+)\.(?:jpg|png)', content)
        # Filter strings likely to be product images
        images = [m for m in matches if len(m) > 8]
        
        # Unique
        images = list(dict.fromkeys(images))
        print("Found Amazon Image IDs:")
        for idx in images[:5]:
            print(f"https://m.media-amazon.com/images/I/{idx}._AC_SL1500_.jpg")
            
        browser.close()

if __name__ == "__main__":
    main()
