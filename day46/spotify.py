import spotipy
import requests as req
import os


class SpotifyClient:

    sa = spotipy.oauth2.SpotifyOAuth(
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        redirect_uri="http://example.com",
        state=None,
        scope="playlist-modify-public,playlist-modify-private,user-read-email,user-read-private",
        cache_path=None,
        username=None,
        proxies=None,
        show_dialog=False,
        requests_session=True,
        requests_timeout=None
    )

    def __init__(self):
        super(SpotifyClient, self).__init__()
        # Get AuthZ token for API calls
        self.user_id = None
        self.token = SpotifyClient.sa.get_access_token(code=None, as_dict=True, check_cache=True)['access_token']
        print(f"Token:: {self.token}")

    # Get current user details
    def get_user(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = req.get(url="https://api.spotify.com/v1/me", headers=headers)
        response.raise_for_status()
        self.user_id = response.json()["id"]
        return response.json()

    def create_playlist(self, date):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        body = {
            "name": f"{date} Billboard 100",
            "description": "My playlist",
            "public": "false"
        }

        response = req.post(url=f"https://api.spotify.com/v1/users/{self.user_id}/playlists", headers=headers,
                            json=body)
        response.raise_for_status()
        print(f"{response.json()}")
        return response.json()['id']

    def get_song_uri_api(self, song, year):
        uri = None
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = req.get(
            url=f"https://api.spotify.com/v1/search?query=track%3A{song}+year%3A{year}&type=track&offset=0&limit=1",
            headers=headers)
        response.raise_for_status()
        try:
            uri = response.json()["tracks"]["items"][0]["uri"]
            print(f"URL:: {uri}")
        except IndexError:
            print(f"Doesn't exist in Spotify. Skipped.")
        return uri

    def add_song_to_playlist(self, playlist_id, uris):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = req.post(url=f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={uris}",
                            headers=headers)
        response.raise_for_status()
        print(f"{response.json()}")
        return response.json()['snapshot_id']