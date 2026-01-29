from tkinter import *
from PIL import Image, ImageTk, ImageFilter

# Load image
img = Image.open("bird.jpg")

def update(val):
    blur = int(val)
    out = img.filter(ImageFilter.GaussianBlur(blur))
    tkimg = ImageTk.PhotoImage(out)
    panel.config(image=tkimg)
    panel.image = tkimg

# Create window
root = Tk()
root.title("Image Blur Slider")

# Image panel
tkimg = ImageTk.PhotoImage(img)
panel = Label(root, image=tkimg)
panel.image = tkimg
panel.pack()

# Blur control slider
Scale(
    root,
    from_=0,
    to=10,
    orient=HORIZONTAL,
    label="Blur Level",
    command=update
).pack()

root.mainloop()
