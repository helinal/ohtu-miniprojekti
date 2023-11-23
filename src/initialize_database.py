from database_connection import get_data_base_connection

def initialize_database():
    connection = get_data_base_connection()
    createtable(connection)

def createtable(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE references (citekey, data);
        """)
    connection.commit()

if __name__ == "__main__":
    initialize_database()