import cv2
import tkinter as tk
import numpy as np

img = cv2.imread("gift.jpg")

# Safety check
if img is None:
    print("Image not found!")
    exit()

# Mean color values (BGR)
b, g, r = img.mean(axis=(0, 1))

result = "🎁 Red Gift ❤️" if r > g else "🎁 Green Gift 💚"

root = tk.Tk()
root.title("Gift Color Detector")

tk.Label(
    root,
    text=result,
    font=("Arial", 20)
).pack(padx=20, pady=20)

root.mainloop()
