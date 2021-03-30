library(quantmod)
library(FinTS)
library(randomForest)
library(PerformanceAnalytics)
# library(xts)

equity <- 'GOOS'
from <- '2017-03-21'
to <- '2021-03-30'
getSymbols(equity,from = from, to = to)
goose <- data.frame(GOOS)
goose$Date <- as.Date(rownames(goose))

goose$Returns <- c(NA, diff(log(goose$GOOS.Adjusted)))
# goose_returns <- xts(goose$Returns, order.by = goose$Date)


# 指标计算 --------------------------------------------------------------------

# moving average
goose$Short_term_momentum <- ifelse(goose$GOOS.Adjusted > SMA(goose$GOOS.Adjusted, 5), 
                                    1, -1)
goose$Long_term_momentum <- ifelse(goose$GOOS.Adjusted > SMA(goose$GOOS.Adjusted, 40), 
                                    1, -1)
# Close relative to day range
goose$CRTDR <- (goose$GOOS.Close - goose$GOOS.Low) / (goose$GOOS.High - goose$GOOS.Low)

goose$Intraday <- ifelse(goose$GOOS.Close > goose$GOOS.Open, 1, -1)

goose$RSI <- cut(RSI(goose$GOOS.Adjusted), breaks = c(0 ,30, 70, 100))

goose$diffEMA <- sign(EMA(goose$GOOS.Adjusted, 12) - EMA(goose$GOOS.Adjusted, 26))

goose$diffVolume <- sign(c(NA, diff(goose$GOOS.Volume)))

goose$second_day <- c(goose$Return_sign[-1], NA)
head(goose$second_day)

goose <- goose[-(1:40), ]
