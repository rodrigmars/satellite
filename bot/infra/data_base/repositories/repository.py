from sqlite3 import Connection


def repository(conn: Connection):

    cursor = conn.cursor()

    def execute(query: str):

        try:

            cursor.execute(query)

            conn.commit()

        except Exception as ex:
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    def get(query: str, conn: Connection):

        try:
            cursor.execute(query)

        except Exception as ex:
            pass

        finally:
            cursor.close()
            conn.close()

    return execute, get
