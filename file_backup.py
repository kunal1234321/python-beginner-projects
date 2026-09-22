import os
import shutil

source = input("Enter file path: ")
backup_folder = "backups"

if not os.path.isfile(source):
    print("File not found!")
    exit()

os.makedirs(backup_folder, exist_ok=True)

file_name = os.path.basename(source)
destination = os.path.join(backup_folder, file_name)

shutil.copy2(source, destination)

print("Backup created successfully!")