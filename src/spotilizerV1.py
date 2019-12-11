import turtle
from turtle import Turtle, Screen
import time
import dataRetrieve
import colourChoice
from tkinter import *
import tkinter as tk
import authentication

spotify = authentication.getSpotify()

class Display:
    def __init__(self, screen,startx,starty):

        songProps = dataRetrieve.dataRetrieve()
        # pos = [win.window_width(),win.window_height()]
        pal = colourChoice.choose_palette(songProps["danceability"],songProps["acousticness"])
        pal = colourChoice.energy_mod(pal,songProps["energy"])
        dur = 100
        self.t = turtle.RawTurtle(canvas)
        self.t = Turtle(visible=False)
        self.t.shapesize(3,3,6)
        self.t.speed(9)
        # tstart(self.t)
        spr = Spiralizer(dur)
        c = 0
        c = 0
        index = 0
        index2 = 0
        # win.bgcolor("#"+pal[len(pal)-1])
        for ss in range(0,spr.getIts()):
            self.t.color("#"+pal[index2])
            bw = c - ss
            if (bw > 0 and spr.notInSeen(bw)):
                self.t.setheading(90)  # 90 degrees is pointing straight up
                # 180 degrees means "draw a semicircle"
                # t.circle(5 * abs(loudList[index])/len(loudList), 180)
                c = bw
                spr.addCurr(c)
                # index = (index + 1)%len(loudList)
            else:
                self.t.setheading(270)  # 270 degrees is straight down
                # t.circle(5 * abs(loudList[index])/len(loudList), 180)
                c += ss
                spr.addCurr(c)
                # index = (index + 1)%len(loudList)
            index2 = (index2+1)%(len(pal)-1)


        # self.t.setpos(startx,starty)
        # self.t.speed(0)
        # spr = Spirals()
        # c = 0
        # for ss in range(0,spr.getIts()):
        #     bw = c - ss
        #     if (bw > 0 and spr.notInSeen(bw)):
        #         self.t.setheading(90)  # 90 degrees is pointing straight up
        #         # 180 degrees means "draw a semicircle"
        #         self.t.circle(5 * ss/2, 180)
        #         c = bw
        #         spr.addCurr(c)
        #     else:
        #         self.t.setheading(270)  # 270 degrees is straight down
        #         self.t.circle(5 * ss/2, 180)
        #         c += ss
        #         spr.addCurr(c)

def tstart(turtle):
    turtle.penup()
    turtle.goto(1/2 - pos[0]/2, 1/2)
    turtle.pendown()

# def modelSel(lLevel):
#     if (lLevel >= -10):
#         return 'mbrot'
#     elif (-15 <= lLevel < -10):
#         return 'temp'
#     else:
#         return 'spiral'

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

# def drawSpiral(dur,loudList):
#     t = Turtle(visible=False)
#     t.shapesize(3,3,6)
#     t.speed(9)
#     tstart(t)
#     spr = Spiralizer(dur)
#     c = 0
#     c = 0
#     index = 0
#     index2 = 0
#     win.bgcolor("#"+pal[len(pal)-1])
#     for ss in range(0,spr.getIts()):
#         t.color("#"+pal[index2])
#         bw = c - ss
#         if (bw > 0 and spr.notInSeen(bw)):
#             t.setheading(90)  # 90 degrees is pointing straight up
#             # 180 degrees means "draw a semicircle"
#             t.circle(5 * abs(loudList[index])/len(loudList), 180)
#             c = bw
#             spr.addCurr(c)
#             index = (index + 1)%len(loudList)
#         else:
#             t.setheading(270)  # 270 degrees is straight down
#             t.circle(5 * abs(loudList[index])/len(loudList), 180)
#             c += ss
#             spr.addCurr(c)
#             index = (index + 1)%len(loudList)
#         index2 = (index2+1)%(len(pal)-1)

def turtleConvert(x, y):  # converts from turtle pixels to the complex plane
    return complex(x / 50, y / 50)

