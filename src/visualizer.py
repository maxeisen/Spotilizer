from turtle import *
import time
#from colourChoice import *

def tstart(turtle):
    turtle.penup()
    turtle.goto(1/2-pos[0]/2,pos[1]/2 -1/2)
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
    def __init__(self,colors,dur,winwidth):
        self.__cm = colourChoice.getPalette() #Returns the colour palette for the current song.
        self.__factor = song.length*(winwidth/song.length) #Assign the length of the song to a dur variable
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

win = Screen()
win.setup(width=.75,height=.75)
pos = [win.window_width(),win.window_height()]
dummy = DrawSpiral(win)
win.mainloop()
