# Given a puuid, return the most recent match id 
from RiotAPI.config import getApiKey
import requests

def request(api_url):
    resp = requests.get(api_url)
     # Raise an exception for any HTTP status code >= 400
    try:
        resp.raise_for_status()  # This will raise an HTTPError if the response status is not 200
        return resp.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Handle specific HTTP errors
        raise  # Re-raise the error to allow it to be handled upstream
    except Exception as err:
        print(f"Other error occurred: {err}")  # Handle other possible errors
        raise
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


def getMatchID(puuid):
    api_key = getApiKey()
    base_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    request_url = base_url + puuid + "/ids?start=0&count=1&" + "api_key=" + api_key
    match_id = request(request_url)
    return match_id[0]

def getPlayerMatchData(puuid, matchid):
    api_key = getApiKey()
    base_url = "https://americas.api.riotgames.com/lol/match/v5/matches/"
    request_url = base_url + matchid + "?api_key=" + api_key
    match_data = request(request_url)
    # get player index from match metadata
    part_index = match_data["metadata"]["participants"].index(puuid)
    part_data =  match_data["info"]["participants"][part_index]
    return part_data
    
    