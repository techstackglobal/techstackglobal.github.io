from playwright.sync_api import sync_playwright

def test_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to local index.html...")
        page.goto("http://localhost:8000/index.html")
        
        print("Filling out form...")
        page.fill("input[name='email']", "test@example.com")
        
        print("Submitting form...")
        # We use wait_for_load_state or wait_for_url to catch the redirect
        with page.expect_navigation(timeout=10000) as nav_info:
            page.click("button[type='submit']")
            
        print(f"Landed on: {page.url}")
        
        if "techstackglobal.github.io/thank-you.html" in page.url:
            print("SUCCESS: Redirected to custom thank-you page!")
        elif "formsubmit.co" in page.url:
            print("WARNING: Redirected to FormSubmit landing page instead.")
        else:
            print("Unknown redirect destination.")
            
        # Give it a moment to render
        page.wait_for_timeout(2000)
        
        browser.close()

if __name__ == "__main__":
    test_form()
