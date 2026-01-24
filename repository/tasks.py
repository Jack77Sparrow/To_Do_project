from psycopg2 import DatabaseError
import logging
import datetime
from model.my_models import model, difficulty_model
from db_sqlalchemy.connect import session, Task



def select_all_tasks(status, priority, difficulty):
    
    query = session.query(Task)

    if status is not None:
        query = query.filter(Task.status == status)

    if priority is not None:
        query = query.filter(Task.priority == priority)

    if difficulty is not None:
        query = query.filter(Task.difficulty == difficulty)

    return query.all()

    

def select_today_tasks(conn):
    cur = conn.cursor()
    try:
        cur.execute("select * from tasks t where t.due_to = CURRENT_DATE")
        rows = cur.fetchall()
        cur.close()
        columns = [
        "id", "title", "description", "category",
        "difficulty", "priority", "status",
        "created_at", "last_updated", "due_to"
    ]
        
        return [dict(zip(columns, row)) for row in rows]
    except DatabaseError as err:
        logging.error(err)


def select_task_by_id(conn, task_id: int):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks t WHERE t.id = %s", (task_id, ))
        row = cur.fetchone()
        if row is None:
            return None
        cur.close()
        columns = [
        "id", "title", "description", "category",
        "difficulty", "priority", "status",
        "created_at", "last_updated", "due_to"
    ]
        return dict(zip(columns, row))
    except DatabaseError as err:
        logging.error(err)

    

def update_task(conn, task_id: int, data: dict):
    cur = conn.cursor()

    fields = []
    values = []
    for key, value in data.items():
        fields.append(f"{key} = %s")
        values.append(value)

    fields.append("last_updated = NOW()")
    sql = f"""UPDATE tasks SET {', '.join(fields)} WHERE id = %s RETURNING id"""

    values.append(task_id)
    try:
        
        cur.execute(sql, tuple(values))
        updated = cur.fetchone()
        return updated is not None
    except DatabaseError as err:
        logging.error(err)
    finally:
        cur.close()



def add_task_to_db(conn, data: dict):
    cur = conn.cursor()
    sql = """INSERT INTO tasks (
    title, 
    description, 
    category, 
    difficulty, 
    priority, 
    status, 
    created_at, 
    last_updated, 
    due_to) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"""
    text = f"{data['title']} {data['description']}"
    difficulty = difficulty_model.predict([text])[0]
    category = model.predict([text])[0]
    created_at = datetime.datetime.now()
    last_updated = datetime.datetime.now()
    due_to = (datetime.datetime.strptime(data['due_to'], '%Y-%m-%d').date() if data.get('due_to') else None)
    try:
        cur.execute(sql, (data['title'], 
                          data["description"], 
                          category, 
                          difficulty, 
                          data['priority'], 
                          data['status'], 
                          created_at, 
                          last_updated, 
                          due_to))
        indx = cur.fetchone()
        return indx

    except DatabaseError as err:
        logging.error(err)
    finally:
        cur.close()




def delete_task(conn, task_id: int): 
    cur = conn.cursor()
    sql = """DELETE FROM tasks WHERE id = %s"""
    try:
        cur.execute(sql, (task_id, ))
    except DatabaseError as err:
        logging.error(err)
    finally:
        cur.close()
        logging.info(f"Task deleted {task_id}")




def add_timer_to_taskdb(conn, task_id: int, started_at: datetime):
    cur = conn.cursor()
    sql = """INSERT INTO task_time_logs (task_id, started_at) VALUES (%s, %s) RETURNING task_id"""
    try:
        cur.execute(sql, (task_id, started_at))
    except DatabaseError as err:
        logging.error(err)
    finally:
        cur.close()
        logging.info(f"Task timer {task_id} added")


def update_timer_to_taskdb(conn, task_id: int, stop_at: datetime):
    cur = conn.cursor()
    sql = """UPDATE task_time_logs SET ended_at = %s, duration_sec = EXTRACT(EPOCH FROM (%s - started_at)) WHERE task_id = %s AND ended_at IS NULL;"""
    try:
        cur.execute(sql, (stop_at, stop_at, task_id))
    except DatabaseError as err:
        logging.error(err)
    finally:
        cur.close()
        logging.info(f"Task timer {task_id} added")

    


def select_active_tasks(conn):
    cur = conn.cursor()
    sql = """SELECT task_id FROM task_time_logs WHERE ended_at IS NULL LIMIT 1"""
    try:
        cur.execute(sql)
        data = cur.fetchone()
        return data
    
    except DatabaseError as err:
        logging.error(err)
    finally:
        cur.close()