import pickle
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
    
        self.latest = None
  
    def add_game(self, game):
        #if self.last_updated is None or self.last_updated < game.game_start_time:
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

    # Look at the last 30 games played, extract all summoner's rift top lane games
    def get_game_data(self):
        matches = getMatchIDs(self.puuid, 30, self.region)
        batch_latest = None  # Initialize to keep track of the latest game in this batch

        for match in matches:
            try:
                game = gameData(self.puuid, match, "TOP", self.region)
                # Stop making API calls if the game's timestamp is <= lastest
                if self.latest is not None and game.game_start_time <= self.latest:
                    print(f"Reached previously processed game (ID: {match}) with timestamp {game.game_start_time}. Stopping further API calls.")
                    break
                
                # Update batch_latest only for the first game processed in this batch
                if batch_latest is None:
                    batch_latest = game.game_start_time

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
            
        # After processing all games, update self.latest to the first game's timestamp in this batch
        if batch_latest is not None:
            self.latest = batch_latest
            print(f"Updated latest processed timestamp to {self.latest}")

    def save(self, filename=None):
        # Saves the playerData instance to a file using pickle
        if filename is None:
            filename = f"{self.gameName}_{self.tagLine}_{self.region}_data.pkl"
            
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
            
        print(f"{self.gameName}'s data saved to {filename}.")

    @classmethod
    def load(cls, filename):
        # Loads a playerData instance from a pickle file
        try:
            with open(filename, 'rb') as file:
                instance = pickle.load(file)
            print(f"{instance.gameName}'s data loaded from {filename}.")
            return instance
        
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
            raise
            
        except pickle.UnpicklingError:
            print(f"Error: The file {filename} could not be loaded. It may be corrupted.")
            raise
            
        except Exception as e:
            print(f"An unexpected error occurred while loading {filename}: {e}")
            raise