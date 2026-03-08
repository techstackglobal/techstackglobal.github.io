import urllib.request
from bs4 import BeautifulSoup
import re

files = [
    'posts/best-monitor-for-stock-trading-2026.html',
    'posts/best-headphones-for-working-from-home-2026.html'
]

print("=== VERIFICATION REPORT ===")

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Text checks
    body_text = soup.find('main').get_text(separator=' ')
    words = len(body_text.split())
    
    # Internal Links
    internal_links = []
    for a in soup.find_all('a', href=True):
        if a['href'].startswith('/') or not a['href'].startswith('http'):
            internal_links.append(a['href'])
            
    # Affiliate Links
    affiliate_links = []
    for a in soup.find_all('a', href=True):
        if 'amazon.com' in a['href']:
            href = a['href']
            class_nm = a.get('class', [''])[0]
            target = a.get('target', '')
            rel = a.get('rel', [])
            affiliate_links.append((href, target, ' '.join(rel) if isinstance(rel, list) else rel))

    print(f"\nFILE: {file_path}")
    print(f"Word Count: {words}")
    
    # Check for Dashes in text nodes
    dashes = []
    for text_node in soup.find('main').find_all(string=True):
        if text_node.parent.name not in ['script', 'style']:
            if '—' in text_node or '–' in text_node:
                dashes.append(text_node.strip())
                
    if dashes:
        print(f"FOUND Em/En Dashes: {len(dashes)}")
        for d in dashes:
            print(f" - {d}")
    else:
        print("Em/En Dashes: None found")
        
    print(f"Internal Links: {len(internal_links)}")
    for link in internal_links:
        print(f" - {link}")
        
    print(f"Affiliate Links: {len(affiliate_links)}")
    for link, target, rel in affiliate_links:
        print(f" - {link} (Target: {target}, Rel: {rel})")
        # Test HTTP Status
        try:
            req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            print(f"   HTTP Status: {response.getcode()}")
        except urllib.error.HTTPError as e:
            print(f"   HTTP Status: {e.code}")
        except Exception as e:
            print(f"   HTTP Status: Error ({e})")
