import pyfiglet
from termcolor import colored
from colorama import init
import random

init()

colors = ["red", "green", "yellow", "magenta", "cyan"]

art = pyfiglet.figlet_format("Merry Christmas")

colored_art = colored(art, random.choice(colors))
print(colored_art)

print(colored("""
Ho Ho Ho!
🎅🎄✨
""", "green"))
