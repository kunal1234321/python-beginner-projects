import os

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Folder not found!")
    exit()

total_size = 0

for root, folders, files in os.walk(folder):
    for filename in files:
        file_path = os.path.join(root, filename)

        try:
            total_size += os.path.getsize(file_path)
        except OSError:
            pass

size_mb = total_size / (1024 * 1024)

print(f"Total folder size: {size_mb:.2f} MB")