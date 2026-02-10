import psycopg2
from contextlib import contextmanager
from dotenv import load_dotenv
import os 
import logging

load_dotenv()

password = os.getenv('db_password')
@contextmanager
def create_connection():
    try:
        conn = psycopg2.connect(host="localhost", database='task_manager', user="postgres", password=password)
        yield conn 
        conn.commit()
    except psycopg2.OperationalError as err:
        if conn:
            conn.rollback()
        logging.error(err)
        raise
    finally:
        conn.close()



