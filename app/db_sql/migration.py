from psycopg2 import DatabaseError
import datetime 
import json
import re
import logging

from connect import create_connection

sql_insert_default = """
    INSERT INTO tasks (
    title, description, category, difficulty,
    priority, status, last_updated, due_to
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """


sql_insert_with_created = """
    INSERT INTO tasks (
    title, description, category, difficulty,
    priority, status, created_at, last_updated, due_to
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

def validate_time(value):
    if not value:
        return None
    
    validate = None

    if value == 'now':
        return datetime.datetime.now()

    if re.match(r"\d\d/\d\d/\d{4} \d\d:\d\d", value):
        validate = datetime.datetime.strptime(value, "%d/%m/%Y %H:%M")
    elif re.match(r"\d{4}-\d\d-\d\d", value):
        validate = datetime.datetime.strptime(value, "%Y-%m-%d").date()

    return validate



def migrate_data(conn, filename='data/data.json'):
    with open(filename, 'r') as file:
        tasks = json.load(file)
        try:
            cur = conn.cursor()
            for task in tasks:
                created_at = validate_time(task.get('created_at'))
                if not created_at:
                    cur.execute(sql_insert_default, 
                                (
                                    task.get('title'),
                                    task.get('description'),
                                    task.get('category'),
                                    task.get('difficulty'),
                                    task.get('priority'),
                                    task.get('status'),
                                    validate_time(task.get('last_updated', None)),
                                    validate_time(task.get('due_to', None))
                                )
                                )
                else:
                    cur.execute(sql_insert_with_created, 
                                (
                                    task.get('title'),
                                    task.get('description'),
                                    task.get('category'),
                                    task.get('difficulty'),
                                    task.get('priority'),
                                    task.get('status'),
                                    created_at,
                                    validate_time(task.get('last_updated', None)),
                                    validate_time(task.get('due_to', None))
                                )
                                )

                
            conn.commit()
                
        except DatabaseError as err:
            logging.error(err)
        finally:
            cur.close()


if __name__ == "__main__":
    

    try:
        with create_connection() as conn:
            if conn is not None:
                migrate_data(conn)
            else:
                logging.error("can't create a database connection!")

    except RuntimeError as err:
        logging.error(err)

