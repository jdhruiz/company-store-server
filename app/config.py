import os

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "storedb")
DB_USER = os.getenv("POSTGRES_USER", "storeuser")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "storepass")
