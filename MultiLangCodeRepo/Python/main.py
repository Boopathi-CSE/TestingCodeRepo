import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"


class Task:
    def __init__(self, title, priority="medium", completed=False):
        self.title = title
        self.priority = priority
        self.completed = completed
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                for item in data:
                    task = Task(item["title"], item["priority"], item["completed"])
                    task.created_at = item["created_at"]
                    self.tasks.append(task)
            except Exception as e:
                print("Error loading tasks:", e)

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]

        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def add_task(self, title, priority):
        task = Task(title, priority)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nYour Tasks")
        print("----------------------------")
        for idx, task in enumerate(self.tasks):
            status = "✓" if task.completed else "✗"
            print(f"{idx}. {task.title} | Priority: {task.priority} | Done: {status}")

    def complete_task(self, index):
        try:
            task = self.tasks[index]
            task.completed = True
            self.save_tasks()
            print("Task marked as completed.")
        except IndexError:
            print("Invalid task index.")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted task: {removed.title}")
        except IndexError:
            print("Invalid index.")

    def search_tasks(self, keyword):
        print(f"\nSearch results for '{keyword}'")
        print("----------------------------")

        results = []

        for task in self.tasks:
            if keyword.lower() in task.title.lower():
                results.append(task)

        if len(results) == 0:
            print("No matching tasks found.")
            return

        for task in results:
            print(f"{task.title} | Priority: {task.priority}")

    def show_stats(self):
        total = len(self.tasks)
        completed = 0

        for task in self.tasks:
            if task.completed:
                completed += 1

        pending = total - completed

        print("\nTask Statistics")
        print("-------------------")
        print("Total tasks:", total)
        print("Completed:", completed)
        print("Pending:", pending)

        completion_rate = (completed / total) * 100
        print("Completion rate:", round(completion_rate, 2), "%")

    # BUG 2 exists here
    def tasks_by_priority(self):
        priority_map = {}

        for task in self.tasks:
            if task.priority not in priority_map:
                priority_map[task.priority] = []

            priority_map[task.priority].append(task.title)

        print("\nTasks Grouped by Priority")
        print("----------------------------")

        for p in priorities:  # <-- BUG: variable doesn't exist
            print(p.upper())
            for t in priority_map[p]:
                print(" -", t)


def show_menu():
    print("\n==== TODO MANAGER ====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Show Statistics")
    print("7. Show Tasks by Priority")
    print("0. Exit")


def main():
    manager = TaskManager()

    while True:
        show_menu()

        choice = input("Select option: ")

        if choice == "1":
            title = input("Task title: ")
            priority = input("Priority (low/medium/high): ")
            manager.add_task(title, priority)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            index = int(input("Enter task index: "))
            manager.complete_task(index)

        elif choice == "4":
            index = int(input("Enter index to delete: "))
            manager.delete_task(index)

        elif choice == "5":
            keyword = input("Enter keyword: ")
            manager.search_tasks(keyword)

        elif choice == "6":
            manager.show_stats()

        # BUG 1 triggered if there are no tasks
        elif choice == "7":
            manager.tasks_by_priority()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()