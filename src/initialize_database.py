from database_connection import get_data_base_connection
from config import BIBTEX_FILE_PATH


def initialize_database():
    connection = get_data_base_connection()
    drop_tables(connection)
    createtable(connection)
    with open(BIBTEX_FILE_PATH, 'w', encoding='utf-8'):
        pass


def createtable(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE bibtex (citekey TEXT, data TEXT, tag TEXT);
        """)
    connection.commit()


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists bibtex;
    ''')

    connection.commit()


if __name__ == "__main__":
    initialize_database()
