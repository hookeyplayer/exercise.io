library(xlsx)
msci2017 <- read.xlsx('msci2017.xlsx', 1,head = TRUE)
head(msci2017)
str(msci2017)

# 按国家统计 2017
country <- factor(msci2017$Country,
                  levels = c('Brazil', 'Chile', 'China', 'Colombia',
                             'Czech Republic', 'Egypt', 'Greece', 'Hungary',
                             'India', 'Indonesia', 'Korea', 'Malaysia',
                             'Mexico', 'Pakistan', 'Peru', 'Philippines',
                             'Poland', 'Qatar', 'Russia', 'South Africa',
                             'Taiwan', 'Thailand', 'Turkey', 'United Arab Emirates')
                  )
head(country)
table(country)

# 按版块统计
msci2019 <- read.xlsx('msci2019.xlsx', 1,head = TRUE)
sector <- factor(msci2017$Sector,
                 levels = c('Communication Services', 'Consumer Discretionary',
                            'Consumer Staples', 'Energy', 'Financials',
                            'Health Care', 'Industrials', 'Materials',
                            'Information Technology', 'Real Estate', 'Utilities')
                 )

a <- table(country, sector)
a
margin.table(a, 1) # 行
margin.table(a, 2) # 列

prop.table(a, 2)

# 导出
write.xlsx(a, "/Users/xiaofan/论文数据/contingency_table.xlsx",
           sheetName = "2017", append = TRUE)

# 按国家统计 2017
country2 <- factor(msci2019$Country,
                  levels = c('Brazil', 'Chile', 'China', 'Colombia', 'Argentina',
                             'Czech Republic', 'Egypt', 'Greece', 'Hungary',
                             'India', 'Indonesia', 'Korea', 'Malaysia',
                             'Mexico', 'Pakistan', 'Peru', 'Philippines',
                             'Poland', 'Qatar', 'Russia', 'South Africa',
                             'Taiwan', 'Thailand', 'Turkey', 'United Arab Emirates',
                             'Saudi Arabia')
                  )
table(country2)
sector2 <- factor(msci2019$Sector,
                 levels = c('Communication Services', 'Consumer Discretionary',
                            'Consumer Staples', 'Energy', 'Financials',
                            'Health Care', 'Industrials', 'Materials',
                            'Information Technology', 'Real Estate', 'Utilities')
)
b <- table(country2, sector2)
b
write.xlsx(b, "/Users/xiaofan/论文数据/contingency_table.xlsx",
           sheetName = "2019", append = TRUE)


# gl,seq,rep
# rt, rnorm
