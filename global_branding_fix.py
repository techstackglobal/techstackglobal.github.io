import os
import re

repo_root = r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog'

def update_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # 1. Update Organization Schema Logo (high-res apple icon is best for Google)
    schema_pattern = r'("@type"\s*:\s*"Organization",\s*"name"\s*:\s*"TechStack Global",\s*"url"\s*:\s*"https://techstackglobal.github.io/",\s*"logo"\s*:\s*)"[^"]+"'
    new_content = re.sub(schema_pattern, r'\1"https://techstackglobal.github.io/apple-touch-icon.png"', new_content)

    # 2. Update Favicon Links with Cache-Busting ?v=2
    # Matches href="/favicon.ico", href="../favicon.ico", etc.
    new_content = re.sub(r'href=["\']([^"\']*favicon\.ico)(\?v=\d+)?["\']', r'href="\1?v=2"', new_content)
    new_content = re.sub(r'href=["\']([^"\']*favicon-32x32\.png)(\?v=\d+)?["\']', r'href="\1?v=2"', new_content)
    new_content = re.sub(r'href=["\']([^"\']*favicon-16x16\.png)(\?v=\d+)?["\']', r'href="\1?v=2"', new_content)
    new_content = re.sub(r'href=["\']([^"\']*apple-touch-icon\.png)(\?v=\d+)?["\']', r'href="\1?v=2"', new_content)

    # 3. Handle specific variants like techstack-logo-192.png if they appear in head
    new_content = re.sub(r'href=["\']([^"\']*techstack-logo-192\.png)(\?v=\d+)?["\']', r'href="\1?v=2"', new_content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# List directories to process
dirs_to_process = [repo_root, os.path.join(repo_root, 'posts')]

updated_count = 0
for d in dirs_to_process:
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.endswith('.html'):
                fpath = os.path.join(d, f)
                if update_html_file(fpath):
                    updated_count += 1
                    print(f"Updated: {f}")

print(f"\nGlobal update complete. Total files updated: {updated_count}")
