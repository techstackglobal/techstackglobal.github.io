import re
from pathlib import Path

base_dir = Path(r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog')

def revert(fp):
    c = fp.read_text(encoding='utf-8')
    # Revert image paths from assets/images/products to original m.media-amazon.com 
    n = re.sub(r'(?:\.\./)?assets/images/products/([A-Za-z0-9_\-\.]+?\.jpg)', r'https://m.media-amazon.com/images/I/\1', c)
    if n != c:
        print(f'Reverted {fp.name}')
        fp.write_text(n, encoding='utf-8')

for f in base_dir.glob('*.html'): revert(f)
for f in (base_dir / 'posts').glob('*.html'): revert(f)
print('Done')
