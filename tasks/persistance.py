import pickle
import os
from tasks.task import Task, TimeFormating
from tasks.manager import TaskManager
import sys
import json
import sqlite3

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
    

def database_save(tasks):
    try:
        conn = sqlite3.connect("data/tasks.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                due_to TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                last_updated TEXT NOT NULL
            )
        """)

        for t in tasks:
            due_to = (
                t.due_to.strftime("%Y-%m-%d %H:%M:%S")
                if hasattr(t.due_to, "strftime")
                else str(t.due_to.time)
            )

            cursor.execute("""
                INSERT INTO tasks (title, description, due_to, priority, status, created_at, last_updated)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                t.title,
                t.description,
                due_to,
                t.priority,
                t.status,
                t.created_at,
                t.last_updated
            ))

        conn.commit()

    except sqlite3.Error as e:
        print("DB Error:", e)

    finally:
        conn.close()

        
def clear_database():
    conn = sqlite3.connect("data/tasks.db")
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE tasks;""")

    conn.commit()
    conn.close()