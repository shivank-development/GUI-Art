#!/usr/bin/env python3
"""
fake_hacking_demo_cinematic.py

Upgraded fake hacking demo with:
 - CLI + GUI (Tkinter)
 - Rounded Canvas buttons (hover/press effects)
 - Animated Canvas spinner/horizontal bar
 - Optional sound effects (--sound or GUI checkbox)
 - Monospace font fallback (Consolas, Courier New, Menlo, Monaco, TkFixedFont)
 - Timestamps, randomized delays, message types, fake stack traces
 - Typewriter effect in GUI, non-blocking with after()

Safety: purely cosmetic. Nothing you type is transmitted or stored.
"""

import sys
import time
import random
import argparse
import platform
from datetime import datetime

# ---------------------------
# Content & Config
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

THEMES = {
    "green": {"ok":"#00ff66", "muted":"#6b6b6b", "warn":"#ffb86b", "err":"#ff6b6b", "bg":"#001006", "panel":"#041006"},
    "amber": {"ok":"#ffd66b", "muted":"#8b6b4a", "warn":"#ff9f3b", "err":"#ff4b4b", "bg":"#150b03", "panel":"#201108"},
    "red": {"ok":"#ff8b8b", "muted":"#8b6b6b", "warn":"#ffd66b", "err":"#ff4b4b", "bg":"#1a0000", "panel":"#2b0a0a"},
    "mono": {"ok":"#cfcfcf", "muted":"#7a7a7a", "warn":"#9a9a9a", "err":"#b0b0b0", "bg":"#101010", "panel":"#0f0f0f"}
}

# ---------------------------
# Helpers
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
    return max(0.05, random.gauss(base_speed, base_speed * 0.25))

# ---------------------------
# Sound utilities
# ---------------------------
IS_WINDOWS = platform.system() == "Windows"
def play_beep(kind="tick", sound_enabled=True):
    if not sound_enabled:
        return
    try:
        if IS_WINDOWS:
            import winsound
            if kind == "error":
                # lower fast beep sequence
                winsound.Beep(330, 120)
                winsound.Beep(220, 150)
            elif kind == "done":
                winsound.Beep(880, 120)
                winsound.Beep(660, 80)
            else:
                winsound.Beep(750, 60)
        else:
            # GUI bell or terminal bell fallback
            # In CLI we'll print a bell; in GUI we'll call root.bell() where available
            print("\a", end="", flush=True)
    except Exception:
        pass

# ---------------------------
# CLI Mode
# ---------------------------
ANSI_RESET = "\033[0m"
def hex_to_ansi(hexc):
    hexc = hexc.lstrip('#')
    try:
        r = int(hexc[0:2],16); g = int(hexc[2:4],16); b = int(hexc[4:6],16)
        return f"\033[38;2;{r};{g};{b}m"
    except Exception:
        return ""

def cli_print_line(msg_type, text, theme):
    colors = {"INFO": theme["ok"], "WARN": theme["warn"], "ERROR": theme["err"], "DEBUG": theme["muted"]}
    ansi = hex_to_ansi(colors.get(msg_type, theme["muted"]))
    print(f"{ansi}[{timestamp()}] {msg_type:5} {text}{ANSI_RESET}")

def cli_spinner(duration=1.0, sound=False, theme=None):
    # Simple ASCII spinner
    frames = "|/-\\"
    start = time.time()
    idx = 0
    while time.time() - start < duration:
        ch = frames[idx % len(frames)]
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.06)
        sys.stdout.write("\b")
        idx += 1
    if sound:
        play_beep("tick", sound_enabled=True)
    print()

