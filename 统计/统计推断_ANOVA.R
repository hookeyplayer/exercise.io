# 检验多个样本的均值
# μ1=μ2=μ3=...=0

# 单变量 anova
# Null: μ1=μ2
set.seed(123)
var1 <- rnorm(12, mean=2, sd=1)
var2 <- c("B", "B", "B", "B", "C", "C", "C", "C", "C", "D", "D", "B")
data <- data.frame(var1, var2)
fit <- aov(data$var1 ~ data$var2, data=data)
fit
summary(fit); # fail to reject NULL

# 2个变量
# Null:μ1=μ2
set.seed(123)
var1 <- rnorm(12, mean=2, sd=1)
var2 <- c("B", "B", "B", "B", "C", "C", "C", "C", "C", "D", "D", "B")
var3 <- c("D", "D", "D", "D", "E", "E", "E", "E", "E", "F", "F", "F")
data <- data.frame(var1, var2, var3)
fit <- aov(data$var1 ~ data$var2 + data$var3, data=data)
fit
summary(fit)

# 方差序贯分析
anova(fit)

# multivariate
# Null:μ1=μ2=μ3
data("iris")
str(iris) # 150 obs. of  5 variables
summary(iris)
ans <- manova(cbind(iris$Sepal.Length, iris$Petal.Length) ~ iris$Species,
              data=data)
ans
summary(ans)
summary.aov(ans)
