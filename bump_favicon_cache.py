import os
import re

root = r'C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts'

files = [
    'best-noise-cancelling-headphones-2026.html',
    'best-podcast-microphones-2026.html',
    'best-ultrawide-monitors-2026.html',
]

for filename in files:
    fpath = os.path.join(root, filename)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Bump favicon version query strings: ?v=1 -> ?v=5
    updated = content.replace('favicon-32.png?v=1', 'favicon-32.png?v=5')
    updated = updated.replace('favicon-16.png?v=1', 'favicon-16.png?v=5')
    updated = updated.replace('favicon.ico?v=1', 'favicon.ico?v=5')
    updated = updated.replace('techstack-logo-192.png?v=1', 'techstack-logo-192.png?v=5')

    if updated != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f'Updated: {filename}')
    else:
        print(f'No change needed: {filename}')
