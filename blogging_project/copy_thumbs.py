import shutil
import os

source_dir = r"C:\Users\PMLS\.gemini\antigravity\brain\0999bfc6-ed83-4b9f-bde2-66534d0702ea"
target_dir = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"

files_to_copy = {
    "thumb_shopify_vs_bigcommerce_1771998587497.png": "thumb_shopify.png",
    "thumb_fiverr_pro_b2b_1771998654019.png": "thumb_fiverr.png",
    "thumb_tech_stack_2026_1771998772256.png": "thumb_stack.png",
    "thumb_affiliate_blueprint_1771998886968.png": "thumb_affiliate.png",
    "thumb_automation_guide_1771999409394.png": "thumb_guide.png"
}

for src_name, target_name in files_to_copy.items():
    src_path = os.path.join(source_dir, src_name)
    target_path = os.path.join(target_dir, target_name)
    
    if os.path.exists(src_path):
        shutil.copy2(src_path, target_path)
        print(f"Copied {src_name} to {target_name}")
    else:
        print(f"Error: {src_path} not found")
