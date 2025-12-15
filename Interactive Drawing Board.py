import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Drawing Pad")

# Create a canvas
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Function to draw small circles where the mouse moves
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill="black", outline="black")

# Bind left mouse button motion to the draw function
canvas.bind("<B1-Motion>", draw)

# Run the app
root.mainloop()
