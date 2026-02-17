# Run by cron every day at 00:00

import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from UI.web_interface.WEB_interface import db_session
from app.db_sqlalchemy.models import Task, TaskTimeLogs
from sqlalchemy import update, select
from datetime import date, datetime
from sqlalchemy.orm import Session

def mark_overdue(session: Session = next(db_session())):
    """marks overdue for tasks"""
    now = date.today()
    stmt = update(Task).where(
        (~Task.status.in_(['done', 'overdue'])) &
        (Task.is_archived == False) &
        (Task.due_to < now)
    ).values(status='overdue', is_archived=True)
    subquery = select(Task.id).where(
        (~Task.status.in_(["done", "overdue"])) &
        (Task.is_archived == False) &
        (Task.due_to < now)
    ).subquery()

    stmt2 = (
        update(TaskTimeLogs)
        .where(
            (TaskTimeLogs.task_id.in_(select(subquery))) &
            (TaskTimeLogs.started_at != None) &
            (TaskTimeLogs.ended_at == None) 
        )
        .values(ended_at=datetime.now())
    )
    session.execute(stmt2)
    session.execute(stmt)

    session.commit()
    print("Overdue tasks complete")

if __name__ == "__main__":
    mark_overdue()

