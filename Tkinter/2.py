#layout management
'''
Pack
— show you how to use the pack geometry
manager to arrange widgets on a window.
Grid — learn how to use the grid geometry manager to
place widgets on a container.
Place — show you how to use the place geometry
manager to precisely position widgets within its
container using the (x, y) coordinate system.
'''
'''
The pack geometry manager has many configurations.
Most Commonly Used Options:
fill, expand, side, ipadx, ipady, padx, and pady.
'''
from tkinter import *
sc = Tk()
sc.config(bg="black")
sc.geometry("500x500")
sc.title("lables")
#makinng a lable
# lb = Label(sc, text="Ayesha", font = ("Lucida Bright", 40, "italic"), bg="yellow")
# lb.pack()
#we can pass arguments in this so that to specify the positions
# lb.pack(padx= 10, pady = 100, fill = "x")
#padx and pady are the distance from the x and y axis and the fill is used to fill the entire row
#there are also ipadx and ipady functions for the alignment of the text in the lable
# lb.pack(padx= 10, pady = 100, ipadx=100, ipady=50, expand = True)
#expand function is used to align it in the center
'''
side function is used to align the two lables
# '''
lb = Label(sc, text="Ayesha", font = ("Lucida Bright", 40, "italic"), bg="yellow")
lb.pack(padx=20,side="left")

lb1 = Label(sc, text="javed", font = ("Lucida Bright", 40, "italic"), bg="yellow")
lb1.pack(padx= 20, side="left")





sc.mainloop()