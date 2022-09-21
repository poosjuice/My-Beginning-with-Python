# Make sure to use relevant imports, this one will be "import matplotlib.pylot as plt"
import matplotlib.pyplot as plt


# In this lesson we'll be looking at plotting Graphs with Python
# Starting below we'll take a variable "x" & assign it a list

# x = [1, 3, 5, 10]
# plt.plot(x)  # This line will plot the list we assigned to the "x" variable
# plt.show()   # This line here will just initiate a window to pop up showing our plotted variable
# This is a simple single plot graph

# Now we'll make a more complex but proper looking Graph

# First part is points for Line 1
x = [3, 9, 14]
y = [2, 7, 30]
plt.plot(x, y, c="green", linewidth=2, label="Line 1", marker='o',
         markerfacecolor="purple")

# Second part is points for Line 2
x2 = [1, 15, 18]  # Naming it "x2" & "y2" so when the code is run it can differentiate
y2 = [0, 3, 12]
plt.plot(x2, y2, c="purple", linewidth=2, label="Line 2", linestyle="dashed",
         marker='o', markerfacecolor="green")

# Now we're going to add the labels to "x" & "y" & give the graph a title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two lines")

# The final part will be getting the legend to show on the plot for both lines
plt.legend()
plt.show()
