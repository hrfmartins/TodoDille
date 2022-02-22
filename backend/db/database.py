import os
import mysql.connector
from mysql.connector import errorcode


class Database:
    def __init__(self):
        if os.environ.get('ENV'):
            self.user = os.environ.get('DB_USER')
            self.password = os.environ.get('DB_PASSWORD')
            self.host = os.environ.get('DB_HOST')
            self.database = os.environ.get('DB_NAME')
            self.raise_on_warnings = True

        else:
            self.user = "user"
            self.password = "password"
            self.host = "localhost"
            self.database = "db"
            self.raise_on_warnings = True

        self.connection = None
        self.cursor = None

    def get_config(self):
        return {
            'user': self.user,
            'password': self.password,
            'host': self.host,
            'database': self.database,
            'raise_on_warnings': self.raise_on_warnings,
        }

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.get_config())
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access Error")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Non Existent DB")
            else:
                print(err)
        self.cursor = self.connection.cursor(dictionary=True)

    def execute(self, query, values):
        self.connect()
        self.cursor.execute(query, values)
        self.cursor.nextset()
        self.connection.commit()

    def get_result(self, query, variables=None):
        self.connect()
        if variables is None:
            variables = []
        self.cursor.execute(query, variables)
        self.cursor.nextset()
        return self.cursor.fetchall()

