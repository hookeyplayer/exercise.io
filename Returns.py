# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:25:06 2020

@author: xiaofan
"""
import numpy as np
import calendar
import datetime as dt
#import pandas_datareader.data as web #pip install pandas-datareader
import matplotlib.pyplot as plt; plt.rcdefaults()
import pandas as pd
import math
#from time import time
#import warnings
#warnings.filterwarnings("ignore")
import yfinance as yf # pip install yfinance --upgrade --no-cache-dir
yf.pdr_override()
symbol = ['^HSI']
start = '2000-09-01'
end = '2020-09-01'
df = yf.download(symbol, start, end)
# =============================================================================
# window-customized time series
# =============================================================================
# subplots of Return and Adj Close
#df['Returns'] = df['Adj Close'].pct_change().dropna()
#df[['Adj Close', 'Returns']].plot(subplots = True, figsize = (8, 6))
#print(df.tail())

# moving averages(trends)
#df['42d'] = df['Adj Close'].rolling(window = 42).mean()
#df['252d'] = df['Adj Close'].rolling(window = 252).mean()
#df[['Adj Close', '42d', '252d']].plot(grid = True)

# =============================================================================
# monthly transformation
# =============================================================================
#monthly = df.asfreq('BM')
#monthly['Returns'] = df['Adj Close'].pct_change().dropna()
#
#monthly = monthly.reset_index()
#monthly['Month'] = monthly['Date'].dt.month # dt is function from datetime 
#print(monthly)
#plt.bar(monthly['Years'], monthly['Returns'], align = 'center')
#plt.figure(figsize = (10, 4))

#a = pd.date_range(start = '2018-01-03', end = '2018-01-08')

#print(dataset.head())

# =============================================================================
# second way of fetch data from website
# =============================================================================
#DAX = web.DataReader('^GDAXI', data_source = 'yahoo', start = '2010-01-01',
#                       end = '2020-08-31')
#DAX.info()
#DAX['Close'].plot(grid = True, figsize = (8, 6))

