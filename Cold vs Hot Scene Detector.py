import cv2

img = cv2.imread("scene.jpg")

# Safety check
if img is None:
    print("Image not found!")
    exit()

blue = img[:, :, 0].mean()
red = img[:, :, 2].mean()

print("Cold Scene" if blue > red else "Hot Scene")
