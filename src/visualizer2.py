from tkinter import *
import tkinter as tk
from turtle import *
from PIL import Image, ImageTk
import authentication
import dataRetrieve
import colourChoice
import random
import urllib.request

spotify = authentication.getSpotify()
songProps = dataRetrieve.dataRetrieve()
# screen = turtle.Screen()
# screen.screensize()
# screen.setup(width = 1.0, height = 1.0)
#
# screen.bgpic(ImageTk("albumCover.gif"))


# def play():
#     try:
#         spotify.start_playback(device_id=None, context_uri=None, uris=None, offset=None)
#     except:
#         return None
#
#
# def previous():
#     spotify.previous_track(device_id=None)
#
# def pause():
#     try:
#         spotify.pause_playback(device_id=None)
#     except:
#         return None
#
# def forward():
#     spotify.next_track(device_id=None)

# def albumDisplayUpdate():
#     albumID = spotify.current_user_playing_track()['item']['album']['id']
#     albumCoverID = dataRetrieve.setAlbumCover(albumID)
#     albumDisplay.after(0, changeAlbumArt(albumCoverID))
#
# image = Image.open("play.png")
# photo = ImageTk.PhotoImage(image)
#
# screen = Screen()
#
# def changeAlbumArt(albumCoverID):
#         # print(albumCoverID)
#         albumCoverNew = ImageTk.PhotoImage(Image.open(albumCoverID))
#         # print("updating")
#         albumDisplay.configure(image = albumCoverNew)
#         albumDisplay.image = albumCoverNew
#         # canvas.bgpic(albumCoverID)
#         # call(["python3", "visualizer.py"])

def setColors(energy, danceability, acousticness):
    # print("setting colors")
    # print(energy)
    # print(danceability)
    # print(acousticness)
    # darkColours = ["612b16", "270e80", "66404c", "2e4d65", "2b7643", "612b91", "612bcd", "1f404c", "227643", "612bff", "470e6d", "a9404c", "0a7643", "271680", "37404c", "68404c", "612b58", "062936", "062936", "22064f", "22124f"]
    darkColourHex = ['0','1','2','3','4','6']
    pal = colourChoice.choose_palette(danceability, acousticness)
    pal = colourChoice.energy_mod(pal, energy)
    # print(pal)
    bgChosen = pal[random.randint(0,3)]
    bgColour = bgChosen[0:4] + "00"
    # print(bgChosen + "->" + bgColour)
    # print(bgColour)
    root.config(background="#"+bgColour)
    topFrame.config(background="#"+bgColour)
    titleFrame.config(background="#"+bgColour)
    canvas.config(background="#"+bgColour)
    if (bgColour[0] in darkColourHex):
        # print("DARK!")
        songLabel.config(background="#"+bgColour, foreground="#ffffff")
    else:
        songLabel.config(background="#"+bgColour, foreground="#000000")
    welcomeLabel.config(background="#"+bgColour, foreground="#000000")
    # buttonColour = pal[random.randint(0,3)]
    # button1.config(highlightbackground="#"+buttonColour)
    # button2.config(highlightbackground="#"+buttonColour)
    # button3.config(highlightbackground="#"+buttonColour)
    # button4.config(highlightbackground="#"+buttonColour)


# visualizer code

def tstart(turtle):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-700, 1/2)
    turtle.pendown()

class Spiralizer:
    def __init__(self,dur):
        self.__cm = ['red']#colourChoice.getPalette() #Returns the colour palette for the current song.
        self.__factor = dur*(960/dur)#song.length*(winwidth/song.length) #Assign the length of the song to a dur variable
        self.__seen = []
        self.__its = int(dur)
    def getIts(self):
        return self.__its
    def notInSeen(self,curr):
        if (curr in self.__seen):
            return False
        else:
            return True
    def addCurr(self,curr):
        self.__seen.append(curr)
    def getColor(self):
        return self.__cm

def drawSpiral(turtle, dur, loudList, tempo, pal):
    turtle.hideturtle()
    turtle.shapesize(3,3,6)
    # turtle.speed(100) #testing
    if (0 < tempo <= 80):
        # print("slow")
        turtle.speed(3)
    elif (80 < tempo <= 140):
        # print("faster")
        turtle.speed(7)
    else:
        # print("fastest")
        turtle.speed(10.1)
    # print(tempo)
    tstart(turtle)
    spr = Spiralizer(dur)
    c = 0
    index = 0
    index2 = 0
    for ss in range(0,spr.getIts()):
        t.color("#"+pal[index2])
        bw = c - ss
        if (bw > 0 and spr.notInSeen(bw)):
            turtle.setheading(90)  # 90 degrees is pointing straight up
            # 180 degrees means "draw a semicircle"
            turtle.circle(5 * abs(loudList[index])/len(loudList), 180)
            # print(loudList[index]/10.0)
            turtle.width(loudList[index]/10.0)
            c = bw
            spr.addCurr(c)
            index = (index + 1)%len(loudList)
        else:
            turtle.setheading(270)  # 270 degrees is straight down
            turtle.circle(5 * abs(loudList[index])/len(loudList), 180)
            c += ss
            spr.addCurr(c)
            index = (index + 1)%len(loudList)
        index2 = (index2+1)%(len(pal)-1)

