#histograms
import matplotlib.pyplot as plot

data = [1,2,3,4,5,6,7,8]
plot.hist(data, bins=3, edgecolor='black', color='pink')

#bins divide it into the number of intervals we want
#edgecolor is the color of the border of the bins
#color is the color of the bins

plot.show()
