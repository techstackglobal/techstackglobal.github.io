import os
import glob

posts_dir = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts"
html_files = glob.glob(os.path.join(posts_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply standard premium styling to all posts
    # Replace glass-panel with glass-card
    content = content.replace('class="blog-card glass-panel"', 'class="blog-card glass-card"')
    content = content.replace('class="tldr-verdict glass-panel"', 'class="tldr-verdict glass-card"')
    content = content.replace('class="glass-panel"', 'class="glass-card"')
    
    # Ensure affiliate links have the FA amazon icon and bold styling if not already present
    # We will just let the global CSS handle it via `.affiliate-btn` which is already applied.
    
    # Save back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print(f"Migrated {len(html_files)} files to premium Stitch layout components.")
