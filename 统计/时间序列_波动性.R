require(quantmod)
library(PerformanceAnalytics)
startdate <- '2019-02-01'
enddate <- '2021-02-01' 

aapl_close <- getSymbols.yahoo('AAPL',
                               from=startdate,
                               auto.assign=F)[, 6]
head(aapl_close)

# coefficients ------------------------------------------------------------

# weeklyreturn/monthlyReturn/quarterlyReturn...
aapl_logrets <- na.omit(dailyReturn(aapl_close, type="log"))
