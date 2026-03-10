import shutil
import os

repo_root = r'c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog'
icons_dir = os.path.join(repo_root, 'assets', 'icons')

# Mapping of TSG (New) -> Destination (Old/Legacy Path)
sync_map = {
    'apple-touch-icon.png': 'techstack-logo-192.png',
    'favicon-32x32.png': 'favicon-32.png',
    'favicon-16x16.png': 'favicon-16.png'
}

print("Starting asset synchronization...")

for src_name, dest_name in sync_map.items():
    src_path = os.path.join(repo_root, src_name)
    dest_path = os.path.join(icons_dir, dest_name)
    
    if os.path.exists(src_path):
        print(f"Copying {src_name} to {dest_path}")
        shutil.copy2(src_path, dest_path)
    else:
        print(f"Warning: Source {src_path} not found.")

print("Asset synchronization complete.")