def cli_simulation(theme_name="green", base_speed=0.8, sound=False):
    theme = THEMES.get(theme_name, THEMES["green"])
    print("\n*** FAKE HACKING SIMULATION (CLI) ***")
    print("This is a simulated animation. Nothing you type is transmitted or stored.")
    input("Press Enter to start the simulation (your input is NOT used)...")
    for step in STEPS:
        typ = random.choices(["INFO","DEBUG","WARN","INFO"], weights=[0.6,0.15,0.15,0.1])[0]
        cli_print_line(typ, f"{step}...", theme)
        # spinner or progress occasionally
        if random.random() < 0.5:
            d = choose_delay(base_speed)
            cli_spinner(duration=d, sound=sound, theme=theme)
        else:
            # dots
            for _ in range(random.randint(1,3)):
                print(".", end="", flush=True)
                time.sleep(min(0.35, choose_delay(base_speed)/3))
            print()
        if typ == "ERROR" or random.random() < 0.08:
            print(hex_to_ansi(theme["muted"]) + timestamp() + " DEBUG " + random.choice(STACK_SNIPPETS) + ANSI_RESET)
            if sound:
                play_beep("error", sound_enabled=True)
        time.sleep(choose_delay(base_speed) * 0.3)
    cli_print_line("INFO", "Cracking completed!", theme)
    if sound: play_beep("done", sound_enabled=True)
    cli_print_line("INFO", "Password Matched!", theme)
    cli_print_line("INFO", f"Username: {random_username()}", theme)
    cli_print_line("INFO", f"Password: {random_password()}", theme)
    print("\nReminder: this is fake — do not use this tool to collect real secrets.\n")

