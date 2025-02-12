from dotenv import load_dotenv
import os
import base64
import json
from requests import get, post
load_dotenv()
## retrives the client data from the env file 
client_id = os.getenv("Spotify_CLIENT_ID")
client_secret = os.getenv("Spotify_CLIENT_SECRET")
## getsb client id and concatinates to client secret in order to obtain the authorization token 
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes =  auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    print (token)
    return {"Authorization": f"Bearer {token}"}

def get_playlist(playlist_id, market):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}?market={market}"  # URL of the API endpoint
    token = get_token()  # Get the token
    headers = get_auth_header(token)  # Get the Authorization header
    result = get(url, headers=headers)  # Send GET request to the API

    if result.status_code == 200:  # Check if request was successful
        json_result = json.loads(result.content)  # Parse the JSON response
        print(json_result)
        return json_result
    else:
        print(f"Error: {result.status_code}")
        return None

get_playlist("1gttEp6fJBdgfuqu2Ap0Yk", "US")
