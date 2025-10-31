from tkinter import *

def calculate(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error: {e}"

root = Tk()
root.title("Calculator")
root.geometry("400x420")
root.resizable(False, False)
root.config(bg="#202124")  

entry = Entry(root, font=("Arial", 18), border=5, relief=SUNKEN, justify=RIGHT, bg="#ffffff", fg="#000000")
entry.pack(fill=X, padx=10, pady=10)

def button_click(symbol):
    entry.insert(END, symbol)

def clear_entry():
    entry.delete(0, END)

def backspace():
    current_text = entry.get()
    entry.delete(0, END)
    entry.insert(END, current_text[:-1])

def evaluate_expression():
    expression = entry.get()
    result = calculate(expression)
    entry.delete(0, END)
    entry.insert(END, result)

frame = Frame(root, bg="#202124")
frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

for i, symbol in enumerate(buttons):
    btn = Button(frame, text=symbol, width=6, height=2, font=("Arial", 14),
                 bg="#3c4043", fg="white",
                 command=(evaluate_expression if symbol == '=' else lambda s=symbol: button_click(s)))
    btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)

bottom_frame = Frame(root, bg="#202124")
bottom_frame.pack(pady=5, fill=X)

Button(bottom_frame, text="Clear", width=10, height=2, font=("Arial", 14),
       bg="#ea4335", fg="white", command=clear_entry).pack(side=LEFT, padx=10)

Button(bottom_frame, text="⌫", width=10, height=2, font=("Arial", 14),
       bg="#5f6368", fg="white", command=backspace).pack(side=RIGHT, padx=10)

root.bind("<Return>", lambda e: evaluate_expression())
root.bind("<BackSpace>", lambda e: backspace())
root.bind("<Escape>", lambda e: clear_entry())

root.mainloop()
