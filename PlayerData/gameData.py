import re
import pandas as pd 
from RiotAPI.makeRequests import getMatchData, getMatchTimeline


class gameData:
    def __init__(self, puuid, matchId, role, region):
        self.match_id = matchId
        self.puuid = puuid
        self.role = role.upper()
        self.region = region

        self.outcome = None
        self.patch = None
        self.teamId = None
        self.game_start_time = None

        self.main_player_participant_num = None
        self.main_player_champion = None
        self.main_player_timeline = None
        self.main_player_events = None

        self.enemy_laner_participant_num = None
        self.enemy_laner_champion = None
        self.enemy_laner_timeline = None

        self.ally_jungler_participant_num = None
        self.ally_jungler_champion = None

        self.enemy_jungler_participant_num = None
        self.enemy_jungler_champion = None

        try:
            match_json = getMatchData(self.match_id, self.region)
        except Exception as e:
            print(f"Error fetching match data: {e}")
            return None

        # Non summoner's rift game
        if match_json['info']['gameMode'] != "CLASSIC":
            raise ValueError(f"Match {self.match_id} is not a game of Summoner's Rift.")

        else:
            self.patch = re.match(r'(\d+\.\d+)', match_json['info']['gameVersion']).group(0)
            self.game_start_time = int(match_json['info']['gameStartTimestamp'])

        for i, participant in enumerate(match_json['info']['participants']):
            # Capitalize role name in init
            if participant['puuid'] == self.puuid and participant['teamPosition'] == self.role:
                self.outcome = participant['win']
                self.teamId = participant['teamId']

                self.main_player_participant_num = i + 1
                self.main_player_champion = participant['championName']

            # Case where main player if off role
            elif participant['puuid'] == self.puuid and participant['teamPosition'] != self.role:
                raise ValueError(f"Player is not assigned to {self.role} role in match {self.match_id}")

            # Enemy laner
            elif participant['puuid'] != self.puuid and participant['teamPosition'] == self.role:
                self.enemy_laner_participant_num = i + 1
                self.enemy_laner_champion = participant['championName']
            
            # If self.teamId has not been defined yet, main player is in the second half of the list, therefore we're looking at the enemy jungler
            # Can only do this because role will always be top for right now 
            elif participant['teamPosition'] == "JUNGLE" and (self.teamId == None or participant["teamId"] != self.teamId):
                self.enemy_jungler_participant_num = i + 1
                self.enemy_jungler_champion = participant['championName']
            
            elif participant['teamPosition'] == "JUNGLE" and (participant["teamId"] == self.teamId):
                self.ally_jungler_participant_num = i + 1
                self.ally_jungler_champion = participant['championName']

        timeline_json = getMatchTimeline(self.match_id, self.region)
        self.main_player_timeline = self.getParticipantFrames(self.main_player_participant_num, timeline_json)
        self.enemy_laner_timeline = self.getParticipantFrames(self.enemy_laner_participant_num, timeline_json)
        self.main_player_events = self.getEvents(self.main_player_participant_num,timeline_json)
    
    def getParticipantFrames(self, participant_number, data):
        frames_data = []
        
        # Loop through each frame
        for frame in data['info']['frames']:
            # Extract the participant's frame data based on their number
            participant_frame = frame['participantFrames'].get(str(participant_number), {})
            # TODO frame['events]['timestamp]
            participant_frame['timestamp'] = frame['timestamp']  # Add the timestamp for context
            frames_data.append(participant_frame)

        # Convert the list of frame data to a DataFrame
        return pd.DataFrame(frames_data)
    
        # Get all events associated with a particular puuid
    def getEvents(self, participant_number, data):
        events = []
        # Loop through each frame
        for frame in data['info']['frames']:
            for event in frame['events']:
                if 'participantId' in event and event['participantId'] == participant_number:
                    events.append(event)
                    
                elif 'assistingParticipantIds' in event and participant_number in event['assistingParticipantIds']:
                    events.append(event)
                
                elif 'killerId' in event and participant_number == event['killerId']:
                    events.append(event)
                    
                elif 'victimId' in event and participant_number == event['victimId']:
                    events.append(event)
                 
        # Convert the list of frame data to a DataFrame
        return pd.DataFrame(events)