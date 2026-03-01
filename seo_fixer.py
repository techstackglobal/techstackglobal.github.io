import os
import glob
from bs4 import BeautifulSoup
import argparse

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_URL = "https://techstackglobal.github.io"

def get_expected_live_url(filepath):
    rel_path = os.path.relpath(filepath, BASE_DIR).replace('\\', '/')
    return f"{BASE_URL}/{rel_path}"

def get_html_files():
    skip_dirs = ['.git', '.vscode', 'node_modules', '.gemini']
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def parse_html(filepath):
    # try utf-8, fallback to windows-1252 or utf-16
    encodings = ['utf-8', 'utf-16', 'latin-1']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            return BeautifulSoup(content, 'html.parser'), enc
        except UnicodeDecodeError:
            continue
    raise Exception(f"Could not decode {filepath}")

def save_html(filepath, soup, encoding):
    # Prevent BS4 from self-closing tags improperly or messing up formatting too much
    html = str(soup)
    with open(filepath, 'w', encoding=encoding) as f:
        f.write(html)

def phase_2():
    for f in get_html_files():
        soup, enc = parse_html(f)
        head = soup.find('head')
        if not head: continue
        
        expected_url = get_expected_live_url(f)
        
        # remove all existing canonicals
        for c in soup.find_all('link', attrs={'rel': 'canonical'}):
            c.decompose()
            
        new_tag = soup.new_tag('link', rel='canonical', href=expected_url)
        head.append(new_tag)
        save_html(f, soup, enc)

def phase_3():
    for f in get_html_files():
        soup, enc = parse_html(f)
        head = soup.find('head')
        if not head: continue
        
        expected_url = get_expected_live_url(f)
        
        # Fix og:url
        og_url = soup.find('meta', attrs={'property': 'og:url'})
        if og_url:
            og_url['content'] = expected_url
        else:
            og_url = soup.new_tag('meta', property='og:url', content=expected_url)
            head.append(og_url)
            
        # Add og:image if missing
        og_image = soup.find('meta', attrs={'property': 'og:image'})
        if not og_image:
            og_image = soup.new_tag('meta', property='og:image', content='https://techstackglobal.github.io/og-image.jpg')
            head.append(og_image)
            
        save_html(f, soup, enc)

def phase_4():
    # Only target specific files
    targets = {
        'affiliate-disclosure.html': 'Read the TechStack Global affiliate disclosure policy to understand how we fund our independent research and hardware reviews.',
        'privacy-policy.html': 'Review the TechStack Global privacy policy to understand how we collect, handle, and protect your personal data and browsing information.',
        'terms-of-service.html': 'Read the TechStack Global terms of service and user agreement outlining the conditions for using our guides, reviews, and website content.',
        'apple-macbook-pro-m4-pro-review.html': 'Apple MacBook Pro M4 Pro (2026) review for developers and creators. Unmatched battery life and performance, but is the premium price worth it?'
    }
    
    for f in get_html_files():
        basename = os.path.basename(f)
        if basename in targets:
            soup, enc = parse_html(f)
            head = soup.find('head')
            if not head: continue
            
            desc = targets[basename]
            
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                meta_desc['content'] = desc
            else:
                meta_desc = soup.new_tag('meta', attrs={'name': 'description', 'content': desc})
                # Check for charset and place it after
                head.insert(1, meta_desc)
                
            save_html(f, soup, enc)

def phase_5():
    # Fix >70 char titles. Must keep 2026 and brand. Target 55-65 chars.
    for f in get_html_files():
        soup, enc = parse_html(f)
        title_tag = soup.find('title')
        if not title_tag: continue
        
        title = title_tag.get_text(strip=True)
        changed = False
        
        # Handle specific overly long titles
        if "best-premium-laptop-for-work-2026.html" in f:
            if len(title) > 70:
                title_tag.string = "Best Premium Laptops for Work (2026) | TechStack Global"
                changed = True
        elif "surface-laptop-studio-2-review.html" in f:
            if len(title) > 70:
                title_tag.string = "Microsoft Surface Laptop Studio 2 Review (2026)"
                changed = True
        elif "dell-xps-15-9530-review.html" in f:
            if len(title) > 70:
                title_tag.string = "Dell XPS 15 9530 Review (2026): A Creator's Powerhouse"
                changed = True
        elif "is-a-4k-monitor-worth-it.html" in f:
            if len(title) > 70:
                title_tag.string = "Is a 4K Monitor Worth It for Office Work in 2026?"
                changed = True
        elif "is-samsung-990-pro-worth-it.html" in f:
            if len(title) > 70:
                title_tag.string = "Is the Samsung 990 Pro SSD Worth It in 2026?"
                changed = True
        elif "do-you-need-thunderbolt-dock.html" in f:
            if len(title) > 70:
                title_tag.string = "Do You Need a Thunderbolt 4 Dock in 2026?"
                changed = True
                
        if changed:
            save_html(f, soup, enc)

