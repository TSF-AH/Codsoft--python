import json
tasks = []
def add_task():
    your_task = input("Enter your task: ")

    task = {
        "Task": your_task,
        "Completed": False
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully.")
def view_task():
    if len(tasks) == 0:    
        print("No tasks added yet.")
    else:
        print("=" * 40)

        for number, task in enumerate(tasks, start=1):

            if task["Completed"]:
                status = "✔ Completed"
            else:
                status = "❌ Pending"

            print(f"{number}. {task['Task']}")
            print(f"Status : {status}")
            print("-" * 40)
def complete_task():

    if len(tasks) == 0:
        print("No tasks available.")
    else:
        task_number = int(input("Enter task number completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["Completed"] = True
            save_tasks()
            print("Task completed successfully.")
        else:
            print("Invalid task number.")
def delete_task():
    if len(tasks) == 0:
        print("No tasks available.")

    else:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            save_tasks()
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
def exit_task():
    print("exiting. thank you.")
def save_tasks():
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent = 4)
def load_tasks():
    global tasks
    try:
        with open("tasks.json","r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks =[]
load_tasks()
while True:
    print("=" * 40)
    print(" TO-DO LIST")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()

    elif choice == 3:
        complete_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        exit_task()
        break
    else:
        print("Invalid choice.")
