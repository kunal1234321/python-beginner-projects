import csv

input_file = "contacts.csv"
output_file = "cleaned_contacts.csv"

with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    contacts = list(reader)

cleaned = []

for contact in contacts:
    name = contact["name"].strip()
    email = contact["email"].strip().lower()

    if name and email and "@" in email:
        cleaned.append({
            "name": name,
            "email": email
        })

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "email"])
    writer.writeheader()
    writer.writerows(cleaned)

print(f"Cleaned {len(cleaned)} contacts successfully!")