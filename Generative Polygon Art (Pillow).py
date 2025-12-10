from PIL import Image, ImageDraw
import random

w, h = 400, 400
img = Image.new("RGB", (w, h), "black")
draw = ImageDraw.Draw(img)

# Draw 200 random colorful triangles
for _ in range(200):
    points = [(random.randint(0, w), random.randint(0, h)) for _ in range(3)]
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    draw.polygon(points, fill=color)

img.show()
