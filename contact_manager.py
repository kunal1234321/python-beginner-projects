import json
import os

file_name = "contacts.json"

if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        contacts = json.load(file)
else:
    contacts = []

name = input("Enter name: ")
email = input("Enter email: ")
phone = input("Enter phone: ")

contacts.append({
    "name": name,
    "email": email,
    "phone": phone
})

with open(file_name, "w", encoding="utf-8") as file:
    json.dump(contacts, file, indent=4)

print("Contact saved successfully!")