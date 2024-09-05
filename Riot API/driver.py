from makeRequests import *

puuids = getPUUIDs()

for puuid in puuids:
    print(puuid)
    match_id = getMatchId(puuid)
    print(match_id)
    player_data = getPlayerMatchData(puuid,match_id)
    print(player_data)