# ---------------------------
# GUI Mode (Tkinter)
# ---------------------------
def gui_simulation(theme_name="green", base_speed=0.8, sound=False):
    try:
        import tkinter as tk
        from tkinter import ttk
        from tkinter.scrolledtext import ScrolledText
    except Exception:
        print("Tkinter not available on this system — falling back to CLI.")
        cli_simulation(theme_name, base_speed, sound)
        return

    theme = THEMES.get(theme_name, THEMES["green"])

    root = tk.Tk()
    root.title("Fake Hacking — Cinematic Demo (Local Only)")
    root.configure(bg=theme["bg"])
    root.geometry("920x560")
    root.minsize(640, 360)

    # Font fallback
    preferred = ["Consolas", "Courier New", "Menlo", "Monaco"]
    for f in preferred:
        try:
            test = (f, 12)
            # just attempt to use - if not available tkinter will fallback silently
            break
        except Exception:
            continue
    monospace_font = ("Consolas", 13)  # Tk will fallback if not available

    # Top log (ScrolledText)
    log = ScrolledText(root, wrap=tk.WORD, state="disabled",
                       bg=theme["panel"], fg=theme["ok"], insertbackground=theme["ok"],
                       font=monospace_font, padx=12, pady=12, bd=0, highlightthickness=0)
    log.pack(fill=tk.BOTH, expand=True, padx=12, pady=(12,6))

    # Tag styles
    log.tag_configure("TIME", foreground=theme["muted"], font=(monospace_font[0], 10))
    log.tag_configure("INFO", foreground=theme["ok"], font=(monospace_font[0], 12))
    log.tag_configure("WARN", foreground=theme["warn"], font=(monospace_font[0], 12, "bold"))
    log.tag_configure("ERROR", foreground=theme["err"], font=(monospace_font[0], 12, "bold"))
    log.tag_configure("DEBUG", foreground=theme["muted"], font=(monospace_font[0], 10, "italic"))
    log.tag_configure("DIM", foreground=theme["muted"], font=(monospace_font[0], 10))

    # Bottom frame
    bottom = tk.Frame(root, bg=theme["bg"])
    bottom.pack(fill=tk.X, padx=12, pady=(0,12))

    # Canvas-based rounded button implementation
    class RoundedButton(tk.Canvas):
        def __init__(self, master, text, command=None, width=110, height=36, radius=10, bg=theme["panel"], fg=theme["ok"], hover_bg=None, **kwargs):
            super().__init__(master, width=width, height=height, bg=master["bg"], highlightthickness=0, bd=0)
            self.width, self.height, self.radius = width, height, radius
            self.command = command
            self.text = text
            self.bg = bg
            self.fg = fg
            self.hover_bg = hover_bg or bg
            self.is_hover = False
            self.pressed = False
            self.draw_button()
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
            self.bind("<ButtonPress-1>", self.on_press)
            self.bind("<ButtonRelease-1>", self.on_release)

        def draw_button(self):
            self.delete("all")
            r = self.radius
            w,h = self.width, self.height
            # rounded rectangle via arcs + rectangle
            self.create_arc((0,0, r*2, r*2), start=90, extent=90, fill=self.bg, outline=self.bg)
            self.create_arc((w-2*r,0, w, r*2), start=0, extent=90, fill=self.bg, outline=self.bg)
            self.create_arc((0,h-2*r, r*2, h), start=180, extent=90, fill=self.bg, outline=self.bg)
            self.create_arc((w-2*r,h-2*r, w, h), start=270, extent=90, fill=self.bg, outline=self.bg)
            self.create_rectangle((r,0,w-r,h), fill=self.bg, outline=self.bg)
            self.create_rectangle((0,r,w,h-r), fill=self.bg, outline=self.bg)
            # text
            self.create_text(w//2, h//2, text=self.text, fill=self.fg, font=(monospace_font[0], 11, "bold"))

        def on_enter(self, _e):
            self.is_hover = True
            self.bg = self.hover_bg
            self.draw_button()

        def on_leave(self, _e):
            self.is_hover = False
            self.bg = theme["panel"]
            self.draw_button()

        def on_press(self, _e):
            self.pressed = True
            # simulate press by shifting text slightly
            self.move("all", 0, 1)

        def on_release(self, _e):
            if self.pressed and self.command:
                try:
                    self.command()
                except Exception:
                    pass
            self.pressed = False
            self.draw_button()

    # Spinner Canvas (circular) - rotates an arc
    class Spinner(tk.Canvas):
        def __init__(self, master, size=48, thickness=6, color=theme["ok"], bg=master["bg"], **kwargs):
            super().__init__(master, width=size, height=size, bg=bg, highlightthickness=0, bd=0)
            self.size = size; self.thickness = thickness; self.color = color
            self.angle = 0
            self.arc = None
            self.running = False

        def start(self, speed=8):
            if self.running: return
            self.running = True
            self._spin(speed)

        def _spin(self, speed):
            self.delete("all")
            s = self.size
            pad = self.thickness//2
            extent = 90
            # draw arc with angle rotation
            self.create_arc(pad, pad, s-pad, s-pad, start=self.angle, extent=extent, style="arc", width=self.thickness, outline=self.color)
            self.angle = (self.angle + speed) % 360
            if self.running:
                self.after(40, lambda: self._spin(speed))

        def stop(self):
            self.running = False
            self.delete("all")

    # Horizontal progress bar using Canvas
    class HBar(tk.Canvas):
        def __init__(self, master, width=300, height=14, color=theme["ok"], bg=master["bg"], **kwargs):
            super().__init__(master, width=width, height=height, bg=bg, highlightthickness=0, bd=0)
            self.full = width; self.height = height; self.color = color
            self.fill_rect = None
            self.create_rectangle(0,0,width,height, outline=theme["muted"], width=1, fill=theme["panel"])
        def set_progress(self, frac):
            frac = max(0.0, min(1.0, frac))
            w = int(self.full * frac)
            self.delete("fill")
            self.create_rectangle(0,0,w,self.height, outline="", fill=self.color, tags="fill")

    # Controls layout
    left = tk.Frame(bottom, bg=theme["bg"])
    left.pack(side=tk.LEFT, fill=tk.X, expand=True)
    right = tk.Frame(bottom, bg=theme["bg"])
    right.pack(side=tk.RIGHT)

    # Theme selector & sound toggle & speed slider
    tk.Label(left, text="Theme:", bg=theme["bg"], fg=theme["muted"], font=(monospace_font[0],10)).pack(side=tk.LEFT, padx=(0,6))
    theme_var = tk.StringVar(value=theme_name)
    theme_menu = ttk.OptionMenu(left, theme_var, theme_name, *THEMES.keys())
    theme_menu.pack(side=tk.LEFT)

    sound_var = tk.BooleanVar(value=sound)
    sound_cb = ttk.Checkbutton(left, text="Sound", variable=sound_var)
    sound_cb.pack(side=tk.LEFT, padx=(10,6))

    tk.Label(left, text="Speed:", bg=theme["bg"], fg=theme["muted"], font=(monospace_font[0],10)).pack(side=tk.LEFT, padx=(10,6))
    speed_var = tk.DoubleVar(value=base_speed)
    speed_scale = ttk.Scale(left, from_=0.2, to=2.0, variable=speed_var, orient=tk.HORIZONTAL, length=160)
    speed_scale.pack(side=tk.LEFT, padx=(0,6))

    # Start button (rounded)
    def noop(): pass
    start_btn = RoundedButton(right, "Start", command=lambda: start_sim(), width=120, height=40, radius=12, bg=theme["panel"], fg=theme["ok"], hover_bg=theme["ok"])
    start_btn.pack(side=tk.RIGHT, padx=(6,8))

    # Spinner and HBar place
    spinner = Spinner(right, size=36, thickness=5, color=theme["ok"], bg=theme["bg"])
    spinner.pack(side=tk.RIGHT, padx=(0,6))
    hbar = HBar(right, width=220, height=12, color=theme["ok"], bg=theme["bg"])
    hbar.pack(side=tk.RIGHT, padx=(6,8))

    # Logging helpers
    def append_raw(text, tag=None):
        log.configure(state="normal")
        if tag:
            log.insert(tk.END, text, tag)
        else:
            log.insert(tk.END, text)
        log.see(tk.END)
        log.configure(state="disabled")

    def typewriter_line(text, tag, idx=0, delay=10):
        if idx < len(text):
            log.configure(state="normal")
            log.insert(tk.END, text[idx], tag)
            log.configure(state="disabled")
            log.see(tk.END)
            root.after(delay, lambda: typewriter_line(text, tag, idx+1, delay))
        else:
            append_raw("\n")

    def log_entry(msg_type, text, instant=False):
        ts = f"[{timestamp()}] "
        append_raw(ts, "TIME")
        tag = msg_type if msg_type in ("INFO","WARN","ERROR","DEBUG","DIM") else "INFO"
        if instant:
            append_raw(text + "\n", tag)
        else:
            # speed dependent char delay
            sp = speed_var.get()
            char_delay = max(4, int(18 * sp))
            typewriter_line(text, tag, idx=0, delay=char_delay)

    # Simulation state & flow (non-blocking)
    sim = {"running":False, "idx":0, "after_id":None}

    def simulate_step():
        i = sim["idx"]
        if i >= len(STEPS):
            log_entry("INFO", "\nCracking completed!", instant=False)
            root.after(int(600 * speed_var.get()), lambda: log_entry("INFO", "Password Matched!", instant=False))
            root.after(int(1000 * speed_var.get()), lambda: log_entry("INFO", f"Username: {random_username()}", instant=False))
            root.after(int(1400 * speed_var.get()), lambda: log_entry("INFO", f"Password: {random_password()}", instant=False))
            if sound_var.get(): root.after(1500, lambda: play_beep("done", sound_enabled=True))
            root.after(int(1800 * speed_var.get()), lambda: log_entry("DIM", "\nReminder: this is fake — do not use this UI to collect real secrets.", instant=False))
            sim["running"] = False
            # stop spinner/hbar
            spinner.stop()
            hbar.set_progress(0)
            start_btn.on_release(None)
            return

        step_text = STEPS[i] + "..."
        typ = random.choices(["INFO","DEBUG","WARN","ERROR"], weights=[0.6,0.15,0.15,0.1])[0]
        log_entry(typ, step_text, instant=False)

        sp = speed_var.get()
        # Choose animated progress: spinner or horizontal bar
        if random.random() < 0.5:
            # spinner rotation for a randomized duration
            spinner.start(speed=int(6 + sp*3))
            duration = choose_delay(sp)
            if sound_var.get(): play_beep("tick", sound_enabled=True)
            # schedule stop and maybe stack trace
            def finish_spinner():
                spinner.stop()
                if typ == "ERROR" or random.random() < 0.08:
                    log_entry("DEBUG", random.choice(STACK_SNIPPETS), instant=False)
                    if sound_var.get(): play_beep("error", sound_enabled=True)
                # small wait then next
                root.after(int(200 * sp), step_continue)
            root.after(int(duration * 1000), finish_spinner)
        else:
            # horizontal bar animation
            total_ms = int(max(300, choose_delay(sp)*1000))
            steps = max(8, int(total_ms / 60))
            def bar_tick(c=0):
                frac = c/steps
                hbar.set_progress(frac)
                if c < steps:
                    root.after(int(total_ms/steps), lambda: bar_tick(c+1))
                else:
                    hbar.set_progress(0)
                    if typ == "ERROR" or random.random() < 0.08:
                        log_entry("DEBUG", random.choice(STACK_SNIPPETS), instant=False)
                        if sound_var.get(): play_beep("error", sound_enabled=True)
                    root.after(int(120 * sp), step_continue)
            bar_tick(0)

        # set maybe a random after guard - but progress handlers call step_continue themselves
    def step_continue():
        sim["idx"] += 1
        # small randomized delay before next log entry
        root.after(int(120 * speed_var.get()), simulate_step)

    def start_sim():
        if sim["running"]:
            return
        # reset
        log.configure(state="normal"); log.delete("1.0", tk.END); log.configure(state="disabled")
        sim.update({"running":True, "idx":0})
        # disable press effect
        start_btn.on_press(None)
        # initial lines
        append_raw("*** FAKE HACKING SIMULATION (GUI) ***\n", "DIM")
        append_raw("This is a simulated animation. Nothing you type is transmitted or stored.\n\n", "DIM")
        simulate_step()
        if sound_var.get(): play_beep("tick", sound_enabled=True)

    # Bind Enter key and button
    root.bind("<Return>", lambda e: start_sim())

    # theme change handler
    def apply_theme(*_):
        new = theme_var.get()
        nt = THEMES.get(new, THEMES["green"])
        root.configure(bg=nt["bg"])
        log.configure(bg=nt["panel"])
        log.tag_configure("TIME", foreground=nt["muted"])
        log.tag_configure("INFO", foreground=nt["ok"])
        log.tag_configure("WARN", foreground=nt["warn"])
        log.tag_configure("ERROR", foreground=nt["err"])
        log.tag_configure("DEBUG", foreground=nt["muted"])
        # update shapes color
        start_btn.bg = nt["panel"]
        start_btn.fg = nt["ok"]
        start_btn.draw_button()
        spinner.color = nt["ok"]
        hbar.color = nt["ok"]
    theme_var.trace_add("write", apply_theme)

    # initial guidance
    append_raw("*** FAKE HACKING SIMULATION (GUI) ***\n", "DIM")
    append_raw("Press Start (or press Enter) to run the fake cracking demo.\n\n", "DIM")

    root.mainloop()

# ---------------------------
# Main
# ---------------------------
def main():
    parser = argparse.ArgumentParser(description="Fake Hacking Demo — Cinematic (pure Python)")
    parser.add_argument("--mode", choices=("cli","gui"), default="cli", help="Run in CLI or GUI mode")
    parser.add_argument("--theme", choices=list(THEMES.keys()), default="green", help="Color theme preset")
    parser.add_argument("--speed", type=float, default=0.8, help="Base speed (lower = faster)")
    parser.add_argument("--sound", action="store_true", help="Enable sound (win: winsound; otherwise bell)")
    args = parser.parse_args()

    if args.mode == "cli":
        cli_simulation(theme_name=args.theme, base_speed=args.speed, sound=args.sound)
    else:
        gui_simulation(theme_name=args.theme, base_speed=args.speed, sound=args.sound)

if __name__ == "__main__":
    main()
