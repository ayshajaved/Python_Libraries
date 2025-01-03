import matplotlib.pyplot as plt
#Pie chart
# Data to plot
labels = ['Category A', 'Category B', 'Category C', 'Category D']  # Labels for each slice
sizes = [30, 20, 25, 25]  # Values for each slice
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']  # Colors for each slice
# explode = (0.1, 0, 0, 0)  # Explode the 1st slice (Category A)
explode = (0.1, 0.2, 0.3, 0.4)  # Explode all slices

# Create the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=140)

# Add a title
plt.title('Sample Pie Chart')

# Display the chart
plt.show()
