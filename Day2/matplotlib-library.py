# Matplotlib is used to plot the graphs, charts for visualizing the data
# Basic Plot (Line Plot)
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 15, 25, 20]


plt.plot(x, y)
plt.show()


# Titles & Lables
plt.plot(x, y)
plt.title("Sales Trend")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()


# Multiple Lines
y2 = [5, 15, 10, 22]


plt.plot(x, y)
plt.plot(x, y2)
plt.show()


# Scatter Plot
plt.scatter(x, y)
plt.scatter(x, y2)
plt.show()


# Bar Chart
categories = ["A", "B", "C"]
values = [10, 25, 18]


plt.title("Bar Chart for Categories & Values")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.bar(categories, values)
plt.show()


# Histogram
data = [10, 20, 20, 30, 30, 40, 40, 40]


plt.hist(data)
plt.show()


# Pie Chart
labels = ["A", "B", "C", "D", "E"]
sizes = [10, 50, 15, 10, 15]


plt.pie(sizes, labels=labels)
plt.show()


# Grid
plt.plot(x, y)
plt.grid()
plt.show()


# Legend
plt.plot(x, y, label="Sales")
plt.plot(x, y2, label="Profit")


plt.legend()
plt.show()


# Figure Size
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.show()


# Subplots(Multiple Graphs)
plt.subplot(1, 2, 1)
plt.plot(x, y)


plt.subplot(1, 2, 2)
plt.plot(x, y2)


plt.show()


# Saving the Plot Image
plt.plot(x, y)
plt.savefig("line-chart.png")


# Line Style & Markers
plt.plot(x, y, linestyle="--", marker="o")
plt.show()


# Box Plot
data = [10, 20, 30, 40, 100]


plt.boxplot(data)
plt.show()