def phase_6():
    # Add H1 to about.html
    about_path = os.path.join(BASE_DIR, 'about.html')
    if os.path.exists(about_path):
        soup, enc = parse_html(about_path)
        
        # Check if it already has H1
        if not soup.find('h1'):
            # Find the best place (probably top of post-body)
            article = soup.find('article', class_='post-body') or soup.find('main')
            if article:
                h1 = soup.new_tag('h1')
                h1.string = "About TechStack Global"
                h1['class'] = 'post-title' # Optional styling
                article.insert(0, h1)
                save_html(about_path, soup, enc)

                    
def phase_7():
     # Add Missing Schema
     webpage_schema = '''{
 "@context": "https://schema.org",
 "@type": "WebPage",
 "name": "%s",
 "url": "%s"
}'''
     article_schema = '''{
 "@context": "https://schema.org",
 "@type": "Article",
 "headline": "%s",
 "author": {
   "@type": "Organization",
   "name": "TechStack Global"
 },
 "publisher": {
   "@type": "Organization",
   "name": "TechStack Global"
 }
}'''
     collection_schema = '''{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "TechStack Global Blog",
  "url": "https://techstackglobal.github.io/blog.html"
}'''

     for f in get_html_files():
        soup, enc = parse_html(f)
        head = soup.find('head')
        if not head: continue
        
        # Check if it already has schema
        if soup.find('script', attrs={'type': 'application/ld+json'}):
            continue
            
        basename = os.path.basename(f)
        title_tag = soup.find('title')
        title = title_tag.get_text() if title_tag else "TechStack Global"
        url = get_expected_live_url(f)
        
        schema_content = None
        if basename in ['about.html', 'privacy-policy.html', 'affiliate-disclosure.html', 'terms-of-service.html', 'contact.html']:
            schema_content = webpage_schema % (title, url)
        elif basename == 'blog.html':
            schema_content = collection_schema
        elif basename in ['best-laptops-for-students-2026.html', 'budget-laptops-under-1000.html', 'best-headphones-for-classes.html']:
            schema_content = article_schema % title
        
        if schema_content:
            script_tag = soup.new_tag('script', type='application/ld+json')
            script_tag.string = schema_content
            head.append(script_tag)
            save_html(f, soup, enc)

def phase_8():
    for f in get_html_files():
        soup, enc = parse_html(f)
        head = soup.find('head')
        if not head: continue
        
        # Get OG values
        og_title = soup.find('meta', attrs={'property': 'og:title'})
        title_val = og_title['content'] if og_title and og_title.get('content') else (soup.find('title').get_text() if soup.find('title') else '')
        
        og_desc = soup.find('meta', attrs={'property': 'og:description'})
        desc_val = og_desc['content'] if og_desc and og_desc.get('content') else ''
        if not desc_val:
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            desc_val = meta_desc['content'] if meta_desc and meta_desc.get('content') else ''
            
        og_image = soup.find('meta', attrs={'property': 'og:image'})
        image_val = og_image['content'] if og_image and og_image.get('content') else 'https://techstackglobal.github.io/og-image.jpg'
        
        # Remove old twitter tags
        for t in soup.find_all('meta'):
            if t.get('name', '').startswith('twitter:'):
                t.decompose()
        
        card = soup.new_tag('meta', attrs={'name': 'twitter:card', 'content': 'summary_large_image'})
        t_title = soup.new_tag('meta', attrs={'name': 'twitter:title', 'content': title_val})
        t_desc = soup.new_tag('meta', attrs={'name': 'twitter:description', 'content': desc_val})
        t_image = soup.new_tag('meta', attrs={'name': 'twitter:image', 'content': image_val})
        
        head.append(card)
        head.append(t_title)
        if desc_val: head.append(t_desc)
        head.append(t_image)
        
        save_html(f, soup, enc)

def phase_9():
    for f in get_html_files():
        soup, enc = parse_html(f)
        changed = False
        for img in soup.find_all('img'):
            if not img.get('alt') or not str(img['alt']).strip():
                # Extract filename as basis for alt text
                src = img.get('src', '')
                basename = os.path.basename(src).split('.')[0].replace('-', ' ').title()
                img['alt'] = f"{basename} visual" if basename else "Page imagery"
                changed = True
        
        if changed:
            save_html(f, soup, enc)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", type=int)
    args = parser.parse_args()
    
    if args.phase == 2: phase_2()
    elif args.phase == 3: phase_3()
    elif args.phase == 4: phase_4()
    elif args.phase == 5: phase_5()
    elif args.phase == 6: phase_6()
    elif args.phase == 7: phase_7()
    elif args.phase == 8: phase_8()
    elif args.phase == 9: phase_9()
    else: print("Unknown phase")
