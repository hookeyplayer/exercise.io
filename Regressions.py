import numpy as np
import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import yfinance as yf
from scipy import stats
symbol1 = 'GEMCX'
symbol2 = 'GSAGX'
start = '2018-09-01'
end = '2020-09-01'
gsem = yf.download(symbol1, start, end)
gscef = yf.download(symbol2, start, end)
# =============================================================================
# transform
# =============================================================================
gsem = gsem.fillna(method = 'ffill')
gsem['log_return'] = np.log(gsem['Adj Close'] / gsem['Adj Close'].shift(1))
gscef = gscef.fillna(method = 'ffill')
gscef['log_return'] = np.log(gscef['Adj Close'] / gscef['Adj Close'].shift(1))

# =============================================================================
# OLS Regression
# =============================================================================
#df = pd.DataFrame({'A': gsem['log_return'], 'B': gscef['log_return']})
#result = sm.ols(formula = 'A ~ B', data = df).fit()
#print(result.summary())
# correlation
stats.spearmanr(gsem['Adj Close'], gscef['Adj Close'])
print(np.corrcoef(gsem['Adj Close'], gscef['Adj Close']))


# =============================================================================
## plotting
## =============================================================================
#plt.plot(gsem['log_return'], gscef['log_return'], 'r.')
#ax = plt.axis() # grab x-axis values
#x = np.linspace(ax[0], ax[1] + 0.01)
#plt.plot(x, -0.0003 + x * 0.9303, 'b')
#plt.grid(True)
#plt.xlabel('Goldman Sachs Emerging Market Index')
#plt.ylabel('Goldman Sachs China Equity Fund')
#plt.title('Scatter of log returns and regresson line')

#upper = plt.subplot(2, 1, 1)
#upper.plot(gsem['Adj Close'])
#upper.legend(loc = 'upper left')
#upper.set_title('Stock' + symbol1 + 'Closing Price')
#upper.set_ylabel('Price')
#lower = plt.subplot(2, 1, 2)
#lower.plot(gscef['Adj Close'], color = 'r')
#lower.set_title('Stock' + symbol2 + 'Closing Price')
#lower.set_ylabel('Price')
#gsem['VolPositive'] = gsem['Low'] < gsem['Adj Close']
#colors = gsem['VolPositive'].map({True: 'g', False: 'r'})
#lower.bar(gsem.index, gsem['Volume'], color = colors, alpha = 0.5) # slight
#lower.set_ylabel('Volume')