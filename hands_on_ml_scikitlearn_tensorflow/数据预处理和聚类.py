#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 21:04:45 2020

@author: xiaofan
"""
# =============================================================================
# standardscaler方法
# =============================================================================
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
# 两个特征分别对应x, y轴
X, y = make_blobs(n_samples=40, centers=2, random_state=30, cluster_std=2)
plt.scatter(X[:, 0], X[:, 1], c=y)
#%%
# 点不变，坐标轴变化，变为均值0，方差1
X_1 = StandardScaler().fit_transform(X)
plt.scatter(X_1[:, 0], X_1[:, 1], c=y)
#%%
# =============================================================================
# minmaxscaler方法
# =============================================================================
from sklearn.preprocessing import MinMaxScaler
# 所有特征值都在0和1之间
X_2 = MinMaxScaler().fit_transform(X)
plt.scatter(X_2[:, 0], X_2[:, 1], c=y)
#%%
# =============================================================================
# robustscaler方法
# =============================================================================
from sklearn.preprocessing import RobustScaler
# 和strandard方法类似
X_3 = RobustScaler().fit_transform(X)
plt.scatter(X_3[:, 0], X_3[:, 1], c=y)
#%%
# =============================================================================
# normalizer欧几里得方法
# =============================================================================
# 所有样本特征向量转化为欧几里得距离=1， 数据的分布变成半径=1的圆/球
# 关注数据的方向
from sklearn.preprocessing import Normalizer
X_4 = Normalizer().fit_transform(X)
plt.scatter(X_4[:, 0], X_4[:, 1], c=y)
#%%
# =============================================================================
# Bernoulli二项方法
# =============================================================================
# default threshold = 0
from sklearn.preprocessing import Binarizer
X_5 = Binarizer().fit_transform(X)
plt.scatter(X_5[:, 0], X_5[:, 1], c=y)
#%%
# =============================================================================
# quantile transform方法
# =============================================================================
from sklearn.preprocessing import QuantileTransformer
# uniform, spread most frequent values
# 减小outlier的影响，故而该方法robust
X_6 = QuantileTransformer().fit_transform(X)
plt.scatter(X_6[:, 0], X_6[:, 1], c=y)
#%%
# =============================================================================
# maxAbsmethod
# =============================================================================
from sklearn.preprocessing import MaxAbsScaler
# 讲最大值设为基准1
X_6 = MaxAbsScaler().fit_transform(X)
plt.scatter(X_6[:, 0], X_6[:, 1], c=y)
#%%
# =============================================================================
# 练习
# =============================================================================
from sklearn.datasets import load_wine
from  sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
wine = load_wine()
X_train, X_test, y_train, y_test = train_test_split(wine.data,
                                                    wine.target, random_state=8)
print(X_train.shape, X_test.shape) # (133, 13) (45, 13)
#%%
# MLP 神经网络拟合数据
mlp = MLPClassifier(hidden_layer_sizes=[100, 100],max_iter=400, random_state=62)
mlp.fit(X_train, y_train)
print('score:{:.2f}'.format(mlp.score(X_train, y_train))) #0.99
print('score:{:.2f}'.format(mlp.score(X_test, y_test))) #0.91

#%% 
# ？？错误的转换
X_train_pp = MinMaxScaler().fit_transform(X_train)
X_test_pp = MinMaxScaler().fit_transform(X_test)
mlp.fit(X_train_pp, y_train)

print('score:{:.2f}'.format(mlp.score(X_train_pp, y_train))) #1
print('score:{:.2f}'.format(mlp.score(X_test_pp, y_test))) #0.96

#%%
# 正确的转换
scaler = MinMaxScaler().fit(X_train)
X_train_pp = scaler.transform(X_train)
X_test_pp = scaler.transform(X_test)
mlp.fit(X_train_pp, y_train)

print('score:{:.2f}'.format(mlp.score(X_train_pp, y_train))) #1
print('score:{:.2f}'.format(mlp.score(X_test_pp, y_test))) #0.98
