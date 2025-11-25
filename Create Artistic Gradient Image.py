from PIL import Image

w, h = 300, 300
img = Image.new("RGB", (w, h))

# Fill each pixel with a color pattern
for x in range(w):
    for y in range(h):
        img.putpixel((x, y), (x % 256, y % 256, (x * y) % 256))

# Display the generated image
img.show()
