require(fOptions)
# Calculate a ECO on a stock.
# Ex-dividend dates in 3 and 6 months, each dividend is expected to be 1.
# P0 = 80, K = 80, σ = 0.25 per annum, rf = 0.07; T = 1.
K <- 80
r <- 0.07
sigma <- 0.25
tau <- 1
# pv of expected dividends
d <- exp(-(tau/4) * r) + exp(-(tau/2) * r)
S <- K - d
y <- (log(S/K) + (r - sigma^2 / 2) * tau) / (sigma * sqrt(tau))
cdfy <- pnorm(y) # Φ(d2)
cdfn <- pnorm(y + sigma * sqrt(tau)) # Φ(d1)
# BS formula
C <- S * cdfn - (K * exp(-r * tau) * cdfy)


# Continuously compounded dividend yield is 0.015.
# S0 = 100, K = 100, option expires in 275 days, volatility is 0.45.
# Continuously compounded rf = 0.03.
GBSOption('p', 100 * exp(-0.015 * (275/365)), 100, 275/365, 0.03, 0.03, 0.45)


# 绘制二叉树
# Stock P0 = 900, K = 950, r = 0.02, T = 3m, Volatility = 0.22
tree <- BinomialTreeOption(TypeFlag = 'ce', S = 900, X = 950, 1/4, 0.02, b = 0.02, sigma = 0.22, n = 3)
BinomialTreePlot(tree, dy = 1, xlab = 'Time steps', ylab = 'number of up steps', xlim = c(0, 4))
title(main = 'European Call Option')