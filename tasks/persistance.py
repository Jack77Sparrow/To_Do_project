import pickle
import os
from tasks.task import Task
import sys

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
