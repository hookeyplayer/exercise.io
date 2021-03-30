library(readr)
library(zoo)
library(sandwich)
library(strucchange)

df <- read_csv("MSCI Emerging Markets Historical Data.csv",
               col_names = TRUE)

# 日期从chr到date转化
df$Date <- as.Date(df$Date,
                   format='%B %d, %Y')
str(df)

# 产生单变量时间序列
df.zoo <- zoo(df$Price,
              order.by = df$Date) 
str(df.zoo)
class(df.zoo)
sum(is.na(df.zoo))

plot.zoo(df.zoo,
         xlab = "Дата",
         ylab = "Цена",
         col = "mediumblue",
         lwd = 1) 
title("Временные ряды индекс MSCI развивающихся рынков")
grid()

bp <- breakpoints(df.zoo$)
