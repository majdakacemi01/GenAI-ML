# db.py
import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL missing in .env")

def get_conn():
    """
    Return a new psycopg connection. Caller should use context manager.
    """
    return psycopg.connect(DATABASE_URL, autocommit=True, row_factory=dict_row)

def init_db():
    """
    Create the blogs table if it doesn't exist.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS blogs (
      id SERIAL PRIMARY KEY,
      title TEXT NOT NULL,
      content TEXT NOT NULL,
      created_at TIMESTAMP DEFAULT NOW(),
      updated_at TIMESTAMP DEFAULT NOW()
    );
    """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(create_table_sql)
