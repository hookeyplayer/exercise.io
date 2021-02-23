# Simulation of Cointegration ---------------------------------------------
set.seed(20200229)
N <- 100  
x <- cumsum(rnorm(N)) 
gamma <- 0.7    
# simulate the cointegrating series
y <- gamma * x + rnorm(N) 
plot(x, col="black", type='l', lwd=2, ylab='simulated values')  
lines(y,col="skyblue", lwd=2) 

# Augmented Dickey-Fuller Test 单位根检验 -------------------------------------------------------------------
library('urca')
summary(ur.df(x,type="none"))  
summary(ur.df(y,type="none"))  
# Both series are individually unit root process.

# Engle-Granger -----------------------------------------------------------
# Step 1: Run linear regression yt on xt (simple OLS estimation).
# Step 2: Test residuals for the presence of a unit root.
#regression without constant
coin <- lm(y ~ x - 1)     
summary(ur.df(coin$resid)) # Reject
# Pair trading (statistical arbitrage) exploits such cointegrating relationship,
# aiming to set up strategy based on the spread between two time series.
# If two series are cointegrated,
# we expect their stationary linear combination to revert to 0.
# By selling relatively expensive and buying cheaper one,
# wait for the reversion to make profit.
# 
# Intuition: Linear combination of time series (which form cointegrating relationship) 
# is determined by underlying (long-term) economic forces,
# e.g., same industry companies may grow similarly;
# spot and forward price of financial product are bound together by no-arbitrage principle;
# FX rates of interlinked countries tend to move together.

# Two variable: Engle-Granger
# Multivariate: Johansen procedure

library(quantmod)
getSymbols('DTB3', src = 'FRED')
getSymbols('DTB6', src = 'FRED')
DTB3.sub = DTB3['1999-03-18/2021-02-01']
DTB6.sub = DTB6['1999-03-18/2021-02-01']
plot(DTB3.sub)
lines(DTB6.sub, col = 'pink')

# ADF test ----------------------------------------------------------------
a = as.numeric(na.omit(DTB3.sub))
b = as.numeric(na.omit(DTB6.sub))
y = cbind(a, b)
cointregr <- lm(a ~ b)
r = cointregr$residuals
library(urca)
summary(ur.df(r,type = 'none'))

# Phillips and Ouliaris test ----------------------------------------------
# NULL: Two series are not cointegrated. 
library(tseries)
pocointregr <- po.test(y, demean = T, lshort = T)
pocointregr$parameter
pocointregr$p.value

# Johansen Procedure test -------------------------------------------------
# K is lag order
johansentest <- ca.jo(y, type = c('trace'), ecdet = c('none'), K = 2)
summary(johansentest)
# The test statistic for r = 0 is 113.71 > critical, indicating rejection of NULL;
# for r  ≤ 1, cannot reject NULL.
# Thus, conclude that one cointegrating relationship exists.
yJoregr = cajorls(johansentest, r = 1)
yJoregr
# The coefficient of error-correction term is negative:
# short-term deviation from long-term equilibrium would push to zero-equilibrium


