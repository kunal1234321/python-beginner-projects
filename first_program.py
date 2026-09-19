tasks = []

while True:
    task = input("Enter a task (or type 'done'): ")

    if task == "done":
        break

    tasks.append(task)

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

print("\nTasks saved successfully!")

