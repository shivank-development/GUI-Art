import pyfiglet, pyttsx3, random, time
from rich.console import Console
from rich.text import Text

console = Console()

halloween_fonts = ["slant", "big", "doom", "standard"]
font = random.choice(halloween_fonts)

art = pyfiglet.figlet_format("Happy Halloween!", font=font)
console.print(art, style="bold orange_red1")

pumpkin = """
       🎃🎃🎃
     🎃     🎃
    🎃  👀  🎃
     🎃 👄 🎃
       🎃🎃🎃
"""

console.print(Text(pumpkin, style="bold orange1"))

engine = pyttsx3.init()
engine.say("Happy Happy")
engine.runAndWait()
