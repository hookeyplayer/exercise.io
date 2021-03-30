library(quantmod)
library(PerformanceAnalytics)
library(finTS)
library(rpart)
library(rpart.plot)
library(rattle)
library(xts)

# 下载数据 --------------------------------------------------------------------
equity <- 'GOOS'
from <- '2017-03-21'
to <- '2021-03-30'
getSymbols(equity,from = from, to = to)
plot(GOOS$GOOS.Adjusted)
goose <- data.frame(GOOS)

# 原始数据没有一列是日期，此处添加此日期列
goose$Date <- as.Date(rownames(goose))

goose$Returns <- c(NA, diff(log(goose$GOOS.Adjusted)))

# Buy and Hold 策略
# Returns原始类型是numeric，需要改成时间序列
goose_returns <- xts(goose$Returns, order.by = goose$Date)
charts.PerformanceSummary(goose_returns)

#年化收益计算
table.AnnualizedReturns(goose_returns)

# 涨跌indicator的表示
goose$Return_sign <- ifelse(goose$Returns > 0, 'Up', 'Down')

# 第二天的单独挑出来为一列
goose$Weekday <- factor(weekdays(goose$Date))
goose$Intraday <- factor(ifelse(goose$GOOS.Close - goose$GOOS.Open > 0, 1, -1))
goose <- goose[-c(1, nrow(goose)), ] 

goose$Second_day <- c(goose$Return_sign[-1], NA)

train <- goose[1:600,]
test <- goose[-(1:600),]

simple_tree <- rpart(data = train, 
                     Second_day ~ Return_sign + Weekday + Long_term_momentum +
                       Intraday + diffVolume,
                     method = 'class')
fancyRpartPlot(simple_tree,
               sub = 'Simple tree from rforfinance.ru')

Prediction <- as.character(predict(simple_tree, test, type = 'class'))
# predict 类型是factor
Strategies <- data.frame(rep('Up', nrow(test)), Prediction)
colnames(Strategies) <- c('buy&hold', 'simple tree strategy')
Strategies <- rbind(c(NA, NA), Strategies[-nrow(Strategies), ])
head(Strategies)

Strategies <- ifelse(Strategies == 'Up', test$Returns, -test$Returns)
charts.PerformanceSummary(xts(Strategies, order.by = test$Date))

table.AnnualizedReturns(xts(Strategies, order.by = test$Date))

maxDrawdown(xts(Strategies, order.by = test$Date))
