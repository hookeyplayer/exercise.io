# goodness of fit Chi-squqre
# 研究对象是出现频次
# Null:No significant difference between the observed and expected values.
data <- c(B=200, c=300, D=400)
chisq.test(data)


# 比较2个categorical变量的关系
# Null:two variables independent

var1 <- c("Male", "Female", "Male", "Female", "Male",
          "Female", "Male", "Female", "Male", "Female")
var2 <- c("chocolate", "strawberry", "strawberry",
          "strawberry", "chocolate", "chocolate", "chocolate",
          "strawberry", "strawberry", "strawberry")
data <- data.frame(var1, var2)
data # 2 vectors
data.table <- table(data$var1, data$var2)
data.table

# contingency test
chisq.test(data.table)
