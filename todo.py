""" The selected code is a script for managing a to-do list using a SQLite database """
import sqlite3
from sys import argv


def setup():
    """ The function creates a new database with activities to do.
    Database contains tabel called: id, title of activity and description is done or not"""
    with sqlite3.connect('todo.db') as sql_connection:
        sql = ''' CREATE TABLE todos(
            todo_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title VARCHAR(100) UNIQUE NOT NULL,
            is_done INTEGER DEFAULT 0   
        )'''
        sql_cursor = sql_connection.cursor()
        sql_cursor.execute(sql)
        sql_connection.commit()


if len(argv) == 2 and argv[1] == 'setup':
    setup()


with sqlite3.connect('todo.db') as connection:
    cursor = connection.cursor()
    for todo in cursor.execute('SELECT * FROM todos WHERE is_done=0'):
        print(todo)

    print('''
    Choose operation
    0 - Add new task
    1 - Set task as done
    ''')

    value = input('Which action do you want to perform? ')

    if value == '0':
        title = input('Add task to do: ')
        cursor.execute('INSERT INTO todos(title) VALUES (?)', (title,))
        connection.commit()

    elif value == '1':
        todo_id = input('Enter the ID of the task you have completed:  ')
        cursor.execute('UPDATE todos SET is_done=1 WHERE todo_id=?', todo_id)
        connection.commit()

    else:
        print('You made the wrong choice')
