from bs4 import BeautifulSoup
import re
import os

target_files = [
    'posts/best-noise-cancelling-headphones-2026.html',
    'posts/best-podcast-microphones-2026.html',
    'posts/best-ultrawide-monitors-2026.html'
]
ref_file = 'posts/shure-sm7b-review.html'
base_dir = r"C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"

# Read reference file for header and favicon
with open(os.path.join(base_dir, ref_file), 'r', encoding='utf-8') as f:
    ref_soup = BeautifulSoup(f, 'html.parser')

ref_header = ref_soup.find('header', class_='glass-header')
ref_favicons = ref_soup.find_all('link', rel=lambda r: r and ('icon' in r or 'apple-touch-icon' in r))

affiliate_links_fixed = 0
non_affiliate_buttons_removed = 0
favicon_standardized_count = 0

for file_path in target_files:
    full_path = os.path.join(base_dir, file_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Navigation Restoration
    # Replace existing header
    existing_header = soup.find('header', class_='glass-header')
    if existing_header and ref_header:
        existing_header.replace_with(ref_soup.new_tag("div")) # placeholder
        soup.find("div").replace_with(ref_header.copy())

    # 2. Affiliate Link Integrity
    # Find all amazon links. Ensure tag, target, rel
    amazon_links = soup.find_all('a', href=re.compile(r'amazon\.com'))
    for link in amazon_links:
        href = link.get('href', '')
        changed = False
        
        # tag
        if '?tag=techstackglob-20' not in href and '&tag=techstackglob-20' not in href:
            if '?' in href:
                link['href'] = href.replace('?', '?tag=techstackglob-20&', 1)
            else:
                link['href'] = href + '?tag=techstackglob-20'
            changed = True
            
        # target
        if link.get('target') != '_blank':
            link['target'] = '_blank'
            changed = True
            
        # rel
        current_rel = link.get('rel', [])
        if isinstance(current_rel, str):
            current_rel = current_rel.split()
        required_rels = ['nofollow', 'noopener', 'sponsored']
        if not all(r in current_rel for r in required_rels):
            # Combine current logic plus required
            final_rels = set(current_rel + required_rels)
            link['rel'] = " ".join(sorted(final_rels)) # output space separated string
            changed = True
            
        if changed:
            affiliate_links_fixed += 1

    # 3. Remove non-affiliate CTR buttons
    btn_links = soup.find_all('a', class_=re.compile(r'btn-(primary|secondary|tertiary)'))
    for btn in btn_links:
        href = btn.get('href', '')
        if 'amazon.com' not in href:
            btn.decompose()
            non_affiliate_buttons_removed += 1

    # 4. Favicon Restore
    # Remove existing favicon links
    for old_fav in soup.find_all('link', rel=lambda r: r and ('icon' in r or 'apple-touch-icon' in r)):
        old_fav.decompose()
    
    # Insert standard favicons in head
    head = soup.find('head')
    if head and list(ref_favicons):
        for fav in reversed(ref_favicons): # reversed since inserting at beginning usually pushes down, but insert after meta
            if head.find_all('meta'):
                head.find_all('meta')[-1].insert_after(fav.copy())
            else:
                head.insert(0, fav.copy())
        favicon_standardized_count += 1
        
    # Bump v1 to v5
    for link in soup.find_all('link', rel=lambda r: r and ('icon' in r or 'apple-touch-icon' in r)):
        if '?v=1' in link['href']:
            link['href'] = link['href'].replace('?v=1', '?v=5')

    # 5. Mobile toggle fix 
    # Ensure script is loaded exactly before </body>
    if not soup.find('script', src='../script.js'):
        script_tag = soup.new_tag('script', src='../script.js')
        if soup.body:
            soup.body.append(script_tag)

    # Write out
    with open(full_path, 'w', encoding='utf-8') as f:
        # Use str(soup) to keep formatting reasonably close (though it might reformat slightly)
        # Using a safer approach with regex on original text if we just wanted exact text replace, but bs4 is robust for DOM manipulation.
        f.write(soup.prettify(formatter="html"))

print(f"Affiliate Links Fixed: {affiliate_links_fixed}")
print(f"Non-Affiliate Buttons Removed: {non_affiliate_buttons_removed}")
print(f"Favicon Standardized Pages: {favicon_standardized_count}")

