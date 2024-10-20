
from ..RiotAPI.makeRequests import *

class playerData:
    def __init__(self, gameName, tagLine, region):
        self.gameName = gameName
        self.tagLine = tagLine
        self.region = region
        self.puuid = getPUUID(gameName,tagLine,region)
        self.games_list = []  # List of all gameData objects
        self.patch_dict = {}  # Dict: patch -> list of gameData objects
        self.champ_dict = {}  # Dict: champion -> list of gameData objects
        self.patch_champ_dict = {}  # Dict: patch -> champion -> list of gameData objects
    def get_game_data(self,)

    def add_game(self, game):
        # Add to games_list
        self.games_list.append(game)
        
        # Add to patch_dict
        if game.patch not in self.patch_dict:
            self.patch_dict[game.patch] = []
        self.patch_dict[game.patch].append(game)
        
        # Add to champ_dict
        if game.main_champion not in self.champ_dict:
            self.champ_dict[game.main_champion] = []
        self.champ_dict[game.main_champion].append(game)
        
        # Add to patch_champ_dict
        if game.patch not in self.patch_champ_dict:
            self.patch_champ_dict[game.patch] = {}
        if game.main_champion not in self.patch_champ_dict[game.patch]:
            self.patch_champ_dict[game.patch][game.main_champion] = []
        self.patch_champ_dict[game.patch][game.main_champion].append(game)