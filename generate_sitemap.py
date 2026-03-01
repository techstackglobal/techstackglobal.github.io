import os
import glob
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_URL = "https://techstackglobal.github.io"

def get_html_files():
    skip_dirs = ['.git', '.vscode', 'node_modules', '.gemini']
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    date_str = datetime.now().strftime('%Y-%m-%d')
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    html_files = get_html_files()
    
    for f in html_files:
        rel_path = os.path.relpath(f, BASE_DIR).replace('\\', '/')
        if rel_path == 'index.html':
            url = f"{BASE_URL}/"
            priority = "1.0"
        elif rel_path == 'blog.html':
            url = f"{BASE_URL}/{rel_path}"
            priority = "0.9"
        elif rel_path.startswith('posts/'):
            url = f"{BASE_URL}/{rel_path}"
            priority = "0.8"
        else:
            url = f"{BASE_URL}/{rel_path}"
            priority = "0.6"
            
        xml_content += f'  <url>\n'
        xml_content += f'    <loc>{url}</loc>\n'
        xml_content += f'    <lastmod>{date_str}</lastmod>\n'
        xml_content += f'    <changefreq>monthly</changefreq>\n'
        xml_content += f'    <priority>{priority}</priority>\n'
        xml_content += f'  </url>\n'
        
    xml_content += '</urlset>\n'
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(xml_content)
        
    print(f"Sitemap generated at {sitemap_path}")

if __name__ == "__main__":
    main()
