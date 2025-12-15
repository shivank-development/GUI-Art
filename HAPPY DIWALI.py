import pyfiglet
from termcolor import colored
import random

def wish_happy_diwali():
    diwali_message = pyfiglet.figlet_format("Happy Diwali!")
    colors = ['red', 'yellow', 'green', 'cyan', 'magenta', 'blue']

    for line in diwali_message.split("\n"):
        print(colored(line, color=random.choice(colors)))

    print("\n✨ Wishing You a Bright and Joyful Diwali! ✨\n")

wish_happy_diwali()
