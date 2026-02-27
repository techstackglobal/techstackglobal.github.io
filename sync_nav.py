import os
import glob
import re

nav_pattern = re.compile(r'<ul class="nav-links"[^>]*>.*?</ul>', re.DOTALL)

def update_nav(directory, prefix=""):
    new_nav = f"""            <button class="menu-toggle" aria-label="Toggle Menu">
                <i class="fa-solid fa-bars"></i>
            </button>
            <ul class="nav-links" id="nav-links">
                <li><a href="{prefix}index.html">Home</a></li>
                <li><a href="{prefix}amazon-stack.html">Amazon Stack</a></li>
                <li><a href="{prefix}blog.html">Guides</a></li>
                <li><a href="{prefix}about.html">About</a></li>
                <li><a href="{prefix}contact.html">Contact</a></li>
            </ul>"""

    for file_path in glob.glob(os.path.join(directory, '*.html')):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Let's preserve the "active" class on the current page
        active_class = ' class="active"'
        basename = os.path.basename(file_path)
        
        # Determine which link should be active based on file name
        target_nav = new_nav
        if basename == 'index.html':
            target_nav = target_nav.replace(f'href="{prefix}index.html"', f'href="{prefix}index.html" class="active"')
        elif basename == 'amazon-stack.html':
            target_nav = target_nav.replace(f'href="{prefix}amazon-stack.html"', f'href="{prefix}amazon-stack.html" class="active"')
        elif basename == 'blog.html':
            target_nav = target_nav.replace(f'href="{prefix}blog.html"', f'href="{prefix}blog.html" class="active"')
        elif basename == 'about.html':
            target_nav = target_nav.replace(f'href="{prefix}about.html"', f'href="{prefix}about.html" class="active"')
        elif basename == 'contact.html':
            target_nav = target_nav.replace(f'href="{prefix}contact.html"', f'href="{prefix}contact.html" class="active"')
            
        new_content = nav_pattern.sub(target_nav, content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")
        else:
            print(f"No changes needed in {file_path}")

update_nav('.', '')
update_nav('posts', '../')
