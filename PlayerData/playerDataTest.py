import unittest
from playerData import playerData


class TestPlayerData(unittest.TestCase):
    def test_player_data_initialization(self):
        # Example of testing the player data init
        
        test_gameName = "Yuxin baby"
        test_tagLine = "god"
        test_region = "NA"
        
        yuxin = playerData(test_gameName, test_tagLine, test_region)
            
        # Add assertions
        self.assertEqual(yuxin.gameName, test_gameName)
        self.assertEqual(yuxin.tagLine, test_tagLine)
        
        yuxin.get_game_data()
        print(yuxin.games_list)
        

if __name__ == "__main__":
    unittest.main()
