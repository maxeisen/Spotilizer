import assets.secrets as secrets
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
    SPOTIPY_CLIENT_ID=secrets.SPOTIPY_CLIENT_ID
    SPOTIPY_CLIENT_SECRET=secrets.SPOTIPY_CLIENT_SECRET
    SPOTIPY_REDIRECT_URI = 'http://google.com/'
    token = util.prompt_for_user_token(username, scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
    spotify = spotipy.Spotify(auth=token)
    return (spotify)
