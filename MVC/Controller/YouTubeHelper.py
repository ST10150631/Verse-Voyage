from ytmusicapi import YTMusic

class YouTubeHelper:
    def __init__(self):
        self.ytmusic = YTMusic('headers_auth.json')  # Ensure you have the correct headers file

    def create_playlist(self, playlist_name, song_list):
        # Create a new playlist
        playlist_id = self.ytmusic.create_playlist(playlist_name, "Playlist created by YouTubeHelper")
        
        # Search for each song and add to the playlist
        for song in song_list:
            search_results = self.ytmusic.search(song, filter='songs')
            if search_results:
                song_id = search_results[0]['videoId']
                self.ytmusic.add_playlist_items(playlist_id, [song_id])
        
        # Return the link to the playlist
        return f"https://music.youtube.com/playlist?list={playlist_id}"

# Example usage
if __name__ == "__main__":
    helper = YouTubeHelper()
    songs = ["Song 1", "Song 2", "Song 3"]
    playlist_link = helper.create_playlist("My Playlist", songs)
    print(f"Playlist created: {playlist_link}")