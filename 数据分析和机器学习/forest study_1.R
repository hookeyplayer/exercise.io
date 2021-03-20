# 用决策树来建模strategy

library(quantmod)
library(PerformanceAnalytics)
library(FinTS)
library(rpart)
library(rattle)
library(rpart.plot)

getSymbols('AAPL', from='2016-03-20', to='2021-03-20', src='yahoo')
AAPL <- data.frame(AAPL)
AAPL$Date <- rownames(AAPL)
colnames(AAPL) <- c('Open', 'High', 'Low', 'Close', 'Volume', 'Adjusted', 'Date')
AAPL$Date <- as.Date(AAPL$Date)

# логарифмичесая доходность
AAPL$Returns <- c(NA, diff(log(AAPL$Adjusted)))
str(AAPL)

# 日收益和drawdown
strategy <- xts(AAPL$Returns, order.by=AAPL$Date)
charts.PerformanceSummary(strategy)

# 回报、std dev、夏普
table.AnnualizedReturns(strategy)
