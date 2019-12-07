import spotipy
import json
import authentication

spotify = authentication.getSpotify()

#
# currentPlayback = spotify.current_playback()
# currentSong = currentPlayback['item']
# currentSongID = currentSong['id']
def getAnalysis(songID):
    analysis = spotify.audio_analysis(songID)
    return (analysis)

# print(spotify.track(currSongID)['name'])
# print(results)
