import barcode
from barcode.writer import ImageWriter

data = "123456789012"

code128 = barcode.get("code128", data, writer=ImageWriter())
filename = code128.save("my_barcode")

print("Barcode generated:", filename)
