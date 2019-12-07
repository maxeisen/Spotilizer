import spotipy
import json

token = "BQCQ5XDrLOHfJaZUtTKJeIe_LhrVps1YiqDV2y46QcFMUKp_shoGX5VFQg1nAQPNLviftMzM1hLjs2Zr9GekmXo1EJx6pq_XWXMO1_MZLX5Q3pT9czki0-d_CVwDzi2gtqf6x8fYr5z1tvxoog"
spotify = spotipy.Spotify(auth=token)

currSong = spotify.current_user_playing_track()
currSongID = currSong['item']['id']
# print(currSongID)

trackAnalysis = spotify.audio_analysis(currSongID)

# print(results)
