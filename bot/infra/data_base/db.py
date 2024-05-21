import sqlite3


def get_connection(db_file):
    return sqlite3.connect(db_file)


def init_db(conn: sqlite3.Connection):

    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS occurrences (
            id INT PRIMARY KEY NOT NULL,
            author TEXT NOT NULL,
            type INT NOT NULL,
            num INT NOT NULL
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NULL,
        )""")

    cursor.close()

    conn.close()
