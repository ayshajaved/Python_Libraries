#frame like div in the html, for easy target and creating blocks for efficient working
from tkinter import *
def new():
    nw = Toplevel(sc)
    nw.title("new window")
    nw.config(bg="black")
    l = Label(nw, text = "New window created!!")
    l.pack()
    nw.mainloop()

sc = Tk()
f1= Frame(sc, bd= 5, bg="pink")
f1.place(x=0, y = 0, height=400, width=400)
f2= Frame(sc, bd= 5, bg="red")
l = Label(f1, text="In pink", bg= "white")
l.place(x= 100, y= 100, width=100, height=100)
f2.place(x=400, y = 0, height=400, width=400)
f3= Frame(sc, bd= 5, bg="yellow")
f3.place(x=800, y = 0, height=400, width=400)

#top level
'''
it is the apearing of the new window on a function
'''
b = Button(f2, text="new window", bg="white",command= new)
b.place(x= 100, y= 100, width=100, height=100)

#canva
#it is used to draw shapes, lines, arcs in a window
cv= Canvas(f3, bg="blue")
cv.place(x= 10, y = 10, height=1000, width=1000 )
# coor = 10, 10, 300, 300
# cv.create_line(coor, fill= "yellow")
cor = 50, 50, 300, 300
# cv.create_arc(cor, start= 0, extent= 359.9, fill = "yellow")

#oval or circle
# cv.create_oval(20, 20, 300, 300, fill="green")
# cv.create_polygon(20,20,100,20,40,150, fill="green")
im = PhotoImage(file = "im.png")
cv.create_image(100,100 , image = im)
sc.mainloop()