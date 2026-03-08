import os
from bs4 import BeautifulSoup

# Define clusters
CLUSTERS = [
    {
        "name": "OLED Monitors",
        "A": "posts/alienware-aw3423dwf-review.html",
        "B": "posts/samsung-odyssey-g8-review.html",
        "Bridge": "posts/samsung-odyssey-g8-vs-alienware-aw3423dwf.html"
    },
    {
        "name": "Pro Audio",
        "A": "posts/shure-sm7b-review.html",
        "B": "posts/shure-sm7db-review.html",
        "Bridge": "posts/shure-sm7b-vs-sm7db.html"
    },
    {
        "name": "Noise Cancelling",
        "A": "posts/sony-wh-1000xm5-review.html",
        "B": "posts/bose-qc-ultra-review.html",
        "Bridge": "posts/sony-xm5-vs-bose-qc-ultra.html"
    }
]

def check_link(source_file, target_file):
    if not os.path.exists(source_file):
        return f"MISSING FILE: {source_file}"
    
    with open(source_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        
        # Check for both relative and root-relative links
        target_name = os.path.basename(target_file)
        for link in links:
            if target_name in link:
                return "CONNECTED"
    return "DISCONNECTED"

print(f"{'Cluster':<20} | {'Link Direction':<25} | {'Status'}")
print("-" * 60)

for c in CLUSTERS:
    # A -> Bridge
    print(f"{c['name']:<20} | {'A -> Bridge':<25} | {check_link(c['A'], c['Bridge'])}")
    # B -> Bridge
    print(f"{c['name']:<20} | {'B -> Bridge':<25} | {check_link(c['B'], c['Bridge'])}")
    # Bridge -> A
    print(f"{c['name']:<20} | {'Bridge -> A':<25} | {check_link(c['Bridge'], c['A'])}")
    # Bridge -> B
    print(f"{c['name']:<20} | {'Bridge -> B':<25} | {check_link(c['Bridge'], c['B'])}")
    # A -> B (Optional but good)
    print(f"{c['name']:<20} | {'A -> B':<25} | {check_link(c['A'], c['B'])}")
    # B -> A (Optional but good)
    print(f"{c['name']:<20} | {'B -> A':<25} | {check_link(c['B'], c['A'])}")
    print("-" * 60)
