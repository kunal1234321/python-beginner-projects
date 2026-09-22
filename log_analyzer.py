file_name = input("Enter log file name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    errors = 0
    warnings = 0

    for line in lines:
        if "ERROR" in line.upper():
            errors += 1

        if "WARNING" in line.upper():
            warnings += 1

    print("Total lines:", len(lines))
    print("Errors:", errors)
    print("Warnings:", warnings)

except FileNotFoundError:
    print("Log file not found!")