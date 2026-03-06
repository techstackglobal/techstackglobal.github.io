import os
import urllib.parse
from bs4 import BeautifulSoup

files_to_test = [
    r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts\best-microphones-for-remote-work-2026.html',
    r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts\best-headphones-for-zoom-meetings-2026.html'
]
base_dir = r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog'

for file_path in files_to_test:
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href.startswith('http') or href.startswith('#') or href.startswith('mailto:') or not href:
             continue
        # Check local file
        href = href.split('?')[0].split('#')[0]
        if href.startswith('/'):
            target = os.path.join(base_dir, href[1:].replace('/', '\\'))
        else:
            target = os.path.join(os.path.dirname(file_path), href.replace('/', '\\'))
        target = os.path.normpath(target)
        if not os.path.exists(target):
             print(f'WARNING: Broken internal link: {href} -> {target}')
print('Done link check')
