import cv2
import numpy as np
import tkinter as tk

img = cv2.imread("face.jpg")

# Safety check
if img is None:
    print("Image not found!")
    exit()

# Red channel average (BGR format)
avg = np.mean(img[:, :, 2])

root = tk.Tk()
root.title("Skin Tone")

msg = "Warm Tone 🌞" if avg > 140 else "Cool Tone ❄️"

tk.Label(
    root,
    text=msg,
    font=("Arial", 18)
).pack(padx=20, pady=20)

root.mainloop()
