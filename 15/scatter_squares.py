import matplotlib.pyplot as plt 

x_values = list(range(1, 1001)) 
y_values = [x**2 for x in x_values] 
plt.scatter(x_values, y_values, s=40) 
# 设置图表标题并给坐标轴加上标签

# --snip--

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000]) 
plt.show()