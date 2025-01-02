from tkinter import *
#menu button
sc = Tk()
sc.geometry("500x500")
sc.title("Notepad")
m = Menubutton(sc, text = "language")
m.menu = Menu(m)   #we can pass tearoff parameter as 0 to stop the movement of the menu
m["menu"] = m.menu
m.menu.add_checkbutton(label="Python")
m.menu.add_checkbutton(label="Java")
m.menu.add_checkbutton(label="C")
m.pack()

#menu
file_menu = Menu(sc) #file_menu is the obj of the menu at screen
f_menu = Menu(file_menu,tearoff=0 ) #f_menu is holding the file_menu
f_menu.add_command(label="Open file") #commands are added in the f_menu
f_menu.add_command(label="New file")
f_menu.add_command(label="Save file")
sc.config(menu=file_menu) #file_menu is added in the screen
file_menu.add_cascade(label="file", menu=f_menu) #name of file_menu is added using cascade function

f1_menu = Menu(file_menu,tearoff=0 ) #f_menu is holding the file_menu
f1_menu.add_command(label="Undo") #commands are added in the f_menu
f1_menu.add_command(label="redo")
f1_menu.add_separator() #sepeartor is added
f1_menu.add_command(label="copy")
sc.config(menu=file_menu) #file_menu is added in the screen, this can be erased and only once it can be written above the all
file_menu.add_cascade(label="functions ", menu=f1_menu) 

#menu in menu, submenu
file_menu = Menu(sc) #file_menu is the obj of the menu at screen
sc.config(menu=file_menu) #file_menu is added in the screen
#file
f_menu = Menu(file_menu,tearoff=0 ) #f_menu is holding the file_menu
f_menu.add_command(label="Open file") #commands are added in the f_menu
f_menu.add_command(label="New file")
f_menu.add_command(label="Save file")
file_menu.add_cascade(label="file", menu=f_menu) #name of file_menu is added using cascade function
#sub menu is added
sub_menu = Menu(f_menu, tearoff=0)
sub_menu.add_command(label="yes")
sub_menu.add_command(label="no")
f_menu.add_cascade(label="options",menu = sub_menu) 
#functions
f1_menu = Menu(file_menu,tearoff=0 ) #f_menu is holding the file_menu
f1_menu.add_command(label="Undo") #commands are added in the f_menu
f1_menu.add_command(label="redo")
f1_menu.add_separator() #sepeartor is added
f1_menu.add_command(label="copy")
file_menu.add_cascade(label="functions ", menu=f1_menu) 



sc.mainloop()