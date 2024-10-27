
from RiotAPI.makeRequests import getPUUID, getMatchIDs
from gameData import gameData


class playerData:
    def __init__(self, gameName, tagLine, region):
        self.gameName = gameName
        self.tagLine = tagLine
        self.region = region
        self.puuid = getPUUID(gameName, tagLine, region)
    
        self.games_list = []  # List of all gameData objects
        self.patch_dict = {}  # Dict: patch -> list of gameData objects
        self.champ_dict = {}  # Dict: champion -> list of gameData objects
        self.patch_champ_dict = {}  # Dict: patch -> champion -> list of gameData objects
    
        self.last_updated = None
  
    def add_game(self, game):
        if self.last_updated is None or self.last_updated < game.game_start_time:
            self.games_list.append(game)
       
            # Add to patch_dict
            if game.patch not in self.patch_dict:
                self.patch_dict[game.patch] = []
            self.patch_dict[game.patch].append(game)

            # Add to champ_dict
            if game.main_player_champion not in self.champ_dict:
                self.champ_dict[game.main_player_champion] = []
            self.champ_dict[game.main_player_champion].append(game)

            # Add to patch_champ_dict
            if game.patch not in self.patch_champ_dict:
                self.patch_champ_dict[game.patch] = {}
            if game.main_player_champion not in self.patch_champ_dict[game.patch]:
                self.patch_champ_dict[game.patch][game.main_player_champion] = []
            self.patch_champ_dict[game.patch][game.main_player_champion].append(game)
            # Update last_updated after successfully adding the game
            self.last_updated = game.game_start_time

    # Look at the last 30 games played, extract all summoner's rift top lane games
    def get_game_data(self):
        matches = getMatchIDs(self.puuid, 30, self.region)

        for match in reversed(matches): # Process older matches first 
            try:
                game = gameData(self.puuid, match, "TOP", self.region)
            except ValueError as e:
                # Log the error for awareness, but continue processing
                print(f"Skipping match {match}: {e}")
                continue
            except Exception as e:
                # Handle unexpected errors separately for debugging
                print(f"Unexpected error for match {match}: {e}")
                continue
            else:
                self.add_game(game)     
