# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:41:20 2020

@author: xiaofan
"""
# =============================================================================
# 数据下载
# =============================================================================
import os
import pandas as pd
housing = pd.read_csv('https://raw.githubusercontent.com/WillKoehrsen/Hands-On-Machine-Learning/master/handson-ml-master/datasets/housing/housing.csv')
housing.info()
#housing = tarfile.open(download_url)
#%%
# =============================================================================
# 数据清洗
# =============================================================================
# 方法一：丢弃
housing.dropna(subset = ['total_rooms'])
housing.drop('total_rooms', axis = 1)
# 方法二：中位数填补
median = housing['total_rooms'].median()
housing['total_rooms'].fillna(median)
#%%
# 方法三：库
from sklearn.preprocessing import Imputer
imputer = Imputer(strategy = 'mean') 
#使用前提是没有字符串的列数据
housing.drop('ocean_proximity', axis = 1)
imputer.fit(housing)
#%%