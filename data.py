import json

with open("person.json", "r") as file:
    person = json.load(file)

print("Name:", person["name"])
print("Skill:", person["skill"])
print("Goal:", person["goal"])