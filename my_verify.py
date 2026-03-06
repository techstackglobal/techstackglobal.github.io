import os
from bs4 import BeautifulSoup
import requests

files_to_test = [
    r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts\best-microphones-for-remote-work-2026.html',
    r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts\best-headphones-for-zoom-meetings-2026.html'
]

dash_chars = ['—', '–']

for file_path in files_to_test:
    print(f'\\n--- Testing {os.path.basename(file_path)} ---')
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check dashes
    for tag in ['p', 'h1', 'h2', 'h3', 'h4', 'li']:
        for el in soup.find_all(tag):
            text = el.get_text()
            for dash in dash_chars:
                if dash in text:
                    print(f'WARNING: Dash {dash} found in text: {text[:50]}...')
    
    # Check images
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if not src.startswith('/posts/images/') and not src.startswith('../posts/images/'):
             print(f'WARNING: Invalid image source: {src}')
        
        # we will check if it exists relative to the root
        abs_src = 'c:\\Users\\PMLS\\Desktop\\Youtube Shorts\\b2b_blog' + src.replace('/', '\\')
        if not os.path.exists(abs_src):
             print(f'WARNING: Image file missing locally: {abs_src}')
             
        if img.get('loading') != 'lazy':
             print(f'WARNING: Missing loading=lazy on image: {src}')
        if not img.get('alt'):
             print(f'WARNING: Missing alt text on image: {src}')
             
    # Check affiliate links
    for a in soup.find_all('a', class_='btn-primary'):
        href = a.get('href', '')
        if 'amazon.com' in href:
            if 'tag=techstackglob-20' not in href:
                print(f'WARNING: Missing affiliate tag in: {href}')
            if a.get('target') != '_blank':
                print(f'WARNING: Missing target=_blank in: {href}')
            if a.get('rel') != ['nofollow', 'noopener', 'sponsored']:
                print(f'WARNING: Invalid rel attribute in: {href}')
                
    # Check tables
    for table in soup.find_all('table'):
        parent = table.find_parent('div', class_='table-responsive')
        if not parent:
            print(f'WARNING: Table missing table-responsive wrapper')
            
    print('Done checking HTML structure.')
