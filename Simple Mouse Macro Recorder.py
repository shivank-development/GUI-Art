import pyautogui
import time

events = []

for _ in range(30):
    events.append(pyautogui.position())
    time.sleep(0.1)

print("Recorded", len(events), "mouse positions.")
