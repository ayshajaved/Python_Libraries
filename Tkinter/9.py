from tkinter import *
#text box
sc =Tk()
def ok():
    v = t.get("1.0", "end")
    l1.config(text = v)
sc.config(bg="pink")
sc.geometry("500x500")
sc.title("Text box")
t = Text(sc, font= ("Felix Titling", 10), bg="white")
t.place(x =50, y =50, height= 200)
l = Button(sc, text = "Done", bg="pink", font= ("Felix Titling",20), command = ok)
l.place(x = 50, y = 270)
l1 = Label(sc, text = "", bg="pink", font= ("Felix Titling",10), justify="left")
l1.place(x = 50, y = 350)


 




sc.mainloop()