import os

root = input("Search in: ")
name = input("File name: ")

# /clcoding

found = False

for path, _, files in os.walk(root):
    if name in files:
        print("Found at:", os.path.join(path, name))
        found = True
        break

if not found:
    print("Not found.")
