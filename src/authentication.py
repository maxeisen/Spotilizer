import spotipy
import os
import sys
import json
import webbrowser
import spotipy.util as util

#put your username here
username = "0000000000"
scope = 'user-modify-playback-state user-read-playback-state user-read-currently-playing'

def getSpotify():
    SPOTIPY_CLIENT_ID='068c0eb38bd249cd82d1097fae9e0644'
    SPOTIPY_CLIENT_SECRET='070b7a269c9040aea67420066725096a'
    SPOTIPY_REDIRECT_URI = 'http://google.com/'
    token = util.prompt_for_user_token(username, scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
    spotify = spotipy.Spotify(auth=token)
    return (spotify)
