import random, time, os

text = "Reality is loading ..."
glitches = [')', ',', '-', '*', '#', '@', '~', '!', '/', '\\']

def glitchify(t):
    return ''.join(ch + random.choice(glitches + ['']) for ch in t)

for i in range(30):
    os.system('cls' if os.name == 'nt' else 'clear')  # clears console
    print(glitchify(text))
    time.sleep(0.1)

print("\nReality loaded successfully.")
