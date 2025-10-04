# toDoApp.py
#hello lim
tasks=[]

def addtask(task) :
  tasks.append(task)
  print("task added!")

def showTasks( ):
    if len(tasks)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

def removetask(tasknumber):
    tasks.pop(tasknumber) 
    print("task removed!!")

def main():
    while True:
        print("Task MANAGER!!!")
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4. Exit")
        ch = input("enter choice : ")
        print("=====================================")
        if ch=="1":
            t = input("enter task : ")
            addtask(t)
            print("=====================================")
        elif ch=="2":
            showTasks()
            print("=====================================")
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            removetask(n)
            print("=====================================")
        elif ch=="4":
            break;
        else:
            print("wrong choice!!")
            print("=====================================")
main()





