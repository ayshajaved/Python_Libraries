'''
treeview, heirarical pattern
'''
from tkinter import *
from tkinter import ttk
sc = Tk()
l = Label(text ="Ayesha javed")
l.pack()
tr = ttk.Treeview(sc) 
tr.insert("", END, text = "PYTHON", iid=0)
tr.insert("", END, text = "JAVA", iid=1)
tr.insert("", END, text = "WEB", iid=2)

tr.insert("", END, text = "ML", iid= 3)
tr.insert("", END, text = "DS", iid= 4)
tr.insert("", END, text = "HTML", iid= 5)
tr.insert("", END, text = "CSS", iid= 6)
tr.insert("", END, text = "JAVASCRIPT", iid= 7)
tr.move(3,0,0)
tr.move(4,0,1)
tr.move(5,2,0)
tr.move(6,2,1)
tr.move(7,2,2)

tr.pack()
sc.mainloop()