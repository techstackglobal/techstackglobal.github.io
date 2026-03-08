import sys, glob, re

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

def fix_all_posts():
    updated = 0
    for path_str in glob.glob('posts/*.html'):
        with open(path_str, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Cleanly update Nav Component
        # Find any <ul ... id="nav-links"> or ul.nav-links and replace entire thing
        if '<ul class="nav-links"' in html or 'id="nav-links"' in html:
            html = re.sub(r'<ul[^>]*class="nav-links"[^>]*>.*?</ul>', NAV_HTML, html, flags=re.DOTALL)
            html = re.sub(r'<ul[^>]*id="nav-links"[^>]*>.*?</ul>', NAV_HTML, html, flags=re.DOTALL)
            
        # 2. Add / update missing script.js tag before </body>
        if '../script.js' not in html and 'script.js' not in html:
            html = html.replace('</body>', '  <script src="../script.js"></script>\n </body>')
            
        # 3. Change main content class so CSS grid triggers
        html = re.sub(r'<main[^>]*class="container section-padding"[^>]*>', '<main class="article-container">', html)
        html = re.sub(r'<main[^>]*class="container"[^>]*>', '<main class="article-container">', html)

        # 4. Safely inject sidebar immediately following the closing </article> tag
        if 'class="sticky-sidebar"' not in html:
            html = html.replace('</article>', '</article>\n' + SIDEBAR_HTML)
            
        with open(path_str, 'w', encoding='utf-8') as f:
            f.write(html)
        updated += 1

    print(f"Fixed {updated} posts safely using direct string manipulation.")

fix_all_posts()
