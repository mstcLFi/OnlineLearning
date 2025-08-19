from PIL import Image

# Open your white logo
original_icon = "MSTC logo wit RGB.png"  # white version
img = Image.open(original_icon)

# Target size for navbar logo (width & height in px)
target_size = 512  # you can adjust if needed

# Create a square canvas with transparency
square_img = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))

# Resize the original while keeping aspect ratio
img_ratio = img.width / img.height
if img_ratio > 1:  # width > height
    new_width = target_size
    new_height = int(target_size / img_ratio)
else:              # height >= width
    new_height = target_size
    new_width = int(target_size * img_ratio)

resized_img = img.resize((new_width, new_height), Image.LANCZOS)

# Paste the resized image centered on the square canvas
paste_x = (target_size - new_width) // 2
paste_y = (target_size - new_height) // 2
square_img.paste(resized_img, (paste_x, paste_y), resized_img.convert("RGBA"))

# Save the navbar-specific white logo
square_img.save("navbar-logo-wit.png", format="PNG")
print(f"Saved navbar-logo-wit.png ({target_size}x{target_size})")
