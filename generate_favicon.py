import os
from PIL import Image, ImageDraw, ImageFont

def create_favicon():
    target_dir = os.path.join("assets", "favicon")
    os.makedirs(target_dir, exist_ok=True)
    
    bg_color = (2, 6, 23) # #020617
    text_color = (255, 255, 255) # #ffffff
    
    # ---------------------------------------------------------
    # 1) Generate the 16x16 PIXEL-PERFECT grid to avoid ALL blur
    # ---------------------------------------------------------
    pixel_map = [
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0011101110011100",
        "0001001000100000",
        "0001001110101100",
        "0001000010100100",
        "0001001110011100",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000"
    ]
    
    img16 = Image.new('RGB', (16, 16), color=bg_color)
    for y, row in enumerate(pixel_map):
        for x, char in enumerate(row):
            if char == '1':
                img16.putpixel((x, y), text_color)
                
    # Save the perfect 16x16
    img16.save(os.path.join(target_dir, "favicon-16x16.png"))
    
    # Scale up mathematically exactly for 32x32 so it remains perfectly crisp
    img32 = img16.resize((32, 32), Image.Resampling.NEAREST)
    img32.save(os.path.join(target_dir, "favicon-32x32.png"))

    # ---------------------------------------------------------
    # 2) Generate the 512x512 High-Res Icons using standard vectors
    # ---------------------------------------------------------
    size = 1024
    img = Image.new('RGB', (size, size), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("C:\\Windows\\Fonts\\arialbd.ttf", int(size * 0.45))
    except IOError:
        font = ImageFont.load_default()

    text = "T S G"
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_w = right - left
    text_h = bottom - top
    
    if text_w > size * 0.9:
        scale = (size * 0.9) / text_w
        font = ImageFont.truetype("C:\\Windows\\Fonts\\arialbd.ttf", int(size * 0.45 * scale))
        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
        text_w = right - left
        text_h = bottom - top

    x = (size - text_w) / 2 - left
    y = (size - text_h) / 2 - top
    draw.text((x, y), text, fill=text_color, font=font)
    
    resample = Image.Resampling.LANCZOS
    
    img.resize((512, 512), resample).save(os.path.join(target_dir, "android-chrome-512x512.png"))
    img.resize((192, 192), resample).save(os.path.join(target_dir, "android-chrome-192x192.png"))
    img.resize((180, 180), resample).save(os.path.join(target_dir, "apple-touch-icon.png"))
    
    # Multi-size ICO: 16 (pixel art), 32 (pixel art), 48 (lanczos)
    img48 = img.resize((48, 48), resample)
    icon_sizes = [(16, 16), (32, 32), (48, 48)]
    
    # We can create a multi-sized ICO by passing multiple images to the save method,
    # or let PIL downscale from img. Since we want our custom 16 and 32, we should use append_images.
    img16.save(os.path.join(target_dir, "favicon.ico"), format='ICO', sizes=icon_sizes, append_images=[img32, img48])
    
if __name__ == "__main__":
    create_favicon()
    print("Favicons generated with True Pixel-Perfect precision!")
