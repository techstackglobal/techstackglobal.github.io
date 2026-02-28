import time
from playwright.sync_api import sync_playwright
import urllib.request
import ssl

def check_live():
    print("Waiting for GitHub Pages to deploy...")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    max_retries = 30
    for i in range(max_retries):
        try:
            req = urllib.request.Request("https://techstackglobal.github.io/index.html", headers={'User-Agent': 'Mozilla/5.0'}, method='GET')
            # Bypass cache
            req.add_header('Cache-Control', 'no-cache')
            res = urllib.request.urlopen(req, context=ctx)
            content = res.read().decode()
            if "serious upgrades helping you make" in content:
                print("Deployment detected! Proceeding to UI and Console checks.")
                break
        except Exception as e:
            pass
        
        print(f"Waiting for deployment... ({i+1}/{max_retries})")
        time.sleep(10)
    else:
        print("FAIL: Deployment check timed out.")
        return

    results = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # 1. Desktop Check
        desktop_page = browser.new_page(viewport={'width': 1280, 'height': 800})
        console_errors = []
        desktop_page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        
        try:
            r = desktop_page.goto("https://techstackglobal.github.io/", wait_until="networkidle")
            results["Desktop render"] = "OK" if r.ok else "FAIL"
            
            # Check for dash characters in intro
            intro_text = desktop_page.locator(".homepage-intro p").text_content()
            results["No dash characters"] = "OK" if "—" not in intro_text and "-" not in intro_text else f"FAIL ({intro_text})"
            
            # Check console errors
            results["No console errors"] = "OK" if len(console_errors) == 0 else f"FAIL ({console_errors})"
        except Exception as e:
             results["Desktop render"] = f"FAIL ({e})"
        
        # 2. Mobile render and wrapping
        mobile_page = browser.new_page(viewport={'width': 375, 'height': 667})
        try:
            mobile_page.goto("https://techstackglobal.github.io/", wait_until="networkidle")
            results["Mobile render"] = "OK"
            
            # Check horizontal overflow
            overflow = mobile_page.evaluate("""() => {
                return document.documentElement.scrollWidth > window.innerWidth;
            }""")
            results["No layout shift / Overflow"] = "FAIL (Overflow detected)" if overflow else "OK"
            
            # Ensure text is not squished by checking bounding box of intro
            intro_box = mobile_page.locator(".homepage-intro p").bounding_box()
            results["No wrapping issues"] = "OK" if intro_box and intro_box["width"] > 300 else f"FAIL (Width: {intro_box['width'] if intro_box else 'None'})"

        except Exception as e:
            results["Mobile render"] = f"FAIL ({e})"

        browser.close()

    for k, v in results.items():
        print(f"{k}: {v}")

check_live()
