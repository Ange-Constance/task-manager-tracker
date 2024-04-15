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

