"""
    Class of Player that defines player as an object for future uses
"""

class Player:
    def __init__(self,player_obj):
        self.name = player_obj["name"]
        self.position = ""
        self.goals = player_obj["goals"]
        self.assists = player_obj["assists"]
        self.minutes_played = player_obj["minutes_played"]
        self.apps = player_obj["apps"]
        self.rating = player_obj["rating"]

    def set_position(self,pos):
        self.position = str(pos)

