import glob
from bs4 import BeautifulSoup

def fix_nav():
    desired_nav_html = """
    <ul class="nav-links" id="nav-links">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../amazon-stack.html">Amazon Stack</a></li>
        <li><a href="../blog.html">Guides</a></li>
        <li><a href="../about.html">About</a></li>
        <li><a href="../contact.html">Contact</a></li>
    </ul>
    """
    new_nav_soup = BeautifulSoup(desired_nav_html, 'html.parser').find('ul')
    
    changed = 0
    for file in glob.glob('posts/*.html'):
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find('ul', id='nav-links', class_='nav-links')
        if not ul:
            # Let's try to find just ul.nav-links
            ul = soup.find('ul', class_='nav-links')
            
        if ul:
            old_str = str(ul)
            new_str = str(new_nav_soup)
            if old_str != new_str:
                ul.replace_with(new_nav_soup)
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(soup.prettify())
                changed += 1
                
    print(f"Fixed navigation in {changed} files.")

if __name__ == '__main__':
    fix_nav()
