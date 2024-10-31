from PlayerData.playerData import playerData

def main():
    player_name = "Yuxin baby"
    tagline = "god"
    region = "NA"
    filename = f"{player_name}_{tagline}_{region}_data.pkl"

    # Step 1: Load or initialize player instance
    try:
        player_instance = playerData.load(filename)
    except FileNotFoundError:
        print(f"No saved data found for {player_name}. Creating a new instance.")
        player_instance = playerData(gameName=player_name, tagLine=tagline, region=region)

    # Step 2: Perform analysis
    player_instance.get_game_data()
    print(player_instance.champ_dict.keys())

    # Step 3: Save updated player data
    player_instance.save()
    print(f"{player_name}'s data saved successfully.")

if __name__ == "__main__":
    main()