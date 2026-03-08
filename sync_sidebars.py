import os
from bs4 import BeautifulSoup

# Define categories and their corresponding links
CATEGORIES = {
    "Monitors & Displays": ["posts/best-ultrawide-monitors-2026.html", "posts/is-a-4k-monitor-worth-it.html", "posts/best-ultrawide-monitor-for-programming-2026.html"],
    "Audio & Podcasting": ["posts/best-noise-cancelling-headphones-2026.html", "posts/best-podcast-microphones-2026.html", "posts/shure-sm7b-vs-sm7db.html"],
    "Laptops & Workstations": ["posts/best-premium-laptop-for-work-2026.html", "posts/best-laptops-for-students-2026.html", "posts/dell-xps-15-9530-review.html"],
    "Storage & Accessories": ["posts/samsung-990-pro-ssd-review.html", "posts/do-you-need-thunderbolt-dock.html", "posts/is-samsung-990-pro-worth-it.html"],
}

# Global Expert Picks shown on all posts
EXPERT_PICKS = [
    {"name": "Best Ultrawide Monitors (2026)", "link": "best-ultrawide-monitors-2026.html", "icon": "fa-display"},
    {"name": "Remote Work Setup Guide", "link": "best-remote-work-setup-2026.html", "icon": "fa-house-laptop"},
    {"name": "Top Headphones for Work", "link": "best-headphones-for-remote-work-2026.html", "icon": "fa-headphones"},
]

def get_post_category(soup):
    badge = soup.find('span', class_='badge')
    if badge:
        text = badge.get_text().strip()
        if "Monitor" in text: return "Monitors & Displays"
        if "Audio" in text or "Podcast" in text: return "Audio & Podcasting"
        if "Laptop" in text: return "Laptops & Workstations"
        if "Storage" in text or "SSD" in text: return "Storage & Accessories"
    return None

def update_sidebar(file_path):
    print(f"Updating {os.path.basename(file_path)}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    sidebar = soup.find('aside', class_='sticky-sidebar')
    
    # If no sidebar exists, find the main container to append to
    main_container = soup.find('main', class_=['article-container', 'container'])
    
    # 1. Preserve "Quick Verdict" or existing specific widgets if sidebar exists
    verdict = None
    if sidebar:
        verdict = sidebar.find('div', class_='verdict-widget')
    
    # 2. Reconstruct sidebar
    new_sidebar = soup.new_tag('aside', **{'class': 'sticky-sidebar'})
    
    if verdict:
        new_sidebar.append(verdict)

    # Add Sidebar Section: Expert Top Picks
    expert_widget = soup.new_tag('div', **{'class': 'sidebar-widget'})
    expert_h4 = soup.new_tag('h4')
    expert_h4.string = "Expert Top Picks"
    expert_widget.append(expert_h4)
    
    ul = soup.new_tag('ul', style="list-style: none; padding: 0; margin: 0;")
    for item in EXPERT_PICKS:
        li = soup.new_tag('li', style="margin-bottom: 0.85rem;")
        a = soup.new_tag('a', href=item['link'], style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem; display: flex; align-items: center;")
        i = soup.new_tag('i', **{'class': f"fa-solid {item['icon']}"}, style="margin-right: 12px; color: var(--accent); width: 20px; text-align: center;")
        a.append(i)
        a.append(soup.new_string(item['name']))
        li.append(a)
        ul.append(li)
    
    expert_widget.append(ul)
    new_sidebar.append(expert_widget)

    # 3. Add Category-Specific Widget
    category = get_post_category(soup)
    if category and category in CATEGORIES:
        cat_widget = soup.new_tag('div', **{'class': 'sidebar-widget'}, style="margin-top: 2rem;")
        cat_h4 = soup.new_tag('h4')
        cat_h4.string = f"More in {category.split(' ')[0]}"
        cat_widget.append(cat_h4)
        
        ul_cat = soup.new_tag('ul', style="list-style: none; padding: 0;")
        for link in CATEGORIES[category]:
            if os.path.basename(link) == os.path.basename(file_path):
                continue
            
            li_cat = soup.new_tag('li', style="margin-bottom: 0.75rem;")
            a_cat = soup.new_tag('a', href=os.path.basename(link), style="color: #9ca3af; text-decoration: none; font-size: 0.85rem;")
            a_cat.string = "→ " + os.path.basename(link).replace('-', ' ').replace('.html', '').title()
            li_cat.append(a_cat)
            ul_cat.append(li_cat)
        
        cat_widget.append(ul_cat)
        new_sidebar.append(cat_widget)

    # Replace old or append to main
    if sidebar:
        sidebar.replace_with(new_sidebar)
    elif main_container:
        main_container.append(new_sidebar)
    else:
        print(f"  ❌ No sidebar OR main container found in {file_path}")
        return

    # Save changes
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

# Run on all posts
posts_dir = 'posts'
for filename in os.listdir(posts_dir):
    if filename.endswith('.html'):
        update_sidebar(os.path.join(posts_dir, filename))

print("\n✅ All sidebars synced!")
