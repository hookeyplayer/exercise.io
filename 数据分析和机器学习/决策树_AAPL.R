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

# 预测正负знак
AAPL$ReturnsSign <- ifelse(AAPL$Returns<0, 'Down', 'Up')
AAPL$ReturnsTmr <- c(AAPL$ReturnsSign[-1], NA)

# 创建因子变量
AAPL$Weekday <- factor(weekdays(AAPL$Date))
AAPL$Intraday <- factor(ifelse(AAPL$Close-AAPL$Open, 1, -1))
AAPL <- AAPL[-c(1, nrow(AAPL)),]
head(AAPL)

train <- AAPL[1:600,]
test <- AAPL[-(1:600),]

# 绘制决策树
simple.tree <- rpart(data=train, 
                     ReturnsTmr ~ ReturnsSign+Weekday+Intraday,
                     method='class')
fancyRpartPlot(simple.tree, sub='simple tree')
