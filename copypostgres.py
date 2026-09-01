import os
import psycopg2
from dotenv import load_dotenv

connection = None
cursor = None

try:
    
    load_dotenv('credentials.env')

    connection=psycopg2.connect(
        host=os.getenv('DB_HOST'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PWD'),
        port=os.getenv('DB_PORT'))
    
    print("Connected success")

    cursor = connection.cursor()
    cursor.execute('select * from students')

    mystudents=cursor.fetchall()
    for column in cursor.description:
        print(column.name, end='\t')
    print()
    column_names = [column[0] for column in cursor.description]
    column_size = len(column_names)
    for student in mystudents:
        for index in range(0,column_size):
            print(student[index], end='\t')
        print()

except psycopg2.Error as e: 
    print("Database error:",e)

finally:
    
    if cursor:
            print("Cursor closed")
            cursor.close()

    if connection:
        print("Connection closed")
        connection.close()

print("Database connection closed.")