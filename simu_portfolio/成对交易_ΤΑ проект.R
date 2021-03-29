library(quantmod)
library(zoo)
library(PerformanceAnalytics)
# получение данных ---------------------------------------------------------

# Каждый: Китайский фармацевтический дистрибутор
stock1 <- "3320.HK" # China Resources Pharmacutical
stock2 <- '1099.HK' # Sinopharm

getSymbols(stock1, src = "yahoo", from = '2016-11-12')
getSymbols(stock2, src = "yahoo", from = '2016-11-12')
# getSymbols(stock3, src = "yahoo", from = '2018-09-12')

crp <- `3320.HK`
sinopharm <- `1099.HK`

length(crp) # 6468
length(sinopharm) # 6468

plot(Ad(sinopharm), ylim = c(0, 40),
     main = 'Визуализация возможно/нет коинтеграции:
     CRP(синий) & Sinopharm (черный)',
     ylab = "Adjusted closing price")
lines(Ad(crp), col = 4)

summary(lm(Ad(crp) ~ Ad(sinopharm)))


# Парный трейдинг (train) -------------------------------------------------

crp_train <- window(Ad(crp), start = '2016-11-12', end = '2020-06-12')
sinopharm_train <- window(Ad(sinopharm), start = '2016-11-12', end = '2020-06-12')
length(crp_train) # 883
length(sinopharm_train) # 883

crp_test <- window(Ad(crp), start = '2020-06-14', end = '2021-03-26')
sinopharm_test <- window(Ad(sinopharm), start = '2020-06-14', end = '2021-03-26')

length(crp_test) # 195
length(sinopharm_test) # 195

summary(lm(Ad(crp_train) ~ Ad(sinopharm_train)))
pairsmodel <- lm(Ad(crp_train) ~ Ad(sinopharm_train))

pairsmodel$residuals
summary(pairsmodel$residuals)

crp_ret <- lag(Return.calculate(crp_test), -1)
sinopharm_ret <- lag(Return.calculate(sinopharm_test), -1)

residuals <- crp_test - pairsmodel$coefficients[2] * sinopharm_test + pairsmodel$coefficients[1]
border_top <- sd(pairsmodel$residuals)
border_bottom <- -sd(pairsmodel$residuals)

pairs_ret <- ifelse(residuals > border_top, (-crp_ret + sinopharm_ret)/2,
                    ifelse(residuals < border_bottom, (crp_ret - sinopharm_ret)/2, 0))
portf <- (crp_ret + sinopharm_ret)/2
together <- cbind(portf, pairs_ret)
colnames(together) <- c('50/50 Portfolio', 'Pairstrading')
charts.PerformanceSummary(together)

table.AnnualizedReturns(together)

crp_adj <- crp[, grep("Adjusted", colnames(crp))]
sinopharm_adj <- sinopharm[, grep("Adjusted", colnames(sinopharm))]
sinopharm_change <- periodReturn(sinopharm_adj, period='daily', type='log')
crp_change <- periodReturn(crp_adj, period='daily', type='log')

crp_returns <- round(crp_change+1, 4)
crp_returns[1] <- 1
norm_crp <- cumprod(crp_returns)
plot(crp_returns, main = "CRP Доходнось логарифмическая")

sinopharm_returns <- round(sinopharm_change+1, 4)
sinopharm_returns[1] <- 1
norm_sinopharm <- cumprod(sinopharm_returns)
plot(sinopharm_returns, main = "Sinopharm Доходнось логарифмическая")

plot(norm_crp, type = "l", ylim = c(0, 2), col = 4,
                   ylab = "Доходнось логарифмическая",
                   main='Парный трейдинг:
     CRP(синий) & Sinopharm (черный)')
lines(norm_sinopharm, col = 'black')
# legend("topleft", c(colnames(yi_adj)[1], colnames(crp_adj)[1]),
#        lty = 1, col = c("red", "blue"), bty = "o", cex = 1)
