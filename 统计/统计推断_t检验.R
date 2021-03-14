# assume 样本从总体随机而来；总体～Normal
# 单样本t检验
set.seed(123)
var1 <- rnorm(100, mean=2, sd=1)
var2 <- rnorm(100, mean=3, sd=1)
var3 <- rnorm(100, mean=3, sd=2)
data <- data.frame(var1, var2, var3)
# H0: μ=0.6
t.test(data$var1, mu=0.6)

# 两个样本（iid）
# H0: μ1-μ2=0
data <- data.frame(var1, var2, var3)
t.test(data$var1, data$var2, var.equal=TRUE, paired=FALSE)

# 两个样本 Welch t检验（独立但不同分布）（方差不同）
t.test(data$var1, data$var2, var.equal=FALSE, paired=FALSE)

# 两个样本dependent
t.test(data$var1, data$var2, paired=TRUE)

