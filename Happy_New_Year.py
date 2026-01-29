from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 500
img = Image.new("RGB", (W, H), (10, 5, 20))
draw = ImageDraw.Draw(img)

# Load fonts
try:
    big = ImageFont.truetype("arial.ttf", 140)
    small = ImageFont.truetype("arial.ttf", 40)
except:
    big = small = ImageFont.load_default()

# Glow text function
def glow_text(x, y, text, color, font):
    temp = Image.new("RGB", (W, H), (0, 0, 0))
    tdraw = ImageDraw.Draw(temp)

    tdraw.text((x, y), text, font=font, fill=color)
    temp = temp.filter(ImageFilter.GaussianBlur(8))

    img.paste(temp, (0, 0), temp.convert("L"))
    draw.text((x, y), text, font=font, fill=color)

# Draw glowing text
glow_text(350, 40, "HAPPY NEW YEAR!", (0, 255, 255), small)
glow_text(280, 150, "FROM", (255, 0, 255), big)
glow_text(420, 330, "PYTHON", (0, 200, 255), small)

# Save image
img.save("neon_new_year_2026.png")
print("Saved neon_new_year_2026.png")
