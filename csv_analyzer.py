import csv

filename = input("Enter CSV filename: ")

with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print("\nCSV Analysis")
print("------------")
print("Total customers:", len(rows))

if rows:
    ages = [int(row["age"]) for row in rows]
    average_age = sum(ages) / len(ages)

    print("Columns:", ", ".join(rows[0].keys()))
    print("Average age:", round(average_age, 2))

with open("report.txt", "w") as file:
    file.write("CSV ANALYSIS REPORT\n")
    file.write("-------------------\n")
    file.write(f"Total customers: {len(rows)}\n")

    if rows:
        file.write(f"Average age: {round(average_age, 2)}\n")

print("\nReport saved as report.txt")    