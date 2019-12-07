from tkinter import *
import authentication

spotify = authentication.getSpotify()
print(spotify.current_playback(market=None))





def play():
    print(spotify.current_user_playing_track())
    try:
        spotify.start_playback(device_id=None, context_uri=None, uris=None, offset=None)
    except:
        return None
    root.screenMessage.set("heythere")
    print("dfdf")

def previous():
    spotify.previous_track(device_id=None)

def pause():
    try:
        spotify.pause_playback(device_id=None)
    except:
        return None

def forward():
    spotify.next_track(device_id=None)

#image = Image.open("play.png")
#photo = ImageTk.PhotoImage(image)

root = Tk()
imagePlay = PhotoImage(file="src/assets/img/play.png")
imageForward = PhotoImage(file="src/assets/img/forwards.png")
imageBackward = PhotoImage(file="src/assets/img/backward.png")
imagePause = PhotoImage(file="src/assets/img/pause.png")
frame1 = Frame(root)

one = Label(root, text="Welcome", bg="orange",fg="white")
one.pack(fill=X)
two = Label(root, text="To Deejay Music Player", bg="white",fg="blue")
two.pack(fill=X)
three = Label(root, text="Created By Dhananjay and Kushagra", bg="green",fg="white")
three.pack(fill=X)

topFrame = Frame(root)#definig a frame that will contain the Widgets
topFrame.pack()
bottomFrame = Frame(root) #Similarly, definging the next Frame
bottomFrame.pack(side=BOTTOM)

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
root.screenMessage.set("Welcome, to Deejay Music Player")
label.pack(side=BOTTOM,fill=X)
root.mainloop()#refreshing the window so that it stays on the screen
