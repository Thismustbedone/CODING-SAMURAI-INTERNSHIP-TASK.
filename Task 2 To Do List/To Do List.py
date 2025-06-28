import os
import tkinter as tk
from tkinter import simpledialog, messagebox

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Calculator")
        self.tasks = load_tasks()

        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.update_listbox()

        btn1 = tk.Button(root, text="1\nView", width=10, height=3, command=self.view_tasks)
        btn2 = tk.Button(root, text="2\nAdd", width=10, height=3, command=self.add_task)
        btn3 = tk.Button(root, text="3\nDelete", width=10, height=3, command=self.delete_task)
        btn4 = tk.Button(root, text="4\nExit", width=10, height=3, command=self.exit_app)

        btn1.grid(row=1, column=0, padx=5, pady=5)
        btn2.grid(row=1, column=1, padx=5, pady=5)
        btn3.grid(row=1, column=2, padx=5, pady=5)
        btn4.grid(row=2, column=1, padx=5, pady=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, 1):
            self.listbox.insert(tk.END, f"{idx}. {task}")

    def view_tasks(self):
        self.update_listbox()
        messagebox.showinfo("Tasks", "Tasks refreshed!")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter task description:")
        if task and task.strip():
            self.tasks.append(task.strip())
            save_tasks(self.tasks)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Empty task not added.")

    def delete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Select a task to delete.")
            return
        idx = selection[0]
        removed = self.tasks.pop(idx)
        save_tasks(self.tasks)
        self.update_listbox()
        messagebox.showinfo("Deleted", f"Task '{removed}' deleted.")

    def exit_app(self):
        save_tasks(self.tasks)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()