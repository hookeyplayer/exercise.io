import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2*np.pi, 2*np.pi, 88)
def f(x):
    return np.sin(x) + 0.5*x
reg = np.polyfit(x, f(x), deg = 5) # degree of fittign polynomial
ry = np.polyval(reg, x) # array of coefficients
#%% basic polynomial
plt.plot(x, f(x), 'b', label = 'f(x)')
plt.plot(x, ry, 'r.', label = 'regression')
#%% OLS
matrix = np.zeros((3+1, len(x)))
matrix[3, :] = x**3
matrix[2, :] = x**2
matrix[1, :] = x
matrix[0, :] = 1
reg2 = np.linalg.lstsq(matrix.T, f(x))[0] # optimal parameter solvation
ry2 = np.dot(reg2, matrix)
plt.plot(x, f(x), 'b', label = 'f(x)')
plt.plot(x, ry2, 'r.', label = 'f(x)2')
plt.legend(loc = 0)
# still looks bad
#%% add sin to basic function
matrix[3, :] = np.sin(x)
reg3 = np.linalg.lstsq(matrix.T, f(x))[0]
ry3 = np.dot(reg3, matrix)
plt.plot(x, f(x), 'b', label = 'f(x)')
plt.plot(x, ry3, 'r.', label = 'f(x)3')
plt.legend(loc = 0)
np.allclose(f(x), ry3) # good
#%% multi-dimensions
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from matplotlib import cm # cmap: color

# define x, y
x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
X, Y = np.meshgrid(x, y) # generate 2d grids out of 1d arrays
Z = np.sin(X) + 0.25*X + np.sqrt(Y) + 0.05*Y**2 # Z must be from X, Y (2d)

#x = X.flatten()
#y = Y.flatten() # yields 1d arrays from 2d grids
fig = plt.figure() # define figure
ax = Axes3D(fig)
surf = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.rainbow)
ax.contour(X, Y, Z, zdir = 'z', offset = -2, cmap = plt.get_cmap('coolwarm'))
#ax.set_zline(-2, 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
fig.colorbar(surf, shrink = .5, aspect = 10)
plt.show()
#%% mlti-dimension regression
import statsmodels.api as sm
x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
matrix = np.zeros((len(x), 6 + 1))
matrix[:, 6] = np.sqrt(y)
matrix[:, 5] = np.sin(x)
matrix[:, 4] = x**2
matrix[:, 3] = y**2
matrix[:, 2] = y
matrix[:, 1] = x
matrix[:, 0] = 1
z = np.sin(x) + 0.25*x + np.sqrt(y) + 0.05*y**2 # onedimension value
model = sm.OLS(z, matrix).fit()
a = model.params
def reg_func(a, x, y):
    f6 = a[6] * np.sqrt(y)
    f5 = a[5] * np.sin(x)
    f4 = a[4] * x**2
    f3 = a[3] * y**2
    f2 = a[2] * y
    f1 = a[1] * x
    f0 = a[0] * 1
    return(np.sum((f0, f1, f2, f3,f4, f5, f6)))
RZ = reg_func(a, x, y)
#%% type of estimation, constructing data points
import scipy.interpolate as spi
x = np.linspace(-2 * np.pi, 2 * np.pi, 25)
def f(x):
    return np.sin(x) + 0.5 * x
# 类比polyfit & polyval
ipo = spi.splrep(x, f(x), k = 1) # k: order of spline in range [1,5]
iy = spi.splev(x, ipo)
#plt.plot(x, f(x), 'b', label = 'f(x)')
#plt.plot(x, iy, 'r.', label = 'interpolation')
np.allclose(f(x), iy) # True
#%% global optimization
#import scipy.optimize as spo
#from math import sqrt
#def Eu():
#    x, y = 
#    return -(0.5*sqrt(s*15 + b*5) + 0.5 * sqrt(s*5 + b*12))
## constraints
#cons = ({'type': 'ineq', 'fun': lambda(s,b): 100 - s*10 -b*10})
## budget constraint




 