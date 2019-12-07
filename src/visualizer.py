from turtle import *
import time
#from colourChoice import *

def tstart(turtle):
    turtle.penup()
    turtle.goto(1/2 - pos[0]/2, 1/2)
    turtle.pendown()

def modelSel(lLevel):
    if (lLevel >= -10):
        return 'mbrot'
    elif (-15 <= lLevel < -10):
        return 'temp'
    else:
        return 'spiral'

class Mandelbrot:
    def __init__(self):
        self.__colormap = ["#FFFFFF","#000000"]

class Spiralizer:
    def __init__(self,dur=120):#,colors,dur,winwidth):
        self.__cm = ['red']#colourChoice.getPalette() #Returns the colour palette for the current song.
        self.__factor = 120*(960/120)#song.length*(winwidth/song.length) #Assign the length of the song to a dur variable
        self.__seen = []
        self.__its = int(dur)
    def getIts(self):
        return self.__its
    def notInSeen(self,curr):
        if not(curr in self.__seen):
            return True
        else:
            return False
    def addCurr(self,curr):
        self.__seen.append(curr)
    def getColor(self):
        return self.__cm

def drawSpiral():
    t = Turtle(visible=False)
    t.speed(5)
    tstart(t)
    spr = Spiralizer()
    c = 0
    tfinish = time.time() + 120
    while(time.time() < tfinish):
        ss = tfinish - time.time()
        print(ss)
        bw = c - ss
        if (bw > 0 and spr.notInSeen(bw)):
            t.setheading(90)  # 90 degrees is pointing straight up
            # 180 degrees means "draw a semicircle"
            t.circle(2 * ss/2, 180)
            c = bw
            spr.addCurr(c)
        else:
            t.setheading(270)  # 270 degrees is straight down
            t.circle(2 * ss/2, 180)
            c += ss
            spr.addCurr(c)

win = Screen()
win.setup(width=.75,height=.75)
pos = [win.window_width(),win.window_height()]
dummy = drawSpiral()
win.mainloop()
