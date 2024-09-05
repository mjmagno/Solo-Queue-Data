import requests
from config import getApiKey
from APIRequest import request

# Return relevant puuids in a list 
def getPUUIDs():
    api_key = getApiKey()

    base_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"

    # Relevant accounts riot_ids    
    shamwwow = "Shamwwow/123"
    khannugurisummit = "KhanNuguriSummit/NA1"
    satxri = "Satxri/NA1"
    
    ids = [shamwwow,khannugurisummit,satxri]
    
    puuids = []
    
    for id in ids:
        api_url = base_url + id + "?api_key=" + api_key
      
        
        player_data = request(api_url)
       

        puuids.append(player_data["puuid"])
        
    return puuids


    
