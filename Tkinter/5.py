from tkinter import *
def py():
    l2.config(text="yes")
sc = Tk()
sc["bg"] = "pink"
sc.geometry("1100x600+90+30")
# image = PhotoImage(file="im.png")
# lb = Label(sc, image=image)
# lb.place(x = 100, y = 100)
# # l1= Label(sc, text = "Ayesha Javed", font= ("Bodoni MT", 30), bg = "pink")
# # l1.place(x= 100,  y = 20)

# #compouund can be used
# lb = Label(sc, image=image, text = "ayesha javed", compound="right", bg="pink", font=(20)) 
# lb.place(x = 100, y = 100)

# #label frame
# #a label with the buttons
lf = LabelFrame(sc, text="Python", font=(20), labelanchor="n", bg="pink")
lf.place(x= 100, y = 100, height=100, width=400)
# #the lable anchor defines the position of the label frame name
# #label can be added in this frame
l = Label(sc, text="Java", font=(20), bg="pink")
l.place(x= 150, y = 150)

l1 = Label(sc, text="C", font=(20), bg="pink")
l1.place(x= 250, y = 150)


l1 = Label(sc, text="HTML", font=(20), bg="pink", fg= "green")
l1.place(x= 350, y = 150)

# #fg is the font colour#
#buttton
b = Button(sc, text = "ON", bg= "orange", relief= "raised",font=(20), command=py)
b.place(x =150, y =350)  
#command is used to call a function and then perform a function like when the button is pressed, no is converted to off
l2 = Label(sc, text="no", font=(20), bg="pink", fg= "green")
l2.place(x= 150, y = 450)
sc.mainloop()