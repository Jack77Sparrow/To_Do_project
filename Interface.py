from tasks.task import Task
from tasks.manager import CMDTaskManager
from datetime import datetime


class CMDInterface:
    def __init__(self, manager: CMDTaskManager):
        self.manager = manager

    def add_task(self):
        title = input("Введіть назву: ")
        if any(title == item.title for item in self.manager.tasks):
            print(f"{title} Вже є в тасках")
            return 

        description = input("Введіть опис: ")
        due_time = input("Введіть час в D.M.Y форматі: ")
        priority = input("Введіть пріорітет таски: ")
        task = Task(
            title=title, description=description, due_to=due_time, priority=priority
        )
        
        self.manager.add_task(task)

    def remove_task(self):
        title = input("Enter a title: ")
        print(self.manager.remove_task(title))

    def show_tasks(self):
        print(self.manager.show_tasks())

    def time_left(self):
        task_name = input("Введіть назву таски ")
        finded_task = self.manager.find_task(task_name)
        print(finded_task.get_time_left())

    def sort_tasks(self):
        priority = input(
            "Сортування тасок:\n- Введіть 'high' для сортування за спаданням пріоритету\n- Введіть 'low' для сортування за зростанням пріоритету\n\n"
        )
        print(self.manager.sorting_by_priority(priority=priority))

    def update_task(self):
        updated_task = input("Введіть таску яку ви хочите оновити: ")
        finded_task = self.manager.find_task(updated_task)
        finded_task.last_updated = datetime.now().strftime("%d/%m/%Y %H:%M")
        if not finded_task:
            print(f"Такої таски не існує")
            return

        field = input(
            "Що ви хочите оновити title/description/due_time/priority/status? "
        )
        old_value = getattr(finded_task, field)
        new_value = "N/A"
        if field == "title":
            new_title = input("Введіть нову назву ")
            finded_task.update_title(new_title)
            print("Назву оновлено")
            new_value = new_title
        elif field == "description":
            new_description = input("Введіть новий опис таски ")
            finded_task.update_description(new_description)
            print("Опис оновлено")
            new_value = new_description
        elif field == "due_time":
            new_time = input("Оновлений час здачі ")
            finded_task.update_dueto(new_time)
            print("Час оновлено")
            new_value = new_time
        elif field == "priority":
            priority_map = {1: "hight", 2: "medium", 3: "low"}
            new_priority_num = int(
                input(
                    "Введіть пріорітет в цифровому форматі (3:low/2:medium/1:hight): "
                )
            )
            old_value = finded_task.priority
            new_value = priority_map.get(new_priority_num, old_value)
            finded_task.set_priority(priority=new_value)

        elif field == "status":
            new_status = input("Оновлений статус задачі: ")
            finded_task.set_status(new_status=new_status)
            new_value = new_status

        finded_task.history.append(
            {
                "field": field,
                "old": old_value,
                "new": new_value,
                "changed_at": datetime.now().strftime("%d/%m/%Y %H:%M"),
            }
        )
        self.manager.history.append(
            {
                "task": finded_task.title,
                "field": field,
                "old": old_value,
                "new": new_value,
                "changed_at": datetime.now().strftime("%d/%m/%Y %H:%M"),
            }
        )
