#!/usr/bin/env python3
"""
fake_hacking_demo_upgraded.py

Upgraded fake hacking demo (pure Python). Two modes:
 - CLI (terminal) with ANSI colors
 - GUI (Tkinter) with Consolas font, dark background, colored tags, typewriter effect

Features:
 - Timestamped log entries
 - Randomized delays and message types (INFO/WARN/ERROR/DEBUG)
 - Progress bars and fake stack traces
 - Theme presets: green, amber, red, mono
 - Non-blocking GUI animation using `after()`
 - Nothing you type is transmitted or saved. This is purely cosmetic.

Usage:
    python fake_hacking_demo_upgraded.py            # CLI mode (default)
    python fake_hacking_demo_upgraded.py --mode gui --theme amber --speed 0.9
"""

import sys
import time
import random
import argparse
from datetime import datetime
from threading import Thread

# ---------------------------
# Config / Content
# ---------------------------
STEPS = [
    "Initializing connection",
    "Enumerating services",
    "Bypassing trivial protections",
    "Brute-forcing common passwords",
    "Checking leaked credential lists",
    "Checking password entropy",
    "Cross-referencing username and targets",
    "Attempting final injection"
]

STACK_SNIPPETS = [
    "File \"auth.py\", line 214, in check_credentials\n    raise ValueError('invalid hash length')",
    "File \"netutils.py\", line 87, in send_packet\n    socket.sendto(payload, addr)\nConnectionResetError: [Errno 104] Connection reset by peer",
    "File \"cracker.py\", line 402, in run_wordlist\n    for pw in wordlist: IndexError: list index out of range",
    "File \"db.py\", line 55, in query_user\n    row = cursor.fetchone()\nTypeError: 'NoneType' object is not callable"
]

# Themes for GUI & CLI
THEMES = {
    "green": {"ok": "#00ff66", "muted": "#6b6b6b", "warn": "#ffb86b", "err": "#ff6b6b", "bg": "#000a03"},
    "amber": {"ok": "#ffd66b", "muted": "#8b6b4a", "warn": "#ff9f3b", "err": "#ff4b4b", "bg": "#110b00"},
    "red": {"ok": "#ff8b8b", "muted": "#8b6b6b", "warn": "#ffd66b", "err": "#ff4b4b", "bg": "#1a0000"},
    "mono": {"ok": "#cfcfcf", "muted": "#7a7a7a", "warn": "#9a9a9a", "err": "#b0b0b0", "bg": "#101010"}
}

# ---------------------------
# Utilities
# ---------------------------
def timestamp():
    return datetime.now().strftime("%H:%M:%S")

def random_username():
    names = ['neo','shadow','mrlwitwma','admin','guest','player','zero','node']
    return f"{random.choice(names)}{random.randint(1,9999)}"

def random_password():
    words = ['sun','moon','star','alpha','omega','dragon','superman','hunter','password']
    specials = ['!','#','$','@','%','&']
    return f"{random.choice(words)}{random.randint(100,999)}{random.choice(specials)}"

def choose_delay(base_speed):
    # randomize each step's delay a bit for realism
    return max(0.05, random.gauss(base_speed, base_speed * 0.25))

# ---------------------------
# CLI: ANSI color helpers
# ---------------------------
ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"
ANSI_DIM = "\033[2m"

def ansi_color(code):
    return f"\033[{code}m"

def cli_print_line(msg_type, text, theme):
    # msg_type: INFO, WARN, ERROR, DEBUG
    colors = {
        "INFO": theme["ok"],
        "WARN": theme["warn"],
        "ERROR": theme["err"],
        "DEBUG": theme["muted"]
    }
    # Convert hex color to ANSI 38;2;r;g;b
    def hex_to_ansi(hexc):
        hexc = hexc.lstrip('#')
        r = int(hexc[0:2],16); g = int(hexc[2:4],16); b = int(hexc[4:6],16)
        return f"\033[38;2;{r};{g};{b}m"
    c = colors.get(msg_type, theme["muted"])
    ansi = hex_to_ansi(c)
    print(f"{ansi}[{timestamp()}] {msg_type:5} {text}{ANSI_RESET}")

