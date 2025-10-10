import numpy as np
from PIL import Image
import random

# Image dimensions
w, h = 400, 400

# Create an empty image array
data = np.zeros((h, w, 3), dtype=np.uint8)

# Fill the image with AI-style patterns
for y in range(h):
    for x in range(w):
        r = int((x * y) % 255)
        g = int((x + y * 2) % 255)
        b = random.randint(0, 255)
        data[y, x] = [r, g, b]

# Convert array to image
img = Image.fromarray(data, 'RGB')
img.save("neural_art.png")

print("AI-style art saved as neural_art.png")
