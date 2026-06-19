import psycopg2
from contextlib import contextmanager
from psycopg2.extras import DictCursor
from lesson_16 import creds


@contextmanager
def get_db_connection():
    conn = psycopg2.connect(
        dbname=creds.dbname,
        user=creds.user,
        password=creds.password,
        host=creds.host,
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