import qrcode

data = input("Enter text/URL for QR code: ")

img = qrcode.make(data)
img.save("qr.png")

print("QR code saved as qr.png")
