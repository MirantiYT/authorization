import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()

class DB:
    db = None
    def __del__(self):
        if self.db: self.db.close()

    def __init__(self):
        database = os.getenv("database")
        host = os.getenv("host")
        user = os.getenv("user")
        password = os.getenv("password")
        try:
            self.db = mysql.connector.connect(
                database = database,
                host = host,
                user = user,
                password = password,
                buffered = True
            )
        except mysql.connector.Error as err:
            print(err)

    def execute(self, sql: str, params: tuple = ()):
        if self.db:
            try:
                with self.db.cursor() as cursor:
                    cursor.execute(sql, params)
                    self.db.commit()
                    return cursor
            except Exception as e:
                print(e)

DB().execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(100) NOT NULL,
    login VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL
)
""")