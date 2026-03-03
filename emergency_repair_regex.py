import re
import os

target_files = [
    'posts/best-noise-cancelling-headphones-2026.html',
    'posts/best-podcast-microphones-2026.html',
    'posts/best-ultrawide-monitors-2026.html'
]

base_dir = r"C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"

# Read reference file for header
with open(os.path.join(base_dir, 'posts/shure-sm7b-review.html'), 'r', encoding='utf-8') as f:
    ref_content = f.read()

header_match = re.search(r'<header class="glass-header">.*?</header>', ref_content, re.DOTALL)
ref_header = header_match.group(0) if header_match else ""

favicon_block = """  <link href="../assets/icons/favicon-32.png?v=5" rel="icon" sizes="32x32" type="image/png" />
  <link href="../assets/icons/favicon-16.png?v=5" rel="icon" sizes="16x16" type="image/png" />
  <link href="../assets/icons/techstack-logo-192.png?v=5" rel="apple-touch-icon" sizes="192x192" />
  <link href="../assets/icons/favicon.ico?v=5" rel="shortcut icon" />"""

for file_path in target_files:
    full_path = os.path.join(base_dir, file_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Navigation Restoration
    if ref_header:
        html = re.sub(r'<header class="glass-header">.*?</header>', ref_header, html, flags=re.DOTALL)

    # 4. Favicon Standardization
    # Remove existing favicons
    html = re.sub(r'<link[^>]*href=[^>]*favicon[^>]*>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<link[^>]*href=[^>]*techstack-logo[^>]*>', '', html, flags=re.IGNORECASE)
    
    # Insert new favicons right before </head>
    html = html.replace('</head>', f'{favicon_block}\n</head>')
    
    # 5. Mobile toggle fix 
    # Ensure script is loaded exactly before </body>
    if '<script src="../script.js"></script>' not in html:
        html = html.replace('</body>', '    <script src="../script.js"></script>\n</body>')
        
    # 3. Remove non-affiliate CTR buttons
    # We find all <a class="btn-*" ...> tags. If they don't contain amazon, remove them.
    # Note: the user said remove buttons styled like .btn-primary that do NOT contain amazon link
    # But wait, what if they link to another page like `<a href="../blog.html" class="btn-secondary">`?
    # User said "No fake engagement buttons. No 'Read More' styled like CTA. Keep: Real Amazon affiliate CTAs only."
    # Wait, the pillar pages themselves don't have non-Amazon primary buttons. Let's just remove them.
    def replace_btn(m):
        btn_html = m.group(0)
        if 'amazon.com' not in btn_html:
            return '' # remove
        return btn_html
    
    html = re.sub(r'<a[^>]*class="[^"]*btn-(primary|secondary)[^"]*"[^>]*>.*?</a>', replace_btn, html, flags=re.DOTALL)
    
    # 2. Affiliate Link Integrity
    def fix_amazon_link(m):
        link_tag = m.group(0)
        href_match = re.search(r'href="([^"]+)"', link_tag)
        if not href_match: return link_tag
        
        href = href_match.group(1)
        if 'techstackglob-20' not in href:
            if '?' in href:
                href = href.replace('?', '?tag=techstackglob-20&', 1)
            else:
                href += '?tag=techstackglob-20'
        
        # fix target
        if 'target="_blank"' not in link_tag:
            link_tag = link_tag.replace('href=', 'target="_blank" href=')
            
        # fix rel
        if 'rel="nofollow noopener sponsored"' not in link_tag:
            if 'rel="' in link_tag:
                link_tag = re.sub(r'rel="([^"]*)"', 'rel="nofollow noopener sponsored"', link_tag)
            else:
                link_tag = link_tag.replace('href=', 'rel="nofollow noopener sponsored" href=')
                
        # put href back
        link_tag = re.sub(r'href="[^"]+"', f'href="{href}"', link_tag)
        return link_tag
    
    html = re.sub(r'<a[^>]*href="[^"]*amazon\.com[^"]*"[^>]*>.*?</a>', fix_amazon_link, html, flags=re.DOTALL)
    
    # Clean up empty newlines if any from removals
    html = re.sub(r'\n\s*\n\s*\n', '\n\n', html)

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed {file_path}")
