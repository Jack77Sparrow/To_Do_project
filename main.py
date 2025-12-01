
import pickle
import os

from UI.CLI_interface import CMDInterface
from UI.GUI_interface import GUIInterface
from tasks.manager import CMDTaskManager

from tasks.persistance import load_from_pickle, save_to_pickle, save_to_json, load_from_json, database_save, clear_database



def main():

    try:
        data = load_from_pickle()
    except pickle.UnpicklingError:
        data = []
    task_manager = CMDTaskManager(tasks=data)
    ui = CMDInterface(task_manager)
    

    commands = {
        "add_task": ui.add_task,
        "remove_task": ui.remove_task,
        "show_tasks": ui.show_tasks,
        "time_left": ui.time_left,
        "update_task": ui.update_task,
        "sort_tasks": ui.sort_tasks,
        "help": ui.help_cmd,
        "clear_data": ui.clear_data,
    }
    print("Введіть help для того щоб дізнатись на що спроможний бот")
   
    while True:
        interface = input("Яким інтерфейсом ви хочете користуватись gui/cmd?: ")
        if interface in ["exit", "q", "quit"]:
            break
        elif interface == 'cmd':
            while True:
                command = input("Введіть команду: ")
                if command in ["exit", "q", "quit"]:
                    save_to_pickle(task_manager.tasks)
                    save_to_json(task_manager.tasks)
                    database_save(task_manager.tasks)
                    break
                action = commands.get(command)
                if action:
                    action()
                else:
                    print("Немає такої команди спробуйте ще")
        elif interface == 'gui':
            GUIInterface(task_manager)
            

if __name__ == "__main__":
    main()
