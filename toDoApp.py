# toDoApp.py

# 1.) Better UI in main - Rich
# 2.) Better LOGIC (Error at remove or pop) - Henry ✅ 10/6/2025 3:16 PM
# 3.) Task Saving after closing app (No need to retype) - Finau ✅ 10/6/2025 5:24PM
# 4.) Proper Error handling - Jabs
# Added Error handlers on addtask, save_task, showTasks, removeTasks, and on main function. 
# Mainly focused on try except blocks so that the program will crash smoothly if the need arises.

import os

tasks = []

def load_tasks():
    try:
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                for line in f:
                    tasks.append(line.strip())
    except Exception as e:
        print(f"Error loading tasks: {e}")

def save_tasks():
    try:
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def addtask(task): 
    try:
        if not task.strip():
            print("Task cannot be empty.")
            return
        tasks.append(task) 
        save_tasks()
        print("Task added!")
    except Exception as e:
        print(f"Error adding task: {e}")

def showTasks(): 
    try:
        if len(tasks) == 0: 
            print("No tasks yet") 
        else: 
            for i in range(len(tasks)): 
                print(i+1, ".", tasks[i])
    except Exception as e:
        print(f"Error showing tasks: {e}")

def removetask(task_number):
    try:
        if not tasks:
            print("No tasks to remove.")
            return
        if not isinstance(task_number, int):
            print("Invalid input: task number must be an integer.")
            return
        idx = task_number - 1
        if idx < 0 or idx >= len(tasks):
            print(f"Invalid task number. Enter a number between 1 and {len(tasks)}.")
            return
        removed = tasks.pop(idx)
        save_tasks()
        print(f"Removed task: {removed}")
    except Exception as e:
        print(f"Error removing task: {e}")

def main():
    load_tasks()
    while True:
        try:
            print("Task MANAGER!!!")
            print("1. Add Task")
            print("2. Show Tasks")
            print("3. Remove Task")
            print("4. Exit")
            ch = input("Enter choice: ").strip()
            print("=====================================")
            if ch == "1":
                t = input("Enter task: ")
                addtask(t)
            elif ch == "2":
                showTasks()
            elif ch == "3":
                if not tasks:
                    print("No tasks to remove.")
                else:
                    try:
                        n = int(input(f"Enter task number to remove (1-{len(tasks)}): ").strip())
                        removetask(n)
                    except ValueError:
                        print("Please enter a valid integer.")
            elif ch == "4":
                print("Exiting....")
                break
            else:
                print("Wrong choice!!")
            print("=====================================")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
