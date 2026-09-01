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

except psycopg2.Error as e:
    print("Database error: ",e)

finally:
    if connection:
        print("Connection closed")
        connection.close()

    print("Database connection closed.")