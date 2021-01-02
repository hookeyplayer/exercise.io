# 用最少的硬币找零
# 1 递归+查表
# 基本条件：要找的零钱价值和某一种硬币币值一样，即只要一个硬币
# 若不匹配，则求解“给（原始价值-1美分）找零所需硬币的数量”，或者
# 求解“给（原始价值-5美分）找零所需硬币的数量”或者
# 求解“给（原始价值-10美分）找零所需硬币的数量”或者
# 求解“给（原始价值-25美分）找零所需硬币的数量”
def recDC(coinValueList, change, knownResults):
	minCoins = change
	if change in coinValueList:
		knownResults[change] = 1
		return 1
	elif knownResults[change] > 0:
		return knownResults[change]
	else:
		for i in [c for c in coinValueList if c <= change]:
			numCoins = 1 + recDC(coinValueList, change-i, knownResults)
			if numCoins < minCoins:
				minCoins = numCoins
				knownResults[change] = minCoins
	return minCoins

coinValueList = [1, 5, 10, 25]
change = 63
knownResults = [0]*64
print(recDC(coinValueList, change, knownResults))

# 2 dp：从为1美分找零的最优解开始，逐步递加
# 保证在算法的每一步过程中已知兑换更小数值的最优解
