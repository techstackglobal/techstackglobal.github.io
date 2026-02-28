import time
from playwright.sync_api import sync_playwright
import urllib.request
import json
import ssl

def check_live():
    # Wait for github pages to build by checking if the sitemap is live
    print("Waiting for GitHub Pages to deploy...")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    max_retries = 30
    for i in range(max_retries):
        try:
            req = urllib.request.Request("https://techstackglobal.github.io/sitemap.xml", headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, context=ctx)
            content = res.read().decode()
            if "<loc>https://techstackglobal.github.io/</loc>" in content:
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
            results["Homepage desktop"] = "OK" if r.ok else "FAIL"
            
            # Check H1 visibility and header overlap
            h1 = desktop_page.locator("h1")
            header = desktop_page.locator("header")
            h1_box = h1.bounding_box()
            header_box = header.bounding_box()
            if h1_box and header_box and h1_box["y"] > header_box["y"] + header_box["height"]:
                results["H1 visible"] = "OK"
            else:
                results["H1 visible"] = "FAIL (Obscured or not found)"

            # Meta & OG tags
            has_meta = desktop_page.evaluate("""() => {
                return !!document.querySelector('meta[name="description"]') && 
                       !!document.querySelector('meta[property="og:title"]') &&
                       !!document.querySelector('meta[property="og:image"]');
            }""")
            results["Meta & OG present"] = "OK" if has_meta else "FAIL"

            # CTA check
            cta = desktop_page.locator(".cta-box")
            results["CTA check"] = "OK" if cta.is_visible() and desktop_page.locator(".cta-box form button").is_visible() else "FAIL"
            
            # Console errors
            results["Console errors"] = "OK" if len(console_errors) == 0 else f"FAIL ({console_errors})"
        except Exception as e:
             results["Homepage desktop"] = f"FAIL ({e})"
        
        # 2. Mobile Emulated Check
        mobile_page = browser.new_page(viewport={'width': 375, 'height': 667})
        try:
            mobile_page.goto("https://techstackglobal.github.io/", wait_until="networkidle")
            results["Homepage mobile"] = "OK"
            
            # Check horizontal overflow
            overflow = mobile_page.evaluate("""() => {
                return document.documentElement.scrollWidth > window.innerWidth;
            }""")
            results["No horizontal overflow"] = "FAIL (Overflow detected)" if overflow else "OK"
        except Exception as e:
            results["Homepage mobile"] = f"FAIL ({e})"

        browser.close()
        
    # Check robots.txt
    try:
        req = urllib.request.Request("https://techstackglobal.github.io/robots.txt", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx)
        rb = res.read().decode()
        if "Allow: /" in rb and "sitemap.xml" in rb:
            results["robots.txt"] = "OK"
        else:
            results["robots.txt"] = "FAIL"
    except Exception:
        results["robots.txt"] = "FAIL"

    # Check OG Image loads
    try:
        req = urllib.request.Request("https://techstackglobal.github.io/assets/og-image.jpg", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx)
        results["OG image loads"] = "OK" if res.status == 200 else "FAIL"
    except Exception:
        results["OG image loads"] = "FAIL"
        
    results["sitemap.xml"] = "OK"

    for k, v in results.items():
        print(f"{k}: {v}")

check_live()
