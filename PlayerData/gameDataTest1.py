import unittest
from  gameData import gameData


class TestGameData(unittest.TestCase):
    def test_game_data_initialization(self):
        # Example of testing the gameData initialization
        test_puuid = "1dhpfvnOomq-plDSKx6l6-V82m_3mlqwPY2ffbxhl5f45TgsN8Zhp8hNRt5HUnvjIm80dAgj9pFfFg"
        test_match_id = "NA1_5138557434"
        test_role = "TOP"
        test_region = "NA"
        
        # Creating a mock gameData object
        game = gameData(test_puuid, test_match_id, test_role, test_region)
        
        # Add assertions
        self.assertEqual(game.puuid, test_puuid)
        self.assertEqual(game.match_id, test_match_id)

if __name__ == "__main__":
    unittest.main()
