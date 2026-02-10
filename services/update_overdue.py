import sys
import os

# додаємо корінь проєкту до sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from app.db_sqlalchemy.models import session, Task
from sqlalchemy import update
from datetime import date

def mark_overdue():
    now = date.today()
    stmt = update(Task).where(
        (~Task.status.in_(['done', 'overdue'])) &
        (Task.is_archived == False) &
        (Task.due_to < now)
    ).values(status='overdue', is_archived=True)
    print(stmt)
    session.execute(stmt)
    session.commit()
    print("Overdue tasks complete")

if __name__ == "__main__":
    mark_overdue()

