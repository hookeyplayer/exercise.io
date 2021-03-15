library(sqldf)
newdf <- sqldf('select * from df where car=1 order by mpg',
               row.names=TRUE)