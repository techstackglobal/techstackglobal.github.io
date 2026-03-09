import os

base = r"C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
html_files = []
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for path in html_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    has_assets = 'assets/icons/favicon' in content
    has_root = 'link href="/favicon' in content or 'link rel="icon" href="/favicon' in content
    
    print(f"{os.path.relpath(path, base)}: assets={has_assets}, root={has_root}")
