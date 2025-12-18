from PIL import Image
import random, math

# Image size
w, h = 300, 300
img = Image.new("RGB", (w, h))

for y in range(h):
    for x in range(w):
        sin_component = 127 * math.sin(x / 15)
        cos_component = 127 * math.cos(y / 15)
        noise = random.randint(0, 50)
        v = int(sin_component + cos_component + noise)

        # psychedelic colors
        img.putpixel((x, y), (v % 256, (v * 2) % 256, (v * 3) % 256))

img.show()
