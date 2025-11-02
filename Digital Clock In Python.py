import time
from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("\033[1;36m" + f"Digital Clock: {current_time}")
    time.sleep(1)
    #print("\033[H\033[J", end="")  # Clear the console before updating the time