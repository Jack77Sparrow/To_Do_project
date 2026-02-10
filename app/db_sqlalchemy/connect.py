
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
from services.logger_config import logger
import traceback


engine = create_engine('postgresql+psycopg2://postgres:Max.Brawl2001@localhost:5432/task_manager')
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


session = SessionLocal()


@contextmanager
def db_session():
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        logger.error(f"Database operation failed:\n", traceback.format_exc())
        raise
    finally:
        session.close()

