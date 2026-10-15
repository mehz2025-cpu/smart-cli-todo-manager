# Smart CLI ToDo Manager
import json

class TaskManager():
    def __init__(self):
        self.tasks = self.load_tasks()
        self.actions = {
                "1": self.add_task,
                "2": self.show_tasks,
                "3": self.complete_task,
                "4": self.delete_task
            }

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        print("Adding Tasks")
        title = input("Task title: ").strip()
        if not title:
            print("Title cannot be empty.")
            return
        else:
            self.tasks.append({"title":title, "done":False})
            self.save_tasks()

    def show_tasks(self):
        print("Showing Tasks")
        if not self.tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(self.tasks):
                status = "✔" if task["done"] else "❌"
                print(f"{i+1}. {task['title']} {status}")

    def complete_task(self):
        x = input("Task number: ")
        try:
            number = int(x)
            if not self.tasks:
                print("No tasks yet!")
            elif number < 1 or number > len(self.tasks):
                print("Invalid task number!")
            else:
                self.tasks[number-1]["done"] = True
                self.save_tasks()
        except ValueError:
            print("Please enter a number!")

    def delete_task(self):
        y = input("Task number: ")
        try:
            num = int(y)
            if not self.tasks:
                print("No tasks yet!")
            elif num < 1 or num > len(self.tasks):
                print("Invalid task number!")
            else:
                self.tasks.pop(num-1)
                self.save_tasks()
        except ValueError:
            print("Please enter a number!")

    def run(self):
        while True:
            print("1.Add Task")
            print("2.Show Task")
            print("3.Complete Task")
            print("4.Delete Task")
            print("5.Exit")
            choice = input("Choice: ")
            action = self.actions.get(choice)
            if action:
                action()
            elif choice == "5":
                break
            else:
                print("Invalid choice!")


manager = TaskManager()
manager.run()



