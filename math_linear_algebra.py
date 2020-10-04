# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:38:29 2020

@author: xiaofan
"""

import numpy as np
import scipy.integrate as sci
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import scipy.linalg as scl 
#%%
# A： map matrix
A = ((1, 2), (3, 4))
A = np.array(A) # tuple to matrix, 横着一组
print(scl.det(A)) # !=0, A nonsingular, thus invertable
A_inv = scl.inv(A)
y = np.ones((2, 1)) # 等式右边， [1, 1] 竖着shape
print(y)
x = A_inv @ y # 求解
print(x)
print(A @ x) # 回测 = y
scl.solve(A, y) # = x
# 最小二乘法
xhat = scl.lstsq(A, y)
print(xhat)
#%% eigvector & eigvalue
A = ((1, 2),
     (2, 1))
A = np.array(A)
evals, evecs = scl.eig(A)
evecs = evecs[:, 0], evecs[:, 1]
fig, ax = plt.subplots(figsize=(10, 8))
xmin, xmax = -3, 3
ymin, ymax = -3, 3
# Set the axes through the origin
#for spine in ['left', 'bottom']:
#    ax.spines[spine].set_position('zero')
#for spine in ['right', 'top']:
#    ax.spines[spine].set_color('none')
#ax.grid(alpha=0.4)
#
#ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
## Plot each eigenvector
#for v in evecs:
#    ax.annotate('', xy=v, xytext=(0, 0), arrowprops=dict(facecolor='blue',
#                shrink=0, alpha=0.6, width=0.5))
## Plot the image of each eigenvector
#for v in evecs:
#    v = A @ v
#    ax.annotate('', xy=v, xytext=(0, 0), arrowprops=dict(facecolor='red', 
#                shrink=0, alpha=0.6, width=0.5))
## Plot the lines they run through
#x = np.linspace(xmin, xmax, 3)
#for v in evecs:
#    a = v[1] / v[0]
#    ax.plot(x, a * x, 'b-', lw=0.4)
    


#%%
I = np.eye(2)
a = np.array([[1.0, 2.0], [3.0, 4.0]]) #横着
print(a)
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
