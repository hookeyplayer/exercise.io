library(PerformanceAnalytics)
library()
library(quantmod) 
library(xts)
library(urca)
library(timeSeries)
library(fPortfolio)

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

# log daily returns of stocks
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
# rename columes
names(six)<-c("ifx", "bayn", "bmw", "alv", "dte", "adidas", "DAX")

# annualize returns, 3y treasury rate 11.26 update risk-free rate 0.41%
Rf <- .41
CAPM.alpha(six[, 1:6],six[,7],Rf=.0041)
CAPM.beta(six[,1:6],six[,7],Rf=.0041)
results <- table.AnnualizedReturns(six, Rf=Rf)
results

# barChart(dax)
3
# (fit <- lm(riskpremium_ifx ~ riskpremium_DAX))
riskpremium_bmw <- six$bmw - Rf
riskpremium_bayn <- six$bayn - Rf
riskpremium_alv <- six$alv - Rf
riskpremium_dte <- six$dte - Rf
riskpremium_adidas <- six$adidas - Rf
(fit <- lm(riskpremium_adidas ~ riskpremium_DAX))
# plot(fit)
# abline(fit, col='red')
summary(fit)
