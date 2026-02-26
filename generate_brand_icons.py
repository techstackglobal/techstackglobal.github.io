import os
import glob
import re
from PIL import Image, ImageDraw

base_dir = r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog'
icons_dir = os.path.join(base_dir, 'assets', 'icons')
os.makedirs(icons_dir, exist_ok=True)

size = 192
img = Image.new('RGBA', (size, size), (0,0,0,0))
draw = ImageDraw.Draw(img)

# Dark sleek background
draw.rounded_rectangle([(0,0), (size-1, size-1)], radius=40, fill=(15, 23, 42, 255))

# Sharp tech 'T' logo in TechStack Blue
draw.rectangle([(50, 60), (142, 85)], fill=(56, 189, 248, 255)) # Top bar
draw.rectangle([(84, 85), (108, 140)], fill=(56, 189, 248, 255)) # Stem

# Save files
img.save(os.path.join(icons_dir, 'techstack-logo-192.png'))

img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
img_32.save(os.path.join(icons_dir, 'favicon-32.png'))

img_16 = img.resize((16, 16), Image.Resampling.LANCZOS)
img_16.save(os.path.join(icons_dir, 'favicon-16.png'))

img_32.save(os.path.join(icons_dir, 'favicon.ico'), format='ICO', sizes=[(16, 16), (32, 32)])

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192">
  <rect width="192" height="192" rx="40" fill="#0f172a"/>
  <path d="M 50 60 L 142 60 L 142 85 L 108 85 L 108 140 L 84 140 L 84 85 L 50 85 Z" fill="#38bdf8"/>
</svg>'''
with open(os.path.join(icons_dir, 'techstack-logo.svg'), 'w') as f:
    f.write(svg)

print('Icons generated.')

html_files = glob.glob(os.path.join(base_dir, '*.html')) + glob.glob(os.path.join(base_dir, 'posts', '*.html'))

new_tags = '''    <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/favicon-16.png">
    <link rel="apple-touch-icon" sizes="192x192" href="/assets/icons/techstack-logo-192.png">
    <link rel="shortcut icon" href="/assets/icons/favicon.ico">'''

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip existing favicon tags
    content = re.sub(r'<link[^>]+rel=[\'"](?:shortcut )?icon[\'"][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<link[^>]+rel=[\'"]apple-touch-icon[\'"][^>]*>', '', content, flags=re.IGNORECASE)
    
    # Clean up empty lines left behind by re.sub
    content = re.sub(r'\n\s*\n\s*</head>', '\n</head>', content)
    
    # Insert new tags
    content = content.replace('</head>', f'{new_tags}\n</head>')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print('HTML headers updated.')
