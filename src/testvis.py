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
        self.t = Turtle(visible=False)
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

screen = Screen()
dummy = Display(screen,1/2 - screen.window_width()/2, screen.window_height()/2 - 1/2)
screen.mainloop()
