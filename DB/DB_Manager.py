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

    def insert_db(self,player_info):
        print(type(player_info.name))
        sql_query= "INSERT INTO players_data VALUES ({},{},{},{},{},{},{})".format(
                                    "'"+player_info.name+"'",
                                    "'team a'",
                                    "'postion b'",
                                    "'"+player_info.goals+ "'",
                                    "'"+player_info.assists+ "'",
                                    "'"+player_info.apps+ "'",
                                    "'"+player_info.rating+ "'")
        print("sql_query-",sql_query)
        self.cursor.execute(sql_query)
        self.DBManager.commit()