from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Integer, String, Column, Text
from sqlalchemy.types import DateTime, Date
from sqlalchemy.sql import func




engine = create_engine('postgresql+psycopg2://postgres:Max.Brawl2001@localhost:5432/task_manager')
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


session = SessionLocal()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    description = Column(Text)
    category = Column(String(20))
    difficulty = Column(String(20))
    priority = Column(String(20))
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    last_updated = Column(DateTime)
    due_to = Column(Date)
