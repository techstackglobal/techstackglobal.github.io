import os
import re

# Paths
blog_dir = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
posts_dir = os.path.join(blog_dir, "posts")
index_file = os.path.join(blog_dir, "index.html")

# Text-only logo HTML
# Using a <span> for "Global" to keep the brand accent while being clean
text_logo_html = '''<div class="logo">
                <a href="{path_to_home}index.html" style="text-decoration: none; color: inherit;">
                    TechStack<span>Global</span>
                </a>
            </div>'''

def apply_text_logo(filepath, is_post=False):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    path_prefix = "../" if is_post else ""
    final_logo = text_logo_html.format(path_to_home=path_prefix)
    
    # Replace ANY existing logo div with the new text-only one
    pattern = r'<div class="logo">.*?</div>'
    new_content = re.sub(pattern, final_logo, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Clean physical logo files
logo_png = os.path.join(blog_dir, "logo.png")
if os.path.exists(logo_png):
    os.remove(logo_png)

# Apply to Index
apply_text_logo(index_file)

# Apply to Posts
for filename in os.listdir(posts_dir):
    if filename.endswith(".html"):
        apply_text_logo(os.path.join(posts_dir, filename), is_post=True)

print("Text-only branding applied globally.")
