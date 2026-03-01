import os
import re

BASE_DIR = os.getcwd()

files_to_update = [
    'posts/apple-macbook-pro-m4-pro-review.html',
    'posts/dell-xps-15-9530-review.html',
    'posts/surface-laptop-studio-2-review.html',
    'posts/shure-sm7b-review.html',
    'posts/samsung-990-pro-ssd-review.html',
    'posts/best-laptops-for-students-2026.html',
    'posts/budget-laptops-under-1000.html'
]

# Pattern for the sidebar widget across different post styles
# Style 1: With card-icon
card_pattern = re.compile(r'<div class="mini-affiliate-card">\s*<div class="mini-card-icon">.*?best-headphones-for-classes\.html.*?</div>\s*</div>', re.DOTALL)
# Style 2: Simple text link in card
text_card_pattern = re.compile(r'<div class="mini-affiliate-card">\s*<div class="mini-card-text">\s*<h5>Best Headphones for Classes</h5>.*?View\s+Guide\s+→</a>\s*</div>\s*</div>', re.DOTALL)

for rel_path in files_to_update:
    abs_path = os.path.join(BASE_DIR, rel_path.replace('/', os.sep))
    if not os.path.exists(abs_path):
        print(f"File not found: {abs_path}")
        continue
    
    with open(abs_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = card_pattern.sub('', content)
    new_content = text_card_pattern.sub('', new_content)
    
    if new_content != content:
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {rel_path}")
    else:
        print(f"No changes for: {rel_path}")

# Also delete the actual file
target_file = os.path.join(BASE_DIR, 'posts', 'best-headphones-for-classes.html')
if os.path.exists(target_file):
    os.remove(target_file)
    print(f"Deleted: {target_file}")
