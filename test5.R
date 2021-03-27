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
