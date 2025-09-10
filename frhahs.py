import time
import random
import os

# --- All messages combined ---
messages = [
    # First batch (your original)
    "jankso: yoo dis shit awesoe asf",
    "zemil: yooo ngl dis stream fireeee",
    "zemil: LOLLOLOLOOLOLOOOL",
    "Thorncurry: LOLLOLOLOOLOLOOOL",
    "ninje: hi",
    "Thorncurry: hehe",
    "Thorncurry: wtf did I miss btw",
    "bandaso: I don understan",
    "bibida: streem go",
    "bibida: ok lol",
    "ninje: hehe",
    "Thorncurry: hi",

    # Second batch (speedrun)
    "BlitzSpeedRun: btw how is everybody doing this fine afternoon.",
    "ZoomRunLive: this is peak streeem",
    "RunLikeHell69: btwwwwww a[jfasijfd",
    "FastForwardXD: STREEEM SOO GOOOD XDXDXD",
    "QuickMemeTTV: ngl im so down bad for a mountain dew",
    "QuickMemeRun: this is peak cinema",
    "ZoomZoomRun: zommdaiiasidi",
    "ZoomZoomRun: I luv lightning McQueen btw",

    # Third batch (hype/meme Twitch-style)
    "lol this is so funny 😂",
    "bro wtf is happening rn",
    "nahhh no wayyy",
    "yooo this stream is crazy",
    "can someone clip that??",
    "im actually dying rn 💀",
    "bro turned into a speedrunner",
    "this is peak content",
    "chat going wild rn",
    "wtf did i just witness",
    "first time catching stream live 👋",
    "yoooo i was here!!",
    "no shot that just happened",
    "hey streamer, love the content ❤️",
    "this feels like 2016 youtube again",
    "the nostalgia is real rn",
    "is anyone else watching at 3am?",
    "bro thinks he’s HIM 💀",
    "nah that timing was perfect",
    "streamer lowkey cracked",
    "you just made my day 😭",
    "i cant breathe bro 💀💀💀",
    "this deserves an oscar fr",
    "chat is moving too fast lmao",
    "nah someone needs to clip this ASAP",
    "best stream i’ve seen all week",
    "my sides hurt from laughing",
    "yo can we get a W in chat?",
    "streamer is GOATed 🐐",
    "you can’t make this up 😂",
    "watch this blow up tomorrow",
    "bro forgot he was live 💀",
    "nahhh he cooked",
    "i been here since the start 🙌",
    "this chat is chaotic lmao",
    "streamer boutta break the internet",
    "literally crying rn 😭😭😭",
    "why is this so addicting",
    "this stream >>> netflix",
    "bro just speedran reality",
    "how is this even real",
    "nahhh im saving this VOD"
]

# --- Merged usernames with colors ---
usernames_colors = {
    # Your original usernames
    "jankso": "\033[91m",        # Red
    "zemil": "\033[92m",         # Green
    "Thorncurry": "\033[93m",    # Yellow
    "ninje": "\033[94m",         # Blue
    "bandaso": "\033[95m",       # Magenta
    "bibida": "\033[96m",        # Cyan

    # Speedrun usernames
    "BlitzSpeedRun": "\033[91m", 
    "ZoomRunLive": "\033[92m",
    "RunLikeHell69": "\033[93m",
    "FastForwardXD": "\033[94m",
    "QuickMemeTTV": "\033[95m",
    "QuickMemeRun": "\033[96m",
    "ZoomZoomRun": "\033[97m",

    # Extra usernames I created earlier
    "CoolKid99": "\033[94m",
    "EpicGamer": "\033[92m",
    "Lurker42": "\033[96m",
    "StreamerFan": "\033[95m",
    "ChatMaster": "\033[91m",
    "Anonymous": "\033[93m",
    "MemerGuy": "\033[90m",
    "UwU123": "\033[35m",
    "PogChamp": "\033[36m",
    "LateNightOwl": "\033[33m"
}

reset_color = "\033[0m"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def chat_simulator():
    chat_history = []
    while True:
        msg = random.choice(messages)

        # Extract username from message if present
        if ": " in msg:
            username, _ = msg.split(": ", 1)
            color = usernames_colors.get(username, "\033[97m")  # default white
        else:
            color = "\033[97m"

        line = f"{color}{msg}{reset_color}"
        chat_history.append(line)

        # Keep last 15 lines visible
        if len(chat_history) > 15:
            chat_history.pop(0)

        clear_terminal()
        for l in chat_history:
            print(l)

        # Random delay to simulate chat
        time.sleep(random.uniform(0.5, 2.5))

if __name__ == "__main__":
    chat_simulator()
