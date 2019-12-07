import spotipy
import os
import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

#put your username here
username = "12165810876"

SPOTIPY_CLIENT_ID='068c0eb38bd249cd82d1097fae9e0644'
SPOTIPY_CLIENT_SECRET='070b7a269c9040aea67420066725096a'
SPOTIPY_REDIRECT_URI = 'http://google.com/'

try:
    token = util.prompt_for_user_token(username,'user-library-read',client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)


birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
token = "BQCwvEqIMI3rFVe7cq07phBaXiKq80IxtXyYpyq4r5WdntrQ1gOjpglfOxXChY8-BjfidOKvJ7_84NTG__6xJZ3gmnUFfvexeV6QhJ8Gj0daArJhVZi4x1cMg_OWYsNnTUkPV71FnUZjvmpsHXSm-g"
spotify = spotipy.Spotify(auth=token)

results = spotify.artist_albums(birdy_uri, album_type='album')
song = spotify.current_user_playing_track()

print(song)
