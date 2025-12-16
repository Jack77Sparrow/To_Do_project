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
        self.root.title("NoteApp — Нотатки")
        self.root.geometry("950x550")
        self.root.configure(bg="#1E1E1E")

        # ----- Стилі -----
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TButton",
                        background="#0E639C",
                        foreground="white",
                        font=("Arial", 11, "bold"),
                        padding=6)
        style.map("TButton",
                  background=[("active", "#1177BB")])

        style.configure("TLabel",
                        background="#1E1E1E",
                        foreground="white",
                        font=("Arial", 12))

        # ----- Ліве меню -----
        sidebar = Frame(self.root, bg="#252526", width=260)
        sidebar.pack(side="left", fill="y")

        Label(sidebar, text="Нотатки", bg="#252526",
              fg="white", font=("Arial", 16, "bold")).pack(pady=15)

        self.notes_list = Listbox(sidebar,
                                  font=("Arial", 13),
                                  bg="#3A3D41",
                                  fg="white",
                                  selectbackground="#0E639C",
                                  border=0,
                                  highlightthickness=0,
                                  activestyle="none")
        self.notes_list.pack(fill="both", expand=True, padx=10, pady=5)
        self.notes_list.bind("<<ListboxSelect>>", self.display_selected_note)

        ttk.Button(sidebar, text="＋ Додати", command=self.add_note_window).pack(pady=10)
        ttk.Button(sidebar, text="🗑 Видалити", command=self.delete_selected_note).pack(pady=5)

        # ----- Основна область -----
        self.display = Frame(self.root, bg="#1E1E1E")
        self.display.pack(side="right", fill="both", expand=True)

        self.title_label = Label(self.display, text="Оберіть нотатку...",
                                 bg="#1E1E1E", fg="white",
                                 font=("Arial", 22, "bold"))
        self.title_label.pack(anchor="nw", padx=25, pady=25)

        self.desc_label = Label(self.display, text="", bg="#1E1E1E",
                                fg="#CCCCCC", font=("Arial", 14),
                                wraplength=600, justify="left")
        self.desc_label.pack(anchor="nw", padx=25, pady=10)

        self.date_label = Label(self.display, text="", bg="#1E1E1E",
                                fg="#CCCCCC", font=("Arial", 12))
        self.date_label.pack(anchor="nw", padx=25, pady=5)

        self.priority_label = Label(self.display, text="", bg="#1E1E1E",
                                    fg="#CCCCCC", font=("Arial", 12))
        self.priority_label.pack(anchor="nw", padx=25, pady=5)

        ttk.Button(self.display, text="✏ Редагувати",
                   command=self.edit_selected_note).pack(anchor="ne", padx=25, pady=10)

        self.refresh_note_list()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    # ----------------------------------------------------------------------
    def refresh_note_list(self):
        self.notes_list.delete(0, END)
        for task in self.manager.tasks:
            self.notes_list.insert(END, task.title)

    def display_selected_note(self, event=None):
        index = self.notes_list.curselection()
        if not index:
            return

        task = self.manager.tasks[index[0]]

        self.title_label.config(text=task.title)
        self.desc_label.config(text=f"Опис:\n{task.description}")
        self.date_label.config(text=f"Дата: {task.due_to.time}")
        self.priority_label.config(text=f"Пріоритет: {task.priority}")

    # ----------------------------------------------------------------------
    def add_note_window(self):
        win = Toplevel(self.root)
        win.title("Додати нотатку")
        win.configure(bg="#252526")

        labels = ["Назва", "Опис", "Дата", "Пріоритет"]
        entries = []

        for i, label in enumerate(labels):
            Label(win, text=label, bg="#252526", fg="white").grid(row=i, column=0, padx=5, pady=7)
            entry = ttk.Entry(win, width=40)
            entry.grid(row=i, column=1, padx=5, pady=7)
            entries.append(entry)

        def save():
            title, desc, date, pr = [e.get() for e in entries]
            task = Task(title=title, description=desc, due_to=date, priority=pr)
            self.manager.add_task(task)
            self.refresh_note_list()
            win.destroy()

        ttk.Button(win, text="💾 Зберегти", command=save).grid(row=4, column=1, pady=12)

    # ----------------------------------------------------------------------
    def delete_selected_note(self):
        index = self.notes_list.curselection()
        if not index:
            return

        task = self.manager.tasks[index[0]]
        self.manager.tasks.remove(task)

        save_to_json(self.manager.tasks)
        save_to_pickle(self.manager.tasks)
        database_save(self.manager.tasks)

        self.refresh_note_list()

        self.title_label.config(text="Оберіть нотатку...")
        self.desc_label.config(text="")
        self.date_label.config(text="")
        self.priority_label.config(text="")

    # ----------------------------------------------------------------------
    def edit_selected_note(self):
        index = self.notes_list.curselection()
        if not index:
            return

        task = self.manager.tasks[index[0]]
        win = Toplevel(self.root)
        win.title("Редагувати нотатку")
        win.configure(bg="#252526")

        labels = ["Назва", "Опис", "Дата", "Пріоритет"]
        data = [task.title, task.description, task.due_to.time, task.priority]
        entries = []

        for i, label in enumerate(labels):
            Label(win, text=label, bg="#252526", fg="white").grid(row=i, column=0, padx=5, pady=7)
            entry = ttk.Entry(win, width=40)
            entry.insert(0, data[i])
            entry.grid(row=i, column=1, padx=5, pady=7)
            entries.append(entry)

        def save():
            task.title = entries[0].get()
            task.description = entries[1].get()
            task.due_to = TimeFormating(entries[2].get())
            task.priority = entries[3].get()

            save_to_json(self.manager.tasks)
            save_to_pickle(self.manager.tasks)
            database_save(self.manager.tasks)
            self.refresh_note_list()
            win.destroy()

        ttk.Button(win, text="💾 Зберегти", command=save).grid(row=4, column=1, pady=12)

    # ----------------------------------------------------------------------
    def on_close(self):
        save_to_json(self.manager.tasks)
        save_to_pickle(self.manager.tasks)
        database_save(self.manager.tasks)
        self.root.destroy()
