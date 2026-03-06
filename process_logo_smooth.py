from PIL import Image
import collections

def clean_logo(source_path):
    img = Image.open(source_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    # 1. Flood fill to identify the outer background.
    # We queue the edges and explore pixels that are relatively bright (>180).
    queue = collections.deque()
    visited = set()
    
    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
        visited.add((x, 0))
        visited.add((x, height - 1))
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))
        visited.add((0, y))
        visited.add((width - 1, y))
        
    bg_pixels = set()
    
    while queue:
        x, y = queue.popleft()
        r, g, b, a = pixels[x, y]
        # Tolerate up to lightness 180 to catch all the anti-aliased glow
        if r > 180 and g > 180 and b > 180:
            bg_pixels.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        
    # 2. Convert white background into transparency gradient
    for x, y in bg_pixels:
        r, g, b, a = pixels[x, y]
        # Find how "white" it is.
        # Pure white (255) -> Alpha 0
        # Darker (180) -> Alpha 255
        lightness = (r + g + b) / 3.0
        
        if lightness >= 250:
            alpha = 0
            # Set color to a dark blue to avoid white halos during resizing
            # Using an approximate dark blue (10, 37, 64)
            r, g, b = 10, 37, 64 
        elif lightness < 180:
            alpha = 255
        else:
            # Linear map 180->255 and 250->0
            # alpha = 255 * (250 - lightness) / (250 - 180)
            alpha = int(255 * (250 - lightness) / 70.0)
            alpha = max(0, min(255, alpha))
            
        pixels[x, y] = (r, g, b, alpha)
        
    print(f"BBox before clean: {img.getbbox()}")
    # Force crop transparent borders
    # we can trim purely by checking alpha > 10
    bbox_img = img.point(lambda p: 255 if p > 10 else 0)
    bbox = bbox_img.getchannel("A").getbbox()
    print(f"BBox based on Alpha > 10: {bbox}")
    if bbox:
        img = img.crop(bbox)
    return img
source_path = "C:/tmp/tsg-logo-source.png"
print(f"Opening {source_path}")
img_transparent = clean_logo(source_path)

# Save sizes using BILINEAR to avoid Lanczos ringing on alpha edges
size_180 = img_transparent.resize((180, 180), Image.Resampling.BILINEAR)
size_180.save("apple-touch-icon.png")

size_32 = img_transparent.resize((32, 32), Image.Resampling.BILINEAR)
size_32.save("favicon-32x32.png")

size_16 = img_transparent.resize((16, 16), Image.Resampling.BILINEAR)
size_16.save("favicon-16x16.png")

# Save ICO with multiple layers
img_transparent.save(
    "favicon.ico",
    format="ICO",
    sizes=[(16, 16), (32, 32)],
    append_images=[size_16, size_32]
)
print("Saved perfectly anti-aliased favicon assets in repo root.")
