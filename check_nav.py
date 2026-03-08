import glob
from bs4 import BeautifulSoup

broken = []
for file in glob.glob('posts/*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    header = soup.find('header', class_='glass-header')
    if not header:
        print(f'{file} is missing <header class="glass-header">')
        broken.append(file)
        continue
        
    nav = header.find('nav', class_='container')
    if not nav:
        print(f'{file} is missing <nav class="container"> inside header')
        broken.append(file)
        continue
    
    # Check if nav links exist
    nav_links = nav.find('ul', id='nav-links', class_='nav-links')
    if not nav_links:
        print(f'{file} is missing <ul id="nav-links" class="nav-links">')
        broken.append(file)

print(f"Total broken navigation pages: {len(broken)}")
