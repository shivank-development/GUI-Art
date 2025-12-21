
#!/usr/bin/env python3
"""
RGB Color Toolkit - Tkinter GUI
Features:
- RGB sliders (0-255) with live preview
- Hex <-> RGB conversion and sync
- Random color generator
- Save colors to a palette (JSON) and export CSS variables
- History of recent conversions
- Copy color code to clipboard
- Light/Dark mode toggle
- Simple tooltips
No external dependencies required (only Python standard library and tkinter).
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import random
import os

APP_TITLE = "RGB Color Toolkit"

class ToolTip:
    """Simple tooltip for widgets."""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwin = None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)

    def show(self, _e=None):
        if self.tipwin or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tipwin = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, background="#ffffe0", relief="solid", borderwidth=1, padx=4, pady=2)
        label.pack()

    def hide(self, _e=None):
        if self.tipwin:
            self.tipwin.destroy()
            self.tipwin = None

class RGBToolkitApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("760x480")
        self.root.minsize(700, 420)
        self.history = []
        self.palette = []
        self.create_style()
        self.create_widgets()
        self.set_color((100, 150, 200))  # initial

    def create_style(self):
        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except:
            pass

        # Variables for theme
        self.dark_mode = tk.BooleanVar(value=False)

    def create_widgets(self):
        # Left frame: controls
        left = ttk.Frame(self.root, padding=12)
        left.pack(side="left", fill="y")

        # Preview area
        preview_frame = ttk.LabelFrame(left, text="Preview", padding=8)
        preview_frame.pack(fill="x", pady=(0,10))
        self.preview_canvas = tk.Canvas(preview_frame, width=220, height=120, bd=0, highlightthickness=0)
        self.preview_canvas.pack()
        self.preview_rect = self.preview_canvas.create_rectangle(0,0,220,120, fill="#000000", outline="")

        # Sliders
        sliders_frame = ttk.LabelFrame(left, text="RGB Sliders", padding=8)
        sliders_frame.pack(fill="x", pady=(0,10))

        self.r_var = tk.IntVar(value=0)
        self.g_var = tk.IntVar(value=0)
        self.b_var = tk.IntVar(value=0)

        for i, (label, var) in enumerate([("R", self.r_var), ("G", self.g_var), ("B", self.b_var)]):
            ttk.Label(sliders_frame, text=label).grid(row=i, column=0, sticky="w")
            s = ttk.Scale(sliders_frame, from_=0, to=255, orient="horizontal", variable=var, command=self.on_slider)
            s.grid(row=i, column=1, sticky="ew", padx=6)
            sliders_frame.columnconfigure(1, weight=1)
            val_label = ttk.Label(sliders_frame, textvariable=var, width=4)
            val_label.grid(row=i, column=2, padx=6)

        # Hex input and convert
        hex_frame = ttk.Frame(left)
        hex_frame.pack(fill="x", pady=(0,10))
        ttk.Label(hex_frame, text="Hex:").grid(row=0, column=0, sticky="w")
        self.hex_entry = ttk.Entry(hex_frame, width=12)
        self.hex_entry.grid(row=0, column=1, padx=6)
        ToolTip(self.hex_entry, "Enter hex like: #RRGGBB or RRGGBB")
        hex_btn = ttk.Button(hex_frame, text="Apply", command=self.on_hex_apply)
        hex_btn.grid(row=0, column=2, padx=6)
        ToolTip(hex_btn, "Apply hex color into sliders/preview")

        # Random and copy buttons
        btn_frame = ttk.Frame(left)
        btn_frame.pack(fill="x", pady=(0,10))

        rand_btn = ttk.Button(btn_frame, text="Random Color", command=self.random_color)
        rand_btn.pack(side="left", padx=(0,6))
        ToolTip(rand_btn, "Generate a random color")

        copy_rgb_btn = ttk.Button(btn_frame, text="Copy RGB", command=self.copy_rgb)
        copy_rgb_btn.pack(side="left", padx=(0,6))
        ToolTip(copy_rgb_btn, "Copy rgb(R,G,B) to clipboard")

        copy_hex_btn = ttk.Button(btn_frame, text="Copy HEX", command=self.copy_hex)
        copy_hex_btn.pack(side="left", padx=(0,6))
        ToolTip(copy_hex_btn, "Copy #RRGGBB to clipboard")

        # Palette controls
        pal_frame = ttk.LabelFrame(left, text="Palette", padding=8)
        pal_frame.pack(fill="x", pady=(0,10))

        save_pal_btn = ttk.Button(pal_frame, text="Save to Palette", command=self.save_palette)
        save_pal_btn.pack(fill="x")
        ToolTip(save_pal_btn, "Save current color into the palette list")

        export_btn = ttk.Button(pal_frame, text="Export Palette (JSON/CSS)", command=self.export_palette)
        export_btn.pack(fill="x", pady=6)
        ToolTip(export_btn, "Export palette as JSON and CSS variables")

        clear_pal_btn = ttk.Button(pal_frame, text="Clear Palette", command=self.clear_palette)
        clear_pal_btn.pack(fill="x")
        ToolTip(clear_pal_btn, "Clear saved palette (local, not files)")

        # Theme toggle
        theme_frame = ttk.Frame(left)
        theme_frame.pack(fill="x", pady=(6,0))
        theme_chk = ttk.Checkbutton(theme_frame, text="Dark Mode", variable=self.dark_mode, command=self.toggle_theme)
        theme_chk.pack(side="left")
        ToolTip(theme_chk, "Toggle Dark / Light theme")

        # Right frame: history and palette display
        right = ttk.Frame(self.root, padding=12)
        right.pack(side="right", fill="both", expand=True)

        # Current color codes display
        codes_frame = ttk.Frame(right)
        codes_frame.pack(fill="x", pady=(0,8))
        self.rgb_label = ttk.Label(codes_frame, text="RGB: rgb(0,0,0)", font=("Segoe UI", 11))
        self.rgb_label.pack(anchor="w")
        self.hex_label = ttk.Label(codes_frame, text="HEX: #000000", font=("Segoe UI", 11))
        self.hex_label.pack(anchor="w")

        # History panel
        history_frame = ttk.LabelFrame(right, text="History", padding=8)
        history_frame.pack(fill="both", expand=True)
        self.history_list = tk.Listbox(history_frame, height=10)
        self.history_list.pack(fill="both", expand=True, side="left")
        self.history_list.bind("<Double-Button-1>", self.load_history_item)
        hist_scroll = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_list.yview)
        hist_scroll.pack(side="right", fill="y")
        self.history_list.config(yscrollcommand=hist_scroll.set)
        ToolTip(self.history_list, "Double-click an item to load it into the preview")

        # Palette visual
        pal_vis_frame = ttk.LabelFrame(right, text="Saved Palette", padding=8)
        pal_vis_frame.pack(fill="x", pady=(8,0))
        self.pal_canvas = tk.Canvas(pal_vis_frame, height=60)
        self.pal_canvas.pack(fill="x")
        ToolTip(self.pal_canvas, "Saved palette swatches")

        # Footer with actions
        footer = ttk.Frame(right, padding=(0,6))
        footer.pack(fill="x", pady=(8,0))
        swap_btn = ttk.Button(footer, text="Swap R/G/B", command=self.swap_channels)
        swap_btn.pack(side="left")
        ToolTip(swap_btn, "Swap the R/G/B values (R->G->B->R)")

        save_hist_btn = ttk.Button(footer, text="Save History", command=self.save_history)
        save_hist_btn.pack(side="right")
        ToolTip(save_hist_btn, "Save history as JSON file")

    # ----------------- Actions -----------------
    def on_slider(self, _e=None):
        r, g, b = self.r_var.get(), self.g_var.get(), self.b_var.get()
        self.set_color((r, g, b), record_history=True)

    def set_color(self, rgb, record_history=False):
        r, g, b = [int(x) for x in rgb]
        hex_code = "#{:02X}{:02X}{:02X}".format(r, g, b)
        self.preview_canvas.itemconfig(self.preview_rect, fill=hex_code)
        self.rgb_label.config(text=f"RGB: rgb({r}, {g}, {b})")
        self.hex_label.config(text=f"HEX: {hex_code}")
        # update sliders without triggering recursion
        self.r_var.set(r); self.g_var.set(g); self.b_var.set(b)
        self.hex_entry.delete(0, tk.END); self.hex_entry.insert(0, hex_code)
        if record_history:
            self.add_history((r,g,b,hex_code))
        self.draw_palette()

    def add_history(self, item):
        r,g,b,hex_code = item
        text = f"rgb({r},{g},{b}) -> {hex_code}"
        self.history.insert(0, {"rgb":[r,g,b], "hex":hex_code})
        # keep 50 items
        self.history = self.history[:50]
        # refresh listbox
        self.history_list.delete(0, tk.END)
        for h in self.history:
            r,g,b = h["rgb"]
            self.history_list.insert(tk.END, f"rgb({r},{g},{b})  {h['hex']}")

    def load_history_item(self, event=None):
        sel = self.history_list.curselection()
        if not sel: return
        idx = sel[0]
        item = self.history[idx]
        r,g,b = item["rgb"]
        self.set_color((r,g,b), record_history=False)

    def on_hex_apply(self):
        h = self.hex_entry.get().strip().lstrip("#")
        if len(h) not in (6,3):
            messagebox.showerror("Invalid Hex", "Please enter a valid 3 or 6-digit hex color.")
            return
        if len(h) == 3:
            h = "".join([c*2 for c in h])
        try:
            r = int(h[0:2], 16)
            g = int(h[2:4], 16)
            b = int(h[4:6], 16)
            self.set_color((r,g,b), record_history=True)
        except ValueError:
            messagebox.showerror("Invalid Hex", "Hex contains invalid characters.")

    def random_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.set_color((r,g,b), record_history=True)

    def copy_rgb(self):
        r,g,b = self.r_var.get(), self.g_var.get(), self.b_var.get()
        txt = f"rgb({r},{g},{b})"
        self.root.clipboard_clear()
        self.root.clipboard_append(txt)
        messagebox.showinfo("Copied", f"Copied {txt} to clipboard")

    def copy_hex(self):
        h = self.hex_entry.get().strip()
        if not h.startswith("#"):
            h = "#" + h
        self.root.clipboard_clear()
        self.root.clipboard_append(h)
        messagebox.showinfo("Copied", f"Copied {h} to clipboard")

    def save_palette(self):
        h = self.hex_entry.get().strip()
        if not h.startswith("#"):
            h = "#" + h
        if not self.is_valid_hex(h):
            messagebox.showerror("Invalid", "Current hex code is invalid.")
            return
        if len(self.palette) >= 24:
            messagebox.showwarning("Palette Full", "Max 24 colors in palette. Export or clear to add more.")
            return
        self.palette.append(h.upper())
        self.draw_palette()

    def draw_palette(self):
        c = self.pal_canvas
        c.delete("all")
        if not self.palette:
            c.create_text(10,30, anchor="w", text="No colors saved.", font=("Segoe UI", 10))
            return
        w = c.winfo_width() or c.winfo_reqwidth()
        # compute swatch sizes
        cols = min(8, len(self.palette))
        sw = max(20, w // cols)
        for i, hexc in enumerate(self.palette):
            x0 = i * sw
            c.create_rectangle(x0, 0, x0+sw, 60, fill=hexc, outline="black")
            c.create_text(x0+4, 44, anchor="nw", text=hexc, font=("Arial", 8), fill=self.best_contrast_text(hexc))

    def export_palette(self):
        if not self.palette:
            messagebox.showinfo("Empty", "Palette empty. Save some colors first.")
            return
        # choose folder
        folder = filedialog.askdirectory(title="Choose folder to export palette files")
        if not folder:
            return
        # export JSON
        json_path = os.path.join(folder, "palette.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({"palette": self.palette}, f, indent=2)
        # export CSS variables
        css_lines = []
        for i, hexc in enumerate(self.palette, start=1):
            css_lines.append(f"--color-{i}: {hexc};")
        css_path = os.path.join(folder, "palette.css")
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(":root {\n")
            for line in css_lines:
                f.write("  " + line + "\n")
            f.write("}\n")
        messagebox.showinfo("Exported", f"Exported to:\n{json_path}\n{css_path}")

    def clear_palette(self):
        if messagebox.askyesno("Clear Palette", "Clear saved palette?"):
            self.palette = []
            self.draw_palette()

    def swap_channels(self):
        # R->G, G->B, B->R
        r,g,b = self.r_var.get(), self.g_var.get(), self.b_var.get()
        self.set_color((g,b,r), record_history=True)

    def save_history(self):
        if not self.history:
            messagebox.showinfo("No history", "No history to save.")
            return
        path = filedialog.asksaveasfilename(title="Save history as JSON", defaultextension=".json", filetypes=[("JSON","*.json")])
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"history": self.history}, f, indent=2)
        messagebox.showinfo("Saved", f"History saved to\n{path}")

    def is_valid_hex(self, h):
        if not h.startswith("#"):
            return False
        hexpart = h.lstrip("#")
        if len(hexpart) not in (3,6): return False
        try:
            int(hexpart, 16); return True
        except:
            return False

    def best_contrast_text(self, hexc):
        """Return black/white depending on perceived brightness for contrast."""
        hexpart = hexc.lstrip("#")
        r = int(hexpart[0:2], 16); g = int(hexpart[2:4], 16); b = int(hexpart[4:6], 16)
        # Perceived brightness
        brightness = (r*299 + g*587 + b*114) / 1000
        return "black" if brightness > 128 else "white"

    def toggle_theme(self):
        if self.dark_mode.get():
            self.style.configure(".", background="#2b2b2b", foreground="#eaeaea")
            self.root.configure(bg="#2b2b2b")
        else:
            self.style.configure(".", background=None, foreground=None)
            self.root.configure(bg=None)

# ----------------- Script entry -----------------
def main():
    root = tk.Tk()
    app = RGBToolkitApp(root)
    # center window
    root.update_idletasks()
    w = root.winfo_width(); h = root.winfo_height()
    ws = root.winfo_screenwidth(); hs = root.winfo_screenheight()
    x = (ws // 2) - (w // 2); y = (hs // 2) - (h // 2)
    root.geometry(f"+{x}+{y}")
    root.mainloop()

if __name__ == "__main__":
    main()
