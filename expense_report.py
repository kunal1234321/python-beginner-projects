import csv

input_file = "expenses.csv"
output_file = "expense_report.txt"

with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    expenses = list(reader)

total = 0

with open(output_file, "w", encoding="utf-8") as file:
    file.write("EXPENSE REPORT\n")
    file.write("-" * 30 + "\n")

    for expense in expenses:
        name = expense["name"].strip()
        amount = float(expense["amount"])

        file.write(f"{name}: {amount}\n")
        total += amount

    file.write("-" * 30 + "\n")
    file.write(f"Total: {total}\n")

print("Expense report created successfully!")