import authentication
import dataRetrieve

spotify = authentication.getSpotify()
currentPlayback = spotify.current_playback()
actualCurrentData = dataRetrieve.dataRetrieve()
song = currentPlayback['item']
songID = song['id']

def setTime()
