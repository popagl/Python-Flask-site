import sqlite3

def check_pw(email):
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor= connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE email='{email}' ORDER BY id DESC;""".format(email = email))
    password = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()

    return password

def signup(email, password):
    connection = sqlite3.connect('users.db', check_same_thread= False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE email = '{email}';""")#.format(email = email, password=password))
    exist = cursor.fetchall()
    if exist is None:
        cursor.execute(
            """ INSERT INTO users(
                email,
                password
            )VALUES(
                '{email}',
                '{password}'
            );""".format(email= email, password = password)
        )
    else: return ('User already Registered!')

    connection.commit()
    cursor.close()
    connection.close()

    return 'Succesfuly Signed Up!'

def check_users():
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT email FROM users ORDER BY id DESC;""")
    db_users = cursor.fetchall()
    users = []
    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()
    return users


def add_todo(email, todo_text):
    connection = sqlite3.connect('todo.db')#, check_same_thread=False)
    cursor = connection.cursor()
    #here i left the project!!!
    cursor.execute("""SELECT * FROM todo WHERE email='{email}';""")#.format(email= email, todo=todo_text))
    todos = cursor.fetchall()

    if email in todos:
        return 'Todo Already exists!'
    else:
        db_todo=cursor.execute(
            """INSERT INTO todo(
                    email,
                    todo_text
            )VALUES(
                   '{email}',
                   '{todo}'
            );"""
        )
        db_todo.append(todos)

    connection.commit()
    cursor.close()
    connection.close()
    return db_todo

def usr_total():
    connection = sqlite3.connect('users.db', check_same_thread= False)
    cursor = connection.cursor()
    cursor.execute(
        """ SELECT COUNT(*) FROM users;"""
    )
    total= cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    message = 'There are {{total}} users in database'.format(total = total)
    return total

def DelUsr(email):
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """ SELECT * FROM users WHERE email = '{email}';"""
    )
    x= cursor.fetchone()[0]
    cursor.execute(
        """ DELETE FROM users WHERE email = '{x}';"""
    )

    return 'User deleted!'


