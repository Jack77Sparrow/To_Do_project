
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))


import datetime
from app.model.my_models import model, difficulty_model
from app.db_sqlalchemy.models import Task, TaskTimeLogs, User
from sqlalchemy import update, func, desc, case, select
from sqlalchemy.exc import NoResultFound
from services.logger_config import logger


ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))





def select_all_tasks(session, status, priority, difficulty, sort_by, order, is_arvhived):
    
    query = session.query(Task)

    if status is not None:
        query = query.filter(Task.status == status)

    if priority is not None:
        query = query.filter(Task.priority == priority)

    if difficulty is not None:
        query = query.filter(Task.difficulty == difficulty)

    if is_arvhived is not None:
        query = query.filter(Task.is_archived == is_arvhived)

    if sort_by is not None:
        if sort_by == "created_at":
            if order == "asc":
                query = query.order_by(Task.created_at)
            else:
                query = query.order_by(desc(Task.created_at))

        if sort_by == "updated_at":
            if order == "asc":
                query = query.order_by(Task.last_updated)
            else:
                query = query.order_by(desc(Task.last_updated))
    
    
    return query.filter(Task.is_deleted == False).all()


    

def select_today_tasks(session):
    query = session.query(Task).where(Task.due_to == datetime.date.today(), Task.is_deleted == False)
    return query.all()


def select_task_by_id(session, task_id: int):
    query = session.query(Task).where(Task.id == task_id, Task.is_deleted == False)
    return query.scalar()

    

def update_task(session, task_id: int, data: dict):
    try:
        task = session.get(Task, task_id)


        if not task:
            raise ValueError(f"Task {task_id} not found")

        
        if data.get('due_to') is not None:  
            task.due_to = data.get("due_to") or None
        
        if data.get('priority') is not None:
            task.priority = data.get("priority")
        
        if data.get('status') is not None:
            task.status = data.get("status")
        
        if data.get('description') is not None:
            task.description = data.get("description")


        task.last_updated = datetime.datetime.now()
        logger.info(f"Task {task.title} succesfully updated")
        session.commit()

        return task
    except Exception:
        logger.error(f"Exception occured:\n", exc_info=True)
    
    



def add_task_to_db(session, data: dict):
    
    try:
        text = f"{data['title']} {data['description']}"
        difficulty = difficulty_model.predict([text])[0]
        category = model.predict([text])[0]
        created_at = datetime.datetime.now()
        last_updated = datetime.datetime.now()
        due_to = (datetime.datetime.strptime(data['due_to'], '%Y-%m-%d').date() if data.get('due_to') else None)

        
        insert_data = Task(title=data.get("title"), 
                                        description=data.get("description"), 
                                        category=category, 
                                        difficulty=difficulty, 
                                        priority=data.get("priority"),
                                        status=data.get("status"),
                                        created_at=created_at,
                                        last_updated=last_updated,
                                        due_to=due_to)
        session.add(insert_data)
        session.commit()
        logger.info(f"Task {data.get("title")} successfully added to db")
        return insert_data
    except Exception:
        logger.error(f"Exception occured:\n", exc_info=True)
        return

        


def delete_task(session, task_id: int): 
    task = session.get(Task, task_id)

    if not task:
        raise ValueError(f"Task {task_id} not found")
    
    task.is_deleted = True

    session.commit()
    logger.info(f"Task {task.title} succesfullty deleted")
    return task_id


def add_timer_to_taskdb(session, task_id: int, started_at: datetime):
    try:
        task_status = session.get(Task, task_id)

        if task_status.status == 'done':
            logger.info(f"Task {task_id} already done")
        else:
            select_active_task = select(TaskTimeLogs.task_id).where(TaskTimeLogs.task_id == task_id).where(TaskTimeLogs.ended_at == None)
            active_tasks = session.execute(select_active_task).all()
            task_timer = TaskTimeLogs(task_id=task_id, started_at=started_at)
            if (task_id, ) in active_tasks:
                print("you cant do this")
            else:
                session.add(task_timer)
                session.commit()
                logger.info(f"Timer for task-{task_id} started_at-{started_at} added succesfully")
            
    except Exception:
        logger.error(f"Exception occured:\n", exc_info=True)

    


def update_timer_to_taskdb(session, task_id: int, stop_at: datetime):
    try:
        sql = update(TaskTimeLogs).where(TaskTimeLogs.task_id == task_id).values(ended_at=stop_at, duration_sec=func.extract('epoch', stop_at-  TaskTimeLogs.started_at))
        session.execute(sql)
        session.commit()
        logger.info(f"Timer for task-{task_id} endet_at-{stop_at} stoped succesfully")
    except Exception:
        logger.error(f"Exception occured:\n", exc_info=True)


def select_active_tasks(session):
    try:
        query = session.query(TaskTimeLogs).where(TaskTimeLogs.ended_at == None).one()
        return query
    except NoResultFound:
        logger.error(f"Exception occured:\n", exc_info=True)
        return None



def select_user_data(session):

    try:
        query = session.query(User.id, User.username, User.email, User.created_at, User.codewars_username, func.count(Task.id).label("total_tasks"), func.count(case((Task.status == "done", 1))
        ).label("done_tasks"),).outerjoin(Task, Task.user_id == User.id).group_by(User.id).one()
        return query
    except NoResultFound as err:
        logger.error(f"Exception occured:\n", exc_info=True)
        return None
    

def update_streak(session, user_id:int):

    
    today = datetime.date.today()
    query = session.query(User).where(User.id == user_id).first()
    today = datetime.date(year=2026, month=2, day=18)
    print(query.current_streak)
    try:
        if query.last_activity_date == today:
            return 
    
        elif query.last_activity_date == today - datetime.timedelta(days=1):
            logger.info(f"streak for USER - {user_id} increase by 1")
            query.current_streak += 1

        else:
            logger.info(f"streak for USER - {user_id} equal 0")
            query.current_streak = 0
    except Exception as e:
        logger.error(f"Exception occured:\n", exc_info=True)
    
    query.last_activity_date = today
    query.longest_streak = max(query.longest_streak, query.current_streak)
    session.commit()
        