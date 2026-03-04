import os
import re

base = r"C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
blog_file = os.path.join(base, "blog.html")

with open(blog_file, "r", encoding="utf-8") as f:
    html = f.read()

# I need to find the 3 pillar guides, extract them, and remove the hub section,
# then inject them right under the <div class="blog-grid" id="blog-posts-container">

# Matches the entire pillar guides hero block
pillar_hero_pattern = re.compile(
    r'<div class="pillar-guides-hero" style="margin-bottom: 4rem;">(.*?)</div>\s*<h2 style="margin-bottom: 2rem; color: var\(--text-secondary\);">Market Analysis & Comparison Guides</h2>', 
    re.DOTALL
)

hero_match = pillar_hero_pattern.search(html)

if hero_match:
    print("Found pillar hero section.")
    hero_content = hero_match.group(1)
    
    # We want to extract each pillar card, adjust their HTML slightly to match regular grid items
    # e.g., border-left -> border-top, h2 -> h3, 'View Pillar Guide' -> 'Read Guide'
    
    # Pillar 1 (Headphones)
    p1 = re.search(r'<!-- PILLAR: Headphones -->(.*?)</p>\s*<div class="card-meta">.*?</div>\s*</div>', hero_content, re.DOTALL)
    if p1:
        c1 = p1.group(0).replace('border-left: 5px solid', 'border-top: 3px solid')
        c1 = c1.replace('<h2 style="font-size: 1.8rem; margin: 0.5rem 0;">', '<h3>').replace('</h2>', '</h3>')
        c1 = c1.replace('Primary Pillar', 'Buyer Guide')
        c1 = c1.replace('View Pillar Guide →', 'Read Guide →')
    else: c1 = ""
    
    # Pillar 2 (Microphones)
    p2 = re.search(r'<!-- PILLAR: Microphones -->(.*?)</p>\s*<div class="card-meta">.*?</div>\s*</div>', hero_content, re.DOTALL)
    if p2:
        c2 = p2.group(0).replace('border-left: 5px solid', 'border-top: 3px solid')
        c2 = c2.replace('<h2 style="font-size: 1.8rem; margin: 0.5rem 0;">', '<h3>').replace('</h2>', '</h3>')
        c2 = c2.replace('Primary Pillar', 'Buyer Guide')
        c2 = c2.replace('View Pillar Guide →', 'Read Guide →')
    else: c2 = ""

    # Pillar 3 (Monitors)
    p3 = re.search(r'<!-- PILLAR: Monitors -->(.*?)</p>\s*<div class="card-meta">.*?</div>\s*</div>', hero_content, re.DOTALL)
    if p3:
        c3 = p3.group(0).replace('border-left: 5px solid', 'border-top: 3px solid')
        c3 = c3.replace('<h2 style="font-size: 1.8rem; margin: 0.5rem 0;">', '<h3>').replace('</h2>', '</h3>')
        c3 = c3.replace('Primary Pillar', 'Buyer Guide')
        c3 = c3.replace('View Pillar Guide →', 'Read Guide →')
    else: c3 = ""

    # Combine extracted standard cards
    standard_cards = f"\n            {c1}\n\n            {c2}\n\n            {c3}\n"
    
    # Remove the entire hero div + h2
    html_no_hero = pillar_hero_pattern.sub('', html)
    
    # Inject standard cards inside the blog grid
    html_final = html_no_hero.replace('<div class="blog-grid" id="blog-posts-container">', f'<div class="blog-grid" id="blog-posts-container">{standard_cards}')
    
    with open(blog_file, "w", encoding="utf-8") as f:
        f.write(html_final)
    print("Reformatted blog.html")
else:
    print("Could not find pillar hero pattern.")

