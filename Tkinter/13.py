'''
message box
showinfo() — notify that an operation completed successfully.
showerror() — notify that an operation hasn't completed due to an error.
showwarrning() notify that an operation completed but something didn't
behave as expected.'''
from tkinter import *
from tkinter.messagebox import showinfo, showerror, showwarning, askokcancel, askretrycancel
sc = Tk()
def test2():
    ans=askretrycancel(title="Enter your choice!", message="welcome to python learning")
    print(ans) #true is returned
    if ans:
        test2()
    else:
        print("Thankyou") #we can also print it in a label
def test1():
    # askokcancel(title="Enter your choice!", message="welcome to python learning")
    #we can also print the answer or the askokcancel
    ans=askokcancel(title="Enter your choice!", message="welcome to python learning")
    print(ans) #true is returned
def test():
    #we can use showerror and showwarning like this
    showinfo(title="Successful", message="Your task is successful!")  #two parameters, title and the message
b = Button(sc, text = "ok", command=test)
b.place(x = 10, y = 10, height=30, width=100)

#messagebox with ok or cancel options
b1 = Button(sc, text = "choice", command=test1)
b1.place(x = 140, y = 10, height=30, width=100)

#messagebox with retry or cancel
b2 = Button(sc, text = "choice_retry", command=test2)
b2.place(x = 260, y = 10, height=30, width=100)

#status bar in tkinter
st = Label(sc, text = "ready", relief="sunken", anchor=W, bd=5)
st.pack(side ="bottom", fill=X)

#colour choser
from tkinter.colorchooser import askcolor
def col():
    #the function returns a tuple, having colour number, code #
    ans = askcolor(title="python")
    print(ans) #((128, 207, 114), '#80cf72')
    sc.config(bg=ans[1]) #bg colour changes
bu = Button(sc,text = "pick colour",command=col)
bu.place(x = 380, y =10, height=30, width= 100  )

sc.mainloop()