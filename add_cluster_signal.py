import os
import re

files_to_update = [
    "posts/best-remote-work-setup-2026.html",
    "posts/budget-laptops-under-1000.html",
    "posts/best-laptops-for-students-2026.html",
    "posts/best-premium-laptop-for-work-2026.html",
    "posts/do-you-need-thunderbolt-dock.html",
    "posts/is-a-4k-monitor-worth-it.html",
    "posts/is-samsung-990-pro-worth-it.html",
]

cluster_signal = '\n<p class="cluster-signal" style="font-style: italic; font-size: 0.92rem; color: #a1a1aa; margin-top: -0.5rem; margin-bottom: 1.5rem;">This guide is part of our <a href="/posts/best-remote-work-setup-2026.html" style="color: var(--accent); text-decoration: underline;">Remote Work Hardware Series</a>.</p>'

for file_path in files_to_update:
    if not os.path.exists(file_path):
        print(f"Missing: {file_path}")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "cluster-signal" in content:
        print(f"Already injected in: {file_path}")
        continue

    # Regex to find <p class="post-meta">...</p> and insert right after it.
    # We account for the fact that some pages might not have it exactly matching.
    # We can also look for <span class="badge">...</span> and <h1 class="post-title">...</h1>
    
    # We will look for <p class="post-meta">....</p>
    pattern = r'(<p class="post-meta">.*?</p>)'
    
    # In budget-laptops-under-1000.html, there's no post-meta!
    # Let's check where to inject if post-meta is missing.
    if re.search(pattern, content):
        new_content = re.sub(pattern, r'\1' + cluster_signal, content, count=1)
    else:
        # If no post-meta, insert after post-title
        pattern_title = r'(<h1 class="post-title">.*?</h1>)'
        new_content = re.sub(pattern_title, r'\1' + cluster_signal, content, count=1)
        
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Injected in: {file_path}")
    else:
        print(f"Failed to inject in: {file_path}")
