#bind function
from tkinter import *
sc = Tk()
def ok(event): #one positional argumnet has to pass
    print("hello python!")
def ok1(event): #one positional argumnet has to pass
    print("hello ayesha!")
def ok2():
    print("hello bitmap!")
b = Button(sc, text = "press")
b.pack()
b.bind('<Button>',ok )
#without passing command, bind is functioning
# now, the third parameter is add that is used when two functions have to be used
b.bind("<Button>", ok1, add="+")

#standered attributes of tkinter
'''Standard Attributes
Dimensions --> height width
The coordinate system 
Colors
Type fonts
Anchors
Relief styles
Bitmaps
For bitmap options in widgets, these bitmaps are guaranteed to be available:
The graphic above shows Button widgets bearing the standard bitmaps.
'error', •gray75', •gray50', •gray25', •gray12', 'hourglass', 'info', •questhead', •question' 'warning'.
Cursors
Images
Geometry strings'''
b = Button(sc, bitmap="questhead", command=ok2, cursor="boa   t")
b.pack()
'''
The Photolmage class : To display a color image in .gif, .pgm, or .ppm
format, you will need this constructor:
tk.Photolmage(file=f)
The Bitmaplmage class To display a two-color image in the .xbm for
you will need this constructor:
tk.Bitmaplmage(file=f[, background=b][, foreground=c])
Label(image=logo).grid()
'''

sc.mainloop()