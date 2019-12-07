import spotipy
import json
import matplotlib.pyplot as plt
import authentication

spotify = authentication.getSpotify()
currentPlayback = spotify.current_playback()
print(currentPlayback)
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
segments = []

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
    segments.append(i["start"])

for j in analysis["beats"]:
    beats.append(j["start"])

for k in analysis["bars"]:
    bars.append(k["start"])

#plt.plot(sectionTempo)
#plt.show()

#print(json.dumps(analysis))

def getTempo():
    return tempo

def getEnergy():
    return energy

def getDanceability():
    return danceability

def getAcousticness():
    return acousticness

def getSectionTimes():
    return sections

def getSectionLoudness():
    return sectionLoudness

def getSegmentTimes():
    return segments

def getSegmentLoudness():
    return segmentLoudness

def getSegmentPitch():
    return segmentPitch

def getSegmentTimbre():
    return segmentTimbre

def getBeatTimes():
    return beats

def getBarTimes():
    return bars

