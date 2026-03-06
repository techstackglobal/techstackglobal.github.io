from PIL import Image

def remove_white_background(img, threshold=240):
    img = img.convert("RGBA")
    data = img.getdata()
    new_data = []
    for item in data:
        # Check if the pixel is white-ish (red, green, blue all above threshold)
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            # Change all white-ish pixels to transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img

source_path = "C:/tmp/tsg-logo-source.png"
print(f"Opening {source_path}")
img = Image.open(source_path)

img_transparent = remove_white_background(img)

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
