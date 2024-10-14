from RiotAPI.makeRequests import *
import pandas as pd

#Return most recent match data for a specific account (0 = Shamwwow, 1 = KhanNuguriSummit, 2 = Satxri )
def returnPlayerData(account):
    puuids = getPUUIDs()
    return getPlayerMatchData(puuids[account],getMatchID(puuids[account]))

#TODO Add other metrics (gold, damage, lane opponent)
def getRelevantData(player_data):
    extracted_data = []
    game_time = player_data['timePlayed'] / 60
    extracted_data.append({
        'Date': pd.to_datetime('today').strftime('%Y-%m-%d'),
        'Champion': player_data['championName'],
        'K': player_data['kills'],
        'D': player_data['deaths'],
        'A': player_data['assists'],
        'W/L': 'W' if player_data['win'] else 'L', 
        'CS': player_data['neutralMinionsKilled'] + player_data['totalMinionsKilled'],
        'Game Time': game_time
    })
    return pd.DataFrame(extracted_data)


player_data = returnPlayerData(0)
print(getRelevantData(player_data))