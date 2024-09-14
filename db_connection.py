import psycopg2
from dotenv import load_dotenv
import os

# Loading  variables from .env file
load_dotenv()

# getting variables from .env
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

try:
    # Connect to the PostgreSQL server by a context manager
    with psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    ) as conn:
        print("Database connection successful")
        # execute all database actions here if needed
except Exception as e:
    print("Database connection failed:", e)
