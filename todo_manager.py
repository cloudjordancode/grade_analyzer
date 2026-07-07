tasks = ["Buy groceries", "Finish homework", "Call the dentist"]
print("=" * 35)
print("    My To-Do List")
print("=" * 35)

for i in range(len(tasks)): 
    print(f"{i + 1}. {tasks[i]}")
print()
print(f"Total tasks: {len(tasks)}")

print()

print("What would user like to do?")
print("1. Add a task")
print("2. Remove a task")
print()

choice =input("Choice: ")

if choice == "1": 
    new_task = input("Enter new task: ")
    tasks.append(new_task)

    print()
    print("Updated list")

    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")

    print()
    print(f"Total Tasks: {len(tasks)}")
    print()


elif choice == "2":
    try: 
        remove_task = int(input("Enter task number to remove: "))
        tasks.pop(remove_task -1)

        print()
        print("Updated list:")

        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

            print()
            print(f"Total tasks: {len(tasks)}")
            print()


    except(ValueError, IndexError):         
        print("Invalid task number")
    else:
        print("Invalid choice.")


