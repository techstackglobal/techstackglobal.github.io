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
    
    # Proper XML with encoding and formatting
    xml_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_urlset_open = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml_content = xml_header + xml_urlset_open
    
    html_files = sorted(get_html_files())
    
    for f in html_files:
        rel_path = os.path.relpath(f, BASE_DIR).replace('\\', '/')
        if rel_path in ['404.html', 'thank-you.html', 'google50e160eb06944afd.html']:
            continue
            
        # Clean URL: remove index.html from the end of URLs for SEO canonicality
        display_path = rel_path
        if display_path.endswith('index.html'):
            display_path = display_path[:-10]
        elif display_path == 'index.html':
            display_path = ''
            
        url = f"{BASE_URL}/{display_path}"
        xml_content += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{date_str}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
        
    xml_content += '</urlset>'
    
    with open(sitemap_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(xml_content)
        
    print(f"Minimal sitemap generated at {sitemap_path}")

if __name__ == "__main__":
    main()
