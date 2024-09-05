from makeRequests import *


#Return most recent match data for a specific account (0 = Shamwwow, 1 = KhanNuguriSummit, 2 = Satxri )
def returnPlayerData(account):
    puuids = getPUUIDs()
    return getPlayerMatchData(puuids[account],getMatchID(puuids[account]))

