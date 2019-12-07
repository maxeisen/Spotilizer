import spotipy
import json
import matplotlib.pyplot as plt
import authentication
# import CurrentTrackAnalysis

spotify = authentication.getSpotify()
currentPlayback = spotify.current_playback()
song = currentPlayback['item']
songID = song['id']

sectionLoudness = []
sectionTempo = []

segmentLoudness = []
segmentPitch = []
segmentTimbre = []

beats = []
bars = []

analysis = spotify.audio_analysis(songID)
features = spotify.audio_features([songID])


energy = features[0]["energy"]
tempo = features[0]["tempo"]
danceability = features[0]["danceability"]
acousticness = features[0]["acousticness"]

for c in analysis["sections"]:
    sectionLoudness.append(c["loudness"])
    sectionTempo.append(c["tempo"])

for i in analysis["segments"]:
    segmentPitch.append(i["pitches"])
    segmentTimbre.append(i["timbre"])

for j in analysis["beats"]:
    beats.append(j["start"])

for k in analysis["bars"]:
    bars.append(k["start"])

print(energy)


#plt.plot(sectionTempo)
#plt.show()

#print(json.dumps(analysis))
