#!/usr/bin/python3
import os
import sys
DIRS_TO_TRACK = [
    "polybar",
    "alacritty",
    "picom",
    "i3",
    "Thunar",
    "wallpaper",
    "neofetch",
    "rofi",
    "git_commit.py",
]
def run_commands(message):
    git_add = "git add "
    for dir in DIRS_TO_TRACK:
        git_add += f"{dir} "
    os.system(git_add)
    os.system(f'git commit -m "{message}"')
    os.system("git push -u origin main")

def main():
# Condition check to make sure there's one and only one argument given
    if len(sys.argv) <= 1:
        print("too few arguments")
        return
    elif len(sys.argv) > 2:
        print("too many arguments")
        return

    run_commands(sys.argv[1])

if __name__ == "__main__":
    main()
