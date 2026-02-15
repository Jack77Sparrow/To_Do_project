
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from services.logger_config import logger
import traceback

from dotenv import load_dotenv
import os
load_dotenv()

postgre_login = os.getenv("POSTGRES_USER")
postgre_password = os.getenv("POSTGRES_PASSWORD")

engine = create_engine(f'postgresql+psycopg2://{postgre_login}:{postgre_password}@db:5432/task_manager')
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()




def db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        logger.error(f"Database operation failed:\n", traceback.format_exc())
        raise
    finally:
        session.close()

