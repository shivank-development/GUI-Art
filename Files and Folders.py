import os

# Specify the path to count files and directories
PATH = r'C:\Users\CLCODING\Downloads'

files = 0
dirs = 0

for root, dirnames, filenames in os.walk(PATH):
    dirs += len(dirnames)
    files += len(filenames)

print('Files:', files)
print('Directories:', dirs)
print('Total:', files + dirs)
print('Path:', PATH)