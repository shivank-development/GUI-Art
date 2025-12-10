from wifi_qrcode_generator.generator import wifi_qrcode
from PIL import Image

ssid = "CLCODING_WIFI"
password = "supersecret123"
security = "WPA"  # WPA/WPA2

# Generate WiFi QR
qr = wifi_qrcode(
    ssid=ssid,
    hidden=False,
    authentication_type=security,
    password=password
)

# Save QR image
qr.make_image().save("wifi_qr.png")

# Open the generated QR code image
Image.open("wifi_qr.png")
