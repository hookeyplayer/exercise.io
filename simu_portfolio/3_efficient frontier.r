# csv file generate six stocks
# df <- read.csv("sixraw.csv", head = TRUE, sep = ",") # adjusted close combined
# str(df)
# return <- log(tail(df, -1) / head(df, -1))

# R-package download six stocks
library(quantmod) 
library(xts)
library(urca)
# library(timeSeries)
library(fPortfolio)
library(PortfolioAnalytics)

ifx <- getSymbols('IFX.DE', from='2010-12-10', to='2020-11-26')
bayn <- getSymbols('BAYN.DE', from='2010-12-10', to='2020-11-26')
bmw <- getSymbols('BMW.DE', from='2010-12-10', to='2020-11-26')
alv <- getSymbols('ALV.DE', from='2010-12-10', to='2020-11-26')
dte <- getSymbols('DTE.DE', from='2010-12-10', to='2020-11-26')
adidas <- getSymbols('ADDYY', from='2010-12-10', to='2020-11-26')

data_env <- new.env()
# dax index processing(fetch + log return)
getSymbols(Symbols='^GDAXI', from='2010-12-10', to='2020-11-26',
                  env = data_env)
dax <- do.call(merge, eapply(data_env, Ad))
# a <- log(dax)
# a[is.na(a)] <- 0
# a <- na.omit(a)
# Augmented Dickey-Fuller Test Unit Root Test
# summary(ur.df(a, type = 'none'))
dax.return <- diff(log(dax))
dax.return[is.na(dax.return)] <- 0 #replace NA values
dax.return <- na.omit(dax.return)

# log returns of stocks
ifx.return <- diff(log(Ad(IFX.DE)))
bayn.return <- diff(log(Ad(BAYN.DE)))
bmw.return <- diff(log(Ad(BMW.DE)))
alv.return <- diff(log(Ad(ALV.DE)))
dte.return <- diff(log(Ad(DTE.DE)))
adidas.return <- diff(log(Ad(ADDYY)))

# merge together stocks with dax
six <- na.omit(merge(ifx.return, bayn.return, bmw.return,
                     alv.return, dte.return, adidas.return,
                     dax.return), join='inner')
head(six)

# portfolio optimization
# covariance matrix_
Q <- rbind(cov(six), rep(1, ncol(six)), colMeans(six))
round(Q, 5) # results rounded to 5 digs
# combine last two rows of matrix(tail) as new columns on the left
Q <- cbind(Q, rbind(t(tail(Q, 2)), matrix(0, 2, 2))) # covariance matrix
round(Q, 5)

# mu = 0.0106 # use dickey fuller test's results
# b <- c(rep(0, ncol(six)), 1, mu)
# b
# solve(Q, b) # optimal weights the Lagrange multipliers
# 
# plot(portfolioFrontier(six))
# Spec <- portfolioSpec()
# `setSolver<-`(Spec, "solveRshortExact")
# Frontier <- portfolioFrontier(as.timeSeries(six), Spec)
# 
# frontierPlot(Frontier, col = rep('orange', 2), pch = 19)
# grid()
# monteCarloPoints(Frontier, mcSteps = 1000, cex = 0.25, pch = 19)
funds <- colnames(six)
portf_maxret <- portfolio.spec(assets = funds)
portf_maxret <- add.constraint(portfolio = portf_maxret,
                               type = "full_investment")
portf_maxret <- add.constraint(portfolio = portf_maxret, type = "box",
                               min=c(.04, .05, .03, .02, .04, .02),
                               max=c(.5, .4, .4, .4, .6, .5))

opt_maxret <- optimize.portfolio(R=returns, portfolio = portf_maxret,
                   optimize_method = "ROI", trace = TRUE)


