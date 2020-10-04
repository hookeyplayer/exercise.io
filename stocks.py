# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:15:10 2020

@author: xiaofan
"""
import scipy.stats as stats
#from fbprophet import Prophet
import numpy as np
import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import yfinance as yf
#%% input
symbols = ['LSE.L', 'DB1.DE']
start = '2017-09-11'
end = '2020-09-11'   
test = yf.download(symbols, start, end)['Adj Close'].dropna()
#test = test.set_inex().rename(columns = {'002475.SZ': '立讯精密',
#                      '0981.HK': '中芯国际', '^GSPC': 'SPmkt'})
test.columns = 'LSE', 'DBAG'
test['LSE'] = test['LSE'] * 1.08
test.head()
fig, axes = plt.subplots(figsize = (10, 8))
#plt.plot(test)
#plt.ylabel("Цена (в Евро)");
logret = np.exp(test.pct_change().dropna())
plt.figure(figsize = (12,8))
plt.plot(logret, alpha = 0.8) 
plt.title('Сравнение волатильность (Log Return) между LSE(синий) и DBAG(оранжевый)')
plt.legend(labels = logret.columns)
plt.grid()
#plt.title('Сравнение волатильность акций между LSE(синий) и DBAG(оранжевый)', weight = 'bold')
#returns = np.log(test / test.shift(1)).dropna()
#plt.plot(returns)
#print(returns)
#plt.grid(True)
#plt.legend(labels = test.columns)
#plt.xlabel("Дата")
## trans to annual
#pfe = returns['PFE'].var() * 250
#moderna= returns['MRNA'].var() * 250
#print(pfe, moderna)
#%% 
matrix = test.cov() * 250 # covariance matrix
corr_matrix = test.corr() * 250
corr_matrix
#%% alpha
test.head()
beta, alpha, r_value, p_value, std_err = stats.linregress(test['DBAG'],
                                                          test['LSE'])
print("Beta: 			%9.6f" % beta)
print("Alpha: 			%9.6f" % alpha)
print("R-Squared: 		%9.6f" % r_value)
print("p-value: 		%9.6f" % p_value)
print("Standard Error: 	%9.6f" % std_err)
#%% VaR 
# hist
import pylab
support = np.linspace(returns['TSLA'].min(), returns['TSLA'].max(), 100)
returns['TSLA'].hist(bins = 50, alpha = .5)
plt.title('Histogram of stock daily returns', weight = 'bold')
tdf, tmean, tsigma = stats.t.fit(qq)

plt.plot(support, stats.t.pdf(support, loc = tmean, scale = tsigma,
                              df = tdf), 'r-')
# QQ-plot正态
#qq = returns['TSLA'].dropna() 
##stats.probplot(qq, plot = pylab) # data: 1darray; dist: 比较分布（默认正态）
#%% Monte Carlo simulation

days = 300
dt = 1/float(days)
sigma = 0.04 # volatility
mu = 0.05  # drift (average growth rate)
# bug below yet to be solved
#def random_walk(startprice):
#    price = np.zeros(days)
#    shock = np.zeros(days)
#    price[0] = startprice
#    for i in range(1, days):
#        shock[i] = np.random.normal(loc = mu * dt, scale = sigma * np.sqrt(dt )
#        price[i] = np.max(0, price[i-1] + shock[i] * price[i-1])
#    return price
#
#for run in range(10):
#    plt.plot(random_walk(10.0))
#plt.xlabel("Time")
#plt.ylabel("Price");
runs = 10000
simulations = np.zeros(runs)
for run in range(runs):
    simulations[run] = random_walk(10.0)[days-1]
q = np.percentile(simulations, 1)
plt.hist(simulations, normed=True, bins=30, histtype='stepfilled', alpha=0.5)
plt.figtext(0.6, 0.8, "Start price: %.2f" % df["Adj Close"][0])
plt.figtext(0.6, 0.7, "Mean final price: %.2f" % simulations.mean())
plt.figtext(0.6, 0.6, "VaR(0.99): %.2f" % (10 - q,))
plt.figtext(0.15, 0.6, "q(0.99): %.2f" % q)
plt.axvline(x=q, linewidth=4, color='r')
plt.title("Final price distribution after {} days".format(days), weight='bold');














