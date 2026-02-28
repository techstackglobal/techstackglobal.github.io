from playwright.sync_api import sync_playwright
import os

html_path = 'file:///' + os.path.abspath('og_template.html').replace('\\', '/')
output_path = os.path.abspath('assets/og-image.jpg')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1200, 'height': 630})
    page.goto(html_path)
    # wait for fonts to load
    page.evaluate("document.fonts.ready")
    
    # Save as highly optimized JPG
    page.screenshot(path=output_path, type='jpeg', quality=85)
    browser.close()

size = os.path.getsize(output_path)
print(f"Saved {output_path} ({size/1024:.1f} KB)")
