
from abc import ABC, abstractmethod
from typing import List, Dict
from tasks.task import Task

class TaskManager(ABC):
    @abstractmethod
    def add_task(self):
        pass

    @abstractmethod
    def find_task(self):
        pass

    @abstractmethod
    def show_tasks(self):
        pass

    @abstractmethod
    def remove_task(self):
        pass


class CMDTaskManager(TaskManager):
    def __init__(self, tasks=None):
        self.tasks: List[Task] = tasks or []
        self.history: List[Dict] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def find_task(self, title):
        for task in self.tasks:
            if title == task.title:
                return task

    def show_tasks(self):
        formating = ""
        for task in self.tasks:
            created = getattr(task, 'created_at', 'N/A')

            last_update = getattr(task, 'last_updated', created)
            formating += f"Title: {task.title} Description: {task.description} Date: {task.due_to} Status: {task.status} Priority: {task.priority} Created at: {created} Last updated: {last_update}\n"

        return formating

    def remove_task(self, title: str):
        task_obj = self.find_task(title)
        if task_obj not in self.tasks:
            return f"{title} немає в тасках"
        else:
            for task in self.tasks:
                if title == task.title:
                    self.tasks.remove(task_obj)
                    return f"Видалено {title} з нотаток"

    def sorting_by_priority(self, priority):
        
        sorting_type = True if priority == 'high' else False
        
        sorted_tasks = sorted(self.tasks, key=lambda t: t.priority, reverse=sorting_type)
        self.tasks = sorted_tasks
        formating = ''
        for task in sorted_tasks:
            formating += f"{task.title}\n"
        print(formating)
        return sorted_tasks
    
    def __str__(self):
        task_names = ""
        for task in self.tasks:
            task_names += task.title
            task_names += "\n"

        return task_names

