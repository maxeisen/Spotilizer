from tkinter import *
import tkinter as tk
import turtle
from PIL import Image, ImageTk
import authentication
import dataRetrieve
import colourChoice
import random
from subprocess import call

spotify = authentication.getSpotify()
songProps = dataRetrieve.dataRetrieve()
# screen = turtle.Screen()
# screen.screensize()
# screen.setup(width = 1.0, height = 1.0)
#
# screen.bgpic(ImageTk("albumCover.gif"))


def play():
    try:
        spotify.start_playback(device_id=None, context_uri=None, uris=None, offset=None)
    except:
        return None


def previous():
    spotify.previous_track(device_id=None)

def pause():
    try:
        spotify.pause_playback(device_id=None)
    except:
        return None

def forward():
    spotify.next_track(device_id=None)

def launchVisualizer():
    call(["python3", "visualizer2.py"])

def albumDisplayUpdate():
    albumID = spotify.current_user_playing_track()['item']['album']['id']
    albumCoverID = dataRetrieve.setAlbumCover(albumID)
    albumDisplay.after(0, changeAlbumArt(albumCoverID))

#image = Image.open("play.png")
#photo = ImageTk.PhotoImage(image)

#screen = Screen()

def changeAlbumArt(albumCoverID):
        # print(albumCoverID)
        albumCoverNew = ImageTk.PhotoImage(Image.open(albumCoverID))
        # print("updating")
        albumDisplay.configure(image = albumCoverNew)
        albumDisplay.image = albumCoverNew

def setColors(energy, danceability, acousticness):
    # print(energy)
    # print(danceability)
    # print(acousticness)
    # darkColours = ["612b16", "270e80", "66404c", "2e4d65", "2b7643", "612b91", "612bcd", "1f404c", "227643", "612bff", "470e6d", "a9404c", "0a7643", "271680", "37404c", "68404c", "612b58", "062936", "062936", "22064f", "22124f"]
    darkColourHex = ['0','1','2','3','4','6']
    pal = colourChoice.choose_palette(danceability, acousticness)
    pal = colourChoice.energy_mod(pal, energy)
    # print(pal)
    bgColour = pal[random.randint(0,3)]
    # print(bgColour)
    root.config(background="#"+bgColour)
    topFrame.config(background="#"+bgColour)
    if (bgColour[0] in darkColourHex):
        # print("DARK!")
        songLabel.config(background="#"+bgColour, foreground="#ffffff")
    else:
        songLabel.config(background="#"+bgColour, foreground="#000000")
    welcomeLabel.config(background="#"+bgColour, foreground="#000000")
    buttonColour = pal[random.randint(0,3)]
    button1.config(highlightbackground="#"+buttonColour)
    button2.config(highlightbackground="#"+buttonColour)
    button3.config(highlightbackground="#"+buttonColour)
    button4.config(highlightbackground="#"+buttonColour)


def update():
    currSongName = songLabel.cget("text")
    artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
    songName = spotify.current_user_playing_track()['item']['name']
    if currSongName != (songName + " - " + artistName):
        albumDisplayUpdate()
        songLabel.config(text = (songName + " - " + artistName))
        songID = spotify.current_user_playing_track()['item']['id']
        # print(songID)
        songProps = dataRetrieve.dataRetrieve(songID)
        songEnergy = songProps["energy"]
        songDanceability = songProps["danceability"]
        songAcousticness = songProps["acousticness"]
        setColors(songEnergy, songDanceability, songAcousticness)
    root.after(100, update)


root = tk.Tk()
root.title("Spotilizer")
root.geometry("2000x1000+200+200")
root.config(background="#1DB954")
# canvas = tk.Canvas(master = root, width = 500, height = 500)
#print(canvas)
# canvas.pack()
# t = turtle.RawTurtle(canvas)
imagePrevious = ImageTk.PhotoImage(Image.open("assets/img/backward.png"))
imagePlay = ImageTk.PhotoImage(Image.open("assets/img/play.png"))
imagePause = ImageTk.PhotoImage(Image.open("assets/img/pause.png"))
imageForward = ImageTk.PhotoImage(Image.open("assets/img/forward.png"))
frame1 = Frame(root)

welcomeLabel = Label(root, font= ("Proxima Nova", 10), text="© Spotilizer 2019", bg="#1DB954",fg="white")
songLabel = Label(root, pady=40, text="", font=("Gotham", 26), bg="#1DB954",fg="white")
artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
songName= spotify.current_user_playing_track()['item']['name']
songLabel.config(text = (songName + " - "+ artistName))

topFrame = Frame(root)#definig a frame that will contain the Widgets
topFrame.pack()
topFrame.config(background="#1DB954")
#bottomFrame = Frame(root) #Similarly, definging the next Frame
#bottomFrame.pack(side=BOTTOM)

#---------Various Buttons----------
welcomeLabel.pack(side=BOTTOM)
albumID = spotify.current_user_playing_track()['item']['album']['id']
albumCoverID = dataRetrieve.setAlbumCover(albumID)
albumCoverRaw = Image.open(albumCoverID)
albumCover = ImageTk.PhotoImage(albumCoverRaw)
albumCoverRaw.close()
albumDisplay = Label(topFrame, image=albumCover)
albumDisplay.pack(side=TOP,padx=5,pady=10)
button1 = Button(topFrame, padx=10, pady=10, highlightbackground="#ffffff", relief=RAISED, highlightthickness=0, bd=0, cursor="hand", text="Previous", image=imagePrevious, command=lambda:[previous(), albumDisplayUpdate()]) #Positioning Button as (<FrameName>,<Text to Appear>,<Text Color>)
button1.pack(side=LEFT,padx=50,pady=20)
button2 = Button(topFrame, padx=10, pady=10, highlightbackground="#ffffff", relief=RAISED, highlightthickness=0, bd=0, cursor="hand", text="Play", image=imagePlay, command=lambda:[play(), albumDisplayUpdate()])
button2.pack(side=LEFT,padx=50,pady=20)
button5 = Button(topFrame, padx=10, pady=10, relief=RAISED, cursor="hand", text="Visualizer", command=launchVisualizer)
button5.pack(side=LEFT,padx=50,pady=20)
button3 = Button(topFrame, padx=10, pady=10, highlightbackground="#ffffff", relief=RAISED, highlightthickness=0, bd=0, cursor="hand", text="Pause", image=imagePause, command=lambda:[pause(), albumDisplayUpdate()])
button3.pack(side=LEFT,padx=50,pady=20)
button4 = Button(topFrame, padx=10, pady=10, highlightbackground="#ffffff", relief=RAISED, highlightthickness=0, bd=0, cursor="hand", text="Forward", image=imageForward, command=lambda:[forward(), albumDisplayUpdate()])
button4.pack(side=LEFT,padx=50,pady=20)
songLabel.pack(fill=X)

initialSongID = spotify.current_user_playing_track()['item']['id']
initialSongProps = dataRetrieve.dataRetrieve(initialSongID)
initialSongEnergy = initialSongProps["energy"]
initalSongDanceability = initialSongProps["danceability"]
initialSongAcousticness = initialSongProps["acousticness"]
setColors(initialSongEnergy, initalSongDanceability, initialSongAcousticness)

root.after(100, update)
root.mainloop()
