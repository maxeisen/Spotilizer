import spotipy
import json
import authentication

spotify = authentication.getSpotify()


currentPlayback = spotify.current_playback()
currentSong = currentPlayback['item']
currentSongID = currentSong['id']
songAnalysis = spotify.audio_analysis(currentSongID)
print(songAnalysis)

# print(spotify.track(currSongID)['name'])
# print(results)
