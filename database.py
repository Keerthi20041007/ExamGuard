#in database.py we write the code related to python and sqlite connection
import sqlite3

DB = "database/examguard.db"


def get_db():
    connection = sqlite3.connect(DB, timeout=30)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS candidates(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
            """
        )
        connection.commit()