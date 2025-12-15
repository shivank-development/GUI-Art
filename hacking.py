#!/usr/bin/env python3
"""
fake_hacking_demo.py

Single-file Python demo that simulates a "fake hacking" animation.
Two modes: CLI or GUI (Tkinter). Nothing you type is transmitted or saved.
"""

import sys
import time
import random
import argparse
from threading import Thread

# -------------------------
# Simulation helpers
# -------------------------
STEPS = [
    "Initializing connection...",
    "Enumerating services...",
    "Bypassing trivial protections...",
    "Brute-forcing common passwords...",
    "Trying leaked credential lists...",
    "Checking password entropy...",
    "Cross-referencing username and targets...",
    "Attempting final injection..."
]


def random_username():
    names = ['neo', 'shadow', 'mrlwitwma', 'admin', 'guest', 'player', 'zero', 'node']
    return f"{random.choice(names)}{random.randint(1, 9999)}"


def random_password():
    words = ['sun', 'moon', 'star', 'alpha', 'omega', 'dragon', 'superman', 'hunter', 'password']
    specials = ['!', '#', '$', '@', '%', '&']
    return f"{random.choice(words)}{random.randint(100,999)}{random.choice(specials)}"


# -------------------------
# CLI Mode (terminal)
# -------------------------
def cli_simulation(speed=0.8):
    """
    A simple terminal-based simulation. Press Enter to start.
    The typed text is ignored for the simulated 'cracked' result.
    """
    def animate_dots(base, duration=0.8, steps=4):
        # show small dot animation inline
        for i in range(steps):
            print(base + "." * ((i % 3) + 1), end="\r", flush=True)
            time.sleep(duration / steps)
        print(" " * 80, end="\r")  # clear line

    print("\n*** FAKE HACKING SIMULATION (for demo only) ***")
    print("Note: This is a simulated animation. No data is sent anywhere.")
    input("Press Enter to start the simulation (your input is not used)...")

    for step in STEPS:
        print(step)
        if random.random() > 0.6:
            animate_dots("progress", duration=0.7)
            print(f"progress: {random.randint(1, 99)}%")
        time.sleep(speed)

    # Final result (generated locally)
    print("\nCracking completed!")
    print("Password Matched!")
    print("Username:", random_username())
    print("Password:", random_password())
    print("\nReminder: this is fake — do not use this UI to collect real secrets.\n")


# -------------------------
# GUI Mode (Tkinter)
# -------------------------
def gui_simulation(speed=0.8):
    try:
        import tkinter as tk
        from tkinter import scrolledtext
    except Exception as e:
        print("Tkinter is not available on this system. Falling back to CLI.")
        cli_simulation(speed=speed)
        return

    root = tk.Tk()
    root.title("Fake Hacking — Demo (Local only)")
    root.geometry("720x420")
    root.resizable(False, False)

    # Top scrolled text (read-only simulation log)
    log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", font=("Consolas", 11), bg="black", fg="#00ff66")
    log.pack(fill=tk.BOTH, expand=True, padx=8, pady=(8, 4))

    bottom = tk.Frame(root)
    bottom.pack(fill=tk.X, padx=8, pady=(0, 8))

    label = tk.Label(bottom, text="This is a simulated animation. Nothing is transmitted.", fg="#AAAAAA")
    label.pack(side=tk.LEFT)

    start_btn = tk.Button(bottom, text="Start", width=10)
    start_btn.pack(side=tk.RIGHT)

    def append_log(txt):
        log.configure(state="normal")
        log.insert(tk.END, txt + "\n")
        log.see(tk.END)
        log.configure(state="disabled")

    def worker():
        append_log("*** FAKE HACKING SIMULATION (for demo only) ***")
        append_log("Note: This is a simulated animation. No data is sent anywhere.")
        for step in STEPS:
            append_log(step)
            if random.random() > 0.6:
                append_log("progress: " + str(random.randint(1, 99)) + "%")
            time.sleep(speed)
        append_log("\nCracking completed!")
        append_log("Password Matched!")
        append_log("Username: " + random_username())
        append_log("Password: " + random_password())
        append_log("\nReminder: this is fake — do not use this UI to collect real secrets.")

    def on_start():
        # disable button while running
        start_btn.config(state="disabled")
        t = Thread(target=worker, daemon=True)
        t.start()
        # re-enable button after the thread ends (polling)
        def check_done():
            if t.is_alive():
                root.after(200, check_done)
            else:
                start_btn.config(state="normal")
        check_done()

    start_btn.config(command=on_start)
    # pressing Enter will also start
    root.bind("<Return>", lambda _e: on_start())

    # initial guidance
    append_log("System ready.")
    append_log("Click Start or press Enter to run the fake cracking demo.")
    root.mainloop()


# -------------------------
# Main
# -------------------------
def main():
    parser = argparse.ArgumentParser(description="Fake Hacking Demo (pure Python, local only)")
    parser.add_argument("--mode", choices=("cli", "gui"), default="cli", help="Run in 'cli' (terminal) or 'gui' (Tkinter)")
    parser.add_argument("--speed", type=float, default=0.8, help="Base delay (seconds) between simulation steps; lower = faster")
    args = parser.parse_args()

    if args.mode == "cli":
        cli_simulation(speed=args.speed)
    else:
        gui_simulation(speed=args.speed)


if __name__ == "__main__":
    main()
