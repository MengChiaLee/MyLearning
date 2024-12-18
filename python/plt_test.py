# import matplotlib.pyplot as plt

# # 示例数据
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # 绘制带有自定义颜色、样式和标记的线图
# plt.plot(x, y, color='b', linestyle='--', marker='o', label='Line')

# # 添加标题和标签
# plt.title('Customized Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# # 显示图例
# plt.legend()

# # 显示图形
# plt.show()
#######################################################

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建网格
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 计算 Z 值
Z = np.sin(np.sqrt(X**2 + Y**2))

# 绘制三维表面图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# 设置标题和坐标轴标签
ax.set_title('3D Surface Plot')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

