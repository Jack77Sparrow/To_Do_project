
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
from app.db_sqlalchemy.connect import db_session



def get_all_tasks_service(db,
                          status, 
                          priority, 
                          difficulty,
                          sort_by,
                          order,
                          is_archived):
    return select_all_tasks(session=db, 
                            status=status, 
                            priority=priority,
                            difficulty=difficulty, 
                            sort_by=sort_by, 
                            order=order, 
                            is_arvhived=is_archived)



def get_today_tasks_service(db):
    return select_today_tasks(db)
    

def get_task_by_id(db, task_id: int):
    return select_task_by_id(db, task_id)
    

def update_task_service(db, task_id: int, update_data):
    clean_data = update_data.model_dump(exclude_none=True)
    
    if not clean_data:
        return False

    updated = update_task(db, task_id, clean_data)
    return updated


def add_task_to_database(db, data: dict):
    return add_task_to_db(db, data)


def delete_task_from_db(db, task_id: int):
    return delete_task(db, task_id)
    

def add_task_timer_services(db, task_id: int):
    started_at = datetime.now()
    return add_timer_to_taskdb(db, task_id, started_at)



def update_task_timer_services(db, task_id: int):
    stop_at = datetime.now()
    return update_timer_to_taskdb(db, task_id, stop_at)



def select_active_tasks_services(db):
    return select_active_tasks(db)


def select_user_data_services(db):
    user_data = select_user_data(db)
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
    return update_streak(next(db_session()), user_id=user_id)