from tkinter import *
from tkinter import ttk
import tkinter as tk

from tasks.manager import CMDTaskManager
from tasks.task import Task, TimeFormating

from tasks.persistance import save_to_json, save_to_pickle, database_save

class GUIInterface:

    def __init__(self, manager: CMDTaskManager):
        self.manager = manager
        self.root = Tk()
        self.root.title("TO_DO_list")
        ttk.Label(self.root, text="Назва задачі").grid(row=0, column=0, padx=5, pady=5)
        self.entry_task_name = ttk.Entry(self.root, width=30)
        self.entry_task_name.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="Опис задачі").grid(row=1, column=0, padx=5, pady=5)
        self.entry_description = ttk.Entry(self.root, width=30)
        self.entry_description.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="Дата виконання").grid(row=2, column=0, padx=5, pady=5)
        self.entry_due_to = ttk.Entry(self.root, width=30)
        self.entry_due_to.grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="пріоритет").grid(row=3, column=0, padx=5, pady=5)
        self.entry_priority = ttk.Entry(self.root, width=30)
        self.entry_priority.grid(row=3, column=1, padx=5, pady=5)


        ttk.Button(self.root, text="add task", command=self.add_task).grid(row=4, column=1, pady=5)
        ttk.Button(self.root, text='show tasks', command=self.show_tasks).grid(row=4, column=0, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)


    def on_close(self):
        save_to_json(self.manager.tasks)
        save_to_pickle(self.manager.tasks)
        database_save(self.manager.tasks)
        self.root.destroy()

    
    def add_task(self):
        
        title = self.entry_task_name.get()
        description = self.entry_description.get()
        due_to = self.entry_due_to.get()
        priority = self.entry_priority.get()
        task = Task(
            title=title, description=description, due_to=due_to, priority=priority
        )
        self.manager.add_task(task)
        self.entry_task_name.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)
        self.entry_due_to.delete(0, tk.END)
        self.entry_priority.delete(0, tk.END)
        print(title)

    def show_tasks(self):
        note_root = Toplevel(self.root)
        tasks = self.manager.tasks
        print(tasks)
        for position, task in enumerate(tasks):
            print(position)
            notebook = ttk.Notebook(note_root)
            notebook.grid(column=1+position, row=0, padx=10, pady=10)
            title = task.title
            tab1 = ttk.Frame(notebook, padding=10)
            notebook.add(tab1, text=f'{title}')
            
            # title = task.title
            description = task.description
            due_to = task.due_to.time
            priority = task.priority
            frame = ttk.LabelFrame(tab1, text="Інформація про задачу", padding=10)
            frame.grid(column=1, row=1, sticky="w", padx=5, pady=5)


            # ttk.Label(tab1, text=f"{title}").grid(column=1+position, row=1)
            ttk.Label(frame, text=f"Опис: {description}").grid(column=1, row=2, sticky='w')
            ttk.Label(frame, text=f"Дата виконання: {due_to}").grid(column=1, row=3, sticky='w')
            ttk.Label(frame, text=f"Пріоритет: {priority}").grid(column=1, row=4, sticky='w')

