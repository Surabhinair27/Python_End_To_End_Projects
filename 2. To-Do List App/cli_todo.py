# ✅ To-Do List CLI App
# ---------------------------------
# File based task manager
# Tasks tasks.txt me save hongi
# ---------------------------------

import os   # file check karne ke liye


FILE_NAME = "tasks.txt"   # file name jahan tasks store honge


# 📂 File se tasks load karo
def load_tasks():
    # agar file exist karti hai
    if os.path.exists(FILE_NAME):
        # read mode me open karo
        with open(FILE_NAME, "r") as f:
            # lines list me return karo
            return f.read().splitlines()
    return []


# 💾 Tasks save karo file me
def save_tasks(tasks):
    # write mode (overwrite)
    with open(FILE_NAME, "w") as f:
        # har task new line me likho
        for task in tasks:
            f.write(task + "\n")


# ➕ Add task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!\n")


# ❌ Delete task
def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("🗑️ Task deleted!\n")


# 📋 Show tasks
def show_tasks(tasks):
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


# 🚀 Main menu
def main():

    tasks = load_tasks()

    while True:
        print("==== TO-DO MENU ====")
        print("1 Add Task")
        print("2 Delete Task")
        print("3 Show Tasks")
        print("4 Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            show_tasks(tasks)
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
