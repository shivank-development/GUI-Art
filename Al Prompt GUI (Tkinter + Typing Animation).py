import tkinter as tk
import time
import threading
import random

# List of AI responses
responses = [
    "Thinking deeply ...",
    "Analyzing ...",
    "Got it! Here's what I think "
]

# Function to run the AI response simulation
def respond():
    def run():
        # Pick a random response
        ai_text.set(random.choice(responses))
        # Add a simple "thinking" animation
        for _ in range(3):
            time.sleep(0.3)
            ai_text.set(ai_text.get() + ".")
    
    # Run in a separate thread so GUI doesn't freeze
    threading.Thread(target=run).start()

# Tkinter GUI setup
root = tk.Tk()
root.title("AI Prompt Interface")

tk.Label(root, text="Enter your prompt:").pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Ask AI", command=respond).pack()

ai_text = tk.StringVar()
tk.Label(root, textvariable=ai_text, font=("Courier", 12), fg="blue").pack(pady=10)

root.mainloop()
