from PIL import Image, ImageDraw
from IPython.display import display

img = Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(img)

draw.rectangle([50, 50, 150, 150], outline="black", width=3)

display(img)  
