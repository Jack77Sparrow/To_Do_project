
import pickle
import os

from Interface import CMDInterface
from tasks.manager import CMDTaskManager

from tasks.persistance import load_from_pickle, save_to_pickle



def main():
    data = load_from_pickle()
    task_manager = CMDTaskManager(tasks=data)
    ui = CMDInterface(task_manager)
    commands = {
        "add_task": ui.add_task,
        "remove_task": ui.remove_task,
        "show_tasks": ui.show_tasks,
        "time_left": ui.time_left,
        "update_task": ui.update_task,
        "sort_tasks": ui.sort_tasks
    }

    while True:
        command = input("Введіть команду: ")
        if command in ["exit", "q", "quit"]:
            save_to_pickle(task_manager.tasks)
            break
        action = commands.get(command)
        if action:
            action()
        else:
            print("Немає такої команди спробуйте ще")


if __name__ == "__main__":
    main()
