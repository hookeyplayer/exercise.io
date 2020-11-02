# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:05:00 2020

@author: xiaofan
"""

from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split # 数据集拆分工具
# 数据类型的量等于5
datatuple = make_blobs(n_samples = 500, centers = 5, random_state = 8)
X, y = datatuple
plt.scatter(X[:, 0], X[:, 1], c = y, cmap = plt.cm.spring, edgecolor = 'k')
#%%
import numpy as np
clf = KNeighborsClassifier()
clf.fit(X, y)
#%%
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmp = plt.cm.Pastel1)