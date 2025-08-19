from PIL import Image

# Open your original icon
original_icon = "MSTC logo kleur RGB.png"
img = Image.open(original_icon)

# Define the sizes we need
sizes = {
    "apple-touch-icon.png": 180,
    "icon-32.png": 32,
    "icon-192.png": 192,
    "icon-512.png": 512,
}

for filename, target_size in sizes.items():
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
    
    square_img.save(filename, format="PNG")
    print(f"Saved {filename} ({target_size}x{target_size})")

print("All icons generated successfully!")
