import sqlite3
from utils import get_path_file


def get_connection():
    return sqlite3.connect(get_path_file("satellite.db"))
