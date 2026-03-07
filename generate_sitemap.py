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
    
    # Minimal XML without indentation or extra tags
    xml_content = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    
    html_files = sorted(get_html_files())
    
    for f in html_files:
        rel_path = os.path.relpath(f, BASE_DIR).replace('\\', '/')
        if rel_path in ['404.html', 'thank-you.html', 'google50e160eb06944afd.html']:
            continue
            
        url = f"{BASE_URL}/{rel_path}"
        xml_content += f'<url><loc>{url}</loc><lastmod>{date_str}</lastmod></url>'
        
    xml_content += '</urlset>'
    
    with open(sitemap_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(xml_content)
        
    print(f"Minimal sitemap generated at {sitemap_path}")

if __name__ == "__main__":
    main()
