import matplotlib.pyplot as plt
import numpy as np

# Data for the 3D plot
x = np.linspace(-5, 5, 20)  # X values
y = np.linspace(-5, 5, 20)  # Y values
X, Y = np.meshgrid(x, y)    # Create a grid
Z = X**2 + Y**2             # Z values (a simple quadratic function)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')  # Plot with color map

# Add labels and title
ax.set_title("Simple 3D Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Show the plot
plt.show()
