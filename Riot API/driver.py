from getPUUID import getPUUIDs
from getMatchData import getMatchId

puuids = getPUUIDs()

for puuid in puuids:
    print(puuid)
    print(getMatchId(puuid))
