import sqlite3

connection= sqlite3.connect('todo.db')
cursor = connection.cursor()

# sa fac un tabel sau o alta baza de date??????
cursor.execute(
    """CREATE TABLE todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email varchar(32),
        todo_text varchar(100)
    );"""
)


