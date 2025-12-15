from PIL import Image

# Open image
img = Image.open("bird.jpeg")

# Get all pixels (R, G, B)
pixels = list(img.getdata())

# Extract 1 LSB from the Red channel of first 8 pixels
bits = [(p[0] & 1) for p in pixels[:8]]

# Convert bits to string
msg = "".join(str(b) for b in bits)

print("Hidden bits:", msg)
