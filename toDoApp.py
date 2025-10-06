# toDoApp.py

# 1.) Better UI in main - Rich ✅ 10/6/2025 10:06 PM
# 2.) Better LOGIC (Error at remove or pop) - Henry ✅ 10/6/2025 3:16 PM
# 3.) Task Saving after closing app (No need to retype) - Finau ✅ 10/6/2025 5:24 PM
# 4.) Proper Error handling - Jabs ✅ 10/6/2025 - 6:36 PM
# Added Error handlers on addTask, saveTask, showTask, removeTask, and on main function. 
# Mainly focused on try except blocks so that the program will crash smoothly if the need arises.
# Follows a camelCase format for variable names.

import os

tasks = []     # Stores all current tasks in memory

def loadTask():     # Load tasks from 'tasks.txt' if the file exists
    try:
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                for line in f:
                    tasks.append(line.strip())
    except Exception as e:
        print(f"Error loading tasks: {e}")

def saveTask():     # Save current tasks to 'tasks.txt'
    try:
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def addTask(task):     # Add a new task to the list and save it
    try:
        if not task.strip():
            print("\n Task cannot be empty.\n")
            return
        tasks.append(task) 
        saveTask()
        print("\n Task added succesfully!\n")
    except Exception as e:
        print(f"Error adding task: {e}")

def showTask():     # Display all tasks with numbering
    try:
        print("\n" + "=" * 45)
        print("YOUR TASK LIST".center(45))
        print("=" * 45)
        
        if len(tasks) == 0: 
            print("\n No tasks yet. Add a task first.\n") 
        else: 
            for i in range(len(tasks)): 
                print(i+1, ".", tasks[i])
    except Exception as e:
        print(f"Error showing tasks: {e}")

def removeTask(task_number):     # Remove a task by its number (1-based index)
    try:
        if not tasks:
            print("\nNo tasks to remove.\n")
            return
        if not isinstance(task_number, int):
            print("\nInvalid input: task number must be an integer.\n")
            return
        idx = task_number - 1
        if idx < 0 or idx >= len(tasks):
            print(f"\nInvalid task number. Enter a number between 1 and {len(tasks)}.\n")
            return
        removed = tasks.pop(idx)
        saveTask()
        print(f"\nRemoved task: {removed}\n")
    except Exception as e:
        print(f"Error removing task: {e}")
        
def header():
    print("\n")
    print("=" * 45)
    print("||                                         ||")
    print("||            TASK MANAGER                 ||")
    print("||                                         ||")
    print("=" * 45)

def menu():
    print("\n MENU OPTIONS:")
    print(" " + "-" * 45)
    print("    [1] Add Task")
    print("    [2] Show Tasks")
    print("    [3] Remove Task")
    print("    [4] Exit")
    print(" " + "-" * 45)
    
def main():
    loadTask()
    while True:
        try:
            header()
            menu()

            ch = input(" Enter your choice (1 - 4): ").strip()
            
            if ch == "1":
                print("\n" + "-" * 45)
                print(" ADD NEW TASK")
                print("-" * 45)
                t = input(" Enter task description: ")
                addTask(t)
                
            elif ch == "2":
                showTask()
                
            elif ch == "3":
                if not tasks:
                    print(" No tasks to remove.")
                else:
                    try:
                        n = int(input(f" Enter task number to remove (1 - {len(tasks)}): ").strip())
                        removeTask(n)
                    except ValueError:
                        print("ERROR! Please enter a valid integer.")
                        
            elif ch == "4":
                print("\n" + "=" * 45)
                print("\n Thank you for using Task Manager!")
                print(" Goodbye!\n")
                print("=" * 45 + "\n")
                break
                
            else:
                print("ERROR! Invalid choice. Choose from (1 - 4).\n")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main() # Start the task manager





