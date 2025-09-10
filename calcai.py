import tkinter as tk
from tkinter import font

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customizable Calculator")
        self.geometry("360x520")
        self.config(bg="black")

        # Fonts
        self.custom_font = font.Font(family="Roboto", size=16)

        # State
        self.expression = ""
        self.menu_open = False

        # Menu frame (hidden by default)
        self.menu_frame = tk.Frame(self, bg="gray20", width=200, height=520)
        self.menu_frame.place(x=-200, y=0)

        # === TOP BAR ===
        self.topbar = tk.Frame(self, bg="black", height=40)
        self.topbar.pack(fill="x", side="top")

        # Hamburger button
        self.hamburger_btn = tk.Button(
            self.topbar, text="≡", font=("Roboto", 16),
            bg="black", fg="white", command=self.toggle_menu, relief="flat"
        )
        self.hamburger_btn.pack(side="left", padx=5, pady=5)

        # === CALCULATOR AREA ===
        self.calc_frame = tk.Frame(self, bg="black")
        self.calc_frame.pack(expand=True, fill="both")

        # Entry and result preview
        self.entry = tk.Entry(self.calc_frame, font=("Roboto", 20),
                              borderwidth=5, relief="flat", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4,
                        pady=(10, 5), padx=10, sticky="nsew")

        self.preview = tk.Label(self.calc_frame, text="", font=("Roboto", 14),
                                fg="gray", bg="black", anchor="e")
        self.preview.grid(row=1, column=0, columnspan=4,
                          padx=10, sticky="nsew")

        # Buttons
        self.create_buttons()

        # Menu content
        self.create_menu()

        # Themes
        self.apply_theme("neon")

    def create_buttons(self):
        btns = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
            ("C", 6, 0)
        ]

        self.buttons = {}
        for (text, r, c) in btns:
            btn = tk.Button(self.calc_frame, text=text, font=self.custom_font,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
            self.buttons[text] = btn

        # Expandable grid
        for i in range(7):
            self.calc_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.calc_frame.columnconfigure(j, weight=1)

        # Place clear button full row
        self.buttons["C"].grid(row=6, column=0, columnspan=4, sticky="nsew")

    def create_menu(self):
        tk.Label(self.menu_frame, text="Themes", font=("Roboto", 14),
                 bg="gray20", fg="white").pack(pady=10)

        tk.Button(self.menu_frame, text="Dark Theme", font=self.custom_font,
                  command=lambda: self.apply_theme("dark")).pack(fill="x", padx=10, pady=5)
        tk.Button(self.menu_frame, text="Light Theme", font=self.custom_font,
                  command=lambda: self.apply_theme("light")).pack(fill="x", padx=10, pady=5)
        tk.Button(self.menu_frame, text="Neon Theme", font=self.custom_font,
                  command=lambda: self.apply_theme("neon")).pack(fill="x", padx=10, pady=5)

        tk.Label(self.menu_frame, text="Other", font=("Roboto", 14),
                 bg="gray20", fg="white").pack(pady=10)
        tk.Button(self.menu_frame, text="Exit Calculator", font=self.custom_font,
                  command=self.destroy).pack(fill="x", padx=10, pady=5)

    def toggle_menu(self):
        if self.menu_open:
            self.menu_frame.place(x=-200, y=0)
        else:
            self.menu_frame.place(x=0, y=0)
        self.menu_open = not self.menu_open

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.preview.config(text="")
                self.expression = str(result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.preview.config(text="")
                self.expression = ""
        elif char == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)
            self.preview.config(text="")
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
            try:
                self.preview.config(text=str(eval(self.expression)))
            except:
                self.preview.config(text="")

    def apply_theme(self, theme):
        if theme == "dark":
            bg, fg, btn_bg, btn_fg, spcl_bg, spcl_fg = "black", "white", "gray25", "white", "orange", "black"
        elif theme == "light":
            bg, fg, btn_bg, btn_fg, spcl_bg, spcl_fg = "white", "black", "lightgray", "black", "orange", "white"
        elif theme == "neon":
            bg, fg, btn_bg, btn_fg, spcl_bg, spcl_fg = "black", "green", "black", "green", "black", "green"
        else:
            return

        # Window + frames
        self.config(bg=bg)
        self.topbar.config(bg=bg)
        self.calc_frame.config(bg=bg)
        self.preview.config(bg=bg, fg="gray" if theme != "neon" else "green")

        # Entry
        self.entry.config(bg=bg, fg=fg, insertbackground=fg)

        # Hamburger button
        self.hamburger_btn.config(bg=bg, fg=fg)

        # Buttons
        for text, btn in self.buttons.items():
            if text in ["=", "C", "+", "-", "*", "/"]:
                btn.config(bg=spcl_bg, fg=spcl_fg, activebackground=btn_bg, activeforeground=btn_fg)
            else:
                btn.config(bg=btn_bg, fg=btn_fg, activebackground=spcl_bg, activeforeground=spcl_fg)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
