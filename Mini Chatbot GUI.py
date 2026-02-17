import tkinter as tk

def respond():
    txt = entry.get()
    chat.insert(tk.END, "You: " + txt + "\nBot: I heard you\n\n")
    entry.delete(0, tk.END)

# Create window
root = tk.Tk()
root.title("Mini Chatbot")

# Chat display
chat = tk.Text(root, width=40, height=15)
chat.pack(padx=10, pady=5)

# User input
entry = tk.Entry(root, width=40)
entry.pack(padx=10)

# Send button
tk.Button(root, text="Send", command=respond).pack(pady=5)

root.mainloop()
