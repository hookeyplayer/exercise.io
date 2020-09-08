import numpy as np
import scipy.integrate as sci
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
#%%
I = np.eye(2)
a = np.array([[1.0, 2.0], [3.0, 4.0]])
y = np.array([[5.], [7.]])
#%% Inverse
ainv = np.linalg.inv(a) # not precise
# dot product_new @
dotprod_new = a @ ainv
# dot product_old python
dotprod_old = np.dot(a, ainv)

# Transpose
T = a.transpose()
# a.T
# Trace:对角线之和
np.trace(a)
eig = np.linalg.eig(a)
# solve
np.linalg.solve(a, y)
np.arange(30).shape = 2, 5, 3 # 两个5x3
#%% 
m = np.arange(5)
n = np.arange(0, 9, 2) # ([0 2 4 6 8])
v = np.vstack([m, n]) # vertical往下构建
h = np.hstack([m, n]) # horizontal
#%% 
a = 0.5
b = 9.5
x = np.linspace(0, 10) # draw line

def f(x):
    return np.sin(x) + 0.5*x
intx = np.linspace(a, b)
inty = f(intx)
fig, ax = plt.subplots(figsize = (7,5))
plt.plot(x, f(x), 'g', linewidth = 2)
plt.ylim(ymin = 0)
verts = [(a, 0)] + list(zip(intx, f(intx))) + [(b, 0)]
# 多边形
poly = Polygon(verts, facecolor = '0.8', edgecolor = '0.3')
ax.add_patch(poly)
# 积分公式
plt.text(0.75*(a+b), 1.5, r'$\int_a^b f(x)dx$')
plt.figtext(0.9, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')
# 自变量范围x轴标注
ax.set_xticks((a, b))
# 将显示数值改为显示a, b
ax.set_xticklabels(('$a$', '$b$'))
# 显示因变量d两个端点值
ax.set_yticks([f(a), f(b)])
#%% 数学符号
import sympy as sy
# 化简
x = sy.Symbol('x')
f = x**2 + 3 + 0.5*x**2 + 3/2
sy.simplify(f)
# 打印公式（人的方式）
print(sy.pretty(f))

print(sy.pretty(sy.sqrt(x)))
# 解方程，
y = sy.Symbol('y')
sy.solve(x**2 + y**2)
# 积分打印公式
a = sy.Symbol('a')
b = sy.Symbol('b')
print(sy.pretty(sy.Integral(sy.sin(x) + 0.5*x, (x, a, b))))
# 积分
int_func_limits = sy.integrate(sy.sin(x) + 0.5*x, (x, a, b))
print(int_func_limits)
# use dict for substitution of values to yield integral
int_func_limits.subs({a: 0.5, b: 9.5}).evalf()
# second way
print(sy.integrate(sy.sin(x) + 0.5*x, (x, 0.5, 9.5)))
#%% 求导
x = sy.Symbol('x')
int_func = sy.integrate(sy.sin(x) + 0.5*x, x)
# 积分求导等于里面本身
int_func.diff()
# convex minimization problem
y = sy.Symbol('y')
f = (sy.sin(x) + 0.05*x**2 + sy.sin(y) + 0.05*y**2)
# partial dirivatives with respect to one variables
del_x= sy.diff(f, x)
del_x
xo = sy.nsolve(del_x, -1) # -1或是其他值都没事儿
xo
del_y= sy.diff(f, y)
yo = sy.nsolve(del_y, -2)
# global min that both partial derivatives are zero
f.subs({x: xo, y:yo}).evalf()
