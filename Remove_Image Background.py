from rembg import remove
from PIL import Image

input_path = 'RG.jpg'
output_path = 'RG_NEW.png'

# Open input image
inp = Image.open(input_path)

# Remove background
output = remove(inp)

# Save output image
output.save(output_path)

# Display the output image
Image.open(output_path)
