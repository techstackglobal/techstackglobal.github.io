import os
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_URL = "https://techstackglobal.github.io"

def get_html_files():
    skip_dirs = ['.git', '.vscode', 'node_modules', '.gemini', '.agent', '.planning', '.venv', 'tmp', 'tools', 'blogging_project']
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
    
    # HERALD Standard: High-compatibility XML with strict UTF-8
    xml_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    # Optional XML stylesheet can help in some cases, but for GSC, the structure is most critical
    xml_urlset_open = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml_content = xml_header + xml_urlset_open
    
    html_files = sorted(get_html_files())
    
    # 1. Primary Page (Root)
    xml_content += f'  <url>\n    <loc>{BASE_URL}/</loc>\n    <lastmod>{date_str}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>\n'

    for f in html_files:
        rel_path = os.path.relpath(f, BASE_DIR).replace('\\', '/')
        
        # Skip utility and low-value pages
        if rel_path in ['404.html', 'thank-you.html', 'index.html'] or 'google' in rel_path:
            continue
            
        # GSD Strategy: Strict canonical URLs
        # Remove .html extension for cleaner indexing if server supports it, 
        # but for GH Pages, we keep the .html but ensure consistency.
        # We also want to assign priority based on depth.
        
        url = f"{BASE_URL}/{rel_path}"
        
        # Priority Logic: Higher priority for core clusters
        priority = "0.8"
        if "posts/" in rel_path:
            priority = "0.7"
        if rel_path in ["blog.html", "amazon-stack.html"]:
            priority = "0.9"
            
        xml_content += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{date_str}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{priority}</priority>\n  </url>\n'
        
    xml_content += '</urlset>'
    
    # Write with explicit UTF-8 and ensure NO BOM to prevent GSC parsing errors
    with open(sitemap_path, 'wb') as f:
        f.write(xml_content.encode('utf-8'))
        
    print(f"GSD Optimized sitemap generated at {sitemap_path}")

if __name__ == "__main__":
    main()
