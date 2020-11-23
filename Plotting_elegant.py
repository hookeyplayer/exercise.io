# subplot on one axis
from scipy.stats import norm
from random import uniform
import matplotlib.pyplot as plt
import numpy as np

# 一、手动
squares = [1, 4, 9, 16, 25]
# linewidth():线条粗细
# 这种方法绘制的图因为没有指明x轴，所以横坐标0对应1， 横坐标4对应25，是错的
# plt.plot(squares, linewidth=5)
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=5)
# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14) 
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
#%%

# 二、自动
x_values = list(range(1, 1001)) 
# 生成y值的列表解析
y_values = [x**2 for x in x_values]
# RGB颜色模式，红绿蓝，近0深，近1浅
# 颜色映射突出数据规律
plt.scatter(x_values, y_values, edgecolor='none', s=8, c=(0, 0.9, 0.9)) 
# 设置每个坐标轴的取值范围 
plt.axis([0, 1100, 0, 1100000])
plt.show()
#%%
# =============================================================================
# # 一副三线
# =============================================================================
fig, ax = plt.subplots()
x = np.linspace(-4, 4, 150)
for i in range(3):
    m, s = uniform(-1, 1), uniform(1, 2) # mean and sd
    y = norm.pdf(x, loc = m, scale = s)
    current_label = f'$\mu = {m:.2}$'
    ax.plot(x, y, linewidth = 2, alpha = 0.6, label = current_label)
ax.legend()
plt.show()
#%%
# =============================================================================
# # 一副6图,3x2
# =============================================================================
num_rows, num_cols = 3, 2 
fig, axes = plt.subplots(num_rows, num_cols, figsize=(10, 12))
for i in range(num_rows):
    for j in range(num_cols):
        m, s = uniform(-1, 1), uniform(1, 2)
        x = norm.rvs(loc=m, scale=s, size=100) # randown variable single value
        axes[i, j].hist(x, alpha=0.6, bins=20) # 直方图
        t = f'$\mu = {m:.2}, \quad \sigma = {s:.2}$'
        axes[i, j].set(title=t, xticks=[-4, 0, 4], yticks=[])
plt.show()

# =============================================================================
# # 3D图
# =============================================================================

from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
def f(x, y):
    return np.cos(x**2 + y**2) / (1 + x**2 + y**2)
xgrid = np.linspace(-3, 3, 50)
ygrid = xgrid
x, y = np.meshgrid(xgrid, ygrid)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, f(x, y), rstride=2, cstride=2, cmap=cm.jet,
                alpha=0.7, linewidth=0.25)
ax.set_zlim(-0.5, 1.0)
plt.show()
#%%
from numpy import *
from numpy.random import rand, randn
from numpy.fft import fft, ifft
from numpy.lib.scimath import *
from scipy.stats import beta
import matplotlib.pyplot as plt
# I matrix
a = np.identity(3)
# method 1
#np.random.beta(5, 5, size=3)
q = beta(5, 5) # Beta(a, b), with a = b = 5
obs = q.rvs(2000) # 2000 observations
grid = np.linspace(0.01, 0.99, 100)
fig, ax = plt.subplots()
ax.hist(obs, bins=40, density=True)
ax.plot(grid, q.pdf(grid), 'k-', linewidth=2)
plt.show()
#q.cdf(0.4)
#q.pdf(0.8)
#%%
# method 2 等价于上
obs = beta.rvs(5, 5, size = 2000)
grid = np.linspace(0.01, 0.99, 100)
fig, ax = plt.subplots()
ax.hist(obs, bins=40, density=True) # density is line
ax.plot(grid, beta.pdf(grid, 5, 5), 'k-', linewidth=2)
plt.show()
