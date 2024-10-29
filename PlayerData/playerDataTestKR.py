import unittest
from playerData import playerData


class TestPlayerDataKR(unittest.TestCase):
    def test_player_data_kr_initialization(self):
        # Example of testing the player data init
        
        test_gameName = "칼과 창 방패"
        test_tagLine = "KR1"
        test_region = "KR"
        
        goat = playerData(test_gameName, test_tagLine, test_region)
            
        # Add assertions
        self.assertEqual(goat.gameName, test_gameName)
        self.assertEqual(goat.tagLine, test_tagLine)
        
        goat.get_game_data()
        print(goat.games_list)
        print(goat.champ_dict)
        print(goat.patch_dict)
        

if __name__ == "__main__":
    unittest.main()
