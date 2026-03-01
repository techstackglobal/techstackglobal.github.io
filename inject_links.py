import os
import re

BOTTOM_HUB = """
<!-- Internal: Complete Decision Hub -->
<section class="internal-decision-hub" style="margin-top:2rem;padding:1rem;border-radius:8px;background:rgba(255,255,255,0.02);">
  <h3 style="margin:0 0 .5rem 0;">Complete Decision Hub</h3>
  <p style="margin:0 0 .5rem 0;font-size:0.98rem;">Not sure how these parts fit together? Use the guides below to build the right remote work stack for your budget and role.</p>
  <ul style="margin:.5rem 0 0 1rem;line-height:1.7;">
    <li><a href="/posts/best-remote-work-setup-2026.html">Ultimate Remote Work Setup (2026)</a></li>
    <li><a href="/posts/best-premium-laptop-for-work-2026.html">Best Premium Laptop for Work</a></li>
    <li><a href="/posts/budget-laptops-under-1000.html">Budget Laptops Under $1000</a></li>
    <li><a href="/posts/is-samsung-990-pro-worth-it.html">Is Samsung 990 PRO Worth It?</a></li>
    <li><a href="/posts/do-you-need-thunderbolt-dock.html">Do You Need a Thunderbolt Dock?</a></li>
  </ul>
</section>
</article>"""

def inject_top_snippet(html, intro_text):
    top_snippet = f"""
<!-- Internal: top related links -->
<p class="internal-top-links" style="margin-top:0.8rem;font-size:0.95rem;">
  {intro_text} 
  <a href="/posts/best-remote-work-setup-2026.html">Ultimate Remote Work Setup (2026)</a> • 
  <a href="/posts/best-premium-laptop-for-work-2026.html">Premium Laptop Comparison</a> • 
  <a href="/posts/best-laptops-for-students-2026.html">Laptops for Students</a>
</p>
"""
    # Find insertion point, usually after the first paragraph or TLDR box
    # Example: <p class="post-meta">...</p>\n<p>...</p> or <div class="tldr-verdict...">...</div>
    if '</div>\n<div class="audience-grid"' in html:
        return html.replace('</div>\n<div class="audience-grid"', f'</div>\n{top_snippet}<div class="audience-grid"', 1)
    if '</div>\n<div style="text-align: center;' in html:
        return html.replace('</div>\n<div style="text-align: center;', f'</div>\n{top_snippet}<div style="text-align: center;', 1)
    if '<p>Picture this:' in html:
        return html.replace('<p>Picture this:', f'{top_snippet}\n<p>Picture this:', 1)
    # Generic fallback: after h1
    return html.replace('</h1>', f'</h1>\n{top_snippet}', 1)

def inject_hub(html):
    return html.replace('</article>', BOTTOM_HUB, 1)

def update_dock_page():
    path = 'posts/do-you-need-thunderbolt-dock.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = inject_top_snippet(html, "Before choosing your dock, explore:")
    html = inject_hub(html)
    
    # Contextual links
    Contextual_string = " Docks are the glue between your laptop and monitor — our <a href=\"/posts/is-a-4k-monitor-worth-it.html\">4K monitor guide</a> explains what bandwidth you'll need."
    # Insert near the end of the overview paragraph
    html = html.replace('unleash their full potential as\n desktop replacements.</p>', f'unleash their full potential as\n desktop replacements.{Contextual_string}</p>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)


def update_student_page():
    path = 'posts/best-laptops-for-students-2026.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = inject_top_snippet(html, "Related student setup guides:")
    html = inject_hub(html)
    
    # Contextual links
    Contextual_string = " Need bargain power? Check <a href=\"/posts/budget-laptops-under-1000.html\">Budget Laptops Under $1000</a>. Want longevity? See <a href=\"/posts/best-premium-laptop-for-work-2026.html\">Premium Laptop Comparison</a>."
    html = html.replace('writing assignments. It\'s built for durability and long-term value.</p>', f'writing assignments. It\'s built for durability and long-term value.{Contextual_string}</p>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

def update_4k_page():
    path = 'posts/is-a-4k-monitor-worth-it.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = inject_top_snippet(html, "Related display and workflow guides:")
    html = inject_hub(html)
    
    # Contextual links
    Contextual_string = " A 4K monitor changes the laptop you should buy — compare choices in our <a href=\"/posts/best-premium-laptop-for-work-2026.html\">Premium Laptop Comparison</a>."
    html = html.replace('can severely limit your ability to multitask successfully.</p>', f'can severely limit your ability to multitask successfully.{Contextual_string}</p>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

def update_ssd_page():
    path = 'posts/is-samsung-990-pro-worth-it.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = inject_top_snippet(html, "Related storage and performance guides:")
    html = inject_hub(html)
    
    # Contextual links
    Contextual_string = " For balanced storage + speed in a remote setup see our <a href=\"/posts/best-remote-work-setup-2026.html\">Ultimate Remote Work Setup (2026)</a>."
    html = html.replace('15GB video file transfer that used to take three minutes now takes 18 seconds.</p>', f'15GB video file transfer that used to take three minutes now takes 18 seconds.{Contextual_string}</p>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

def update_premium_page():
    path = 'posts/best-premium-laptop-for-work-2026.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = inject_top_snippet(html, "Compare with related workstation guides:")
    html = inject_hub(html)
    
    # Contextual links
    Contextual_string = " For pro workflows the right dock matters — read our <a href=\"/posts/do-you-need-thunderbolt-dock.html\">Thunderbolt dock explainer</a> to choose the right one."
    html = html.replace('ports. Apple forces you into dongles if you need traditional USB-A.</p>', f'ports. Apple forces you into dongles if you need traditional USB-A.{Contextual_string}</p>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)


def update_hub_page():
    path = 'posts/best-remote-work-setup-2026.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    top_hub_snippet = """
<!-- Internal: top related links -->
<p class="internal-top-links" style="margin-top:0.8rem;font-size:0.95rem;">
  Explore stacks: 
  <a href="/posts/best-premium-laptop-for-work-2026.html">Premium laptop stack</a> • 
  <a href="/posts/budget-laptops-under-1000.html">Budget-friendly stack</a> • 
  <a href="/posts/is-samsung-990-pro-worth-it.html">Storage & SSD guide</a>
</p>
"""
    html = html.replace('</div>\n<div class="audience-grid"', f'</div>\n{top_hub_snippet}<div class="audience-grid"', 1)
    
    html = inject_hub(html)
    
    # Contextual already reasonably linked, but let's ensure Samsung 990 Pro + 4K monitor are mentioned
    if 'is-samsung-990-pro-worth-it.html' not in html:
        html = html.replace('<li><strong>Storage:</strong> 2TB NVMe SSD for local backups</li>', '<li><strong>Storage:</strong> 2TB NVMe SSD for local backups (see our <a href="/posts/is-samsung-990-pro-worth-it.html">Samsung 990 PRO guide</a>)</li>')
    if 'do-you-need-thunderbolt-dock.html' not in html:
        html = html.replace('<li><strong>The Hub:</strong> Thunderbolt 4 Dock</li>', '<li><strong>The Hub:</strong> Thunderbolt 4 Dock (read <a href="/posts/do-you-need-thunderbolt-dock.html">our dock explainer</a>)</li>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    update_dock_page()
    update_student_page()
    update_4k_page()
    update_ssd_page()
    update_premium_page()
    update_hub_page()
    print("All pages successfully updated with clustered internal links.")

if __name__ == '__main__':
    main()
