require("finreportr")
require("dplyr")
CompanyInfo("AAPL")
# list
AnnualReports("AAPL")
# 三张财务表
apple_is <- GetIncome("AAPL", 2017)
df_is <- data.frame(AAPL.IS)
apple_bs <- GetBalanceSheet("AAPL", 2017)
df_bs <- data.frame(apple_bs)
apple_cf <- GetCashFlow("AAPL", 2017)
df_cf <- data.frame(apple_cf)
head(df_is)
head(df_bs)
head(df_cf)


# coefficients ------------------------------------------------------------

net_revenue <- filter(df_is, Metric=="Revenue, Net")
assets <- filter(df_bs, Metric=="Assets")
# 最近一年
rev_to_assets = as.numeric((tail(net_revenue$Amount, 1)))/as.numeric((tail(assets$Amount, 1)))
rev_to_assets # 0.6107711
                            