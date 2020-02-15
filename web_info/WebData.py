
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
from web_info.Player import Player

class ScrapeWebData:
    def __init__(self,conf):
        options = Options()
        options.add_argument('--headless')
        #options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(conf.data['Driver_Path'])
        self.players = []
        self.players_scraped_data = []

    def close_con(self):
        self.driver.close()

    def get_url_data(self, url):
        self.driver.get(url)

    def click_accept_terms(self):
        print("accpring terms")
        try:
            accept_btn = self.driver.find_element_by_xpath('//*[@id="qcCmpButtons"]/button[2]')
            accept_btn.click()
        except Exception as e:
            print(e)
            pass

    def extract_players_data(self):

        result_fetched = None
        max_retries = 3
        while result_fetched is None and max_retries:
            time.sleep(2)
            self.click_accept_terms()
            time.sleep(3)

            table_players_stats = (self.driver.find_element_by_id('player-table-statistics-body'))
            table_players_stats = table_players_stats.text

            self.players_scraped_data = table_players_stats.splitlines()

            if self.players_scraped_data != []:
                result_fetched = "got info"
            print("1.{}".format(self.players_scraped_data))
            max_retries-=1
        # delete the unnecessary row number
        if max_retries == 0:
            return False
        del self.players_scraped_data[:len(self.players_scraped_data):3]
        print(self.players_scraped_data)
        return True

    def parse_players_scraped_data(self):
        print(self.players_scraped_data)
        self.players = []
        for i in range(len(self.players_scraped_data)):

            if i % 2:
                data_of_players = self.players_scraped_data[i].split(' ')

                player_data = {}
                player_data['name'] = name
                player_data['goals'] = data_of_players[-9]
                player_data['assists'] = data_of_players[-8]
                player_data['minutes_played'] = data_of_players[-10]
                player_data['rating'] = data_of_players[-1]
                player_data['apps'] = data_of_players[-11].split("(")[0]

                player_sample = Player(player_data)
                self.players.append(player_sample)

                print("Scraped...")
            else:
                name = self.players_scraped_data[i]
                print("players_scraped_data-",self.players_scraped_data)
                #print("The player name is: {}".format(self.players[i]))

        return self.players
