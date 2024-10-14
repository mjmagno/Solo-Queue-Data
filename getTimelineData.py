from RiotAPI.makeRequests import *
import json
import os 

puuids = getPUUIDs()
puuid = puuids[0]
match_id = getMatchID(puuid)

timeline = getMatchTimeline(match_id)
file_name = 'timelinetest1.json' 
with open(file_name, 'w') as file:
    json.dump(timeline, file, indent=4)  # Save the dictionary to a JSON file