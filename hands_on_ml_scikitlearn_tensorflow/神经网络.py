#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:23:32 2020

@author: xiaofan
"""

import numpy as np
import matplotlib.pyplot as plt
line = np.linspace(-5, 5, 200)

plt.plot(line, np.maximum(line, 0), label='lelu') # 负值全部去掉
plt.plot(line, np.tanh(line), label='tanh') # 特征值压缩进[-1, 1]
plt.legend(loc='best')

#%%
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
wine = load_wine()
X = wine.data[:, :2]
y = wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# multiple layer perception
# 参数 activation调整非线性的方法，α和线性模型里一样
# 对隐藏层的结果进行:非线性矫正rectify nonlinearity，或双曲正切处理tangens hyperbolicus
# logistic非线性方法返回的特征值0和1之间
# hidden_layer_size：[100,]只有一个隐藏层，且该层中节点数100；若[10, 10]则两个隐藏层
# 隐藏层的节点数越小，则丢失很多细节。节点数(等于训练数据集的特征数量)代表边界中最大的直线数，该数值越大边界越平滑
mlp = MLPClassifier(solver='lbfgs', activation='tanh') # 边界完全是曲线
mlp.fit(X_train, y_train)
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))
# ravel返回flattened array
z = mlp.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape) 
plt.pcolormesh(xx, yy, z, cmap=plt.cm.Pastel2)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', s=50) #s调整原点size
plt.xlim(xx.min(), xx.manx())
#%%
mlp_alpha = MLPClassifier(solver='lbfgs', activation='tanh', alpha=1)
mlp_alpha.fit(X_train, y_train)
z2 = mlp_alpha.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.pcolormesh(xx, yy, z2, cmap=plt.cm.Pastel2)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', s=50) #α的增加让模型变简单
#%%