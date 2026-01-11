import cv2
import numpy as np

img = cv2.imread("christmas.jpg")

# Safety check
if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
brightness = np.mean(gray)

if brightness > 170:
    print("🎄 Festive & Bright Christmas!")
elif brightness > 100:
    print("❄️ Cozy Winter Evening")
else:
    print("🌙 Silent Christmas Night")
