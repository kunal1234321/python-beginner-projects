import os

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Folder not found!")
    exit()

print("\nFiles found:")
print("-" * 30)

for root, folders, files in os.walk(folder):
    for filename in files:
        file_path = os.path.join(root, filename)
        size = os.path.getsize(file_path)

        print(filename, "-", size, "bytes")

print("\nScan completed!")