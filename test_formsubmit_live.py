import time
import urllib.request
from playwright.sync_api import sync_playwright

def test_form_live():
    print("Waiting for GitHub Pages to deploy the thank-you page...")
    while True:
        try:
            req = urllib.request.Request("https://techstackglobal.github.io/thank-you.html", method="HEAD")
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    break
        except Exception:
            pass
        time.sleep(2)
        print("Still waiting for deployment...")

    print("Deployment detected! Proceeding to FormSubmit test.")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to LIVE index.html...")
        page.goto("https://techstackglobal.github.io/index.html")
        
        print("Filling out form...")
        page.fill("input[name='email']", "test-live@example.com")
        
        print("Submitting form...")
        with page.expect_navigation(timeout=15000) as nav_info:
            page.click("button[type='submit']")
            
        print(f"Landed on: {page.url}")
        
        if "techstackglobal.github.io/thank-you.html" in page.url:
            print("SUCCESS: Redirected to custom thank-you page!")
        elif "formsubmit.co" in page.url:
            print("WARNING: Redirected to FormSubmit landing page instead.")
        else:
            print("Unknown redirect destination.")
            
        browser.close()

if __name__ == "__main__":
    test_form_live()
