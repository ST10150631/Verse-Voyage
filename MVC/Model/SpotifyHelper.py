from dotenv import load_dotenv
import os
load_dotenv()
## retrives the client data from the env file 
client_id = os.getenv("Spotify_CLIENT_ID")
client_secret = os.getenv("Spotify_CLIENT_SECRET")

