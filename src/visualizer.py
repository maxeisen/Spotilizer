from turtle import *

def tstart(turtle,swin):
    pos = [swin.window_width(),swin.window_height()]
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



win = Screen()
win.setup(width=.75,height=.75)
t = Turtle(visible= False)
t2 = Turtle(visible= False)
tstart(t,win)
tstart(t2,win)
t.showturtle()
t2.showturtle()



win.mainloop()
