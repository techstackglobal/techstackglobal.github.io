import os
import shutil
import re
import glob

base = r"C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
icons_dir = os.path.join(base, "assets", "icons")
src = os.path.join(icons_dir, "favicon-original.png")

# 1. Copy the T favicon to ALL favicon slots
targets = [
    os.path.join(icons_dir, "favicon-16.png"),
    os.path.join(icons_dir, "favicon-32.png"),
    os.path.join(icons_dir, "favicon.ico"),
    os.path.join(icons_dir, "techstack-logo-192.png"),
    os.path.join(base, "favicon.ico"),
]
for t in targets:
    shutil.copy2(src, t)
    print(f"Copied to {t}")

# 2. Delete all old versioned favicon files (v2, v4, v5, original temp)
to_delete = glob.glob(os.path.join(icons_dir, "*-v2*")) + \
            glob.glob(os.path.join(icons_dir, "*-v4*")) + \
            glob.glob(os.path.join(icons_dir, "*-v5*")) + \
            glob.glob(os.path.join(icons_dir, "favicon-v*.png")) + \
            [os.path.join(icons_dir, "favicon-original.png")]

for f in to_delete:
    if os.path.exists(f):
        os.remove(f)
        print(f"Deleted {f}")

# 3. Bump cache buster to v6 in ALL html files
skip_dirs = {'.git', '.vscode', 'node_modules', '.gemini'}
html_files = []
for root, dirs, files in os.walk(base):
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

changed = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # Bump any ?v=N on favicon links to v6
    new_content = re.sub(
        r'(assets/icons/(?:favicon-(?:16|32)|favicon|techstack-logo-192)\.(?:png|ico))\?v=\d+',
        r'\1?v=6',
        new_content if changed else content
    )
    # Also handle ../assets/icons/ paths
    new_content = re.sub(
        r'(\.\./assets/icons/(?:favicon-(?:16|32)|favicon|techstack-logo-192)\.(?:png|ico))\?v=\d+',
        r'\1?v=6',
        new_content
    )
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        changed += 1
        print(f"Updated cache buster: {os.path.relpath(path, base)}")

print(f"\nDone. {changed} HTML files updated.")
print("Favicon set to the dark navy T icon sitewide.")
