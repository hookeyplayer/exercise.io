library(quantmod)
library(vars)
getSymbols('EEM')
eem.sub = EEM['2016-03-19/2021-03-19']
head(eem.sub)
getSymbols('^GSPC')
snp.sub = GSPC['2016-03-19/2021-03-19']
head(snp.sub)

eem.ret <- diff(log(Ad(eem.sub)))
snp.ret  <- diff(log(Ad(snp.sub)))
head(eem.ret)
head(snp.ret)

whole <- na.omit(merge(eem.ret, snp.ret), join='inner')

plot(eem.ret)
lines(snp.ret, col = 'pink')

rgmodel <- lm(eem.ret ~ snp.ret, data=whole)
rgmodel
summary(rgmodel)

eem.m  <- to.monthly(eem.ret)$eem.ret.Close
snp.m <- to.monthly(snp.ret)$snp.ret.Close


# 滞后阶数暂定为4
var1 <- VAR(whole, lag.max=4, ic="AIC")
VARselect(whole,lag.max=4)
summary(var1)

coef(var1)
residuals(var1)
fitted(var1)    #list of fitted values

# VMA的φ，相隔s期的动态乘子的多维推广，即n维列向量对n维行向量求偏导得到的矩阵
Phi(var1)
plot(var1, plot.type='multiple')

#confidence interval for bootstrapped error bands
var.irf <- irf(var1, ci=0.95)
plot(var.irf)
