import time
from itertools import cycle

# ANSI escape color codes
colors = cycle([
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m"   # Magenta
])

length = 50000000
for i in range(length + 1):
    bar = "".join(next(colors) + "█" for _ in range(i))  # use █ for effect
    print(f"\r{bar:<50}\033[0m", end="")  # reset color with \033[0m
    time.sleep(0.1)

print("\nDone!")
