import spotipy
import json
import urllib.request
import authentication

spotify = authentication.getSpotify()
currentPlayback = spotify.current_playback()

def dataRetrieve(songID=currentPlayback['item']['id']):
    song = spotify.track(songID)
    albumID = song['album']['id']

    analysis = spotify.audio_analysis(songID)
    features = spotify.audio_features([songID])

    albumCover = setAlbumCover(albumID)

    duration = setDuration(analysis)

    tempo = setTempo(features) # speed of drawing
    energy = setEnergy(features) #colour palette saturation
    danceability = setDanceability(features) # colour change frequency
    acousticness = setAcousticness(features) # warmth/hue of colour palette

    sections = setSections(analysis)
    sectionLoudness = setSectionLoudness(analysis)

    segments = setSegments(analysis)
    segmentPitch = setSegmentPitch(analysis)
    segmentTimbre = setSegmentTimbre(analysis)

    beats = setBeats(analysis)
    bars = setBars(analysis)

    songData = {
        "albumCover": albumCover,
        "duration": duration,
        "tempo": tempo,
        "energy": energy,
        "danceability": danceability,
        "acousticness": acousticness,
        "sections": sections,
        "sectionLoudness": sectionLoudness,
        "segments": segments,
        "segmentPitch": segmentPitch,
        "segmentTimbre": segmentTimbre,
        "beats": beats,
        "bars": bars
    }

    return songData

def redurationCurrent():
    spotify.seek_track(0, device_id=None)

def setAlbumCover(albumID):
    imageURL = str(spotify.album(albumID)['images'][0]['url'])
    imageName = 'albumCover_' + imageURL[56:60] + '.png'
    urllib.request.urlretrieve(imageURL, imageName)
    return imageName

def setDuration(analysis):
    return analysis["track"]["duration"]

def setTempo(features):
    return features[0]["tempo"]

def setEnergy(features):
    return features[0]["energy"]

def setDanceability(features):
    return features[0]["danceability"]

def setAcousticness(features):
    return features[0]["acousticness"]

def setSections(analysis):
    sections = []
    for c in analysis["sections"]:
        sections.append(c["duration"])
    return sections

def setSectionLoudness(analysis):
    sectionLoudness = []
    for c in analysis["sections"]:
        sectionLoudness.append(c["duration"])
    return sectionLoudness

def setSegments(analysis):
    segments = []
    for i in analysis["segments"]:
        segments.append(i["duration"])
    return segments

def setSegmentPitch(analysis):
    segmentPitch = []
    for i in analysis["segments"]:
        segmentPitch.append(i["pitches"])
    return segmentPitch

def setSegmentTimbre(analysis):
    segmentTimbre = []
    for i in analysis["segments"]:
        segmentTimbre.append(i["timbre"])
    return segmentTimbre

def setBeats(analysis):
    beats = []
    for i in analysis["beats"]:
        beats.append(i["duration"])
    return beats

def setBars(analysis):
    bars = []
    for i in analysis["bars"]:
        bars.append(i["duration"])
    return bars
