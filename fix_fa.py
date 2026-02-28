import sys

files = [
    'about.html', 
    'contact.html', 
    'affiliate-disclosure.html', 
    'privacy-policy.html', 
    'terms-of-service.html'
]

fa_tag = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'

count = 0
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if fa_tag not in content:
        print(f"Adding Font Awesome to {filepath}")
        content = content.replace(
            '<link rel="stylesheet" href="style.css">', 
            '<link rel="stylesheet" href="style.css">\n    ' + fa_tag
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Fixed {count} files.")
