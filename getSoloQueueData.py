from RiotAPI.makeRequests import *
import json
import os 

puuids = getPUUIDs()
matches = {}

numMatches = {}
numMatches[puuids[0]] = 8
numMatches[puuids[1]] = 10
numMatches[puuids[2]] = 4

for puuid, numGames in numMatches.items():
    matches[puuid] = getMatchIDs(puuid,numGames)






for puuid, matchList in matches.items():
    # Create the subfolder if it doesn't exist
    os.makedirs(puuid, exist_ok=True)
    
    for i, match in enumerate(matchList):
        file_name = f'{puuid}/data_{i+1}.json'  # Save to the subfolder
        with open(file_name, 'w') as file:
            json.dump(getMatchData(match), file, indent=4)  # Save the dictionary to a JSON file
# Shamwwow : 8, Satxri : 4, KhanNuguriSummit: 10