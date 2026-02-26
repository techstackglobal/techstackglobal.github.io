import os

# Paths
blog_dir = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
posts_dir = os.path.join(blog_dir, "posts")
index_file = os.path.join(blog_dir, "index.html")

# Replacement patterns
# In Index
index_target = '<a href="index.html"><img src="logo.png" alt="TechStack Global" style="height: 50px;"></a>'
index_replacement = '<a href="index.html" style="display: flex; align-items: center;"><img src="logo.png?v=2" alt="TechStack Global" style="height: 70px;"></a>'

# In Posts
post_logo_replacement = '<div class="logo"><a href="../index.html" style="display: flex; align-items: center;"><img src="../logo.png?v=2" alt="TechStack Global" style="height: 70px;"></a></div>'

def patch_file(filepath, target, replacement):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if target in content:
        new_content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Patch Index
if patch_file(index_file, index_target, index_replacement):
    print("Updated index.html")
else:
    # Try a more generic match for index if exact failed
    pass

# Patch Posts
for filename in os.listdir(posts_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for any logo div with logo.png
        import re
        # Match <div class="logo">...logo.png...</div>
        new_content = re.sub(r'<div class="logo">.*?logo\.png.*?</div>', post_logo_replacement, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated post: {filename}")
        else:
            # Try to catch the old B2B Automation text if it's still there
            new_content = re.sub(r'<div class="logo">.*?B2B<span>Automation</span>.*?</div>', post_logo_replacement, content, flags=re.DOTALL)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated post (from old text): {filename}")
            else:
                print(f"No logo found in post: {filename}")
