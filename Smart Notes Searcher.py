note = input("File name: ")
word = input("Search word: ")

with open(note, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if word.lower() in line.lower():
        print(f"[Line {i+1}] {line.strip()}")
