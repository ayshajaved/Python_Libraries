# with open("D:/PROGRAMMING/python/practise.txt", "r") as f:
#     content = f.read()
#     # print(content)
#     words = content.split()
#     # print(words)
#     print(f"The number of words are {len(words)}")
#     words_d = {}
#     for i in set(words):
#         words_d[i] = words.count(i)
#     for key, value in words_d.items():
#         print(f"{key}:{value}")

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create the plot
plt.plot(x, y)

# Add titles and labels
plt.title("Sample Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display the plot
plt.show()
