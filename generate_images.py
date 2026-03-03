import os
from PIL import Image, ImageDraw, ImageFont

def create_hero_image(filename, text1, text2):
    # Create a simple, brand-consistent hero image (e.g., dark background with tech flair)
    width, height = 1200, 630
    # Dark blueish/grayish tech background
    img = Image.new('RGB', (width, height), color=(15, 23, 36))
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, or fallback to default
    try:
        font_large = ImageFont.truetype("arialbd.ttf", 60)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    # we can just draw some text
    # Calculate text bounding boxes to center them
    bbox_large = draw.textbbox((0, 0), text1, font=font_large)
    w_large = bbox_large[2] - bbox_large[0]
    h_large = bbox_large[3] - bbox_large[1]
    
    bbox_small = draw.textbbox((0, 0), text2, font=font_small)
    w_small = bbox_small[2] - bbox_small[0]
    h_small = bbox_small[3] - bbox_small[1]
    
    # Draw text
    draw.text(((width - w_large) / 2, (height - h_large) / 2 - 40), text1, fill=(255, 255, 255), font=font_large)
    draw.text(((width - w_small) / 2, (height - h_small) / 2 + 40), text2, fill=(0, 255, 157), font=font_small)
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img.save(filename, format="JPEG", quality=85)

create_hero_image(
    "c:/Users/PMLS/Desktop/Youtube Shorts/b2b_blog/posts/images/pillar-headphones-hero.jpg",
    "Best Noise Cancelling Headphones",
    "2026 Buyer's Guide"
)

create_hero_image(
    "c:/Users/PMLS/Desktop/Youtube Shorts/b2b_blog/posts/images/pillar-mics-hero.jpg",
    "Best Podcast Microphones",
    "2026 Buyer's Guide"
)

create_hero_image(
    "c:/Users/PMLS/Desktop/Youtube Shorts/b2b_blog/posts/images/pillar-monitors-hero.jpg",
    "Best Ultrawide Monitors",
    "2026 Buyer's Guide"
)

print("Images generated successfully.")
