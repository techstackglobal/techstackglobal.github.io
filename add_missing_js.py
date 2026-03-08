import glob
from bs4 import BeautifulSoup

added_count = 0
files_to_update = glob.glob('posts/*.html')
print(f"Scanning {len(files_to_update)} files for missing script.js...")

for file in files_to_update:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all('script')
    
    has_script_js = False
    for s in scripts:
        src = s.get('src')
        if src and ('script.js' in src):
            has_script_js = True
            break
            
    if not has_script_js:
        print(f"Adding script.js to {file}")
        new_script = soup.new_tag('script', src='../script.js')
        if soup.body:
            soup.body.append(new_script)
            with open(file, 'w', encoding='utf-8') as f:
                # To prevent BeautifulSoup from messing up formatting, write prettify if possible or just inject string.
                # String injection is often safer if BS breaks formatting.
                pass
            
            # Since BS prettify sometimes destroys formatting or indents weirdly, let's use simple string replace
            html = html.replace('</body>', '  <script src="../script.js"></script>\n</body>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(html)
            added_count += 1
        else:
            print(f'{file} missing body tag!')

print(f'\nDone! Added ../script.js to {added_count} files.')
