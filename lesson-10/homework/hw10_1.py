'''Homework 1. ToDo List Application

Define Task Class:
Create a Task class with attributes such as task title, description, due date, and status.
Define ToDoList Class:
Create a ToDoList class that manages a list of tasks.
Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
Create Main Program:
Develop a simple CLI to interact with the ToDoList.
Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
Test the Application:
Create instances of tasks and test the functionality of your ToDoList.
'''
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = "Incomplete"
    
    def mark_complete(self):
        self.status = "Complete"
    
    def __str__(self):
        return f"{self.title} - {self.description} (Due: {self.due_date.date()}) [{self.status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return f"Task '{title}' marked as complete."
        return "Task not found."
    
    def list_tasks(self, only_incomplete=False):
        if only_incomplete:
            tasks = [task for task in self.tasks if task.status == "Incomplete"]
        else:
            tasks = self.tasks
        
        return "\n".join(str(task) for task in tasks) if tasks else "No tasks available."

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nToDo List Application")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully!")
        
        elif choice == "2":
            title = input("Enter task title to mark as complete: ")
            print(todo_list.mark_task_complete(title))
        
        elif choice == "3":
            print("\nAll Tasks:")
            print(todo_list.list_tasks())
        
        elif choice == "4":
            print("\nIncomplete Tasks:")
            print(todo_list.list_tasks(only_incomplete=True))
        
        elif choice == "5":
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
