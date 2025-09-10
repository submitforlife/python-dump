import time
import random

# Chat file OBS will read
CHAT_FILE = "chat.txt"

# --- Usernames with simulated "colors" ---
users = [
    "[RED] bibida",
    "[GREEN] ninje",
    "[BLUE] zemil",
    "[YELLOW] Thorncurry",
    "[PURPLE] bandaso",
    "[CYAN] jankso"
]

# --- Sample messages ---
messages = [
    "hi",
    "yoo dis shit awesoe asf",
    "yooo ngl dis stream fireeee",
    "omgggg",
    "LOLLOLOLOOLOLOOOL",
    "hehe",
    "ok lol",
    "streem go",
    "wtf did I miss btw",
    "I don understan"
]

# Max lines to display (scroll effect)
MAX_LINES = 12

# Start fresh
with open(CHAT_FILE, "w", encoding="utf-8") as f:
    f.write("")

# Simulate chat loop
while True:
    user = random.choice(users)
    msg = random.choice(messages)

    # Append new message
    with open(CHAT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{user}: {msg}\n")

    # Keep only last N lines (scrolling effect)
    with open(CHAT_FILE, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        if len(lines) > MAX_LINES:
            lines = lines[-MAX_LINES:]
        f.seek(0)
        f.writelines(lines)
        f.truncate()

    # Random delay (0.3–2.5 sec)
    time.sleep(random.uniform(0.3, 2.5))
