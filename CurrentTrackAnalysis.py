import spotipy
import json
import authentication

spotify = authentication.getSpotify()


currentPlayback = spotify.current_playback()
print(currentPlayback)
currSong = currentPlayback['item']
# print(currentPlayback)

# trackAnalysis = spotify.audio_analysis(currSongID)

# print(spotify.track(currSongID)['name'])
# print(results)
