import tkinter as tk
import random
import threading
import time

# --- Messages ---
messages = [
    "jankso: yoo dis shit awesoe asf",
    "zemil: yooo ngl dis stream fireeee",
    "Thorncurry: LOLLOLOLOOLOLOOOL",
    "ninje: hi",
    "BlitzSpeedRun: btw how is everybody doing this fine afternoon.",
    "ZoomRunLive: this is peak streeem",
    "RunLikeHell69: btwwwwww a[jfasijfd",
    "FastForwardXD: STREEEM SOO GOOOD XDXDXD",
    "QuickMemeTTV: ngl im so down bad for a mountain dew",
    "QuickMemeRun: this is peak cinema",
    "ZoomZoomRun: zommdaiiasidi",
    "ZoomZoomRun: I luv lightning McQueen btw",
    "CoolKid99: bro this is insane",
    "EpicGamer: anyone else seeing this glitch?",
    "Lurker42: first time catching this stream",
    "StreamerFan: love this content!",
    "ChatMaster: lol wtf",
    "Anonymous: wow amazing",
    "MemerGuy: PogChamp",
    "UwU123: hehe cute",
    "PogChamp: epic speedrun",
    "LateNightOwl: can't stop watching",
    "lol this is so funny",
    "bro wtf is happening rn",
    "nahhh no way",
    "yooo this stream is crazy",
    "can someone clip that?",
    "im actually dying rn"
]

# --- Usernames colors ---
usernames_colors = {
    "jankso": "red",
    "zemil": "green",
    "Thorncurry": "orange",
    "ninje": "blue",
    "BlitzSpeedRun": "purple",
    "ZoomRunLive": "cyan",
    "RunLikeHell69": "magenta",
    "FastForwardXD": "yellow",
    "QuickMemeTTV": "pink",
    "QuickMemeRun": "lightblue",
    "ZoomZoomRun": "white",
    "CoolKid99": "blue",
    "EpicGamer": "green",
    "Lurker42": "cyan",
    "StreamerFan": "magenta",
    "ChatMaster": "red",
    "Anonymous": "yellow",
    "MemerGuy": "gray",
    "UwU123": "purple",
    "PogChamp": "teal",
    "LateNightOwl": "orange",
    "SpeedySam": "lightgreen",
    "CrazyCarl": "lightblue",
    "NostalgiaNed": "pink",
    "FastFiona": "purple",
    "EpicElla": "cyan",
    "GamingGreg": "orange",
    "StreamerSally": "magenta",
    "ClipKing": "red",
    "HyperHank": "yellow",
    "QuietQuinn": "white",
    "ChatQueen": "teal",
    "LurkLord": "blue",
    "MemerMax": "gray",
    "ViewerVicky": "green",
    "TwitchTom": "pink"
}

# --- Tkinter Setup ---
root = tk.Tk()
root.title("Livestream Chat Overlay")
root.geometry("500x400")
root.configure(bg='black')
root.wm_attributes("-transparentcolor", "black")
root.attributes("-topmost", True)
root.resizable(False, False)

chat_text = tk.Text(root, bg='black', fg='white', font=("Segoe UI", 12), state='disabled', wrap='word')
chat_text.pack(fill=tk.BOTH, expand=True)

# Add tags for username colors
for user, color in usernames_colors.items():
    chat_text.tag_config(user, foreground=color, font=("Segoe UI", 12, "bold"))

def add_message(msg):
    chat_text.configure(state='normal')
    if ": " in msg:
        username, text = msg.split(": ", 1)
        color_tag = username if username in usernames_colors else None
        if color_tag:
            chat_text.insert(tk.END, username, color_tag)
        else:
            chat_text.insert(tk.END, username)
        chat_text.insert(tk.END, f": {text}\n")
    else:
        chat_text.insert(tk.END, msg + "\n")

    # Keep only last 15 lines
    lines = chat_text.get("1.0", tk.END).splitlines()
    if len(lines) > 15:
        chat_text.delete("1.0", f"{len(lines)-15+1}.0")

    chat_text.see(tk.END)
    chat_text.configure(state='disabled')

def simulate_chat():
    while True:
        msg = random.choice(messages)
        add_message(msg)
        time.sleep(random.uniform(0.5, 2.0))

threading.Thread(target=simulate_chat, daemon=True).start()
root.mainloop()
