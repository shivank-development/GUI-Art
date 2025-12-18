import time

t = int(input("Focus minutes: ")) * 60
start = time.time()

print("Focus started... Stay focused 🔕")

time.sleep(t)

end = time.time()
print("Done! Focused for", round((end - start) / 60, 1), "minutes.")
