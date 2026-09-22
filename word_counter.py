file_name = input("Enter text file name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()

    print("Characters:", len(text))
    print("Words:", len(words))
    print("Lines:", len(text.splitlines()))

except FileNotFoundError:
    print("File not found!")