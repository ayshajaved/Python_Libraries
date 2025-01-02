'''
There are 4 tkinter variables :
BooleanVar()
StringVar()
IntVar()
DoubleVar()
var = Tkinter variable(master, value = any_value)
'''
'''
variable setter and getter
get()
set()
getvar() setvar() these are used when the name parameter is used
'''
from tkinter import *
sc = Tk()
v = StringVar(sc, value = "python")
print(v) #gives an encrypted location for the value
print(v.get()) #gives the value

#we can also set
# va = IntVar(sc)
# va.set(12)
# print(va.get())

#parameters 
# v = StringVar(sc, value="hy i am ayesha", name = "2")
# print(v.get())
# #using getvar()
# print(sc.getvar("2"))  #by name

#lable parameters
# sc["bg"] = "yellow"
# l = Label(sc, text = "hello \n i am \n ayesha", font = ("Lucida Bright", 20), bg = "white", cursor="plus", relief= "raised",underline=1 ,justify="left")
# l.place(x = 100, y = 200)

#user input of text in run time
sc["bg"] = "yellow"
entry = input("Enter:- ")
v = StringVar()
l = Label(sc,textvariable=v, font = ("Lucida Bright", 20), bg = "white", cursor="plus", relief= "raised", justify="left")
l.place(x = 100, y = 200)
v.set(entry)







sc.mainloop()
