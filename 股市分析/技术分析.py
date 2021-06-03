# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt
from matplotlib import dates as mdates
import mplfinance as mpl
import ta

import warnings
warnings.filterwarnings("ignore")

symbol = 'TSLA'
start = '2019-01-01'
end = '2021-06-01'
df = yf.download(symbol, start, end)

# **1. Accumulation Distribution Line**


df['Money Flow Multiplier'] = (2*df['Adj Close']-df['Low']-df['High'])/(df['High']-df['Low'])
df['Money Flow Volume'] = df['Money Flow Multiplier']*df['Volume']
df['ADL'] = df['Money Flow Volume'].cumsum()
df = df.drop(['Money Flow Multiplier','Money Flow Volume'], axis=1)
df['Volume Positive'] = df['Open'] < df['Adj Close']
df.head()

fig = plt.figure(figsize=(14,10))
ax1 = plt.subplot(3, 1, 1) # nrows, ncols, index
ax1.plot(df['Adj Close'])
ax1.set_title(symbol + ' Closing Price')
ax1.set_ylabel('Price')
ax1.legend(loc='best')

ax2 = plt.subplot(3, 1, 2)
ax2.plot(df['ADL'], label='Accumulation Distribution Line')
ax2.grid()
ax2.legend(loc='best')
ax2.set_ylabel('Accumulation Distribution Line')

ax3 = plt.subplot(3, 1, 3)
ax3v = ax3.twinx()
colors = df['Volume Positive'].map({True: 'g', False: 'r'})
ax3v.bar(df.index, df['Volume'], color=colors, alpha=0.4)
ax3.set_ylabel('Volume')
ax3.set_title(symbol + ' intraday trend')
ax3.grid()
ax3.set_xlabel('Date')

# **2. Average Direction MoveMovement Index**
# 
# ≤ 20, trend is weak;
# ≥ 50, trend is stong.


# 另一种下载数据的方式
apple = yf.Ticker('AAPL')
df = apple.history(start='2020-01-01', end='2021-06-01')
df.head()
df['ADX'] = ta.trend.adx(df['High'], df['Low'], df['Close'], window=20)
df[['ADX']].plot(figsize=(10,8))
plt.show()

# **3. Exponential Moving Average**


df['EMA'] = ta.trend.ema_indicator(df['Close'], window=20)
df[['Close', 'EMA']].plot(figsize=(10,8))
plt.show()

# **4. Bollinger Bands**


df['Low_band'] = ta.volatility.bollinger_lband(df['Close'], window=20)
df['Up_band'] = ta.volatility.bollinger_hband(df['Close'], window=20)
df[['Low_band', 'Up_band', 'Close']].plot(figsize=(10,8), grid=True)
plt.show()

# **5. Relative Strength Index**


df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
df[['RSI']].plot(figsize=(10,8))
plt.show()

