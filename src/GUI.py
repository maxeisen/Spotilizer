from tkinter import *
import tkinter as tk
import turtle
import authentication

spotify = authentication.getSpotify()
print(spotify.current_playback(market=None))


import math
class Mandelbrot:
    def __init__(self, limit=100):
        self.__limit = int(limit)
        self.__colormap = ['black', 'white']
        self.__cardinality = self.__limit

    def computeCardinality(self, c):
        z = 0
        self.__cardinality = self.__limit

        for i in range(self.__limit):
            z = z * z + c

            if abs(z) > 2:
                self.__cardinality = i
                return

    def getColor(self):
        if self.__cardinality == self.__limit:
            return self.__colormap[0]
        return self.__colormap[1]

class Spirals:
    def __init__(self,its=100):
        self.__its = int(its)
        self.__colormap = ['black']
        self.__seen = []
    def getColor(self):
        return self.__colormap
    def getIts(self):
        return self.__its
    def addCurr(self,current):
        self.__seen.append(current)
    def notInSeen(self,current):
        if (current in self.__seen):
            return False
        else:
            return True

from turtle import Turtle, Screen

class Display:
    def __init__(self, screen,startx,starty):
        self.t = turtle.RawTurtle(canvas)
        #self.t = Turtle(visible=False)
        self.t.setpos(startx,starty)
        self.t.speed(0)
        spr = Spirals()
        c = 0
        for ss in range(0,spr.getIts()):
            bw = c - ss
            if (bw > 0 and spr.notInSeen(bw)):
                self.t.setheading(90)  # 90 degrees is pointing straight up
                # 180 degrees means "draw a semicircle"
                self.t.circle(5 * ss/2, 180)
                c = bw
                spr.addCurr(c)
            else:
                self.t.setheading(270)  # 270 degrees is straight down
                self.t.circle(5 * ss/2, 180)
                c += ss
                spr.addCurr(c)
        # mandelbrot = Mandelbrot()
        #
        # for x in range(-150, 255):
        #     for y in range(-150, 255):
        #         mandelbrot.computeCardinality(turtleConvert(x, y))
        #         self.t.color(mandelbrot.getColor())
        #         self.t.goto(x, y)
        #     self.t.up()
        #     self.t.goto(x+1, -150)
        #     self.t.down()
        #     screen.update()


def turtleConvert(x, y):  # converts from turtle pixels to the complex plane
    return complex(x / 100, y / 100)




def play():
    artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
    songName= spotify.current_user_playing_track()['item']['name']
    #root.screenMessage.set(songName + "-"+ artistName)
    songLabel.config(text = (songName + "- "+ artistName))
    try:
        spotify.start_playback(device_id=None, context_uri=None, uris=None, offset=None)
    except:
        return None


def previous():
    spotify.previous_track(device_id=None)
    artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
    songName= spotify.current_user_playing_track()['item']['name']
    songLabel.config(text = (songName + "- "+ artistName))

def pause():
    try:
        spotify.pause_playback(device_id=None)
    except:
        return None

def forward():
    spotify.next_track(device_id=None)
    artistName = spotify.current_user_playing_track()['item']['album']['artists'][0]['name']
    songName= spotify.current_user_playing_track()['item']['name']
    songLabel.config(text = (songName + "- "+ artistName))

#image = Image.open("play.png")
#photo = ImageTk.PhotoImage(image)

#screen = Screen()


root = tk.Tk()
canvas = tk.Canvas(master = root, width = 500, height = 500)
#print(canvas)
canvas.pack()
#t = turtle.RawTurtle(canvas)
imagePlay = PhotoImage(file="assets/img/play.png")
imageForward = PhotoImage(file="assets/img/forwards.png")
imageBackward = PhotoImage(file="assets/img/backward.png")
imagePause = PhotoImage(file="assets/img/pause.png")
frame1 = Frame(root)

welcomeLabel = Label(root, text="Welcome to Spoilizer", bg="orange",fg="white")
welcomeLabel.pack(fill=X)
songLabel = Label(root, text="", bg="green",fg="white")
songLabel.pack(fill=X)

topFrame = Frame(root)#definig a frame that will contain the Widgets
topFrame.pack()
#bottomFrame = Frame(root) #Similarly, definging the next Frame
#bottomFrame.pack(side=BOTTOM)

#---------Various Buttons----------

button1 = Button(topFrame, text="Previous", image=imageBackward, command=previous) #Positioning Button as (<FrameName>,<Text to Appear>,<Text Color>)
button1.pack(side=LEFT,padx=5,pady=20)
button2 = Button(topFrame, text="Play",image=imagePlay, command=play)
button2.pack(side=LEFT,padx=5,pady=20)
button3 = Button(topFrame, text="Pause",image=imagePause, command=pause)
button3.pack(side=LEFT,padx=5,pady=20)
button5 = Button(topFrame, text="Forward",image=imageForward, command=forward)
button5.pack(side=LEFT,padx=5,pady=20)

root.screenMessage = StringVar()
label = Message( root, textvariable=root.screenMessage, relief=RAISED )
root.screenMessage.set("Welcome to Spoilizer")
label.pack(side=BOTTOM,fill=X)
dummy = Display(canvas,1/2 - canvas.winfo_width()/2, canvas.winfo_height()/2 - 1/2)

root.mainloop()#refreshing the window so that it stays on the screen
