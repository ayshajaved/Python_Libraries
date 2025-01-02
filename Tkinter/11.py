from tkinter import *
from tkinter import ttk
#spinbox
sc = Tk()
s = Spinbox(sc, from_=0, to=20, wrap=True)
s.pack()
def ok(a):
    l.config(text=str(v.get()))

#we can use the wrap function so that after 20, rotation occurs
v = DoubleVar()
s = Scale(sc, from_=0, to= 100, orient= HORIZONTAL, variable=v, command=ok)
s.pack()
l = Label(sc, text = "", font= (30))
l.pack()

# command of scale/ slider takes the function argument atleast one

#scroll bar
t = Text(sc, font = (30) )
t.place(x= 100, y =100, height=100, width=100)
s = Scrollbar(sc, orient=VERTICAL, command=t.yview)
s.place(x=200, y = 100, height=100, width=20)
t["yscrollcommand"] = s.set #it betters the communication between the scroll bar and text
#combo box
l = ["python", "java", "C"]
c = ttk.Combobox(sc, values=l)
c.place(x =200, y =250)
c.set("select")

sc.mainloop()