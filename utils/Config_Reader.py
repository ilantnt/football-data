import json
import os.path

class Configuration():
    def __init__(self):
        with open(os.path.dirname(__file__) + '/../config.json') as json_file:
            self.data = json.load(json_file)

    def get_web_driver(self):
        return self.data['Driver_Path']

    def get_spain_teams(self):
        return self.data['Spain_Teams']

    def get_db_auth(self):
        return self.data['MySql']