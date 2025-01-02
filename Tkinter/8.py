#option menu
from tkinter import *
# def ok(v):
#     lb.config(text=v)
#     value.set("language")
sc = Tk()
sc.config(background="white")
sc.title("option menu")
sc.geometry("500x500")
# value = StringVar()
# value.set("language")
# l = ["python", "C", "Java"]
# op = OptionMenu(sc, value ,*l, command = ok)
# op.place(x = 100, y = 100, height = 30, width = 100)
# lb =  Label(sc, text = "")
# lb.place(x = 300, y = 100, height=30, width = 100)

#entry box
'''
entry is the linear data, while for multilines data we can use the text box
'''
def ok():
    lb1.config(text = v.get())
v = StringVar()
lb = Label(sc, text="Password", font=("Felix Titling", 10), bg="white")
lb.place(x = 100, y = 100)
en = Entry(sc, cursor="plus", show="*", justify="right", borderwidth=5, textvariable=v)
en.place(x = 100, y = 120)
b = Button(sc, text="Show",font=("Felix Titling", 10), bg="white", relief="flat", command=ok)
b.place(x= 100, y = 170)
lb1 = Label(sc, text="", font=("Segoe UI Light", 10), bg="pink")
lb1.place(x = 100, y = 200, height=20, width = 100)
sc.mainloop()