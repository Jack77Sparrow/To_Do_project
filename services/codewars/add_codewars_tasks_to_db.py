"""this code runnign by cron every 10 minutes"""



import requests
import pprint
from pathlib import Path
import sys
ROOT_PATH = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_PATH))
print(ROOT_PATH)
from app.db_sqlalchemy.models import CodewarsCompleted, User, Task, TaskTimeLogs
from app.db_sqlalchemy.connect import db_session
from dateutil.parser import isoparse
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import update, func
import traceback

from services.logger_config import logger

from services.tasks import update_streak_services




session = next(db_session())


def save_completed_task_to_db(user_id: int):
    """
    check and update last completed for user
    
    :param user_id: int - user id 
    """
    try:
        # get user from db
        query = session.query(User).where(User.id == user_id).first()
        # initializing variable with user last_completed kata time
        last_completed = query.codewars_last_completed
        if isinstance(last_completed, str):
            last_completed = isoparse(last_completed)
        newest_completed_at = last_completed
        page = 0
        if query.codewars_username is not None:
            url = f'https://www.codewars.com/api/v1/users/{query.codewars_username}/code-challenges/completed?page={page}'
        else:
            logger.info(f"{query.username} is`t have a codewars_username")
        while True:

            request = requests.get(url)

            request.raise_for_status()
            playload = request.json()
            

            for kata in playload['data']:
                completed_at = isoparse(kata["completedAt"])
                # if user last_completed greater than kata completed_at do nothinng
                if last_completed and completed_at <= last_completed:
                    continue
                
                stmt = (insert(CodewarsCompleted).values(user_id=1,
                                                title=kata.get("name"), 
                                                slug=kata.get("slug"), 
                                                completed_at=isoparse(kata.get("completedAt")), 
                                                code_wars_task_id=kata.get("id"),).on_conflict_do_nothing(
                        index_elements=["user_id", "code_wars_task_id"]
                    ))
                    
                session.execute(stmt)
                # if kata completed_at greater than user last_completed reassign last_completed for user by completed_at
                if not newest_completed_at or completed_at > newest_completed_at:
                    newest_completed_at = completed_at


            page+=1
            if page >= playload['totalPages']:
                break

        # updating user last_completed 
        if newest_completed_at:
            query.codewars_last_completed = newest_completed_at
            if last_completed != newest_completed_at:
                update_streak_services(user_id)
                logger.info(f"Update codewars_last_completed for {query.codewars_username}")
            else:
                logger.info(f"Nowthing new")
        
        session.commit()

    except Exception:
        logger.error(f"Exception occured:\n", traceback.format_exc())
        session.rollback()
    finally:
        session.close()

def check_codewars_task_complete(user_id: int):
    """
    Update all pending codewars tasks for user to 'done'
    if they are in the CodewarsCompleted table
    """

    try:
        codewars_completed_tasks = session.query(CodewarsCompleted.title).where(CodewarsCompleted.user_id == user_id).all()

        completed_tasks = {tasks for (tasks, ) in codewars_completed_tasks}
        print(completed_tasks)

        stmt = update(Task).where(Task.user_id == user_id, 
                                Task.status == 'pending', 
                                Task.source == 'codewars', 
                                Task.is_deleted == False, 
                                Task.title.in_(completed_tasks)).values(status='done')
        session.execute(stmt)

        stmt2 = update(TaskTimeLogs).where(TaskTimeLogs.task_id == Task.id, 
                                        TaskTimeLogs.ended_at == None,
                                        Task.title.in_(completed_tasks), 
                                        Task.source == 'codewars').values(ended_at=func.now(), 
                                                                            duration_sec=func.extract('epoch', 
                                                                                                    func.now() -  TaskTimeLogs.started_at))
        session.execute(stmt2)
        
        session.commit()
    except Exception:
        logger.error(f"Exception occured:\n", traceback.format_exc())
        session.rollback()
    finally:
        session.close()
    
if __name__ == "__main__":
    pprint.pprint(save_completed_task_to_db(1))
    check_codewars_task_complete(1)
    print("Update codewars completed table", flush=True)