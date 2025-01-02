import matplotlib.pyplot as mt
#pylot is the designed module of the matplotlib library that is convenient and generate plots easily
x = [1,2,3,4,5]
y = [1,2,3,4,5]

# mt.plot(x,y)
mt.xlabel("x-axis")
mt.ylabel("y-axis")

mt.title("First plot")
#showing a simple graph defining x axis label y axis label, the title of the graph
#Now i will customize the plot

mt.plot(x,y, color = "red", linestyle = "--", label = 'Data Line', marker = "o")
mt.legend() #A legend is a box or area within the plot that provides labels for the elements in the graph, such as lines, markers, or other graphical elements. Each label explains what the corresponding element represents.
mt.xlim(0,5)  #setting limit for x axix
mt.ylim(0,5)  #setting limit for y axis
mt.grid(True) #grid is used to show the grid lines on the plot
mt.show()