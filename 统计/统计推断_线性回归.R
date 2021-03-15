# 单变量
set.seed(123)
x <- rnorm(100, mean=1, sd=1)
y <- rnorm(100, mean=2, sd=2)
data <- data.frame(x, y)
mod <- lm(data$y ~ data$x, data=data)
mod

# 多元回归
x1 <- rnorm(100, mean=1, sd=1)
x2 <- rnorm(100, mean=2, sd=5)
y <- rnorm(100, mean=2, sd=2)
data <- data.frame(x1, x2, y)
mod <- lm(data$y ~ data$x1 + data$x2, data=data)
mod
summary(mod)