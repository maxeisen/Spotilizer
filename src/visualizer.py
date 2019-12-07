from turtle import *
import random
#dur = song time #Length of the song / how long the drawing will go on for.

def turn(i):
    left = (((i & -i) << 1) & i) != 0
    return 'L' if left else 'R'

def curve(iteration):
    return ''.join([turn(i + 1) for i in range(2 ** iteration - 1)])

if __name__ == '__main__':
    hideturtle()
    speed(20)
    i = 1
    mincols = 5
    maxcols = 255
    while True:
        if turn(i) == 'L':
            circle(-4, 90, 36)
        else:
            circle(4, 90, 36)
        i += 1
