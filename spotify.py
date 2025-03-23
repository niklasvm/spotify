from pprint import pp
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv(override=True)

scope = "user-library-read,user-read-playback-position,user-read-recently-played,app-remote-control,streaming,user-read-currently-playing,user-modify-playback-state,user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()

sp.current_playback()["item"]["artists"]

limit=50

items = []
for i in range(10):
    results = sp.current_user_recently_played(limit=50)
    items += results["items"]

items = sp.current_user_recently_played(limit=50)["items"]

for item in items:
    artist = item["track"]["artists"][0]["name"]
    name = item["track"]["name"]
    print(f"{artist} – {name}")

recent=sp.current_user_recently_played(limit=50,)
results["next"]
pp(recent)

for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])