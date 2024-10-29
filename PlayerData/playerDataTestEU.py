import unittest
from playerData import playerData


class TestPlayerDataEU(unittest.TestCase):
    def test_player_data_eu_initialization(self):
        # Example of testing the player data init
        
        test_gameName = "Night Slayer"
        test_tagLine = "SLAAY"
        test_region = "EU"
        
        aomine = playerData(test_gameName, test_tagLine, test_region)
            
        # Add assertions
        self.assertEqual(aomine.gameName, test_gameName)
        self.assertEqual(aomine.tagLine, test_tagLine)
        
        aomine.get_game_data()
        print(aomine.games_list)
        

if __name__ == "__main__":
    unittest.main()
