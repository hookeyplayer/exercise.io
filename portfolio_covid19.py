# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 00:59:27 2020

@author: xiaofan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from sklearn import (linear_model, metrics, neural_network, pipeline,
#                     model_selection)
#import math
import yfinance as yf
symbols = ['MRNA','GILD','JNJ', 'GSK', 'AZN', 'SVA']
start = '2020-03-01'
end = '2020-09-11'
#%%
ac_0 = yf.download(symbols, start, end)['Adj Close']
plt.figure(figsize=(12,8))
plt.plot(ac_0, alpha = 0.8)
plt.legend(labels = ac.columns, loc = 2)
plt.grid()
plt.title('Цена на акции Вакцин Фарма')
#%% Normalize the data
#ac_1 = (ac - ac.min()) / (ac.max() - ac.min())
#plt.figure(figsize = (12,8))
#plt.plot(ac_1)
#plt.title('Pharma Vaccine Stocks Normalize')
#plt.legend(labels = ac_1.columns)
#%% returns 
logret = np.exp(ac_0.pct_change().dropna())
plt.figure(figsize = (12,8))
plt.plot(logret, alpha = 0.8) 
plt.title('Log Returns')
plt.legend(labels = logret.columns)
plt.grid()
#%% Box plot
logret.plot(kind='box',figsize=(12,8))
#%% returns and risks
plt.figure(figsize=(14,12))
plt.scatter(logret.mean(), logret.std(), alpha = 0.8)
plt.title('Риск и доходность')
plt.xlabel('Ожидаемая доходность')
plt.ylabel('Риск')
plt.grid(True)
for label, x, y in zip(logret.columns, logret.mean(), logret.std()):
    plt.annotate(label, xy = (x, y), xytext = (50, 50),
                 textcoords = 'offset points', ha = 'right', va = 'bottom',
                 arrowprops = dict(arrowstyle = '-',
                                   connectionstyle = 'arc3,rad=-0.3'))
#%%
table['Доходность'] = logret.mean()
table['Риск'] = logret.std()
table.sort_values(by = 'Доходность')
#%% heatmap
plt.figure(figsize = (7,7))
corr = logret.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)




