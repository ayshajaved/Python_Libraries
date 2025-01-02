import matplotlib.pyplot as plot

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]
colors = [50,60,70,80,90]
# Scatter Plot
# plot.scatter(x, y, color='blue', label='Data Points',marker='x',s=100) #s is the size of the marker

plot.scatter(x, y, c = colors, label='Data Points',marker='x',s=100) #s is the size of the marker
#marker is defining the marker

# Adding Labels and Title
plot.xlabel('X-axis')
plot.ylabel('Y-axis')
plot.title('Scatter Plot Example')
plot.colorbar() #adding a colour bar by defining c = colors and mapping
# Adding Legend
plot.legend()

# Show Plot
plot.show()
