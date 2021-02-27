library(quantmod) 
tickers <- c('BAYN.DE','IFX.DE','BMW.DE','DTE.DE','ADDYY')
weights <- c(0.2, 0.2, 0.2, 0.2, 0.2)
portfolio_prices <- NULL
# 4只股票/市场指数 的 close price和rate of change整合
for(ticker in tickers) {
  portfolio_prices <- cbind(portfolio_prices,
                            getSymbols.yahoo(ticker,
                                             from='2019-02-01',
                                             periodicity='daily',
                                             auto.assign=FALSE)[, 4])}

# portfolio_prices[is.na(portfolio_prices)] <- 0
portfolio_prices <- na.omit(portfolio_prices)

colSums(is.na(portfolio_prices))

benchmark_prices <- getSymbols.yahoo('^GDAXI',
                                    from='2019-02-01',
                                    periodicity='daily',
                                    auto.assign=FALSE)[, 4]
benchmark_prices <- na.omit(benchmark_prices)


library(PerformanceAnalytics)
portfolio_returns_whole <- na.omit(Return.portfolio(portfolio_prices))
# 处理不知道是否恰当
portfolio_returns_whole[is.infinite(portfolio_returns_whole)] <- 0
SharpeRatio(portfolio_returns_whole, Rf=.035/256)

CAPM.beta(portfolio_returns_whole, benchmark_returns, Rf=.035/256)
CAPM.jensenAlpha(portfolio_returns_whole, benchmark_returns, Rf=.035/256)