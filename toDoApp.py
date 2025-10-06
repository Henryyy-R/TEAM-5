# toDoApp.py
# hello lim
# 1.) Better UI in main - Rich
# 2.) Better LOGIC (Error at remove or pop) - Henry all goods
# 3.) Proper Error Handling - Jabs
# 4.) Task Saving after closing app (No need to retype) - Finau

tasks = []

def addtask(task): 
    tasks.append(task) 
    print("task added!") 
    
def showTasks( ): 
    if len(tasks)==0: 
        print("no tasks yet") 
    else: 
        for i in range (len(tasks)): 
            print(i+1,".",tasks[i])

def removetask(task_number):
    """Remove a task by 1-based task_number (user-facing)."""
    if not tasks:
        print("No tasks to remove.")
        return
    if not isinstance(task_number, int):
        print("Invalid input: task number must be an integer.")
        return
    idx = task_number - 1  # convert to 0-based index
    if idx < 0 or idx >= len(tasks):
        print(f"Invalid task number. Enter a number between 1 and {len(tasks)}.")
        return
    removed = tasks.pop(idx)
    print(f"Removed task: {removed}")

def main():
    while True:
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
            print("=====================================")
        elif ch == "2":
            showTasks()
            print("=====================================")
        elif ch == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                try:
                    n = int(input(f"Enter task number to remove (1-{len(tasks)}): ").strip())
                    removetask(n)
                except ValueError:
                    print("Please enter a valid integer.")
            print("=====================================")
        elif ch == "4":
            print("Exiting....")
            break
        else:
            print("Wrong choice!!")
            print("=====================================")

if __name__ == "__main__":
    main()
