import tkinter as tk
from tkinter import messagebox

class TODOAPP:
    def __init__(self, root):  # Correct constructor method
        self.root = root
        self.root.title("TO DO LIST BY AKSHAY")

        self.tasks = []

        self.frame = tk.Frame(root)  # Use Frame class
        self.frame.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.frame, text="ADD TASK", command=self.add_task)  # Use Button class
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(padx=5, pady=5)

        self.remove_button = tk.Button(self.frame, text="REMOVE TASK", command=self.remove_task)  # Use Button class
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("INPUT ERROR", "PLEASE ENTER A TASK.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("SELECTION ERROR", "PLEASE SELECT A TASK TO REMOVE.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":  # Correct block to run the app
    root = tk.Tk()
    app = TODOAPP(root)  # Initialize the correct class name
    root.mainloop()
