import glob
import os

html_files = glob.glob(r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\**\*.html', recursive=True)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple replace
    new_content = content.replace('href="style.css"', 'href="style.css?v=2"')
    new_content = new_content.replace('href="../style.css"', 'href="../style.css?v=2"')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
print("Cache busting string added to all HTML files!")
