import matplotlib.pyplot as plt

x_value = list(range(1, 6))
y_value = [x**3 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Greens, edgecolor='none', s=40)
plt.show()