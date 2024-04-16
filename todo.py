import psycopg2
from psycopg2 import OperationalError

# Function to connect to ElephantSQL database
def connect():
    try:
        conn = psycopg2.connect(
            dbname='wwveekuf',
            user='wwveekuf',
            password='rrfygom2f9eJ2I-eXCZXSWXcrX8mJdd1',
            host='salt.db.elephantsql.com',
            port='5432'
        )
        print("Connected to ElephantSQL database")
        return conn
    except OperationalError as e:
        print(e)

# Function to create the 'todos' table if it doesn't exist
def create_table(conn):
    try:
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS todos (
                    id SERIAL PRIMARY KEY,
                    task VARCHAR(255) NOT NULL,
                    description TEXT,
                    completed BOOLEAN NOT NULL DEFAULT FALSE
                )"""
        cursor.execute(sql)
        conn.commit()
        print("Table 'todos' created successfully")
    except psycopg2.Error as e:
        print(e)

# Function to add a new to-do item
def add_todo(conn, task, description=None):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO todos (task,description) VALUES (%s,%s)"
        cursor.execute(sql, (task,description))
        conn.commit()
        print("Task added successfully")
    except psycopg2.Error as e:
        print(e)

# Function to display all to-do items
def show_todos(conn):
    try:
        cursor = conn.cursor()
        sql = "SELECT id, task, description, completed FROM todos"
        cursor.execute(sql)
        todos = cursor.fetchall()
        if todos:
            print("Your To-Do List:")
            for todo in todos:
                task_status = "Completed" if todo[3] else "Not Completed"
                print(f"{todo[0]}. {todo[1]} - {todo[2]} ({task_status})")
        else:
            print("No to-do items found")
    except psycopg2.Error as e:
        print(e)

# # Function to mark a to-do item as completed
# def complete_todo(conn, todo_id):
#     try:
#         cursor = conn.cursor()
#         sql = "UPDATE todos SET completed = TRUE WHERE id = %s"
#         cursor.execute(sql, (todo_id,))
#         conn.commit()
#         print("Task marked as completed")
#     except psycopg2.Error as e:
#         print(e)

# Function to edit a to-do item
def edit_todo(conn, todo_id, new_task, new_description=None):
    try:
        cursor = conn.cursor()
        sql = "UPDATE todos SET task = %s, description = %s WHERE id = %s"
        cursor.execute(sql, (new_task, new_description, todo_id))
        conn.commit()
        print("Task updated successfully")
    except psycopg2.Error as e:
        print(e)

# Function to delete a to-do item
def delete_todo(conn, todo_id):
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM todos WHERE id = %s"
        cursor.execute(sql, (todo_id,))
        conn.commit()
        print("Task deleted successfully")
    except psycopg2.Error as e:
        print(e)