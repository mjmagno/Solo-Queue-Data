from dotenv import load_dotenv
import os


 # Load the .env file
load_dotenv()


# Function to get the API key
def getApiKey():
    return os.getenv('RIOT_API_KEY')


