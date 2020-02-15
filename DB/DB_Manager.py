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

    def insert_db(self,player_info,team_name):
        try:
            print(player_info.name)

            sql_query= "INSERT INTO players_data select ({},{},{},{},{},{},{})" \
                       " where NOT EXISTS (SELECT * FROM players_data WHERE name like '{}')".format(
                                        "'"+(player_info.name.replace("'","`"))+"'" if "'" in player_info.name else "'"+player_info.name+"'",
                                        "'"+team_name+"'",
                                        "'postion b'",
                                        0 if player_info.goals=="-" else player_info.goals,
                                        0 if player_info.assists=="-" else player_info.assists,
                                        0 if player_info.apps=="-" else player_info.apps,
                                        player_info.rating,
                                        (player_info.name.replace("'","`")) if "'" in player_info.name else player_info.name)
            print(sql_query)
            self.cursor.execute(sql_query)
            self.DBManager.commit()
        except Exception as e:
            print("Error in inserting data to DB")
            raise(e)