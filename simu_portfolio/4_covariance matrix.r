# library(PerformanceAnalytics)
# library()
library(quantmod)
# library(xts)
# library(urca)
# library(timeSeries)
# library(fPortfolio)

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

# following is Садыков его метод for matrix calculation
mean_vect = colMeans(six)
plot.new()
pairs(six)
cov_mat = cov(six)
cov_mat
sd_vect = sqrt(diag(cov_mat))
sd_vect
