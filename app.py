
from utils.Config_Reader import Configuration
from web_info.WebData import ScrapeWebData
from DB.DB_Manager import DB_handler


def conf_reader():
    conf = Configuration()
    print(conf.data)
    return conf

def get_web_handler(conf):
    handler = ScrapeWebData(conf)
    return handler

def close_connection(handler):
    handler.close_con()

def iterate_teams(conf,handler):
    for team in conf.get_spain_teams():
        print(team)
        handler.get_url_data(team["url"])
        while not handler.extract_players_data():
            handler.get_url_data(team["url"])
        DB_manager= db_connect(conf)
        parse_players_data(handler,DB_manager,team["team_name"])

    for team in conf.get_italy_teams():
        print(team)
        handler.get_url_data(team["url"])
        while not handler.extract_players_data():
            handler.get_url_data(team["url"])
        DB_manager = db_connect(conf)
        parse_players_data(handler, DB_manager, team["team_name"])


def parse_players_data(handler,DB_manager,team_name):
    try:

        players_data_insert = handler.parse_players_scraped_data()
        for player in (players_data_insert):
            DB_manager.insert_db(player,team_name)
    except Exception as e:
        print("Error in scraping {}".format(e))
        raise e

def db_connect(conf):
    DB_manager = DB_handler(conf.get_db_auth())
    try:
        DB_manager.connect()
        return DB_manager
    except Exception as e:
        print(e)
        raise e


if __name__ == '__main__':
    config = conf_reader()
    handler = get_web_handler(config)
    iterate_teams(config,handler)
    close_connection(handler)