library(readr)
cofreewy <- read_table2("http://www.statsci.org/data/general/cofreewy.txt")

# 初次回归
a <- lm(CO~., data=cofreewy)
summary(a)
b <- step(a, direction='backward') 
summary(b) #逐步回归和全部自变量的回归相比舍弃了Hour变量
b <- step(a, direction='backward') 
qqnorm(b$residuals)
qqline(b$residuals)
# 残差的Shapiro-Wilk正态性检验的p值为0.05601
# 严格说0.05的显著性水平下不能拒绝“残差来自正态总体”的假设（数据量小，往往不容易拒绝零假设）
# 并且看逐步回归（b）的残差图也无法判断是正态分布的
# 从散点图看出CO和Hour有正弦曲线的关系
# 周期性可以借助时间序列分析的谐波分析
# 用有穷Fourier级数代表时间序列,可以考察各变量二次项和三次项对CO的影响

# Fourier model二次回归
attach(cofreewy)
cor(cbind(CO, 
          Traffic, Tsq=Traffic^2, Tcub=Traffic^3,
          Wind, Wsq=Wind^2, Wcub=Wind^3,
          Hour, Hsq=Hour^2, Hcub=Hour^3))
c <- lm(CO~Traffic+Wind+I(Wind^2)+I(Wind^3)+
          sin((2*pi/24)*Hour)+cos((2*pi/24)*Hour)+
          sin((4*pi/24)*Hour)+cos((4*pi/24)*Hour))
d <- step(c)
summary(d)
anova(d)
shapiro.test(d$residuals)
# 上述结果的Wind三次项和sin项不理想，所以修改模型

# 修正后三次回归
c1 <- lm(CO~Traffic+Wind+I(Wind^2)+
           cos((2*pi/24)*Hour)+
           cos((4*pi/24)*Hour))
d1 <- step(c1)
summary(d1)
anova(d1)
qqnorm(d1$residuals)
qqline(d1$residuals)
