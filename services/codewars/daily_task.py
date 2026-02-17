"""this script running by cron everyday in 15:00"""


import datetime
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR))
from random_kata import get_random_kata

from app.db_sqlalchemy.models import User, Task
from services.logger_config import logger
import traceback
from UI.web_interface.WEB_interface import db_session


session = next(db_session())

def create_task_codewars(user_id: int = 1):
    """
    Everyday adding random codewars kata to table 'tasks'
    """
    try:
        user = session.get(User, user_id)
        
        users = session.query(User).all()
        print(users)

        # evaluating date for task add 1 day
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        # get kata info 
        kat_data = get_random_kata()

        # check if task already exist
        exist = session.query(Task).filter(Task.user_id == user.id, Task.source == 'codewars', Task.due_to == tomorrow).first()

        # if task not exist adding it to db
        if not exist:
            new_task = Task(title=kat_data.get("title"),
                            description=kat_data.get("link"),
                            priority='medium',
                            status='pending',
                            difficulty=kat_data.get("difficulty"),
                            category='study',
                            due_to=tomorrow,
                            source='codewars',
                            created_at=datetime.datetime.now(),
                            last_updated=datetime.datetime.now(),
                            user_id=user.id)
            session.add(new_task)
            session.commit()
            logger.info(f"Task succesfully created!")

        else:
            logger.error(f"Task for today already exist")
    except Exception as e:
        logger.error(f"Exception occured:\n", traceback.format_exc())
        session.rollback()
    finally:
        # close session
        session.close()

if __name__ == "__main__":
    create_task_codewars()
    logger.info(f"CRON RUN: {datetime.datetime.now()}")
        