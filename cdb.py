import sqlite3
import datetime
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(32),
        password VARCHAR(32),
        date_created DATETIME
    );"""
)
today = datetime.date.today()
cursor.execute(
    """INSERT INTO users(
        email,
        password,
        date_created
    )VALUES(
        'admin',
        'admin',
        '{today}'
    );"""
)

connection.commit()
cursor.close()
connection.close()