import json
import csv
from abc import ABC, abstractmethod


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date or 'No Due Date'}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            due_date=data.get("due_date"),
            status=data["status"]
        )


class FileHandler(ABC):
    @abstractmethod
    def save(self, tasks, file_name):
        pass

    @abstractmethod
    def load(self, file_name):
        pass


class CSVFileHandler(FileHandler):
    def save(self, tasks, file_name):
        with open(file_name, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, file_name):
        tasks = []
        with open(file_name, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tasks.append(Task.from_dict(row)) 
        return tasks


class JSONFileHandler(FileHandler):
    def save(self, tasks, file_name):
        with open(file_name, "w") as f:
            json.dump([task.to_dict() for task in tasks], f)

    def load(self, file_name):
        tasks = []
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
                for item in data:
                    tasks.append(Task.from_dict(item))
        except FileNotFoundError:
            pass 
        return tasks


class TaskManager:
    def __init__(self, file_handler: FileHandler):
        self.tasks = []
        self.file_handler = file_handler

    def add_task(self):
        task_id = input("Enter Task ID: ").strip()
        title = input("Enter Title: ").strip()
        description = input("Enter Description: ").strip()
        due_date = input("Enter Due Date (YYYY-MM-DD) or leave blank: ").strip() or None
        status = input("Enter Status (Pending/In Progress/Completed): ").strip()
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ").strip()
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if not task:
            print("Task not found!")
            return

        print(f"Current Task: {task}")
        title = input(f"Enter New Title (leave blank to keep '{task.title}'): ").strip() or task.title
        description = input(f"Enter New Description (leave blank to keep '{task.description}'): ").strip() or task.description
        due_date = input(f"Enter New Due Date (leave blank to keep '{task.due_date}'): ").strip() or task.due_date
        status = input(f"Enter New Status (leave blank to keep '{task.status}'): ").strip() or task.status

        task.title, task.description, task.due_date, task.status = title, description, due_date, status
        print("Task updated successfully!")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ").strip()
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter Status to filter by (Pending/In Progress/Completed): ").strip()
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered_tasks:
            print("No tasks found with the specified status.")
        else:
            print("Filtered Tasks:")
            for task in filtered_tasks:
                print(task)

    def save_tasks(self):
        file_name = input("Enter file name to save tasks: ").strip()
        self.file_handler.save(self.tasks, file_name)
        print("Tasks saved successfully!")

    def load_tasks(self):
        file_name = input("Enter file name to load tasks from: ").strip()
        self.tasks = self.file_handler.load(file_name)
        print("Tasks loaded successfully!")


def main():
    print("Welcome to the To-Do Application!")
    print("Choose file format for storage:")
    print("1. CSV")
    print("2. JSON")
    choice = input("Enter your choice: ").strip()
    file_handler = CSVFileHandler() if choice == "1" else JSONFileHandler()

    manager = TaskManager(file_handler)

    while True:
        print("\n1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")
        option = input("Enter your choice: ").strip()

        if option == "1":
            manager.add_task()
        elif option == "2":
            manager.view_tasks()
        elif option == "3":
            manager.update_task()
        elif option == "4":
            manager.delete_task()
        elif option == "5":
            manager.filter_tasks()
        elif option == "6":
            manager.save_tasks()
        elif option == "7":
            manager.load_tasks()
        elif option == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()