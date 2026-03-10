import os
import re

BASE_DIR = r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog'
POSTS_DIR = os.path.join(BASE_DIR, 'posts')

def get_meta_content(content, property_name):
    match = re.search(f'<meta property="{property_name}" content="([^"]+)"', content)
    if not match:
        match = re.search(f'<meta name="{property_name}" content="([^"]+)"', content)
    return match.group(1) if match else None

def optimize_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    rel_path = os.path.relpath(fpath, BASE_DIR).replace('\\', '/')
    canonical_url = f"https://techstackglobal.github.io/{rel_path}"

    # 1. Ensure Canonical Tag exists
    if '<link rel="canonical"' not in new_content and '<link href="https://techstackglobal.github.io' not in new_content:
        # Insert before </head>
        new_content = new_content.replace('</head>', f'    <link rel="canonical" href="{canonical_url}" />\n</head>')
        print(f"Added Canonical: {rel_path}")

    # 2. Inject/Update Twitter Metadata based on OpenGraph
    og_title = get_meta_content(new_content, "og:title")
    og_desc = get_meta_content(new_content, "og:description")
    og_image = get_meta_content(new_content, "og:image")

    if og_title and 'name="twitter:title"' not in new_content:
        new_content = new_content.replace('<!-- Twitter -->', f'<!-- Twitter -->\n    <meta name="twitter:title" content="{og_title}">')
    if og_desc and 'name="twitter:description"' not in new_content:
        new_content = new_content.replace('<!-- Twitter -->', f'<!-- Twitter -->\n    <meta name="twitter:description" content="{og_desc}">')
    if og_image and 'name="twitter:image"' not in new_content:
        new_content = new_content.replace('<!-- Twitter -->', f'<!-- Twitter -->\n    <meta name="twitter:image" content="{og_image}">')
    if 'name="twitter:card"' not in new_content:
        new_content = new_content.replace('<!-- Twitter -->', '<!-- Twitter -->\n    <meta name="twitter:card" content="summary_large_image">')

    # 3. Synchronize Schema Logo
    # Old: /assets/icons/techstack-logo-192.png
    # New: /apple-touch-icon.png (high res TSG)
    old_logo_path = "assets/icons/techstack-logo-192.png"
    new_logo_url = "https://techstackglobal.github.io/apple-touch-icon.png"
    if old_logo_path in new_content:
        new_content = new_content.replace(old_logo_path, "apple-touch-icon.png")
        print(f"Updated Schema Logo: {rel_path}")

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Execution logic
files_to_check = []
for root, dirs, files in os.walk(BASE_DIR):
    if any(skip in root for skip in ['.git', '.agent', 'node_modules', '.venv']): continue
    for f in files:
        if f.endswith('.html'):
            files_to_check.append(os.path.join(root, f))

updated = 0
for fpath in files_to_check:
    if optimize_file(fpath):
        updated += 1

print(f"\nOptimization Sweep Complete. Files Prepared: {updated}")
