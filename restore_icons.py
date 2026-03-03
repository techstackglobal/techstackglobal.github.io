import shutil
import os

root = r'C:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog'
src = os.path.join(root, 'assets', 'icons', 'favicon-v5.png')
src_logo = os.path.join(root, 'assets', 'icons', 'techstack-logo-192-v5.png')
src_16 = os.path.join(root, 'assets', 'icons', 'favicon-16-v5.png')
src_32 = os.path.join(root, 'assets', 'icons', 'favicon-32-v5.png')

targets = [
    (src, os.path.join(root, 'favicon.ico')),
    (src, os.path.join(root, 'assets', 'icons', 'favicon.ico')),
    (src_16, os.path.join(root, 'assets', 'icons', 'favicon-16.png')),
    (src_32, os.path.join(root, 'assets', 'icons', 'favicon-32.png')),
    (src_logo, os.path.join(root, 'assets', 'icons', 'techstack-logo-192.png')),
]

for s, t in targets:
    try:
        shutil.copy2(s, t)
        print(f"Restored: {t}")
    except Exception as e:
        print(f"Error restoring {t}: {e}")
