import matplotlib.pyplot as mt
#pylot is the designed module of the matplotlib library that is convenient and generate plots easily
x = [1,2,3,4,5]
y = [1,2,3,4,5]

mt.plot(x,y)
mt.xlabel("x-axis")
mt.ylabel("y-axis")

mt.title("First plot")
#showing a simple graph defining x axis label y axis label, the title of the graph
mt.show()