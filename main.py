
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
        players_insert = handler.parse_players_scraped_data()

        print("nah")
        DB_handler = DB_handler(conf.get_db_auth())
        try:
            DB_handler.connect()
            print("whey")
        except Exception as e:
            print(e)
            raise e


    except Exception as e:
        print("Error is: {}".format(e))