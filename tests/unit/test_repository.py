import pytest
from bot.infra.data_base.db import get_connection
from bot.infra.data_base.repositories.repository import repository
from bot.infra.data_base.repositories.tables_respository import (
    query_create_tables, create_tables, check_table_exists)
from exceptions.custom_errors import RepositoryError


def init_data_base(conn) -> None:

    query = "DROP TABLE IF EXISTS occurrences;"

    query += query_create_tables()

    repository(conn)["execute"](query)


@pytest.fixture
def connection():

    init_data_base(get_connection())

    conn = get_connection()

    create_tables(get_connection())

    yield conn

    conn.close()


def test_create_table_occurrences():

    init_data_base(get_connection())

    result = check_table_exists("occurrences", get_connection())[1][0]

    assert result == 1
