import os
import shutil

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Folder not found!")
    exit()

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1]

        if extension:
            extension = extension[1:].lower()
        else:
            extension = "other"

        target_folder = os.path.join(folder, extension)

        os.makedirs(target_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(target_folder, filename))

print("Files organized successfully!")