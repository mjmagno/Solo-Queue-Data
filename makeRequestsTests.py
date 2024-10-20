from RiotAPI.makeRequests import *
import json
import os 


# Get puuids of three players from three different regions
# Tests for # in tagline, space in gamename, foreign characters, and different regions 
divineMaple = getPUUID("divine maple","#goat","NA")

Aomine = getPUUID("Daiki Aomine", "#RKR", "EU")

KRGwen = getPUUID("14小孩幻想赢对线", "4453", "KR")

print(divineMaple)
print(Aomine)
print(KRGwen)

# Get most recent matchId for each player
mapleID1 = getMatchID(divineMaple,"NA")
aomineID1 = getMatchID(Aomine,"EU")
krplayerID1 = getMatchID(KRGwen,"KR")

print(mapleID1)
print(aomineID1)
print(krplayerID1)

# Get last 5 games for each player 
mapleGames = getMatchIDs(divineMaple,5,"NA")
aomineGames = getMatchIDs(Aomine,5,"EU")
krGames = getMatchIDs(KRGwen,5,"KR")

print(mapleGames)
print(aomineGames)
print(krGames)

# Get match data for each player
mapleGame1 = getMatchData(mapleID1,"NA")
aomineGame1 = getMatchData(aomineID1,"EU")
krGame1 = getMatchData(krplayerID1,"KR")
games = [mapleGame1,aomineGame1,krGame1]

for i, match in enumerate(games):
        file_name = f'match{i}.json'  # Save to the subfolder
        with open(file_name, 'w') as file:
            json.dump(match, file, indent=4)  # Save the dictionary to a JSON file
            
# Get timeline data for each player
mapleTimeline1 = getMatchTimeline(mapleID1,"NA")
aomineTimeline1 = getMatchTimeline(aomineID1,"EU")
krTimeline1 = getMatchTimeline(krplayerID1,"KR")
timelines = [mapleTimeline1,aomineTimeline1,krTimeline1]

for i, match in enumerate(timelines):
        file_name = f'timeline{i}.json'  # Save to the subfolder
        with open(file_name, 'w') as file:
            json.dump(match, file, indent=4)  # Save the dictionary to a JSON file
