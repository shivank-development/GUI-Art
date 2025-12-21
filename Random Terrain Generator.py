from PIL import Image
import random

w, h = 400, 400
img = Image.new("RGB", (w, h))

for y in range(h):
    for x in range(w):
        r = int(random.gauss(128, 60))
        g = int(random.gauss(100, 50))
        b = int(random.gauss(80, 40))
        img.putpixel((x, y), (r % 256, g % 256, b % 256))

img.show()
#img.save("random_terrain.png")