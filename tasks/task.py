from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from typing import List, Dict




class TimeFormating:
    def __init__(self, time):
        temp = datetime.strptime(time, "%d.%m.%Y")
        self.time = datetime.strftime(temp, "%d/%m/%Y")


class Task:
    def __init__(
        self, title, description, due_to: TimeFormating, priority, status="pending", created_at=None
    ):
        self.title = title
        self.description = description
        self.due_to = due_to
        self.priority = priority
        self.status = status
        self.created_at = created_at or datetime.now().strftime("%d/%m/%Y %H:%M")
        self.last_updated = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.history : List[Dict] = []


    
    def mark_processing(self):
        if self.status == "pending":
            self.status = "in process"

    def mark_done(self):
        if self.status == "pending":
            self.status = "done"

        else:
            return f"Status already done"

    def get_time_left(self):
        time_now = datetime.now()
        end_time = datetime.strptime(self.due_to, "%d.%m.%Y")
        time_left = end_time - time_now
        days = time_left.days
        hours = time_left.seconds // 3600
        minutes = (time_left.seconds % 3600) // 60
        return f"Залишилось {days} днів, {hours} годин і {minutes} хвилин"

    def update_title(self, new_title):
        self.title = new_title

    def update_description(self, new_description):
        self.description = new_description

    def update_dueto(self, new_dueto):
        self.due_to = new_dueto

    def set_priority(self, priority):
        self.priority = priority

    def set_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Task {self.title} is {self.status}"

