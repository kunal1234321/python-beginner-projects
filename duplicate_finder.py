import os
from collections import defaultdict

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Folder not found!")
    exit()

files = defaultdict(list)

for root, folders, filenames in os.walk(folder):
    for filename in filenames:
        files[filename].append(os.path.join(root, filename))

found = False

for filename, paths in files.items():
    if len(paths) > 1:
        found = True
        print(f"\nDuplicate: {filename}")

        for path in paths:
            print(" -", path)

if not found:
    print("No duplicate filenames found.")