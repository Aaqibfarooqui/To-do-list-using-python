import os

def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks, filename):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def show_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks, task):
    tasks.append(task)
    print(f"Added task: {task}")

def mark_task_complete(tasks, index):
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
    else:
        print(f"Marked task '{tasks[index-1]}' as complete.")
        del tasks[index-1]

def delete_task(tasks, index):
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
    else:
        print(f"Deleted task '{tasks[index-1]}' from the list.")
        del tasks[index-1]

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            show_tasks(tasks)
            task_index = int(input("Enter task number to mark as complete: "))
            mark_task_complete(tasks, task_index)
        elif choice == '4':
            show_tasks(tasks)
            task_index = int(input("Enter task number to delete: "))
            delete_task(tasks, task_index)
        elif choice == '5':
            save_tasks(tasks, filename)
            print("Tasks saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
