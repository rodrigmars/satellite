from sqlite3 import Connection
from infra.data_base.repositories.repository import repository
from exceptions.custom_errors import RepositoryError


def query_create_tables():
    return """CREATE TABLE IF NOT EXISTS occurrences (
            id INT PRIMARY KEY NOT NULL,
            author TEXT NOT NULL,
            type INT NOT NULL,
            num INT NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NULL
        );"""


def create_tables(conn: Connection) -> None:

    if not repository(conn)["execute"](query_create_tables()):
        raise RepositoryError("Erro ao tentar criar tabela de occurrences")


def check_table_exists(table_name: str, conn: Connection):

    query = f"""SELECT EXISTS (
    SELECT
        name
    FROM
        sqlite_schema
    WHERE
        type='table' AND
        name='{table_name}'
    );"""

    return repository(conn)["fetch_one"](query)
