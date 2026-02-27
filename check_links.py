import os
import re

def check_internal_links():
    base_dir = 'c:/Users/PMLS/Desktop/Youtube Shorts/b2b_blog'
    html_files = []
    
    for root, dirs, files in os.walk(base_dir):
        # Exclude node_modules, .git, etc if present
        if '.git' in root or '.venv' in root:
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
                
    broken_links = []
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Find all href=
            hrefs = re.findall(r'href=["\'](.*?)["\']', content)
            
            for href in hrefs:
                if href.startswith('http') or href.startswith('mailto:') or href.startswith('#') or href == '':
                    continue
                
                # Resolve relative path
                # Strip query params or hash
                href_clean = href.split('?')[0].split('#')[0]
                if not href_clean:
                    continue
                    
                target_path = os.path.normpath(os.path.join(os.path.dirname(filepath), href_clean))
                
                if not os.path.exists(target_path):
                    broken_links.append((filepath, href))
                    
    report_path = 'c:/Users/PMLS/.gemini/antigravity/brain/8acb5e45-297b-4c05-ae50-1d7cdeac50b0/broken_links_report.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        if broken_links:
            f.write("Broken Links Found:\n")
            for source, link in broken_links:
                f.write(f"In {os.path.basename(source)}: {link}\n")
            print(f"Found {len(broken_links)} broken links. Check report.")
        else:
            f.write("No broken internal links found.\n")
            print("No broken internal links found.")

if __name__ == '__main__':
    check_internal_links()
