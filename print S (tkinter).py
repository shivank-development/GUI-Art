import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Star Letter S")

# The ASCII-art S using stars
s_art = """ 
 *****
*     
*     
 *****
      *
*     *
 *****
"""

# Create a Label widget with the star S
label = tk.Label(root, text=s_art, font=("Courier", 20), justify="left")
label.pack(padx=20, pady=20)

# Run the GUI
root.mainloop()


