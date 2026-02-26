import os

# Paths
blog_dir = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
posts_dir = os.path.join(blog_dir, "posts")
index_file = os.path.join(blog_dir, "index.html")

# Global Standard Logo Group (Image + Text)
standard_logo_html = '''<div class="logo">
                <a href="{path_to_home}index.html" style="display: flex; align-items: center; text-decoration: none; color: inherit;">
                    <img src="{path_to_home}logo.png?v=2" alt="TechStack Global" style="height: 60px; margin-right: 12px;">
                    TechStack<span>Global</span>
                </a>
            </div>'''

def fix_all_logos(filepath, is_post=False):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    path_prefix = "../" if is_post else ""
    final_logo = standard_logo_html.format(path_to_home=path_prefix)
    
    import re
    # Replace ANY logo div (Header or Footer) with the standard one
    # This pattern catches various versions we might have had
    pattern = r'<div class="logo">.*?</div>'
    new_content = re.sub(pattern, final_logo, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Fix Index
fix_all_logos(index_file)

# Fix Footer specific text in index (since regex might catch only the first one depending on implementation, but re.sub(..., flags=re.DOTALL) usually does global unless count=1)
# Actually re.sub is global by default.

# Fix All Posts
for filename in os.listdir(posts_dir):
    if filename.endswith(".html"):
        fix_all_logos(os.path.join(posts_dir, filename), is_post=True)
