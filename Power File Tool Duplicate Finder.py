import os
import hashlib

path = input("Folder: ")
seen = {}

for f in os.listdir(path):
    full_path = os.path.join(path, f)

    if os.path.isfile(full_path):
        with open(full_path, "rb") as file:
            data = file.read()

        h = hashlib.md5(data).hexdigest()

        if h in seen:
            print(f"Duplicate: {f}  ==  {seen[h]}")
        else:
            seen[h] = f
