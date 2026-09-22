import os

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Folder not found!")
    exit()

prefix = input("Enter prefix: ")

files = os.listdir(folder)

count = 1

for filename in files:
    file_path = os.path.join(folder, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1]

        new_name = f"{prefix}_{count}{extension}"
        new_path = os.path.join(folder, new_name)

        os.rename(file_path, new_path)

        count += 1

print(f"Renamed {count - 1} files successfully!")