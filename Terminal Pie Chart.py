from math import pi, sin, cos

data = [5, 3, 2]
labels = ["A", "B", "C"]

total = sum(data)

for i, v in enumerate(data):
    percent = v / total * 100
    bar = "█" * int(percent / 5)  # each block = 5%
    print(f"{labels[i]}: {bar} {percent:.1f}%")
