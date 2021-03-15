# no assumption about Normal distribution
# Wilcoxon Signed Rank Test
# 单变量
# H0: μ=μ0
wilcox.test(data[,1], mu=0, alternatives="two.sided")

# 2个变量
# Wilcoxon-Mann-Whitney Test
wilcox.test(data[,1], data[,2], correct=FALSE)

# 多变量
# Kruskal-Wallis test
# H0 :m0 =m1 =m2 =...=mk
data("airquality")
str(airquality) # 153 obs. of  6 variables
summary(airquality)
kruskal.test(airquality$Ozone ~ airquality$Month)
