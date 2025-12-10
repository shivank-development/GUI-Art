from barcode import EAN13
from barcode.writer import ImageWriter
from IPython.display import Image, display

# EAN-13 requires 12 digits, checksum will be added automatically
code_value = "590123412345"   # 12 digits only

# --- PNG barcode ---
barcode_png = EAN13(code_value, writer=ImageWriter())
png_file = barcode_png.save("ean13_clcoding")

# --- SVG barcode ---
barcode_svg = EAN13(code_value)  # Default output = SVG
svg_file = barcode_svg.save("ean13_clcoding_svg")

# Display PNG inside Jupyter Notebook
display(Image(png_file))
