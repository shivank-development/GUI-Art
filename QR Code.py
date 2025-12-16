import qrcode
from PIL import Image

data = "https://x.com/clcoding"

# Create QRCode object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

# Create image
image = qr.make_image(fill_color="black", back_color="white")

# Save image
image.save("qr_code.png")

# Display image
Image.open("qr_code.png")
