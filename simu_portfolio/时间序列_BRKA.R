# 2021.2.20 练习
# 导入数据 --------------------------------------------------------------------
require(quantmod)
data_env <- new.env()
getSymbols(Symbols = 'BRK-A',env = data_env)
brka_close <- do.call(merge, eapply(data_env, Cl))
# head(brka_close)

# 处理数据 --------------------------------------------------------------------
# return的2种方法
library(fImport)
yield <- returns(brka_close)
head(yield)

library(zoo)
# unit in percentage terms
yield_simple <- diff(brka_close) / lag(brka_close, k = -1) * 100
# coredate方法: we only care about price column, not the date
summary(coredata(yield_simple))


# 分析数据 --------------------------------------------------------------------
# 单日跌幅最大
yield_simple[which.min(yield_simple)]

# 分布
hist(yield_simple, breaks = 100,
     main = 'Histogram of Simple Returns', xlab = '%')

# 简单VaR
quantile(yield_simple, na.rm = T, probs = 0.01)

require(forecast)
mod <- auto.arima(yield, stationary = T, seasonal = F, ic = 'aic')

# 置信区间
tsdiag(mod)
