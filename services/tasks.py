from app.db_sql.connect import create_connection
from repository.tasks import (select_today_tasks, 
                              select_all_tasks, 
                              select_task_by_id, 
                              update_task, 
                              add_task_to_db, 
                              delete_task, 
                              add_timer_to_taskdb, 
                              update_timer_to_taskdb, 
                              select_active_tasks, 
                              select_user_data,
                              update_streak
                              )
from datetime import datetime




def get_all_tasks_service(status, 
                          priority, 
                          difficulty,
                          sort_by,
                          order,
                          is_archived):
    return select_all_tasks(status, priority, difficulty, sort_by, order, is_archived)



def get_today_tasks_service():
    return select_today_tasks()
    

def get_task_by_id(task_id: int):
    return select_task_by_id(task_id)
    

def update_task_service(task_id: int, update_data):
    clean_data = update_data.model_dump(exclude_none=True)
    
    if not clean_data:
        return False

    updated = update_task(task_id, clean_data)
    return updated


def add_task_to_database(data: dict):
    return add_task_to_db(data)


def delete_task_from_db(task_id: int):
    return delete_task(task_id)
    

def add_task_timer_services(task_id: int):
    started_at = datetime.now()
    return add_timer_to_taskdb(task_id, started_at)



def update_task_timer_services(task_id: int):
    stop_at = datetime.now()
    return update_timer_to_taskdb(task_id, stop_at)



def select_active_tasks_services():
    return select_active_tasks()


def select_user_data_services():
    user_data = select_user_data()
    dict_data = {
        "id": user_data.id,
        "username": user_data.username,
        "email":user_data.email,
        "created_at":datetime.strftime(user_data.created_at, "%Y %b, %d"),
        "codewars_username":user_data.codewars_username,
        "total_tasks":user_data.total_tasks,
        "done_tasks":user_data.done_tasks
    }

    return dict_data


def update_streak_services(user_id: int = 1):
    return update_streak(user_id=user_id)