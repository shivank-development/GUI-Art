import winsound
import time

# Ask user for delay in seconds
t = int(input("Seconds to wait: "))

# Wait for the specified time
time.sleep(t)

# Play alarm 3 times
for i in range(3):
    winsound.Beep(1000, 300)

print("Alarm Finished!")
