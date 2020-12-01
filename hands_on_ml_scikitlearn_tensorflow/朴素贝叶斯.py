#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:37:39 2020

@author: xiaofan
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# =============================================================================
# Bernoulli naive bayes/二项/0-1分布
# =============================================================================
from sklearn.naive_bayes import BernoulliNB
from sklearn.datasets import make_blobs

#分类数=5， 样本数量300
X, y = make_blobs(n_samples=300, centers=5, random_state=8)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)
# 横轴纵轴=0为交界划分4个象限之后对数据分类，binarize=0
# 特征值1≥0，特征值2≥0 则第一象限
bnb = BernoulliNB().fit(X_train, y_train)

print('training score: {:.2f}'.format(bnb.score(X_train, y_train))) #0.54
print('test score: {:.2f}'.format(bnb.score(X_test, y_test))) #0.37

#%%
#横轴和纵轴的端点
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
# y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
# # 背景色
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02), np.arange(y_min, y_max, .02))
z = bnb.predict(np.c_[(xx.ravel(), yy.ravel())]).reshape(xx.shape)
plt.pcolormesh(xx, yy, z, cmap=plt.cm.Pastel1)

# dataset
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,edgecolor='k', cmap=plt.cm.cool)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.cool, 
            marker = '*', edgecolors='k')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('naive bayes')

#%%
# =============================================================================
# Gaussian naive bayes
# =============================================================================
# 假设样本高斯分布
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB().fit(X_train, y_train)

print('training score: {:.2f}'.format(gnb.score(X_train, y_train))) #0.95
print('test score: {:.2f}'.format(gnb.score(X_test, y_test))) #0.93
z2 = gnb.predict(np.c_[(xx.ravel(), yy.ravel())]).reshape(xx.shape)

plt.pcolormesh(xx, yy, z2)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,edgecolor='y')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker = '*', edgecolors='w')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('gaussian bayes')

#%%M
# =============================================================================
# multinomial naive bayes
# =============================================================================
# 多项式贝叶斯是掷骰子（+掷硬币）：掷n次，每个面朝上的分布
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler  # 特征值转化为0～1，X不可以是负数
scaler = MinMaxScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled =scaler.transform(X_test)
mnb = MultinomialNB().fit(X_train_scaled, y_train)

print('training score: {:.2f}'.format(mnb.score(X_train_scaled, y_train))) #0.24
print('test score: {:.2f}'.format(mnb.score(X_test_scaled, y_test))) #0.17
z3 = mnb.predict(np.c_[(xx.ravel(), yy.ravel())]).reshape(xx.shape)

plt.pcolormesh(xx, yy, z3, cmap=plt.cm.Pastel2)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,edgecolor='k')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker = '*', edgecolors='k')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('multinomial bayes')
#%%
# =============================================================================
# 肿瘤数据集
# =============================================================================
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print(cancer.keys()) # target: 分类值、target_names: 分类名称

# data:特征数据、feature_names:特征名称
print('肿瘤的分类target_names：', cancer['target_names']) #肿瘤的分类： ['malignant' 'benign']
print('\ntarget：\n', cancer['target']) # 0/1
print('\n肿瘤的特征feature_names：\n', cancer['feature_names'])#临床表现，特征值的名称

#%%
# 用高斯分布
from sklearn.naive_bayes import GaussianNB
X, y = cancer.data, cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)
print(X_train.shape) # 426个样本，30个特征数量（target）
print(X_test.shape)
gnb2 = GaussianNB().fit(X_train, y_train)

print('training score: {:.2f}'.format(gnb2.score(X_train, y_train))) #0.95
print('test score: {:.2f}'.format(gnb2.score(X_test, y_test))) #0.94

# 测试第312个样本
print('模型预测的分类：{}'.format(gnb2.predict([X[312]])))
print('正确的分类：', y[312])

#%%
# learning curve
# 训练数集样本量的增加，模型要拟合的数据变多，模型得分逐渐降低，但交叉验证得分变化不明显
# 高斯朴素贝叶斯在预测方面对样本数量对要求并不苛刻
# from sklearn.model_selection import learning_curve
# from sklearn.model_selection import ShuffleSplit # 随即拆分
#
# #定义函数
# def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
#                         n_jobs=1, train_sizes=np.linspace(.01, 1.0, 5)):
#     plt.figure()
#     plt.title(title)
#     if ylim is not None:
#         plt.ylim(*ylim)
#     plt.xlabel('Training examples')
#     plt.ylabel('Scores')
#     train_sizes, train_scores, test_scores = learning_curve(estimator, 
#                                                             X, y, cv=cv, n_jobs=n_jobs,
#                                                             train_sizes=train_sizes)
#     train_scores_mean = np.mean(train_scores, axis=1)
#     test_scores_mean = np.mean(test_scores, axis=1)
#     plt.grid()
#     plt.plot(train_sizes, train_scores_mean, 'o-', color='p',
#              label='training score')
#     plt.plot(train_sizes, test_scores_mean, 'o-', color='g',
#              label='cross validation score')
#     plt.legend(loc='lower right')
#     return plt
#
# # 调用
# title = 'Learning curves'
# estimator = GaussianNB()
#
# # 拆分数量
# cv = ShuffleSplit(n_splits=100, test_size=.2, random_state=0)
# plot_learning_curve(estimator, title, X, y, ylim=(0.9, 1.0), cv=cv, n_jobs=4)
