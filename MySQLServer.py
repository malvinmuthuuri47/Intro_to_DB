"""This python script creates a database in the MySQL server"""

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

config = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "port": os.getenv("DB_PORT")
        }

try:
    # Connect to the server first
    with mysql.connector.connect(**config) as connection:
        print("Connected to MySQL server!")

        create_db_query = """
            CREATE DATABASE IF NOT EXISTS alx_book_store
        """
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            connection.commit()

        print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print("An error occurred: ", e)
