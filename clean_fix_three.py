import sys

SIDEBAR_HTML = """
    <aside class="sticky-sidebar">
     <div class="sidebar-widget">
      <h4>
       Expert Top Picks
      </h4>
      <ul style="list-style: none; padding: 0; margin: 0;">
       <li style="margin-bottom: 0.85rem;">
        <a href="best-ultrawide-monitors-2026.html" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem; display: flex; align-items: center;">
         <i class="fa-solid fa-display" style="margin-right: 12px; color: var(--accent); width: 20px; text-align: center;">
         </i>
         Best Ultrawide Monitors (2026)
        </a>
       </li>
       <li style="margin-bottom: 0.85rem;">
        <a href="best-remote-work-setup-2026.html" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem; display: flex; align-items: center;">
         <i class="fa-solid fa-house-laptop" style="margin-right: 12px; color: var(--accent); width: 20px; text-align: center;">
         </i>
         Remote Work Setup Guide
        </a>
       </li>
       <li style="margin-bottom: 0.85rem;">
        <a href="best-headphones-for-remote-work-2026.html" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem; display: flex; align-items: center;">
         <i class="fa-solid fa-headphones" style="margin-right: 12px; color: var(--accent); width: 20px; text-align: center;">
         </i>
         Top Headphones for Work
        </a>
       </li>
      </ul>
     </div>
    </aside>
"""

NAV_HTML = """<ul class="nav-links" id="nav-links">
     <li>
      <a href="../index.html">
       Home
      </a>
     </li>
     <li>
      <a href="../amazon-stack.html">
       Amazon Stack
      </a>
     </li>
     <li>
      <a href="../blog.html">
       Guides
      </a>
     </li>
     <li>
      <a href="../about.html">
       About
      </a>
     </li>
     <li>
      <a href="../contact.html">
       Contact
      </a>
     </li>
    </ul>"""

def fix_file(path_str):
    with open(path_str, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix the nav list, usually it starts at <ul class="nav-links"> or id="nav-links". We find </ul> to replace
    # We'll use a regex to safely replace the old ul block.
    import re
    html = re.sub(r'<ul[^>]*class="nav-links"[^>]*>.*?</ul>', NAV_HTML, html, flags=re.DOTALL)
    
    # 2. Add script.js if missing
    if 'src="../script.js"' not in html:
        html = html.replace('</body>', '  <script src="../script.js"></script>\n</body>')
        
    # 3. Safely change main container
    html = html.replace('<main class="container">', '<main class="article-container">')
    # Or sometimes they have section-padding
    html = html.replace('<main class="container section-padding">', '<main class="article-container">')

    # 4. Safely inject sidebar if it doesn't already have one
    if 'class="sticky-sidebar"' not in html:
        html = html.replace('</article>', '</article>\n' + SIDEBAR_HTML)

    with open(path_str, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed {path_str} cleanly using direct string manipulation.")

fix_file('posts/best-noise-cancelling-headphones-2026.html')
fix_file('posts/best-podcast-microphones-2026.html')
fix_file('posts/best-ultrawide-monitors-2026.html')

