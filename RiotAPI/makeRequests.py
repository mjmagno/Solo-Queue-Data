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

def getRegionURL(region):
    base_url = ""
    if region == "NA":
        base_url = "https://americas.api.riotgames.com"
    elif region == "KR":
         base_url = "https://asia.api.riotgames.com"
    elif region == "EU":
         base_url = "https://europe.api.riotgames.com"
    return base_url

# Returns puuid for a riot id in a given region 
# Valid regions are NA, KR, EU 
def getPUUID(gameName,tagline,region):
    api_key = getApiKey()
    region_url = getRegionURL(region)
    
    base_url = region_url + "/riot/account/v1/accounts/by-riot-id/"
  
    
    # Incase user adds # to their tagline 
    if '#' in tagline:
        tagline = tagline.replace('#', '')
    
    # Replace white space with %20 for api request
    gameName = gameName.replace(' ', '%20')

    id = gameName + '/' + tagline

    api_url = base_url + id + "?api_key=" + api_key
      
    player_data = request(api_url)
       
    return player_data["puuid"]
        

# Return most recent match
def getMatchID(puuid,region):
    api_key = getApiKey()
    region_url = getRegionURL(region)
    
    base_url = region_url + "/lol/match/v5/matches/by-puuid/"
    
    request_url = base_url + puuid + "/ids?start=0&count=1&" + "api_key=" + api_key
    match_id = request(request_url)
    return match_id[0]


def getMatchIDs(puuid, num_matches,region):
    api_key = getApiKey()
    region_url = getRegionURL(region)
    
    base_url = region_url + "/lol/match/v5/matches/by-puuid/"
    request_url = base_url + puuid + "/ids?start=0&count=" + str(num_matches) + "&" + "api_key=" + api_key
    match_ids = request(request_url)
    return match_ids

def getMatchData(matchid,region):
    api_key = getApiKey()
    region_url = getRegionURL(region)
    
    base_url = region_url + "/lol/match/v5/matches/"
    request_url = base_url + matchid + "?api_key=" + api_key
    match_data = request(request_url)
    return match_data

def getPlayerMatchData(puuid, matchid,region):
    api_key = getApiKey()
    region_url = getRegionURL(region)
    
    base_url = region_url + "/lol/match/v5/matches/"
    request_url = base_url + matchid + "?api_key=" + api_key
    match_data = request(request_url)
    # get player index from match metadata
    part_index = match_data["metadata"]["participants"].index(puuid)
    part_data =  match_data["info"]["participants"][part_index]
    return part_data

def getMatchTimeline(matchid,region):
    api_key = getApiKey()
    region_url = getRegionURL(region)
    
    base_url = region_url + "/lol/match/v5/matches/"
   
    request_url = base_url + matchid + "/timeline?api_key=" + api_key
    match_data = request(request_url)
    return match_data
    
