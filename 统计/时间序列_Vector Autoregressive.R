# 下载数据 --------------------------------------------------------------------
# 3-component VAR model (equity return, stock index, US Treasury bond interest rates)
# Task: Forecast stock market index using additional variables, identify impluse responses.
# Assume exists a hidden long-term relationship between these three components.
rm(list = ls()) 
install.packages('xts');
library(xts)
install.packages('vars');
library('vars')
library('quantmod')
getSymbols('SNP', from='2012-01-02', to='2021-02-01')      
getSymbols('MSFT', from='2012-01-02', to='2021-02-01')
getSymbols('DTB3', src='FRED')  #3-month T-Bill interest rates
chartSeries(MSFT, theme=chartTheme('white'))   

# Cl(MSFT)    #closing prices
# Op(MSFT)    #open prices
# Hi(MSFT)    #daily highest price
# Lo(MSFT)    #daily lowest price
# ClCl(MSFT)  #close-to-close daily return
# Ad(MSFT)    #daily adjusted closing price

# 处理数据 --------------------------------------------------------------------
#indexing time series data
DTB3.sub <- DTB3['2012-01-02/2021-02-01']

SNP.ret  <- diff(log(Ad(SNP)))
MSFT.ret <- diff(log(Ad(MSFT)))

DTB3.sub[is.na(DTB3.sub)] <- 0
DTB3.sub <- na.omit(DTB3.sub) 

dataDaily <- na.omit(merge(SNP.ret, MSFT.ret, DTB3.sub), join='inner')

# VAR modeling usually deals with lower frequency data, so transform data to monthly 
# (or quarterly) frequency.
SNP.M  <- to.monthly(SNP.ret)$SNP.ret.Close
MSFT.M <- to.monthly(MSFT.ret)$MSFT.ret.Close
DTB3.M <- to.monthly(DTB3.sub)$DTB3.sub.Close

# allow a max of 4 lags
# choose the model with best(lowest Akaike Information Criterion value)
var1 <- VAR(dataDaily, lag.max=4, ic="AIC")

VARselect(dataDaily,lag.max=4)

summary(var1)

coef(var1)  #concise summary of the estimated variables
residuals(var1) #list of residuals (of the corresponding ~lm)
fitted(var1)    #list of fitted values
Phi(var1)   #coefficient matrices of VMA representation
plot(var1, plot.type='multiple') #Diagram of fit and residuals for each variables

#confidence interval for bootstrapped error bands
var.irf <- irf(var1, ci=0.9)
plot(var.irf)

