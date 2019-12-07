import spotipy
import json
import matplotlib.pyplot as plt
import authentication

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
sections = []

analysis = spotify.audio_analysis(songID)
features = spotify.audio_features([songID])

tempo = features[0]["tempo"] # speed of drawing
energy = features[0]["energy"] #colour palette saturation
danceability = features[0]["danceability"] # colour change frequency
acousticness = features[0]["acousticness"] # warmth/hue of colour palette

for c in analysis["sections"]:
    sectionLoudness.append(c["loudness"])
    sectionTempo.append(c["tempo"])
    sections.append(c["start"])

for i in analysis["segments"]:
    segmentPitch.append(i["pitches"])
    segmentTimbre.append(i["timbre"])

for j in analysis["beats"]:
    beats.append(j["start"])

for k in analysis["bars"]:
    bars.append(k["start"])

print(acousticness)


#plt.plot(sectionTempo)
#plt.show()

#print(json.dumps(analysis))
