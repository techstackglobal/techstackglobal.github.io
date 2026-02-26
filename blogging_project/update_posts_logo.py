import os

posts_dir = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts"
logo_html_replacement = '''<div class="logo"><a href="../index.html"><img src="../logo.png" alt="TechStack Global" style="height: 50px;"></a></div>'''
# Match the specific structure found in the view_file output
target_pattern = '<div class="logo"><a href="../index.html"\n                    style="text-decoration:none; color:inherit;">TechStack<span>Global</span></a></div>'

# Also handle potential single-line versions if they exist
target_pattern_v2 = '<div class="logo"><a href="../index.html" style="text-decoration:none; color:inherit;">TechStack<span>Global</span></a></div>'

for filename in os.listdir(posts_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        if target_pattern in content:
            content = content.replace(target_pattern, logo_html_replacement)
            updated = True
        elif target_pattern_v2 in content:
            content = content.replace(target_pattern_v2, logo_html_replacement)
            updated = True
            
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"Pattern not found in {filename}")
