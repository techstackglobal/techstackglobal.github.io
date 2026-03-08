import os
from bs4 import BeautifulSoup

file_path = "blog.html"
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

container = soup.find(id="blog-posts-container")
if not container:
    print("Could not find #blog-posts-container")
    exit(1)

cards = container.find_all("div", class_="blog-card")

titans = []
displays = []
audio = []
laptops = []
storage = []
others = []

TITAN_LINKS = [
    "best-ultrawide-monitors-2026.html",
    "best-noise-cancelling-headphones-2026.html",
    "best-remote-work-setup-2026.html",
    "best-podcast-microphones-2026.html"
]

for card in cards:
    link_tag = card.find("a")
    if not link_tag:
        continue
    href = link_tag.get("href", "")
    filename = href.split("/")[-1]

    if filename in TITAN_LINKS:
        titans.append(card)
    elif any(kw in filename for kw in ["monitor", "odyssey", "alienware", "lg-", "4k"]):
        displays.append(card)
    elif any(kw in filename for kw in ["headphone", "mic", "shure", "sony", "bose", "audio"]):
        audio.append(card)
    elif any(kw in filename for kw in ["laptop", "macbook", "surface", "dell-xps"]):
        laptops.append(card)
    elif any(kw in filename for kw in ["samsung-990", "ssd", "thunderbolt", "dock"]):
        storage.append(card)
    else:
        others.append(card)

# Clear container
container.clear()
container.name = "div" # change if needed, but we can just use divs

def create_section(title, description, card_list, highlight=False):
    if not card_list: return None
    
    sec = soup.new_tag("div")
    sec["style"] = "margin-bottom: 4rem;"
    
    # Section Header
    header = soup.new_tag("div")
    header["style"] = "margin-bottom: 2rem; border-bottom: 1px solid var(--border-glass); padding-bottom: 1rem;"
    
    h2 = soup.new_tag("h2")
    h2.string = title
    if highlight:
        h2["style"] = "color: var(--accent); font-size: 2rem;"
    
    p = soup.new_tag("p")
    p["style"] = "color: var(--text-secondary); font-size: 1.1rem;"
    p.string = description
    
    header.append(h2)
    header.append(p)
    sec.append(header)
    
    # Grid
    grid = soup.new_tag("div")
    grid["class"] = ["blog-grid"]
    # If highlight, maybe make grid different? 
    # For now standard blog-grid is fine, it handles responsive grid
    
    for c in card_list:
        grid.append(c)
        
    sec.append(grid)
    return sec

# 1. Titans
sec_titans = create_section(
    "Titan Guides", 
    "Our most comprehensive, definitive guides to industry-standard gear.",
    titans,
    highlight=True
)
if sec_titans: container.append(sec_titans)

# 2. Displays
sec_displays = create_section(
    "🖥️ Displays & Home Office",
    "Ultrawides, 4K panels, and QD-OLED showdowns.",
    displays
)
if sec_displays: container.append(sec_displays)

# 3. Audio
sec_audio = create_section(
    "🎧 Audio & Communications",
    "Active noise-cancellation, professional mics, and remote-work headsets.",
    audio
)
if sec_audio: container.append(sec_audio)

# 4. Laptops
sec_laptops = create_section(
    "💻 Laptops & Workstations",
    "Premium ultrabooks, student budgets, and workstation replacements.",
    laptops
)
if sec_laptops: container.append(sec_laptops)

# 5. Storage
sec_storage = create_section(
    "🔌 Storage & Accessories",
    "PCIe Gen4 SSDs, Thunderbolt 4 docks, and workspace infrastructure.",
    storage
)
if sec_storage: container.append(sec_storage)

# 6. Others
sec_others = create_section(
    "More Guides",
    "Additional tech insights and comparisons.",
    others
)
if sec_others: container.append(sec_others)

# Fix double container class issues if we need to remove the id css wrapper, but blog-grid class is on the id container right now.
# Wait, container currently has id="blog-posts-container" and class="blog-grid"
# If we append .blog-grid inside it, we will have nested grids.
# Let's remove "blog-grid" from the main container.
if "blog-grid" in container.get("class", []):
    container["class"].remove("blog-grid")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print("Successfully reorganized blog.html!")
