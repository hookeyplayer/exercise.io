# Vasicek模型：单因素+mean-reverting+affine+stochastic
vasicek <- function(alpha, beta, sigma, n = 100, r0 = 0.026) {
  v <- rep(0, n)
  v[1] <- r0
  for (i in 2:n) {
    v[i] <- v[i - 1] + alpha * (beta - v[i - 1]) + sigma * rnorm(1)
  }
  return(v)
}
set.seed(13)
r <- replicate(3, vasicek(0.02, 0.056, 0.0006))
# plot columns of matrix against columns of another matrix
matplot(r, type = 'l',
        ylab = '',
        xlab = 'Time',
        xaxt = 'no',
        main = 'Simulation of Interest Rate Using Vasicek Trajectories')
lines(c(-1, 101), c(0.056, 0.056), col = 'grey', lwd = 2, lty = 1)

# 改变sigma
r <- sapply(c(0, 0.0003, 0.0009),
            function(sigma){
              set.seed(23); vasicek(0.02, 0.056, sigma)
            })
matplot(r,
        type = 'l',
        ylab = '',
        xlab = 'Time',
        xaxt = 'no',
        main = 'Vasicek Simulation with sigma 0, 0.03%, 0.09%')

# 改变alpha
# alpha越大，越早到达long-term beta
r <- sapply(c(0.002, 0.02, 0.2),
            function(alpha){
              set.seed(33); vasicek(alpha, 0.056, 0.0006)
            })
matplot(r, type = 'l',
        ylab = '',
        xlab = 'Time',
        xaxt = 'no',
        main = 'Vasicek Simulation with alpha 0.2%, 2%, 20%')


