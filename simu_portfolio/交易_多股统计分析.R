library(quantmod) 
tickers <- c('BAYN.DE','IFX.DE','BMW.DE','DTE.DE','ADDYY')
for(ticker in tickers) {
  portfolio_prices <- cbind(portfolio_prices,
                            getSymbols.yahoo(ticker,
                                             from='2019-02-01',
                                             periodicity='daily',
                                             auto.assign=FALSE)[, 4])}
portfolio_returns <- na.omit(ROC(portfolio_prices))
library(PerformanceAnalytics)
portfolio_returns_whole <- Return.portfolio(portfolio_returns)
table.AnnualizedReturns(portfolio_returns_whole)
table.CalendarReturns(portfolio_returns_whole)
