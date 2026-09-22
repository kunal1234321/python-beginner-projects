expenses = []

while True:
    name = input("Enter expense name (or 'done'): ")

    if name.lower() == "done":
        break

    amount = float(input("Enter amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

total = 0

print("\nExpenses:")

for expense in expenses:
    print(expense["name"], "-", expense["amount"])
    total += expense["amount"]

print("\nTotal:", total)