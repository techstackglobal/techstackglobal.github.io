import os
import glob
from bs4 import BeautifulSoup

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    modified = False

    # 1. Inject CSS
    head = soup.find('head')
    if head:
        existing_link = head.find('link', href=lambda x: x and '/assets/css/layout-upgrade.css' in x)
        if not existing_link:
            new_link = soup.new_tag('link', rel='stylesheet', href='/assets/css/layout-upgrade.css')
            head.append(new_link)
            modified = True

    # 2. Inject Sidebar for posts
    if 'posts' in filepath.replace('\\', '/'):
        article = soup.find('article')
        if article and not soup.find('div', class_='article-layout'):
            # Find Best Pick from TLDR
            best_pick_name = "Top Recommendation"
            best_pick_link = "#"
            
            tldr = soup.find(class_=lambda x: x and ('tldr-verdict' in x or 'tldr-box' in x or 'verdict-box' in x))
            if tldr:
                cta = tldr.find('a', class_='btn-primary')
                if cta:
                    best_pick_link = cta.get('href', '#')
                    # Try to parse name from "Check [Name] on Amazon"
                    text = cta.get_text(strip=True)
                    if "Check" in text and "on Amazon" in text:
                        best_pick_name = text.replace("Check", "").replace("on Amazon", "").strip()
            
            if best_pick_name == "Top Recommendation" and article:
                # fallback
                first_cta = article.find('a', class_='btn-primary')
                if first_cta:
                    best_pick_link = first_cta.get('href', '#')
                    text = first_cta.get_text(strip=True)
                    if "Check" in text and "on Amazon" in text:
                        best_pick_name = text.replace("Check", "").replace("on Amazon", "").strip()

            # Create layout wrapper
            layout_div = soup.new_tag('div', attrs={'class': 'article-layout'})
            
            # Wrap article
            article.wrap(layout_div)
            
            # Create sidebar
            sidebar_html = f'''
            <aside class="sidebar">
                <div class="sidebar-inner">
                    <div class="quick-verdict">
                        <p class="best-pick-label">🏆 Best Pick</p>
                        <p class="product-name">{best_pick_name}</p>
                        <a style="padding: 12px 16px; font-size: 14px; width: 100%; box-sizing: border-box;" href="{best_pick_link}" class="btn-primary" target="_blank" rel="nofollow noopener sponsored">Check Price</a>
                    </div>
                
                    <h3>Quick Navigation</h3>
                    <nav class="quick-nav">
                        <a href="#overview">Overview</a>
                        <a href="#comparison">Comparison Table</a>
                        <a href="#buying-guide">Buying Guide</a>
                        <a href="#verdict">Final Recommendation</a>
                    </nav>
                </div>
            </aside>
            '''
            sidebar_soup = BeautifulSoup(sidebar_html, 'html.parser')
            # Append sidebar after article inside layout_div
            layout_div.append(sidebar_soup)
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            # BeautifulSoup sometimes messes up DOCTYPE and formatting slightly, 
            # but usually it's fine for our simple DOM manipulation here.
            # Using formatter="html" keeps self-closing tags intact.
            f.write(soup.encode(formatter="html").decode('utf-8'))
        print(f"Updated {filepath}")

# Process all html files
files = glob.glob('*.html') + glob.glob('posts/*.html')
for f in files:
    process_file(f)

print("Done.")
