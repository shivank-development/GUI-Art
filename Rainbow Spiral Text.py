import time

text = " Suscribe with Fun"
colors = [31, 32, 33, 34, 35, 36, 37]  # ANSI color codes

for i in range(10):
    line = ""
    for idx, char in enumerate(text):
        color_code = colors[(idx + i) % len(colors)]
        line += f"\033[1;{color_code}m{char}\033[0m"
    print(line)
    time.sleep(0.3)
