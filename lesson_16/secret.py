import psycopg2
import os
import dotenv
from contextlib import contextmanager
from psycopg2.extras import DictCursor


@contextmanager
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
    )
    try:
        yield conn
    finally:
        conn.close()


with get_db_connection() as conn:
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("SELECT * FROM users.role_list")
        results = cur.fetchall()

print(results)