# 3-component VAR model (equity return, stock index, US Treasury bond interest rates)
# Task: 预测 stock market index using additional variables，并识别脉冲响应。
# Assume: 三个变量之间存在长期均衡关系。

rm(list = ls()) 
library(xts)
library('vars')
library('quantmod')

# 下载数据 --------------------------------------------------------------------
getSymbols('SNP', from='2012-01-02', to='2021-02-01')      
getSymbols('MSFT', from='2012-01-02', to='2021-02-01')
getSymbols('DTB3', src='FRED')  #3-month T-Bill interest rates

# 处理数据 --------------------------------------------------------------------
#indexing time series data
DTB3.sub <- DTB3['2018-03-14/2021-03-14']
DTB3.sub[is.na(DTB3.sub)] <- 0
DTB3.sub <- na.omit(DTB3.sub) 

# 对数差分 --------------------------------------------------------------------
SNP.ret  <- diff(log(Ad(SNP)))
MSFT.ret <- diff(log(Ad(MSFT)))

dataDaily <- na.omit(merge(SNP.ret, MSFT.ret, DTB3.sub), join='inner')

# VAR 模型通常使用低频数据，so transform data to monthly (or quarterly).
SNP.M  <- to.monthly(SNP.ret)$SNP.ret.Close
MSFT.M <- to.monthly(MSFT.ret)$MSFT.ret.Close
DTB3.M <- to.monthly(DTB3.sub)$DTB3.sub.Close

# 滞后阶数暂定为4
var1 <- VAR(dataDaily, lag.max=4, ic="AIC")
VARselect(dataDaily,lag.max=4)
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
