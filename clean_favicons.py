import os
import re

base = r"C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
html_files = []
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

root_favicon_block = """<!-- Site Favicons -->
<link href="/favicon.ico" rel="icon"/>
<link href="/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>"""

# Specific patterns to remove
remove_patterns = [
    re.compile(r'\s*<link[^>]+(?:rel="icon"|rel="shortcut icon"|rel="apple-touch-icon"|rel="apple-touch-icon-precomposed")[^>]*>', re.IGNORECASE),
    re.compile(r'\s*<link[^>]+(?:favicon|techstack-logo-192|apple-touch-icon)[^>]*>', re.IGNORECASE),
    re.compile(r'\s*<!-- Site Favicons -->', re.IGNORECASE)
]

for path in html_files:
    if "test-deploy.html" in path: continue
    
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = content
    for pattern in remove_patterns:
        new_content = pattern.sub('', new_content)
    
    # Standardize Head space before </head>
    # Append the root_favicon_block right before </head>
    new_content = new_content.replace('</head>', f'{root_favicon_block}\n</head>')

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Deep cleaned and standardized favicons in {os.path.relpath(path, base)}")

print("Done.")
