
from web_info.WebData import ScrapeWebData
from web_info.Config_Reader import Configuration
from DB.DB_Manager import DB_handler

class Mainer():
    def stam(self):
        return


if __name__ == '__main__':
    try:
        conf = Configuration()
        print(conf.data)

        handler = ScrapeWebData(conf)
        handler.get_url_data("https://www.whoscored.com/Teams/63/Show/Spain-{0}".format("Atletico-Madrid"))
        while not handler.extract_players_data():
            handler.get_url_data("https://www.whoscored.com/Teams/63/Show/Spain-{0}".format("Atletico-Madrid"))

        players_data_insert = handler.parse_players_scraped_data()
        for i in (players_data_insert):

            print("players_data_insert name,",i.name)
            print("players_data_insert goals,",i.goals)
            print("players_data_insert assits,",i.assists)
            print("players_data_insert rating,",i.rating)
            print("players_data_insert apps,",i.apps)
            print("\n")

        DB_handler = DB_handler(conf.get_db_auth())
        try:
            DB_handler.connect()
            print("whey")
            for player in players_data_insert:
                DB_handler.insert_db(player)
        except Exception as e:
            print(e)
            raise e


    except Exception as e:
        print("Error is: {}".format(e))