# 创建新变量3种方式
mydata$sumx  <-  mydata$x1 + mydata$x2
mydata$meanx <- (mydata$x1 + mydata$x2)/2

attach(mydata)
mydata$sumx  <-  x1 + x2
mydata$meanx <- (x1 + x2)/2
detach(mydata)

mydata <- transform(mydata, sumx = x1+x2, meanx = (x1+x2)/2)

# 变量重编码2种方式
leadership$agecat[leadership$age  > 75] <- "Elder"
leadership$agecat[leadership$age >= 55 & leadership$age <= 75] <- "Middle Aged"
leadership$agecat[leadership$age  < 55] <- "Young"

leadership <- within(leadership,{ 
  agecat <- NA 
  agecat[age > 75] <- "Elder"
  agecat[age >= 55 & age <= 75] <- "Middle Aged"
  agecat[age < 55]<- "Young"})

# 变量重命名2种方式
names(leadership)[6:10] <- c("item1", "item2", "item3", "item4", "item5")

library(plyr)
leadership <- rename(leadership, c(manager="managerID", date="testDate"))

# 横向合并
total <- merge(dataframeA, dataframeB, by="ID")
# 不需要公共索引直接横向合并
total <- cbind(A, B)
# 纵向合并
total <- rbind(dataframeA, dataframeB)

# 剔除的3种法
# 下标之前加-号就会剔除
newdata <- leadership[c(-8,-9)]

myvars <- names(leadership) %in% c("q3", "q4")
newdata <- leadership[!myvars]

# 两列设为未定义，一样的剔除效果
leadership$q3 <- leadership$q4 <- NULL

# 选入观测的2种法
attach(leadership)
newdata <- leadership[gender=='M' & age > 30,]
detach(leadership)

newdata <- leadership[leadership$gender=="M" & leadership$age > 30, ]

# 时间范围
leadership$date <- as.Date(leadership$date, "%m/%d/%y")
startdate <- as.Date("2009-01-01")
enddate <- as.Date("2009-10-31")
newdata <- leadership[which(leadership$date >= startdate &
                              leadership$date <= enddate),]

# subset函数
newdata <- subset(leadership, age >= 35 | age < 24,
                 select=c(q1, q2, q3, q4))

# SQL
library(sqldf)
newdf <- sqldf("select * from mtcars where carb=1 order by mpg",
               row.names=TRUE)

x <- c(1, 5, 23, 29)
diff(x) # c(4, 18, 6)

# 搜索或替换
sub("\\s",".","Hello There") # "Hello.There"

# 搜索并返回下标
grep("A",c("b","A","c"),fixed=TRUE) # 2

# 提取或替换
x <- "abcdef"
substr(x, 2, 4) <- "22222" # "a222ef"

# 连接字符串
paste("x",1:3,sep="M") # "xM1" "xM2" "xM3"

# 生成序列
indices <- seq(1,10,2)

# repete
y <- rep(1:3, 2)
y # 1 2 3 1 2 3

# runif()用来生成0到1区间上服从均匀分布的伪随机数
mydata <- matrix(rnorm(30), nrow=6) # 6X5正态分布随机数矩阵
apply(mydata, 1, mean) # 6行均值
apply(mydata, 2, mean) # 5列均值
apply(mydata, 2, mean, trim=0.2) # 截尾，只中间60%数据
