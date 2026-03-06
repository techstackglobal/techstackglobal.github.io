from PIL import Image
import collections

def remove_outer_white(img_path, threshold=240):
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    # Identify background using BFS
    # Start from top-left, top-right, bottom-left, bottom-right
    queue = collections.deque()
    visited = set()
    
    # Add all border pixels to queue
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
        
    # We only want to process white-ish borders
    border_queue = collections.deque()
    for (x, y) in queue:
        r, g, b, a = pixels[x, y]
        if r > threshold and g > threshold and b > threshold:
            border_queue.append((x, y))
            
    queue = border_queue
    
    while queue:
        x, y = queue.popleft()
        r, g, b, a = pixels[x, y]
        
        # Make transparent
        pixels[x, y] = (255, 255, 255, 0)
        
        # Check neighbors
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    nr, ng, nb, na = pixels[nx, ny]
                    if nr > threshold and ng > threshold and nb > threshold:
                        queue.append((nx, ny))
                        
    # Ensure all original fully transparent pixels stay transparent
    for x in range(width):
        for y in range(height):
            if pixels[x, y][3] == 0:
                pixels[x, y] = (255, 255, 255, 0)
                
    return img

source_path = "C:/tmp/tsg-logo-source.png"
print(f"Opening {source_path}")
img_transparent = remove_outer_white(source_path)

# Save sizes
size_180 = img_transparent.resize((180, 180), Image.Resampling.LANCZOS)
size_180.save("apple-touch-icon.png")

size_32 = img_transparent.resize((32, 32), Image.Resampling.LANCZOS)
size_32.save("favicon-32x32.png")

size_16 = img_transparent.resize((16, 16), Image.Resampling.LANCZOS)
size_16.save("favicon-16x16.png")

# Save ICO with multiple layers
img_transparent.save(
    "favicon.ico",
    format="ICO",
    sizes=[(16, 16), (32, 32)],
    append_images=[size_16, size_32]
)
print("Saved all favicon assets in repo root.")
