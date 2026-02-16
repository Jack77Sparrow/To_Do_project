from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, String, Column, Text, Boolean, ForeignKey, UniqueConstraint, text
from sqlalchemy.types import DateTime, Date
from sqlalchemy.sql import func
from pathlib import Path

import sys
ROOT_DIR = Path(__file__).resolve().parents[0]
sys.path.insert(0, str(ROOT_DIR))
print(ROOT_DIR)
from connect import Base







class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(60), nullable=False, unique=True)
    email = Column(String(50), unique=True)
    created_at = Column(DateTime, server_default=func.now())
    tasks = relationship("Task", back_populates="user")
    codewars_username = Column(String, unique=True)
    codewars_last_completed = Column(DateTime(timezone=True), nullable=True)
    last_activity_date = Column(Date)
    current_streak = Column(Integer, nullable=False, server_default=text('0'))
    longest_streak = Column(Integer, nullable=False, server_default=text('0'))
    codewars_completed = relationship(
        "CodewarsCompleted",
        back_populates="user",
        cascade="all, delete-orphan",
    )



class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    description = Column(Text, server_default='')
    category = Column(String(20))
    difficulty = Column(String(20))
    priority = Column(String(20))
    status = Column(String(20), nullable=False)
    source = Column(String(20), nullable=False, server_default="user")
    is_archived = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    last_updated = Column(DateTime, server_default=func.now())

    time_logs = relationship("TaskTimeLogs", back_populates="task")
    
    due_to = Column(Date)
    is_deleted = Column(Boolean, default=False, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship("User", back_populates="tasks")



class TaskTimeLogs(Base):
    __tablename__ = "task_time_logs"
    id = Column(Integer, primary_key=True)

    task_id = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    task = relationship(Task, back_populates="time_logs")

    started_at = Column(DateTime, nullable=False)
    ended_at = Column(DateTime)
    duration_sec = Column(Integer)



class CodewarsCompleted(Base):
    __tablename__ = "codewars_completed"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String)
    slug = Column(String)
    completed_at = Column(DateTime(timezone=True), nullable=False)
    code_wars_task_id = Column(String, nullable=False)
    user = relationship("User", back_populates="codewars_completed")
    __table_args__ = (
        UniqueConstraint("user_id", "code_wars_task_id", name="uq_user_codewars_kata"),
    )

