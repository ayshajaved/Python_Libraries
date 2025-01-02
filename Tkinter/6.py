from tkinter import *
#checkboxes
def but():
    lb.config(text= v.get())

sc = Tk()
sc.config(bg="pink")
sc.geometry("500x500+500+100")
sc.title("Checkboxes")
v = StringVar()
cb = Checkbutton(sc, text = "Female", font = (30), bg="pink", command=but, onvalue="Your language is python", offvalue="Your language is java",variable=v)
cb.deselect()
cb.pack()
lb = Label(sc, text = "", font=(30), bg="pink")
lb.pack()

#radiobutton
va = StringVar()
def ok():
    lb.config(text=va.get())
l = [("python", "p"), ("java", "j"), ("c", "c")]
for i in l:
    rb = Radiobutton(sc, text = i[0], value = i[1], variable=va, bg="pink", command=ok)
    rb.pack()
lb = Label(sc, text = "", font=(30), bg="pink")
lb.pack()

sc.mainloop()