def cli_progress_bar(total_steps=30, duration=1.2, theme=None):
    # quick terminal progress bar with carriage return
    start = time.time()
    while True:
        elapsed = time.time() - start
        frac = min(1.0, elapsed / duration)
        filled = int(frac * total_steps)
        bar = "[" + "#" * filled + "-" * (total_steps - filled) + "]"
        percent = int(frac * 100)
        # color the bar using theme ok color
        if theme:
            # use simple ANSI color conversion like above
            hexc = theme["ok"].lstrip('#'); r=int(hexc[0:2],16); g=int(hexc[2:4],16); b=int(hexc[4:6],16)
            color = f"\033[38;2;{r};{g};{b}m"
        else:
            color = ""
        print(f"\r{color}{bar} {percent}%{ANSI_RESET}", end="", flush=True)
        if frac >= 1.0:
            break
        time.sleep(0.05)
    print()  # newline

# ---------------------------
# CLI Simulation
# ---------------------------
def cli_simulation(theme_name="green", base_speed=0.8):
    theme = THEMES.get(theme_name, THEMES["green"])
    print("\n*** FAKE HACKING SIMULATION (CLI) ***")
    print("This is a simulated animation. Nothing you type is transmitted or stored.")
    input("Press Enter to start the simulation (your input is NOT used)...")

    for step in STEPS:
        typ = random.choices(["INFO","DEBUG","WARN","INFO"], weights=[0.6,0.15,0.15,0.1])[0]
        cli_print_line(typ, f"{step}...", theme)
        # sometimes show a progress bar or brief dots
        if random.random() < 0.45:
            d = choose_delay(base_speed)
            cli_progress_bar(total_steps=28, duration=d, theme=theme)
        else:
            # small dot animation
            for _ in range(random.randint(1,3)):
                print(".", end="", flush=True)
                time.sleep(min(0.35, choose_delay(base_speed)/3))
            print()
        # occasionally show a fake stack trace or debug
        if typ == "ERROR" or random.random() < 0.08:
            snippet = random.choice(STACK_SNIPPETS)
            cli_print_line("DEBUG", snippet, theme)
        time.sleep(choose_delay(base_speed) * 0.3)

    # Final sequence
    cli_print_line("INFO", "Cracking completed!", theme)
    cli_print_line("INFO", "Password Matched!", theme)
    cli_print_line("INFO", f"Username: {random_username()}", theme)
    cli_print_line("INFO", f"Password: {random_password()}", theme)
    print("\nReminder: this is fake — do not use this tool to collect real secrets.\n")

