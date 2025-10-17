"""This python script creates a database in the MySQL server"""

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

config = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("database"),
        "port": os.getenv("DB_PORT")
        }

try:
    # Connect to the server first
    with mysql.connector.connect(**config) as connection:
        print("Connected to MySQL server!")

        with open("alx_book_store.sql", "r") as file:
            sql_script = file.read()

        with connection.cursor() as cursor:
            for statement in sql_script.split(";"):
                ln = statement.strip()
                if ln:
                    cursor.execute(ln)
            connection.commit()

        print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print("An error occurred: ", e)
