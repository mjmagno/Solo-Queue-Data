# Given a puuid, return the most recent match id 
from APIRequest import request
from config import getApiKey
def getMatchId(puuid):
    api_key = getApiKey()
    base_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    request_url = base_url + puuid + "/ids?start=0&count=1&" + "?api_key=" + api_key
    print(request_url)
    match_id = request(request_url)
    print(match_id)
    