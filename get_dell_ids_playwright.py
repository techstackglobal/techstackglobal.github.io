from playwright.sync_api import sync_playwright
import re

def main():
    asin = "B0FBXD383M"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        url = f"https://www.amazon.com/dp/{asin}"
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(5000)
            content = page.content()
            # Look for all image IDs
            matches = re.findall(r'https://m\.media-amazon\.com/images/I/([A-Za-z0-9_\-]+)\.', content)
            unique_ids = list(dict.fromkeys([m for m in matches if len(m) > 8]))
            print(f"ASIN {asin} IDs: {unique_ids}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    main()
