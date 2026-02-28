import glob, os, re

files_root = glob.glob(r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\*.html')
files_posts = glob.glob(r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts\*.html')

def fix_file(filepath, script_src):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if script is already there
        if re.search(r'<script src=[\"\']' + re.escape(script_src) + r'(\?v=\d+)?[\"\']></script>', content):
            return 0
        
        if '</body>' in content:
            new_script = f'    <script src=\"{script_src}\"></script>\n'
            new_content = content.replace('</body>', new_script + '</body>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed: {os.path.basename(filepath)}')
            return 1
    except Exception as e:
        print(f'Error fixing {filepath}: {e}')
    return 0

root_count = sum(fix_file(f, 'script.js') for f in files_root)
posts_count = sum(fix_file(f, '../script.js') for f in files_posts)

print(f'\nTotal Fixed: {root_count + posts_count}')
