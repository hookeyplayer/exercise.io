# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:43:17 2020

@author: xiaofan
"""
import numpy as np
import matplotlib.pyplot as plt
#%% 求解，第一幅两个解（交点），第二幅无解
xmin, xmax = -1, 1
x = np.linspace(xmin, xmax, 200)
def f(x):
    return 0.6 * np.cos(4*x) + 1.4
y = f(x)
ya, yb = np.min(y), np.max(y)
fig, axes = plt.subplots(2, 1, figsize = (8,6))

for ax in axes:
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    ax.set(xlim = (xmin, xmax), xticks = (), 
           ylim = (-0.6, 3.2), yticks = ())
    ax.plot(x, y, 'k-', lw = 2) # k-: black line; lw:
    ax.fill_between(x, ya, yb, facecolor='blue', alpha=0.05) # 填充，alpha调淡度
    ax.vlines([0], ya, yb, lw=3, color='blue', label='range of $f$') # y轴描线
    ax.text(0.04, -0.3, '$0$', fontsize=16)
    ax = axes[0] # 画axes里的第一幅
    ax.legend(loc='upper right', frameon=False) #legend不加框
    ybar = 1.5
    ax.plot(x, x * 0 + ybar, 'k--', alpha=0.5) #横着画虚线
    ax.text(0.05, 0.8 * ybar, '$y$', fontsize=16)
    for i, z in enumerate((-0.35, 0.35)):
        ax.vlines(z, 0, f(z), linestyle='--', alpha=0.5)
        ax.text(z, -0.2, f'$x_{i}$', fontsize=16) # 下标
        
    ax = axes[1] # 画第二幅
    ybar = 2.6
    ax.plot(x, x * 0 + ybar, 'k--', alpha=0.5)
    ax.text(0.04, 0.91 * ybar, '$y$', fontsize=16)
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
