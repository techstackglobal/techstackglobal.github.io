import os
import re

# Paths
blog_dir = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
posts_dir = os.path.join(blog_dir, "posts")
index_file = os.path.join(blog_dir, "index.html")

def remove_logo_from_content(content):
    # This regex targets the entire logo div and everything inside it
    # <div class="logo"> ... </div>
    pattern = r'<div class="logo">.*?</div>'
    return re.sub(pattern, '<!-- LOGO DELETED -->', content, flags=re.DOTALL)

def clean_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = remove_logo_from_content(content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Clean Index
clean_file(index_file)

# Clean Posts
for filename in os.listdir(posts_dir):
    if filename.endswith(".html"):
        clean_file(os.path.join(posts_dir, filename))

# Also delete the physical logo.png if it exists to be safe
logo_png = os.path.join(blog_dir, "logo.png")
if os.path.exists(logo_png):
    os.remove(logo_png)
    print("Deleted physical logo.png")
