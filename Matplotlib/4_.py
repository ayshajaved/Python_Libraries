#histograms
import matplotlib.pyplot as plot

# Datasets for the histogram
data1 = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8]
data2 = [1, 3, 3, 3, 5, 5, 6, 6, 7, 8, 8]
data3 = [2, 2, 3, 4, 4, 4, 6, 7, 8, 8, 9]

# Plot multiple histograms for comparison
plot.hist(data1, bins=5, alpha=0.7, edgecolor='black', color='pink', label='Dataset 1')
plot.hist(data2, bins=5, alpha=0.7, edgecolor='black', color='lightblue', label='Dataset 2')
plot.hist(data3, bins=5, alpha=0.7, edgecolor='black', color='lightgreen', label='Dataset 3')

# Alpha adjusts the transparency (so overlapping histograms are visible)

# Adding grid for better readability
plot.grid(axis='y', linestyle='--', alpha=0.5)

# Annotating specific bars for Dataset 1
plot.text(2, 2, 'Peak', ha='center', color='red')  # Example annotation

# Adding title and labels
plot.title("Expanded Histogram with Multiple Datasets", fontsize=14)
plot.xlabel("Value Ranges", fontsize=12)
plot.ylabel("Frequency", fontsize=12)

# Adding a legend to differentiate datasets
plot.legend(loc='upper left', fontsize=10)

# Display the histogram
plot.show()
