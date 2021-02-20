require('SMFI5')
a <- bond.vasicek(alpha = 0.5,
                  beta = 2.55,
                  sigma = 0.365,
                  q1 = 0.3,
                  q2 = 0,
                  r0 = 3.5,
                  n = 1080,
                  maturities = c(1/12, 3/12, 6/12, 1),
                  days = 365)
# 零息债券的年收益率
plot(a)