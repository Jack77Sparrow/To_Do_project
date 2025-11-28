
from abc import ABC, abstractmethod
from typing import List, Dict
from tasks.task import Task, TimeFormating

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
        W = 20
        for task in self.tasks:
            created = getattr(task, 'created_at', 'N/A')

            last_update = getattr(task, 'last_updated', created)
            # Якщо це TimeFormating → беремо нормальну дату
            if isinstance(task.due_to, TimeFormating):
                due_date = task.due_to.time
            else:
                # старі задачі, де due_to просто строка
                due_date = task.due_to

            formating += (
            f"{task.title[:W]:^{W}}|"
            f"{task.description[:W]:^{W}}|"
            f"{due_date[:W]:^{W}}|"
            f"{task.status[:W]:^{W}}|"
            f"{task.priority[:W]:^{W}}|"
            f"{created[:W]:^{W}}|"
            f"{last_update[:W]:^{W}}\n"
        )

        return formating

    def remove_task(self, title: str):
        task_obj = self.find_task(title)
        if not task_obj:
            return f"Задачу '{title}' не знайдено."
        self.tasks.remove(task_obj)
        return f"Видалено '{title}'"

    def sorting_by_priority(self, priority):
        PRIORITY_ORDER = {
    'high': 3,
    'medium': 2,
    'low': 1
}
        sorting_type = True if priority == 'high' else False
        
        sorted_tasks = sorted(self.tasks, key=lambda t: PRIORITY_ORDER[t.priority], reverse=sorting_type)
        self.tasks = sorted_tasks
        formating = ''
        for task in sorted_tasks:
            formating += f"{task.title}\t{task.priority}\n"
        return formating
    
    def __str__(self):
        task_names = ""
        for task in self.tasks:
            task_names += task.title
            task_names += "\n"

        return task_names

