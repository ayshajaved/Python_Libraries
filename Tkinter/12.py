#notebook pattern
from tkinter import *
from tkinter import ttk
sc = Tk()
n = ttk.Notebook(sc)
n.pack(pady = 10, expand=True)
f = ttk.Frame(n, height=100, width=100)
f.pack(fill= "both", expand=True)
l = Label(f, text="hy python")
l.place(x = 10, y =10)
f1 = ttk.Frame(n, height=500, width=500)
f1.pack(fill= "both", expand=True)
l1 = Label(f1, text="hy java")
l1.place(x = 10, y =10)
n.add(f, text="PYTHON")
n.add(f1, text="JAVA")

#scrolled text is the smart way instead of using the text box and the scrolled bar
#for this the class of scrolledtext is called, where there is the function of ScrolledText
from tkinter.scrolledtext import ScrolledText
s = ScrolledText(sc)
s.pack()





sc.mainloop()