library(quantmod) 
tickers <- c('BAYN.DE','IFX.DE','BMW.DE','DTE.DE','ADDYY')
for(ticker in tickers) {
  portfolio_prices <- cbind(portfolio_prices,
                            getSymbols.yahoo(ticker,
                                             from='2019-02-01',
                                             periodicity='daily',
                                             auto.assign=FALSE)[, 4])}
portfolio_returns <- na.omit(ROC(portfolio_prices))

library(PortfolioAnalytics)
# construct restrictions
pspec <- portfolio.spec(colnames(portfolio_returns))
# add/updata optimization constraints (turnover, diversification, position...)
pspec <- add.constraint(pspec,
                        type='risk',
                        name='StdDev',
                        target=.005)
pspec <- add.constraint(pspec,
                        type='weight_sum',
                        min_sum=.8,
                        max_sum=.99)
pspec <- add.constraint(pspec,
                        type='transaction_cost',
                        pct=.001)
pspec <- add.constraint(pspec,
                        type='return',
                        name='mean')
pspec <- add.constraint(pspec,
                        type='box',
                        min=.1,
                        max=.5)

# 生成随机10000个portfolio


# solver
optimized_portf <- optimize.portfolio(portfolio_returns,
                                      pspec,
                                      optimize_method='ROI',
                                      trace=TRUE)
chart.Weights(optimized_portf)
eff <- extractEfficientFrontier(optimized_portf,
                         match.col='StdDev')
chart.EfficientFrontier(eff,
                         match.col='StdDev')