from turtle import *
import time
import dataRetrieve

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

def drawSpiral(dur,loudList):
    t = Turtle(visible=False)
    t.speed(9)
    tstart(t)
    spr = Spiralizer(dur)
    c = 0
    c = 0
    index = 0
    for ss in range(0,spr.getIts()):
        bw = c - ss
        if (bw > 0 and spr.notInSeen(bw)):
            t.setheading(90)  # 90 degrees is pointing straight up
            # 180 degrees means "draw a semicircle"
            t.circle(5 * abs(loudList[index])/(len(loudList)/2), 180)
            c = bw
            spr.addCurr(c)
            index = (index + 1)%len(loudList)
        else:
            t.setheading(270)  # 270 degrees is straight down
            t.circle(5 * abs(loudList[index])/len(loudList), 180)
            c += ss
            spr.addCurr(c)
            index = (index + 1)%len(loudList)

def turtleConvert(x, y):  # converts from turtle pixels to the complex plane
    return complex(x / 50, y / 50)

class Mandelbrot:
    def __init__(self, dur):
        self.__dur = int(dur)
        self.__colormap = ['black', 'white']
        self.__cardinality = self.__dur

    def computeCardinality(self, c):
        z = 0
        self.__cardinality = self.__dur

        for i in range(self.__dur):
            z = z * z + c

            if abs(z) > 2:
                self.__cardinality = i
                return
    def getColor(self):
        if self.__cardinality == self.__dur:
            return self.__colormap[0]
        return self.__colormap[1]

def mbrotDisplay(dur):
    mandelbrot = Mandelbrot(dur)
    t = Turtle(visible=False)
    t.speed(0)
    tstart(t)
    tfinish = time.time() + dur
    win.tracer(0)
    while (time.time() < tfinish):
        currtime = int(time.time())
        for y in range(-151, 151):
            mandelbrot.computeCardinality(turtleConvert(currtime, y))
            t.color(mandelbrot.getColor())
            t.goto(y, y)
        t.up()
        t.goto(currtime+1, 151)
        t.down()
        win.update()
    win.tracer(1)

win = Screen()
win.setup(width=.75,height=.75)
songProps = dataRetrieve.dataRetrieve()
pos = [win.window_width(),win.window_height()]
dummy = drawSpiral(songProps["duration"],songProps["sectionLoudness"])
win.mainloop()