# class Mandelbrot:
#     def __init__(self, dur):
#         self.__dur = int(dur)
#         self.__colormap = ['black', 'white']
#         self.__cardinality = self.__dur
#
#     def computeCardinality(self, c):
#         z = 0
#         self.__cardinality = self.__dur
#
#         for i in range(self.__dur):
#             z = z * z + c
#
#             if abs(z) > 2:
#                 self.__cardinality = i
#                 return
#     def getColor(self):
#         if self.__cardinality == self.__dur:
#             return self.__colormap[0]
#         return self.__colormap[1]
#
# def mbrotDisplay(dur):
#     mandelbrot = Mandelbrot(dur)
#     t = Turtle(visible=False)
#     t.speed(0)
#     tstart(t)
#     tfinish = time.time() + dur
#     win.tracer(0)
#     while (time.time() < tfinish):
#         currtime = int(time.time())
#         for y in range(-151, 151):
#             mandelbrot.computeCardinality(turtleConvert(currtime, y))
#             t.color(mandelbrot.getColor())
#             t.goto(y, y)
#         t.up()
#         t.goto(currtime+1, 151)
#         t.down()
#         win.update()
#     win.tracer(1)


def play():
    artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
    songName= spotify.current_user_playing_track()['item']['name']
    #root.screenMessage.set(songName + "-"+ artistName)
    songLabel.config(text = (songName + " - " + artistName))
    try:
        spotify.start_playback(device_id=None, context_uri=None, uris=None, offset=None)
    except:
        return None


def previous():
    spotify.previous_track(device_id=None)
    artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
    songName= spotify.current_user_playing_track()['item']['name']
    songLabel.config(text = (songName + " - "+ artistName))

def pause():
    try:
        spotify.pause_playback(device_id=None)
    except:
        return None

def forward():
    spotify.next_track(device_id=None)
    artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
    songName= spotify.current_user_playing_track()['item']['name']
    songLabel.config(text = (songName + " - "+ artistName))

#image = Image.open("play.png")
#photo = ImageTk.PhotoImage(image)

#screen = Screen()


root = tk.Tk()
canvas = tk.Canvas(master = root, width = 500, height = 500)
#print(canvas)
canvas.pack()
#t = turtle.RawTurtle(canvas)
# imagePlay = PhotoImage(file="assets/img/play.png")
# imageForward = PhotoImage(file="assets/img/forwards.png")
# imageBackward = PhotoImage(file="assets/img/backward.png")
# imagePause = PhotoImage(file="assets/img/pause.png")
frame1 = Frame(root)

welcomeLabel = Label(root, text="Welcome to Spotilizer", bg="orange",fg="white")
welcomeLabel.pack(fill=X)
songLabel = Label(root, text="", bg="green",fg="white")
songLabel.pack(fill=X)
artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
songName= spotify.current_user_playing_track()['item']['name']
songLabel.config(text = (songName + " - "+ artistName))

topFrame = Frame(root)#definig a frame that will contain the Widgets
topFrame.pack()
#bottomFrame = Frame(root) #Similarly, definging the next Frame
#bottomFrame.pack(side=BOTTOM)

#---------Various Buttons----------

button1 = Button(topFrame, text="Previous", image=None, command=previous) #Positioning Button as (<FrameName>,<Text to Appear>,<Text Color>)
button1.pack(side=LEFT,padx=5,pady=20)
button2 = Button(topFrame, text="Play",image=None, command=play)
button2.pack(side=LEFT,padx=5,pady=20)
button3 = Button(topFrame, text="Pause",image=None, command=pause)
button3.pack(side=LEFT,padx=5,pady=20)
button5 = Button(topFrame, text="Forward",image=None, command=forward)
button5.pack(side=LEFT,padx=5,pady=20)

dummy = Display(canvas,1/2 - canvas.winfo_width()/2, canvas.winfo_height()/2 - 1/2)

root.mainloop()#refreshing the window so that it stays on the screen

# win = Screen()
# win.setup(width=.75,height=.75)
# songProps = dataRetrieve.dataRetrieve()
# pos = [win.window_width(),win.window_height()]
# pal = colourChoice.choose_palette(songProps["danceability"],songProps["acousticness"])
# pal = colourChoice.energy_mod(pal,songProps["energy"])
# dummy = drawSpiral(songProps["duration"],songProps["sectionLoudness"])
