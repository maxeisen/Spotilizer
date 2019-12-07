import spotipy
import json
import matplotlib.pyplot as plt
import authentication
import CurrentTrackAnalysis

spotify = authentication.getSpotify()
song = "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC"
#song = CurrentTrackAnalysis.currSong

sectionLoudness = []
sectionTempo = []

segmentLoudness = []
segmentPitch = []
segmentTimbre = []

beats = []
bars = []

analysis = spotify.audio_analysis(song)
features = spotify.audio_features(song)

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

#plt.plot(sectionTempo)
#plt.show()

#print(json.dumps(analysis))
