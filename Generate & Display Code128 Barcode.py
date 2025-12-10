# Install required package:
# pip install python-barcode[pillow]

from barcode import Code128
from barcode.writer import ImageWriter

# Create barcode with image output
barcode = Code128("CLCODING-123", writer=ImageWriter())

# Save barcode image
filename = barcode.save("code128_clcoding")

print("Barcode saved as:", filename)
