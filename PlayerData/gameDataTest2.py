import unittest
from gameData import gameData
from RiotAPI.makeRequests import getMatchIDs


class TestGameData(unittest.TestCase):
    def test_game_data_initialization(self):
        # Example of testing the gameData initialization
        test_puuid = "1dhpfvnOomq-plDSKx6l6-V82m_3mlqwPY2ffbxhl5f45TgsN8Zhp8hNRt5HUnvjIm80dAgj9pFfFg"
        test_role = "TOP"
        test_region = "NA"
        
        matchIds = getMatchIDs(test_puuid,20,test_region)
        
        for match in matchIds:
            
        # Creating a mock gameData object
            game = gameData(test_puuid, match , test_role, test_region)
        
        # Add assertions
            self.assertEqual(game.puuid, test_puuid)
            self.assertEqual(game.match_id, match)

if __name__ == "__main__":
    unittest.main()
