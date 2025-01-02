'''
GUI is the graphical user interface, is a system of interactive visual components for the computer software
GUI displays objects that convey information, and represent actions tat can be taken by the user, the objects change size, colour
and visibility when the user interact with them 
GUI libraries in python
1) tkinter
2)pyQT
3)kiwi (mobile application)
4)pysimple
tkinter is the gui tkinter is the standard Python library used for creating graphical user interfaces (GUIs). It provides tools to design and manage windows, buttons, labels, text boxes, and other GUI elements in a Python program
Tkinter Widgets
Button
Canvas
Checkbutton
Entry
Frame
Label
Listbox
Menubutton
Menu
Message
Operator & Description
Radiobutton
Scale
Scrollbar
Text
Toplevel
Spinbox
PanedWindow
LabelFrame
tkMessageBox
"attributes"
Dimensions
Colors
Fonts
 
Relief styles
Bitmaps
Cursors
"Geometry Management"
The pack() Method
The grid() Method
The place() Method
'''
from tkinter import *  
screen = Tk()
#the part in between will be the window characteristics 
screen.title("***MY GUI***")
screen.iconbitmap("C:/Users/DELL/Downloads/1.ico")     #pass .ico format icon image
# screen.config(background= "#a3216f") #HEX code for colour
screen.config(bg = "black") #another way
# screen["bg"] = "white"
# screen.attributes('-alpha', 0.8)  #transparency ,  0-1
# screen.geometry("500x500+100+10") #the 500x 500 is the dimension(width X height) in pixels and the +100 is the y position and +10 is the x position
#now to put the screen exact in the center we have to calculate the center point of the window
# wid = 500
# height = 500
# sys_he = screen.winfo_screenheight()
# sys_wid = screen.winfo_screenwidth()
# # print(sys_he, sys_wid) #720 1280
# center_x = int(sys_wid/2 - wid/2)
# center_y = int(sys_he/2 - height/2)
# screen.geometry(f"{wid}x{height}+{center_x}+{center_y}")
#alternatively very simple way, to be the window in center below:
# screen.geometry("1280x720+0+0") #widhxheight

#fixing the min and max size of te window
# screen.minsize(100,100)
# screen.maxsize(500, 500)

#offing the resizable functiom
screen.geometry("500x500")
screen.resizable(True, True) #passing height, and width parameters as false 

#we can print l.config() to know all the functions of the this config
print(screen.config())
screen.mainloop()
 
