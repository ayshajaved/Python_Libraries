#window sepeartor
from tkinter import *
from tkinter import ttk

sc =Tk()
sc.geometry("500x500")
sc.title("sepeartor")
l1 = Label(sc, text = "python", font= ("Felix Titling",10))
l1.pack()
sep = ttk.Separator(sc, orient="horizontal")
sep.pack(fill=X)
l2 = Label(sc, text = "java", font= ("Felix Titling",10))
l2.pack()

#vertical seperator
sc =Tk()
sc.geometry("500x500")
sc.title("sepeartor")
l1 = Label(sc, text = "python", font= ("Felix Titling",10))
l1.pack(side = "right")
sep = ttk.Separator(sc, orient="vertical")
sep.pack(fill=Y, side="right")
l2 = Label(sc, text = "java", font= ("Felix Titling",10))
l2.pack(side="right")
sc.mainloop()