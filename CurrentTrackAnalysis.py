import spotipy
import json
import authentication

token = authentication.getToken()


spotify = spotipy.Spotify(auth=token)

currSong = spotify.current_user_playing_track()
currSongID = currSong['item']['id']
# print(currSongID)

trackAnalysis = spotify.audio_analysis(currSongID)

print(spotify.track(currSongID)['name'])
# print(results)
