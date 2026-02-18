import tkinter as tk

root = tk.Tk()
root.title("Christmas Greeting")

# Name label
tk.Label(root, text="Your Name?").pack(pady=5)

# Entry box
entry = tk.Entry(root)
entry.pack(pady=5)

# Output label
lab = tk.Label(root, font=("Arial", 16))
lab.pack(pady=10)

# Button function
def ok():
    lab.config(text=f"Merry Christmas {entry.get()} 🎄")

# Button
tk.Button(root, text="Wish 🎅", command=ok).pack(pady=5)

root.mainloop()
