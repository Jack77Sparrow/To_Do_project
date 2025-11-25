import pickle
import os
from tasks.task import Task, TimeFormating
import sys
import json

sys.path.append("/Users/drake/Documents/Projects/To_Do_List/tasks")

def save_to_pickle(data, filename=os.path.join(os.path.dirname(__file__), "..", "data/data.pkl")):
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_from_pickle(filename=os.path.join(os.path.dirname(__file__), "..", "data/data.pkl")):
    if not os.path.exists(filename):
        return []
    with open(filename, "rb") as file:
        data = pickle.load(file)
        return data


def save_to_json(data, filename=os.path.join(os.path.dirname(__file__), "..", "data/data.json")):
    tasks_list = []
    for item in data:
        t = item.__dict__.copy()
        if type(item.due_to) == TimeFormating:
            t['due_to'] = item.due_to.time
        tasks_list.append(t)
    
    print(tasks_list)
    with open(filename, 'w') as file:
        json.dump(tasks_list, file, indent=4)

    
def load_from_json(filename=os.path.join(os.path.dirname(__file__), "..", "data/data.json")):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data