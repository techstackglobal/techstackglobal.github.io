import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    browser = await playwright.chromium.launch()
    urls = [
        "http://127.0.0.1:8080/",
        "http://127.0.0.1:8080/blog.html",
        "http://127.0.0.1:8080/posts/alienware-aw3423dwf-review.html",
        "http://127.0.0.1:8080/posts/sony-wh-1000xm5-review.html",
        "http://127.0.0.1:8080/posts/best-headphones-for-working-from-home-2026.html"
    ]
    
    viewports = [
        {"width": 1440, "height": 900, "name": "1440px"},
        {"width": 1024, "height": 768, "name": "1024px"},
        {"width": 375, "height": 667, "name": "375px"},
        {"width": 320, "height": 568, "name": "320px"}
    ]
    
    for url in urls:
        page_name = url.split('/')[-1] if not url.endswith('/') else "index_html"
        for vp in viewports:
            context = await browser.new_context(viewport={"width": vp["width"], "height": vp["height"]})
            page = await context.new_page()
            try:
                print(f"Opening {url} at {vp['name']}...")
                await page.goto(url)
                # Wait for any lazy loading
                await page.wait_for_timeout(1000)
                await page.screenshot(path=f"screenshot_{page_name}_{vp['name']}.png", full_page=True)
                print(f"Captured {page_name} at {vp['name']}")
            except Exception as e:
                print(f"Failed {url}: {e}")
            finally:
                await context.close()
                
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == '__main__':
    asyncio.run(main())
