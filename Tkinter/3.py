'''
grid()
The grid() method has the following parameters:
column, row, rowspan, columnspan, sticky, padx, pady,
ipad, ipady
'''
from tkinter import *
sc = Tk()
sc['bg'] = "black"
sc.geometry("500x500")
l1 = Label(sc, text="hello", font=("castellar", 20), bg="pink")
# l1.grid()
# #initially, row and column value is 0
l1.grid(padx = 20,  row=0)
l2 = Label(sc, text="bye", font=("Castellar", 20), bg="pink")
l2.grid(padx= 100, row=8)
# '''
# When you specify row=8 for the second label, it is indeed placed in the 8th row, 
# but there are no other widgets or content in the intervening rows (1 to 7). This 
# results in a large gap between the first and second labels, causing the second label 
# to be pushed far down the window, potentially outside the visible area if the window is small.
# '''
# #column span will be studied when we will learn the frames
# sc.mainloop()

'''
The place() method has the following parameters:
x, y, relx, rely, width, height, relwidth, relheight, anchor
'''
# from tkinter import *
# sc = Tk()
# sc['bg'] = "black"
# sc.geometry("500x500")
# l = Label(sc, text="hello", font=("Castellar", 10), bg="pink")
# l.place(x= 10, y=10, height=50, width=50)

# l1 = Label(sc, text="bye", font=("Castellar", 10), bg="pink")
# l1.place(x= 10, y=70, height=50, width=50)
sc.mainloop()