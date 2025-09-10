import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import os


# -----------------------------
# Calculator App
# -----------------------------
def open_calculator(root):
    calc_win = Toplevel(root)
    calc_win.title("Calculator")
    calc_win.geometry("300x400")
    calc_win.configure(bg="black")

    expression = tk.StringVar()
    input_text = tk.Entry(calc_win, textvariable=expression, font=("Roboto", 18), bg="black", fg="green", bd=0, insertbackground="green")
    input_text.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, sticky="nsew")

    def press(item):
        expression.set(expression.get() + str(item))

    def clear():
        expression.set("")

    def equal():
        try:
            result = str(eval(expression.get()))
            expression.set(result)
        except:
            expression.set("i fucking hate you")

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ]

    for (text, row, col) in buttons:
        action = lambda x=text: press(x) if x not in ["=", "C"] else equal()
        if text == "=":
            action = equal
        b = tk.Button(calc_win, text=text, font=("Roboto", 16), fg="green", bg="black", bd=0, command=action)
        b.grid(row=row, column=col, ipadx=20, ipady=20, sticky="nsew")

    clear_btn = tk.Button(calc_win, text="C", font=("Roboto", 16), fg="green", bg="black", bd=0, command=clear)
    clear_btn.grid(row=5, column=0, columnspan=4, ipadx=20, ipady=20, sticky="nsew")

    for i in range(6):
        calc_win.grid_rowconfigure(i, weight=1)
    for j in range(4):
        calc_win.grid_columnconfigure(j, weight=1)


# -----------------------------
# Phone OS Shell
# -----------------------------
class PhoneOS:
    def __init__(self, root, wallpaper_path):
        self.root = root
        self.root.title("Phone OS")
        self.root.geometry("400x700")
        self.root.resizable(False, False)

        # Load and fit wallpaper
        img = Image.open(wallpaper_path)
        screen_w, screen_h = 400, 700
        img.thumbnail((screen_w, screen_h), Image.LANCZOS)
        self.wallpaper = ImageTk.PhotoImage(img)

        # Canvas with wallpaper
        self.canvas = tk.Canvas(root, width=screen_w, height=screen_h, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(screen_w // 2, screen_h // 2, image=self.wallpaper, anchor="center")

        # Add calculator "app icon"
        self.calc_btn = tk.Button(root, text="Calculator", font=("Roboto", 14), command=lambda: open_calculator(root))
        self.calc_window = self.canvas.create_window(150, 600, anchor="center", window=self.calc_btn)


if __name__ == "__main__":
    wallpaper_path = r"C:\Users\cw5zc\Pictures\resized-1.jpg"

    if not os.path.exists(wallpaper_path):
        print("Wallpaper not found! Please check the path.")
    else:
        root = tk.Tk()
        app = PhoneOS(root, wallpaper_path)
        root.mainloop()
