#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 09:23:31 2020

@author: xiaofan
"""

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
# test
X = [[1], [4], [3]]
y = [3, 5, 3]
lr = LinearRegression().fit(X, y)
z = np.linspace(0, 5, 20)

plt.scatter(X, y) # only two dots
plt.plot(z, lr.predict(z.reshape(-1, 1)), c='k') # reshape转换成1列
# coed_是numpy数组，intercept_是float
print('y = {:.3f}'.format(lr.coef_[0]), 'x', '+ {:.3f}'.format(lr.intercept_))

#%% 用大数据集
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=50, n_features=1, n_informative=1,
                       noise=50, random_state=1)
reg = LinearRegression().fit(X, y)
z = np.linspace(-5, 5, 200).reshape(-1, 1)

plt.scatter(X, y, c='g', s=15)
plt.plot(z, reg.predict(z), c='k')

#%% OLS
from sklearn.model_selection import train_test_split
X, y = make_regression(n_samples=100, n_features=2, n_informative=2,
                       random_state=3, noise=50)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)
lr = LinearRegression().fit(X_train, y_train)
print('coeffcient_ = {}'.format(lr.coef_[:]))  # 因为有两个特征，所以是二维数组
print('intercept = {}'.format(lr.intercept_))
print('score:{:.2f}'.format(lr.score(X_test, y_test)))

#%%糖尿病数据集
from sklearn.datasets import load_diabetes
X, y = load_diabetes().data, load_diabetes().target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)
reg = LinearRegression().fit(X_train, y_train)
print('score:{:.2f}'.format(reg.score(X_train, y_train))) #0.53
print('score:{:.2f}'.format(reg.score(X_test, y_test))) # 0.46 < 训练集，故过度拟合

#%%
# 岭回归（避免过度拟合）L2正则化
# 保留特征变量，但通过α来减小特征变量系数
# 复杂度降低，但泛化能力好
from sklearn.linear_model import Ridge
ridgereg = Ridge(alpha=8).fit(X_train, y_train) # α是正则力度，提高α来降低过度拟合
print('score:{:.2f}'.format(ridgereg.score(X_train, y_train))) #0.18
print('score:{:.2f}'.format(ridgereg.score(X_test, y_test))) # 0.19
ridgereg10 = Ridge(alpha=10).fit(X_train, y_train)
ridgereg06 = Ridge(alpha=0.6).fit(X_train, y_train)
plt.plot(ridgereg.coef_, 's', label='ridge α = 1')
plt.plot(ridgereg10.coef_, '*', label='ridge α = 10')
plt.plot(ridgereg06.coef_, 'v', label='ridge α = 0.6')#更接近普通回归
lr = LinearRegression().fit(X_train, y_train)
plt.plot(lr.coef_, 'o', label='linear regression')
plt.xlabel('coeffieicnt index') # x=0, 第1个特征变量；x=1，第2个；共10个特征变量
plt.ylabel('coefficient magnitude') # 特征变量的系数量级
plt.legend()
plt.hlines(0, 0, len(lr.coef_)) #水平线
#%%固定α,改变数据量
# 学习曲线/模型评分折线图
# 总集里采样
from sklearn.model_selection import learning_curve, KFold
# 定义函数来绘制曲线
def plot_learning_curve(est, X, y):
    training_set_size, train_scores, test_scores = learning_curve(est,
                                                                   X, y, train_sizes=np.linspace(.1, 1, 20),
                                                                   cv=KFold(20, shuffle=True))
    estimater_name = est.__class__.__name__
    line = plt.plot(training_set_size, train_scores.mean(axis=1), '--',
                    label="training" + estimater_name)
    plt.plot(training_set_size, test_scores.mean(axis=1), '-',
             label='test' + estimater_name, c=line[0].get_color())
    plt.xlabel('Training set size')
    plt.ylabel('Score')
    plt.ylim(0, 1.1)
    
plot_learning_curve(ridgereg, X, y)
plot_learning_curve(LinearRegression(), X, y)
plt.legend(loc=(0, 1.05), ncol=2, fontsize=11)
# ？结论：若有足够大的数据集，正则化就不太重要

#%%L1，对线性回归进行正则化：套索回归lasso(依旧糖尿病集)
# 跟L1类似，系数接近0
# 但一部分系数会正好=0，即部分特征会被忽略
from sklearn.linear_model import Lasso
lasso = Lasso().fit(X_train, y_train)
print('score in training set:{:.2f}'.format(lasso.score(X_train, y_train))) #。36
print('score in test set:{:.2f}'.format(lasso.score(X_test, y_test))) #。37 都欠拟合

#%%
lasso2 = Lasso(alpha=0.1, max_iter=50).fit(X_train, y_train)   
print('α=0.1, scores for training set:{:.2f}'.format(lasso2.score(X_train,
                                                                      y_train)))  #.52
print('α=0.1, scores for test set:{:.2f}'.format(lasso2.score(X_test,
                                                                      y_test)))  .48
#%% summary
plt.plot(lasso.coef_, '*', label='lasso, α=1')
plt.plot(lasso2.coef_, '+', label='lasso, α=0.1')
# plt.plot(ridgereg.coef_, 's', label='ridge α = 1')
# plt.plot(ridgereg10.coef_, '-', label='ridge α = 10')
plt.plot(ridgereg06.coef_, 'v', label='ridge α = 0.6')#更接近普通回归
# plt.plot(lr.coef_, 'o', label='linear regression')
plt.legend(ncol=2, loc=(0, 1.01))