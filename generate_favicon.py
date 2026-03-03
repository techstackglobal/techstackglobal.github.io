import os
from PIL import Image, ImageDraw, ImageFont

def create_favicon():
    size = 1024
    bg_color = '#020617' # Site primary background (bg-darker)
    text_color = '#ffffff'
    
    img = Image.new('RGB', (size, size), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try Verdana Bold for maximum clarity at tiny sizes
    try:
        font = ImageFont.truetype("C:\\Windows\\Fonts\\verdanab.ttf", int(size * 0.45))
    except IOError:
        font = ImageFont.truetype("C:\\Windows\\Fonts\\arialbd.ttf", int(size * 0.45))

    text = "TSG"
    
    # Get accurate bounding box
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_w = right - left
    text_h = bottom - top
    
    # Center mathematically exactly on the text pixels
    x = (size - text_w) / 2 - left
    y = (size - text_h) / 2 - top
    
    draw.text((x, y), text, fill=text_color, font=font)

    target_dir = os.path.join("assets", "favicon")
    os.makedirs(target_dir, exist_ok=True)
    
    resample = Image.Resampling.LANCZOS
    
    img.resize((512, 512), resample).save(os.path.join(target_dir, "android-chrome-512x512.png"))
    img.resize((192, 192), resample).save(os.path.join(target_dir, "android-chrome-192x192.png"))
    img.resize((180, 180), resample).save(os.path.join(target_dir, "apple-touch-icon.png"))
    img.resize((32, 32), resample).save(os.path.join(target_dir, "favicon-32x32.png"))
    
    # Sharp downscale for 16x16
    img16 = img.resize((128, 128), resample).resize((16, 16), resample)
    img16.save(os.path.join(target_dir, "favicon-16x16.png"))
    
    # generate ico
    icon_sizes = [(16, 16), (32, 32), (48, 48)]
    # Use the 48x48 from lanczos for the base of ico
    icon_img = img.resize((48, 48), resample)
    img.save(os.path.join(target_dir, "favicon.ico"), format='ICO', sizes=icon_sizes)

    # Re-write the manifest to match the new background color
    manifest = """{
    "name": "TechStack Global",
    "short_name": "TSG",
    "icons": [
        {
            "src": "/assets/favicon/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/assets/favicon/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "theme_color": "#020617",
    "background_color": "#020617",
    "display": "standalone"
}"""
    with open(os.path.join(target_dir, "site.webmanifest"), "w") as f:
        f.write(manifest)

if __name__ == "__main__":
    create_favicon()
    print("Favicons re-generated perfectly!")
