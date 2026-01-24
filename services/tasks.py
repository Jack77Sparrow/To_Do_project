from db_sql.connect import create_connection
from repository.tasks import select_today_tasks, select_all_tasks, select_task_by_id, update_task, add_task_to_db, delete_task, add_timer_to_taskdb, update_timer_to_taskdb, select_active_tasks
from datetime import datetime


def with_connection(func):
    def wrapper(*args, **kwargs):
        with create_connection() as conn:
            return func(conn, *args, **kwargs)
    
    return wrapper


@with_connection
def get_all_tasks_service(conn, status, 
                          priority, 
                          difficulty):
    return select_all_tasks(conn, status, priority, difficulty)


@with_connection
def get_today_tasks_service(conn):
    return select_today_tasks(conn)
    
@with_connection
def get_task_by_id(conn, task_id: int):
    return select_task_by_id(conn, task_id)
    
@with_connection
def update_task_service(conn, task_id: int, update_data):
    clean_data = update_data.model_dump(exclude_none=True)
    
    if not clean_data:
        return False

    updated = update_task(conn, task_id, clean_data)
    return updated

@with_connection 
def add_task_to_database(conn, data: dict):
    return add_task_to_db(conn, data)


@with_connection
def delete_task_from_db(conn, task_id: int):
    return delete_task(conn, task_id)
    
@with_connection
def add_task_timer_services(conn, task_id: int):
    started_at = datetime.now()
    return add_timer_to_taskdb(conn, task_id, started_at)


@with_connection
def update_task_timer_services(conn, task_id: int):
    stop_at = datetime.now()
    return update_timer_to_taskdb(conn, task_id, stop_at)


@with_connection
def select_active_tasks_services(conn):
    return select_active_tasks(conn)