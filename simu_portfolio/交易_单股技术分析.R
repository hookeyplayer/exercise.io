# 获取数据 --------------------------------------------------------------------

library(quantmod)
library(magrittr) # 管道函数
library(dplyr)

getSymbols('AAPL',from="2019-01-01",to="2021-02-22")

head(AAPL)
tail(AAPL)
plot(AAPL$AAPL.Adjusted)

AAPL_log_returns <- AAPL%>%Ad()%>%dailyReturn(type='log')
plot(AAPL_log_returns)

summary(AAPL)

AAPL.delFirst<-AAPL[-1,] # 删除首行
head(AAPL.delFirst)

AAPL.onlyFirst<-AAPL[1,] # 截取首行
AAPL.onlyFirst

AAPL[c(1,nrow(AAPL)),] # 首行和末行

# 技术分析 --------------------------------------------------------------------

AAPL%>%Ad()%>%chartSeries()
# Add Bollinger Bands/Volumn/moving average convergence divergence to Chart
AAPL%>%chartSeries(TA='addBBands();addVo();addMACD()',subset='2020')

# Convert Daily to Weekly
wk<-AAPL
weekly<-to.weekly(wk)
weekly[c(1:3,nrow(weekly)),]

# Convert Daily to Monthly
mo<-AAPL
monthly<-to.monthly(mo)
monthly[c(1:3,nrow(monthly)),]

# Average
mean(AAPL_log_returns)

# Volatility 
sd(AAPL_log_returns)

# 对频率分布对normality test - Shapiro-Wilk test
shapiro.test(as.vector(AAPL_log_returns))

# T-Test for a One-Time Series
t.test(AAPL_log_returns, mu=0)

# Simple Moving Average
n <- 20
SMA <- rollapply(AAPL$AAPL.Adjusted,
                 width = n,
                 FUN = mean,
                 by.column = TRUE,
                 fill = NA,
                 align = "right")

# Moving Average Convergence Divergence Oscillator (MACD)
n1 <- 12
n2 <- 26
MACD <- rollapply(AAPL$AAPL.Adjusted,
                  width = n2,
                  FUN = function(v) mean(v[(n2 - n1 + 1):n2]) - mean(v),
                  by.column = TRUE,
                  fill = NA,
                  align = "right")

# Bollinger Bands
n <- 20
BB <- rollapply(AAPL$AAPL.Adjusted,
                width = n,
                FUN = sd,
                by.column = TRUE,
                fill = NA, align = "right")
upperseries <- meanseries + 2 * BB
lowerseries <- meanseries + 2 - BB