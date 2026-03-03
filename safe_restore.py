import subprocess
import re
import os

base = r"C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"

# All HTML files that were modified in the last commit
html_files = [
    "about.html", "affiliate-disclosure.html", "amazon-stack.html", "blog.html",
    "contact.html", "index.html", "privacy-policy.html", "smart-tools.html",
    "terms-of-service.html", "thank-you.html",
    "posts/alienware-aw3423dwf-review.html", "posts/alienware-aw3423dwf-vs-odyssey-g8.html",
    "posts/apple-macbook-pro-m4-pro-review.html", "posts/best-laptops-for-students-2026.html",
    "posts/best-noise-cancelling-headphones-2026.html", "posts/best-podcast-microphones-2026.html",
    "posts/best-premium-laptop-for-work-2026.html", "posts/best-remote-work-setup-2026.html",
    "posts/best-ultrawide-monitors-2026.html", "posts/bose-qc-ultra-review.html",
    "posts/budget-laptops-under-1000.html", "posts/dell-thunderbolt-smart-dock-review.html",
    "posts/dell-xps-15-9530-review.html", "posts/do-you-need-thunderbolt-dock.html",
    "posts/is-a-4k-monitor-worth-it.html", "posts/is-samsung-990-pro-worth-it.html",
    "posts/lg-27us500-w-ultrafine-monitor-review.html", "posts/samsung-990-pro-ssd-review.html",
    "posts/samsung-odyssey-g8-review.html", "posts/samsung-odyssey-g8-vs-alienware-aw3423dwf.html",
    "posts/shure-sm7b-review.html", "posts/shure-sm7b-vs-sm7db.html",
    "posts/shure-sm7db-review.html", "posts/sony-wh-1000xm5-review.html",
    "posts/sony-xm5-vs-bose-qc-ultra.html", "posts/surface-laptop-studio-2-review.html"
]

favicon_pattern = re.compile(
    r'(\.\./assets/icons/(?:favicon-(?:16|32)|favicon|techstack-logo-192)\.(?:png|ico)|assets/icons/(?:favicon-(?:16|32)|favicon|techstack-logo-192)\.(?:png|ico))\?v=\d+'
)

for rel_path in html_files:
    full_path = os.path.join(base, rel_path)
    
    # Get the CORRECT version from HEAD~1 (before the corrupted commit)
    try:
        git_path = rel_path.replace("\\", "/")
        correct_data = subprocess.check_output(
            ['git', 'show', f'HEAD~1:{git_path}'],
            cwd=base
        )
        correct_content = correct_data.decode('utf-8', errors='ignore')
    except subprocess.CalledProcessError:
        print(f"SKIP (not in HEAD~1): {rel_path}")
        continue
    
    # Now apply v=6 favicon bump to the correct content
    updated = favicon_pattern.sub(lambda m: m.group(0).rsplit('?v=', 1)[0] + '?v=6', correct_content)
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(updated)
    
    print(f"Fixed: {rel_path}")

print("\nAll files restored from HEAD~1 with v=6 favicon cache buster applied.")
