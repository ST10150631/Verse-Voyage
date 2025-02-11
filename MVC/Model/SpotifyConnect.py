import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyPlaylist:
    def __init__(self, client_id, client_secret, redirect_uri, playlist_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.playlist_id = playlist_id
        
        # Authenticate using Spotify's OAuth
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                             client_secret=self.client_secret,
                                                             redirect_uri=self.redirect_uri,
                                                             scope="playlist-read-private"))

    def get_playlist_data(self, fields=None):
        """
        Retrieves the playlist data. Allows specifying fields to filter the data.
        """
        # If no specific fields are provided, use the default behavior.
        if fields is None:
            fields = "name,description,images,owner,followers,public,tracks(items(track(name,album(name,href))))"
        
        # Retrieve playlist details from Spotify API with field filtering
        playlist_data = self.sp.playlist(self.playlist_id, fields=fields)

        # Extract relevant fields from the response
        playlist_info = {
            'name': playlist_data['name'],
            'description': playlist_data.get('description', 'No description available'),
            'images': playlist_data['images'],
            'owner': playlist_data['owner']['display_name'],
            'followers': playlist_data['followers']['total'],
            'public': playlist_data['public'],
            'tracks': []
        }

        # Extract track details (name, album name, and album URI)
        for item in playlist_data['tracks']['items']:
            track = item['track']
            track_info = {
                'name': track['name'],
                'album': track['album']['name'],
                'album_uri': track['album']['uri']
            }
            playlist_info['tracks'].append(track_info)

        return playlist_info

# Example usage
if __name__ == "__main__":
    CLIENT_ID = "1ca6946c4bdd4b3a9c54dd9f0854e666"  # Your provided Client ID
    CLIENT_SECRET = "your_spotify_client_secret"  # Replace with your Client Secret
    REDIRECT_URI = "http://localhost:8888/callback"  # Your Redirect URI
    PLAYLIST_ID = "1gttEp6fJBdgfuqu2Ap0Yk"  # Playlist ID you provided

    # Create an instance of SpotifyPlaylist
    spotify_playlist = SpotifyPlaylist(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, PLAYLIST_ID)

    # Retrieve playlist data
    playlist_data = spotify_playlist.get_playlist_data()

    # Print playlist data
    print(f"Playlist Name: {playlist_data['name']}")
    print(f"Description: {playlist_data['description']}")
    print(f"Owner: {playlist_data['owner']}")
    print(f"Followers: {playlist_data['followers']}")
    print(f"Public: {playlist_data['public']}")
    print("Images:")
    for img in playlist_data['images']:
        print(f"  - {img['url']} (Width: {img['width']}, Height: {img['height']})")
    
    print("\nTracks:")
    for track in playlist_data['tracks']:
        print(f"  Track: {track['name']}, Album: {track['album']}, Album URI: {track['album_uri']}")
