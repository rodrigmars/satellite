from sqlite3 import Connection
from repositories.repository import repository
from models.ocurrences import Occurrence


def add(data: Occurrence, conn: Connection) -> None:

    query = f"""INSERT INTO occurrences(author, type_occurrence, numm, created_at)
    VALUES ({data.author}, {data.type_occurrence}, {data.total}, datetime('now', 'localtime'));"""

    repository(conn)["execute"](query)


def edit(data: Occurrence, conn: Connection) -> None:

    query = f"""UPDATE occurrences SET total = {data.total + 1}, updated_at = datetime('now', 'localtime')
    WHERE author = {data.author} AND type = {data.type_occurrence};"""

    repository(conn)["get"](query)