def startVisualizer(t):
    spotify.seek_track(0, device_id=None)
    songProps = dataRetrieve.dataRetrieve()
    t.reset()
    # dataRetrieve.restartCurrent()
    # win.bgpic(songProps["albumCover"])
    pal = colourChoice.choose_palette(songProps["danceability"],songProps["acousticness"])
    pal = colourChoice.energy_mod(pal,songProps["energy"])
    dummy = drawSpiral(t, songProps["duration"], songProps["sectionLoudness"], songProps["tempo"], pal)

# end visualizer code

#
# def update():
#     currSongName = songLabel.cget("text")
#     artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
#     songName = spotify.current_user_playing_track()['item']['name']
#     if currSongName != (songName + " - " + artistName):
#         # albumDisplayUpdate()
#         songLabel.config(text = (songName + " - " + artistName))
#         songID = spotify.current_user_playing_track()['item']['id']
#         # print(songID)
#         songProps = dataRetrieve.dataRetrieve(songID)
#         songEnergy = songProps["energy"]
#         songDanceability = songProps["danceability"]
#         songAcousticness = songProps["acousticness"]
#         setColors(songEnergy, songDanceability, songAcousticness)
#         canvas.delete(ALL)
#         newT = RawTurtle(canvas, visible=False)
#         newT.hideturtle()
#         startVisualizer(newT)
#     root.after(100, update)


root = tk.Tk()
root.title("Visualizer")
width  = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{int(width)}x{int(height)}')
# root.config(background="#1DB954")
# imagePrevious = ImageTk.PhotoImage(Image.open("assets/img/backward.png"))
# imagePlay = ImageTk.PhotoImage(Image.open("assets/img/play.png"))
# imagePause = ImageTk.PhotoImage(Image.open("assets/img/pause.png"))
# imageForward = ImageTk.PhotoImage(Image.open("assets/img/forward.png"))
# frame1 = Frame(root)
titleFrame = Frame(root)
titleFrame.pack(side=TOP)
# titleFrame.config(background="#1DB954")

songLabel = Label(titleFrame, pady=20, text="", font=("Gotham", 26), bg="white",fg="black")
artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
songName= spotify.current_user_playing_track()['item']['name']
startSongID = spotify.current_user_playing_track()['item']['id']
songLabel.config(text = (songName + " - "+ artistName))

topFrame = Frame(root)#definig a frame that will contain the Widgets
topFrame.pack(side=BOTTOM)
# topFrame.config(background="#1DB954")
#bottomFrame = Frame(root) #Similarly, definging the next Frame
#bottomFrame.pack(side=BOTTOM)

#---------GUI---------
songLabel.pack(side=LEFT, fill=X)
welcomeLabel = Label(root, font= ("Proxima Nova", 10), text="Close visualizer before changing song\n© Spotilizer 2019")
welcomeLabel.pack(side=BOTTOM)

canvas = tk.Canvas(master = root, bd=0, highlightthickness=0, relief='ridge', width = width, height = 700)
canvas.pack(side=TOP)
# canvas.config(background="#1DB954")

albumID = spotify.current_user_playing_track()['item']['album']['id']
imageURL = str(spotify.album(albumID)['images'][2]['url'])
imageName = 'albumCover_' + imageURL[56:60] + '.gif'
urllib.request.urlretrieve(imageURL, imageName)
albumCoverRaw = Image.open(imageName)
albumCover = ImageTk.PhotoImage(albumCoverRaw)
albumCoverRaw.close()
albumDisplay = Label(titleFrame, image=albumCover)
albumDisplay.pack(side=RIGHT,padx=5,pady=10)
# button1 = Button(topFrame, padx=10, pady=10, highlightbackground="#ffffff", relief=RAISED, highlightthickness=0, bd=0, cursor="hand", text="Previous", image=imagePrevious, command=lambda:[update(), previous(), albumDisplayUpdate()]) #Positioning Button as (<FrameName>,<Text to Appear>,<Text Color>)
# button1.pack(side=LEFT,padx=50,pady=20)
# button2 = Button(topFrame, padx=10, pady=10, highlightbackground="#ffffff", relief=RAISED, highlightthickness=0, bd=0, cursor="hand", text="Play", image=imagePlay, command=lambda:[update(), play(), albumDisplayUpdate()])
# button2.pack(side=LEFT,padx=50,pady=20)
# button3 = Button(topFrame, padx=10, pady=10, highlightbackground="#ffffff", relief=RAISED, highlightthickness=0, bd=0, cursor="hand", text="Pause", image=imagePause, command=lambda:[update(), pause(), albumDisplayUpdate()])
# button3.pack(side=LEFT,padx=50,pady=20)
# button4 = Button(topFrame, padx=10, pady=10, highlightbackground="#ffffff", relief=RAISED, highlightthickness=0, bd=0, cursor="hand", text="Forward", image=imageForward, command=lambda:[update(), forward(), albumDisplayUpdate()])
# button4.pack(side=LEFT,padx=50,pady=20)

t = RawTurtle(canvas, visible=False)
t.hideturtle()

startProps = dataRetrieve.dataRetrieve(startSongID)
startEnergy = songProps["energy"]
startDanceability = songProps["danceability"]
startAcousticness = songProps["acousticness"]
setColors(startEnergy, startDanceability, startAcousticness)

startVisualizer(t)



# root.after(100, update)
root.mainloop()
