import os
import glob

base_dir = r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog'
html_files = glob.glob(os.path.join(base_dir, '*.html')) + glob.glob(os.path.join(base_dir, 'posts', '*.html'))

replacements = {
    'href="index.html"': 'href="/index.html"',
    'href="blog.html"': 'href="/blog.html"',
    'href="about.html"': 'href="/about.html"',
    'href="contact.html"': 'href="/contact.html"',
    'href="affiliate-disclosure.html"': 'href="/affiliate-disclosure.html"',
    'href="style.css"': 'href="/style.css"',
    'href="favicon.png"': 'href="/favicon.png"',
    'src="script.js"': 'src="/script.js"',
    
    'href="../index.html"': 'href="/index.html"',
    'href="../blog.html"': 'href="/blog.html"',
    'href="../about.html"': 'href="/about.html"',
    'href="../contact.html"': 'href="/contact.html"',
    'href="../affiliate-disclosure.html"': 'href="/affiliate-disclosure.html"',
    'href="../style.css"': 'href="/style.css"',
    'href="../favicon.png"': 'href="/favicon.png"',
    'src="../script.js"': 'src="/script.js"',
    
    'href="posts/': 'href="/posts/',
    'href="blog.html?cat=': 'href="/blog.html?cat='
}

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files with root-relative paths.")
