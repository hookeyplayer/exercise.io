# 1 DP 自顶向下备忘录
# 1.1
known = {0:0, 1:1}
def fib(n):
    if n in known:
        return known[n]
    addup = fib(n-1) + fib(n-2)
    known[n] = addup
    return addup

# 1.2
def dynamic_fib(n):
	memo = [-1] * n
	if n <= 0:
		return n
	return fib(n-1, memo)

def fib(n, memo=[]):
	memo = list(memo)
	if memo[n] != -1:
		return memo[n]
	if n <= 1:
		memo[n] = 1
	else:
		memo[n] = fib(n-1, memo) + fib(n-1, memo)
	return memo[n]

# 2 DP 自底向上
def fib(n):
	flist = [-1] * n
	flist[0] = flist[1] = 1
	if n <= 0:
		return n
	for i in range(2, n):
		flist[i] = flist[i-1] + flist[i-2]
	return flist[n-1]
