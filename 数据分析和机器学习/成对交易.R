library(quantmod)
require(PerformanceAnalytics)
library(timeSeries)
library(MASS)
getSymbols('AAPL',from="2009-01-01",to="2015-01-01")
getSymbols('MSFT',from="2009-01-01",to="2015-01-01")
plot(Ad(AAPL))
lines(Ad(MSFT), col=2)
summary(lm(Ad(AAPL) ~ Ad(MSFT)))
getSymbols('MA',from="2009-01-01",to="2015-01-01")
getSymbols('V',from="2009-01-01",to="2015-01-01")
plot(Ad(MA))
lines(Ad(V), col=2)
summary(lm(Ad(V) ~ Ad(MA)))

train.end <- '2013-01-01'
V.train <- window(Ad(V), start='2009-01-01', end=train.end)
MA.train <- window(Ad(MA), start='2009-01-01', end=train.end)
V.test <- window(Ad(V), start=train.end, end='2015-01-01')
MA.test <- window(Ad(MA), start=train.end, end='2015-01-01')
pairsModel <- lm(MA.train ~ V.train)
summary(pairsModel)

x <- pairsModel$residuals
y <- data.frame(x)[, 1]
plot(y, type='l')
border.top <- sd(y)
border.bottom <- -sd(y)
abline(h=border.top, col=3, lty=2)
abline(h=border.bottom, col=2, lty=2)

# 测试交易策略的有效性
V.ret <- lag(Return.calculate(V.test), -1)
MA.ret <- lag(Return.calculate(MA.test), -1)
residuals <- MA.test - (V.test*pa)
pairsRet <- ifelse(residuals>border.top, (-MA.ret+V.ret)/2, ifelse(residuals<border.bottom, (MA.ret-V.ret)/2, 0))
Portf <- (V.ret+MA.ret)/2
str <- cbind(pairsRet, Portf)
colnames(str) <- c('pairs trade', '50/50 portfolio')
charts.PerformanceSummary(str)
table.AnnualizedReturns(str)
maxDrawdown(str)
table.AnnualizedReturns(str)
maxDrawdown(str)
                   