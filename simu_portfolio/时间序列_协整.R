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
