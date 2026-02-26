import os
import re

# Paths
blog_dir = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
posts_dir = os.path.join(blog_dir, "posts")
index_file = os.path.join(blog_dir, "index.html")

logo_replacement = '''<div class="logo">
                <a href="{path_to_home}index.html" style="display: flex; align-items: center; text-decoration: none;">
                    <img src="{path_to_home}logo.png" alt="TechStack Global" style="height: 60px;">
                </a>
            </div>'''

def apply_new_logo(filepath, is_post=False):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    path_prefix = "../" if is_post else ""
    final_logo = logo_replacement.format(path_to_home=path_prefix)
    
    # Replace the deletion placeholder
    new_content = content.replace('<!-- LOGO DELETED -->', final_logo)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Apply to Index
apply_new_logo(index_file)

# Apply to Posts
for filename in os.listdir(posts_dir):
    if filename.endswith(".html"):
        apply_new_logo(os.path.join(posts_dir, filename), is_post=True)
