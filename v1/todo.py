# Smart CLI ToDo Manager
import json

tasks = []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


tasks = load_tasks()

while True:
    print("1.Add Task")
    print("2.Show Task")
    print("3.Complete Task")
    print("4.Delete Task")
    print("5.Exit")

    choice = input("Choice: ")
    
    if choice == "1":
        print("Adding Tasks")
        title = input("task title: ")
        tasks.append({"title":title, "done":False})
        save_tasks(tasks)

    elif choice == "2":
        print("Showing Tasks")
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks):
                status = "✔" if task["done"] else "❌"
                print(f"{i+1}. {task['title']} {status}")

    elif choice == "3":
        x = input("Task number: ")
        try:
            number = int(x)
            if not tasks:
                print("No tasks yet!")
            elif number < 1 or number > len(tasks):
                print("Invalid task number!")
            else:
                tasks[number-1]["done"] = True
                save_tasks(tasks)
        except ValueError:
            print("Please enter a number!")

    elif choice == "4":
        y = input("Task number: ")
        try:
            num = int(y)
            if not tasks:
                print("No tasks yet!")
            elif num < 1 or num > len(tasks):
                print("Invalid task number!")
            else:
                tasks.pop(num-1)
                save_tasks(tasks)
        except ValueError:
            print("Please enter a number!")

    elif choice == "5":
        print("bye")
        break
    else:
        print("Invalid answer! Try again.")

