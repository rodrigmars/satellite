from sqlite3 import Connection, Cursor
from typing import Any


def repository(conn: Connection):

    cursor = conn.cursor()

    def execute(query: str) -> bool:
        status = True

        try:

            cursor.execute(query)

            conn.commit()

        except Exception as ex:
            print("ERRO>>>>>", ex)
            status = False
            conn.rollback()

        finally:

            cursor.close()
            conn.close()

            return status

    def fetch_one(query: str) -> tuple:

        status = True

        try:

            cursor.execute(query)

            data = cursor.fetchone()

        except Exception as ex:

            status = False
            pass

        finally:
            cursor.close()
            conn.close()

            return status, data

    return {"execute": execute, "fetch_one": fetch_one}