# ---------------------------
# GUI Simulation (Tkinter)
# ---------------------------
def gui_simulation(theme_name="green", base_speed=0.8):
    try:
        import tkinter as tk
        from tkinter import ttk
        from tkinter.scrolledtext import ScrolledText
    except Exception:
        print("Tkinter not available — falling back to CLI.")
        cli_simulation(theme_name=theme_name, base_speed=base_speed)
        return

    theme = THEMES.get(theme_name, THEMES["green"])

    root = tk.Tk()
    root.title("Fake Hacking — Demo (Local Only)")
    root.configure(bg=theme["bg"])
    root.geometry("900x560")
    root.minsize(640, 360)

    # Styles (ttk)
    style = ttk.Style(root)
    # Basic style tweaks — ttk won't make perfectly rounded buttons without images,
    # but we can change padding and relief to give a nicer appearance.
    style.configure("Start.TButton", padding=8, relief="raised", font=("Consolas", 11))
    style.map("Start.TButton",
              foreground=[('active', theme["ok"]), ('!disabled', theme["ok"])],
              background=[('active', theme["bg"]), ('!disabled', theme["bg"])])

    # Top log (ScrolledText) with terminal appearance
    log = ScrolledText(root, wrap=tk.WORD, state="disabled",
                       bg=theme["bg"], fg=theme["ok"], insertbackground=theme["ok"],
                       font=("Consolas", 14), padx=12, pady=12, bd=0, highlightthickness=0)
    log.pack(fill=tk.BOTH, expand=True, padx=12, pady=(12,6))

    # Configure tags for colors and message types
    log.tag_configure("TIME", foreground=theme["muted"], font=("Consolas", 11))
    log.tag_configure("INFO", foreground=theme["ok"], font=("Consolas", 13))
    log.tag_configure("WARN", foreground=theme["warn"], font=("Consolas", 13, "bold"))
    log.tag_configure("ERROR", foreground=theme["err"], font=("Consolas", 13, "bold"))
    log.tag_configure("DEBUG", foreground=theme["muted"], font=("Consolas", 11, "italic"))
    log.tag_configure("DIM", foreground=theme["muted"], font=("Consolas", 11))

    # Bottom controls
    bottom = tk.Frame(root, bg=theme["bg"])
    bottom.pack(fill=tk.X, padx=12, pady=(0,12))

    info_label = tk.Label(bottom, text="Theme:", bg=theme["bg"], fg=theme["muted"], font=("Consolas", 11))
    info_label.pack(side=tk.LEFT, padx=(4,6))
    theme_var = tk.StringVar(value=theme_name)
    theme_menu = ttk.OptionMenu(bottom, theme_var, theme_name, *THEMES.keys())
    theme_menu.pack(side=tk.LEFT)

    start_btn = ttk.Button(bottom, text="Start", style="Start.TButton")
    start_btn.pack(side=tk.RIGHT, padx=(6,4))

    speed_label = tk.Label(bottom, text="Speed:", bg=theme["bg"], fg=theme["muted"], font=("Consolas", 11))
    speed_label.pack(side=tk.RIGHT, padx=(0,6))
    speed_var = tk.DoubleVar(value=base_speed)
    speed_scale = ttk.Scale(bottom, from_=0.2, to=2.0, variable=speed_var, orient=tk.HORIZONTAL, length=160)
    speed_scale.pack(side=tk.RIGHT, padx=(0,8))

    # Helper functions to write to the log with typewriter-style reveal
    def append_raw(text, tag=None):
        log.configure(state="normal")
        if tag:
            log.insert(tk.END, text, tag)
        else:
            log.insert(tk.END, text)
        log.see(tk.END)
        log.configure(state="disabled")

    # Typewriter reveal for one line (non-blocking)
    def typewriter_line(prefix, line_text, tag, idx=0, delay=12):
        # prefix already inserted, now print line_text char by char
        if idx < len(line_text):
            log.configure(state="normal")
            log.insert(tk.END, line_text[idx], tag)
            log.configure(state="disabled")
            log.see(tk.END)
            root.after(delay, lambda: typewriter_line(prefix, line_text, tag, idx+1, delay))
        else:
            # after line complete, append newline
            append_raw("\n")

    # Compose a timestamped log entry and reveal it
    def log_entry(msg_type, text, instant=False):
        ts = f"[{timestamp()}] "
        tag_ts = "TIME"
        tag_msg = msg_type if msg_type in ("INFO","WARN","ERROR","DEBUG") else "INFO"
        append_raw(ts, tag_ts)
        if instant:
            append_raw(text + "\n", tag_msg)
        else:
            # typewriter for the message text with slight speed dependent delay
            speed = speed_var.get()
            # determine per-character delay in ms (faster -> smaller delay)
            char_delay = max(4, int(18 * speed))
            typewriter_line(ts, text, tag_msg, idx=0, delay=char_delay)

    # Simulation sequence manager (non-blocking)
    sim_state = {"running": False, "step_index": 0, "current_after": None}

    def simulate_step():
        i = sim_state["step_index"]
        if i >= len(STEPS):
            # finalization
            log_entry("INFO", "\nCracking completed!", instant=False)
            # short pause then final lines
            root.after(int(600 * speed_var.get()), lambda: log_entry("INFO", "Password Matched!", instant=False))
            root.after(int(1000 * speed_var.get()), lambda: log_entry("INFO", f"Username: {random_username()}", instant=False))
            root.after(int(1400 * speed_var.get()), lambda: log_entry("INFO", f"Password: {random_password()}", instant=False))
            root.after(int(1800 * speed_var.get()), lambda: log_entry("DIM", "\nReminder: this is fake — do not use this UI to collect real secrets.", instant=False))
            sim_state["running"] = False
            start_btn.state(['!disabled'])
            return

        step_text = STEPS[i] + "..."
        msg_type = random.choices(["INFO","DEBUG","WARN","ERROR"], weights=[0.6,0.15,0.15,0.1])[0]
        log_entry(msg_type, step_text, instant=False)

        # Randomized behavior: progress bar or dots or stack trace
        speed = speed_var.get()
        delay = int(800 * speed + random.randint(-200, 600))  # ms base before next action

        # Show a progress bar widget (inline) sometimes
        if random.random() < 0.45:
            # create small visual progress using text updates
            total = 22
            duration = choose_delay(speed)  # seconds
            steps = max(6, int(duration / 0.06))
            filled = 0

            def progress_tick(count=0):
                nonlocal filled
                frac = (count / steps)
                filled = int(frac * total)
                bar = "[" + "#" * filled + "-" * (total - filled) + f"] {int(frac*100)}%"
                # append as instant line (replace previous progress if any by just adding new line)
                append_raw(bar + "\n", "INFO")
                if count < steps:
                    root.after(int(duration * 1000 / steps), lambda: progress_tick(count + 1))
                else:
                    # after finishing progress, maybe print a debug snippet
                    if msg_type == "ERROR" or random.random() < 0.08:
                        snippet = random.choice(STACK_SNIPPETS)
                        root.after(120, lambda: log_entry("DEBUG", snippet, instant=False))
            root.after(250, lambda: progress_tick(0))
            # schedule next step after duration + small buffer
            next_ms = int((duration + 0.16) * 1000)
            sim_state["current_after"] = root.after(next_ms, lambda: step_continue())
        else:
            # dots animation
            dots = random.randint(1,4)
            def dots_tick(count=0):
                if count < dots:
                    append_raw("." , "INFO")
                    root.after(120, lambda: dots_tick(count+1))
                else:
                    append_raw("\n", "INFO")
            root.after(120, lambda: dots_tick(0))
            # maybe a stack trace after small delay
            if msg_type == "ERROR" or random.random() < 0.08:
                root.after(250 + int(200*speed), lambda: log_entry("DEBUG", random.choice(STACK_SNIPPETS), instant=False))
            sim_state["current_after"] = root.after(delay, lambda: step_continue())

    def step_continue():
        sim_state["step_index"] += 1
        simulate_step()

    def start_sim():
        if sim_state["running"]:
            return
        # reset state
        log.configure(state="normal")
        log.delete("1.0", tk.END)
        log.configure(state="disabled")
        sim_state.update({"running": True, "step_index": 0, "current_after": None})
        start_btn.state(['disabled'])
        simulate_step()

    # Button binding and Enter key
    start_btn.config(command=start_sim)
    root.bind("<Return>", lambda e: start_sim())

    # Initial message
    append_raw("*** FAKE HACKING SIMULATION (GUI) ***\n", "DIM")
    append_raw("This is a simulated animation. Nothing you type is transmitted or stored.\n\n", "DIM")
    append_raw("Press Start or press Enter to begin.\n\n", "DIM")

    # Keep theme responsive to changes (menu)
    def on_theme_change(*_):
        new = theme_var.get()
        new_theme = THEMES.get(new, THEMES["green"])
        # update tag colors
        log.tag_configure("TIME", foreground=new_theme["muted"])
        log.tag_configure("INFO", foreground=new_theme["ok"])
        log.tag_configure("WARN", foreground=new_theme["warn"])
        log.tag_configure("ERROR", foreground=new_theme["err"])
        log.tag_configure("DEBUG", foreground=new_theme["muted"])
        root.configure(bg=new_theme["bg"])
        bottom.configure(bg=new_theme["bg"])
        info_label.configure(bg=new_theme["bg"])
        speed_label.configure(bg=new_theme["bg"])
    theme_var.trace_add("write", on_theme_change)

    root.mainloop()

# ---------------------------
# Main & Argparse
# ---------------------------
def main():
    parser = argparse.ArgumentParser(description="Fake Hacking Demo (upgraded)")
    parser.add_argument("--mode", choices=("cli","gui"), default="cli", help="Run in CLI or GUI mode")
    parser.add_argument("--theme", choices=list(THEMES.keys()), default="green", help="Color theme preset")
    parser.add_argument("--speed", type=float, default=0.8, help="Base speed (lower is faster)")
    args = parser.parse_args()

    if args.mode == "cli":
        cli_simulation(theme_name=args.theme, base_speed=args.speed)
    else:
        gui_simulation(theme_name=args.theme, base_speed=args.speed)

if __name__ == "__main__":
    main()
