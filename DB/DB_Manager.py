import mysql.connector
import psycopg2
#
# mycursor = mydb.cursor()
# #
# # mycursor.execute("CREATE DATABASE mydatabase")
# #

class DB_handler:
    def __init__(self,auth):
        print(auth)
        self.host = auth['Host']
        self.user = auth['User']
        self.password = auth['Password']
        self.database = auth['Database']
        self.DBManager = None
        self.cursor = None

    def connect(self):
        self.DBManager = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.DBManager.cursor()

    def insert_db(self,players):
        self.cursor.executemany("""
            INSERT INTO %s (name, gender)
            VALUES (%(name)s, %(gender)s)""", self.database, players)
        self.cursor.commit()