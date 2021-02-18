#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:39:24 2020

@author: xiaofan
"""

from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
# 数据集拆分工具random排列后默认3/4用于训练，1/4用于测试
from sklearn.model_selection import train_test_split 
# 数据类型的量等于5
datatuple = make_blobs(n_samples = 500, centers = 5, random_state = 8)
X, y = datatuple # X是二维矩阵，数据的特征；y是一维向量，数据对应的标签
plt.scatter(X[:, 0], X[:, 1], c = y, cmap = plt.cm.spring, edgecolor = 'k')

import numpy as np
clf = KNeighborsClassifier()
clf.fit(X, y)
print(clf.score(X, y)) #96%的点在正确的分类

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmp = plt.cm.Pastel1)
plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.show()
#%%
from sklearn.datasets import make_regression
X1, y1 = make_regression(n_features=1, n_informative=1, 
                         noise=50, random_state=8) # 标准差为50的噪音
plt.scatter(X1, y1, c = 'orange', edgecolor = 'k')
plt.show()
from sklearn.neighbors import KNeighborsRegressor
reg = KNeighborsRegressor()
reg.fit(X1, y1)
z = np.linspace(-3, 3, 200).reshape(-1 ,1)  
plt.scatter(X1, y1, c='orange')       
plt.plot(z, reg.predict(z), c='b', linewidth=2)
print('模型评分:{:.2f}'.format(reg.score(X1, y1)))     #0.77
#改进版的线将覆盖更多的散点
reg2 = KNeighborsRegressor(n_neighbors=2)
reg2.fit(X1, y1)
plt.scatter(X1, y1)
plt.plot(z, reg2.predict(z), c='k', linewidth=2)
plt.show()
print('模型2评分:{:.2f}'.format(reg2.score(X1, y1)))  #0.86
#%%酒
from sklearn.datasets import load_wine
wine_dataset = load_wine()
# print('酒数据集里的键:\n{}'.format(wine_dataset.keys()))
print('description:\n{}'.format(wine_dataset['data'].shape)) #每条数据有13个特征变量
print(wine_dataset['DESCR'])
X_train,  X_test, y_train, y_test = train_test_split(wine_dataset['data'], 
                                                    wine_dataset['target'],
                                                    random_state=0) # 伪随机数状态设定

print('X_train shape:{}'.format(X_train.shape)) 
print('X_test shape:{}'.format(X_test.shape)) 
print('y_train shape:{}'.format(y_train.shape)) 
print('y_test shape:{}'.format(y_test.shape)) 
#%%
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
# print(knn.score(X_test, y_test)) #0.755
# 加入一瓶新酒
X_new = np.array([[13.2, 2.77, 2.51, 18.5, 96.6, 1.04, 2.55, 0.57,
                   1.47, 6.2, 1.05, 3.33, 820]])
prediction = knn.predict(X_new)
print(wine_dataset['target_names'][prediction]) #新酒['class_2']
