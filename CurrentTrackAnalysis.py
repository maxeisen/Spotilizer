import spotipy
import json
import authentication

spotify = authentication.getSpotify()


currSong = spotify.current_user_playing_track()
# print(currSong)
currSongID = currSong['item']['id']
# print(currSongID)

trackAnalysis = spotify.audio_analysis(currSongID)

print(spotify.track(currSongID)['name'])
# print(results)
