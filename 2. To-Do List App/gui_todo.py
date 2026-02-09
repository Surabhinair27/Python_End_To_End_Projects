# ✅ To-Do List GUI App using Tkinter
# -----------------------------------
# Add / Delete tasks with buttons
# Tasks file me save hoti hain
# -----------------------------------

import tkinter as tk
import os

FILE_NAME = "tasks.txt"


# 📂 Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return f.read().splitlines()
    return []


# 💾 Save tasks
def save_tasks():
    tasks = listbox.get(0, tk.END)

    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


# ➕ Add task
def add_task():
    task = entry.get()

    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()


# ❌ Delete selected
def delete_task():
    selected = listbox.curselection()

    if selected:
        listbox.delete(selected[0])
        save_tasks()


# 🪟 Window create
root = tk.Tk()
root.title("To-Do List App ✅")
root.geometry("350x400")


# 📝 Entry box
entry = tk.Entry(root, width=25)
entry.pack(pady=10)


# ➕ Button
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()


# 📋 Listbox
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)


# ❌ Delete button
del_btn = tk.Button(root, text="Delete Selected", command=delete_task)
del_btn.pack()


# 🔄 Load previous tasks
for task in load_tasks():
    listbox.insert(tk.END, task)


root.mainloop()
