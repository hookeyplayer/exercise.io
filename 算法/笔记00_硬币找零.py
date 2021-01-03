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
# def dpMakeChange(coinValueList, change, minCoins):
# 	for cents in range(change+1):
# 		coinCount = cents
 
# 		for j in [c for c in coinValueList if c <= cents]:
# 			if minCoins[cents-j] + 1 < coinCount:
# 				coinCount = minCoins[cents-j] + 1
# 		minCoins[cents] = coinCount
# 	return minCoins[change]

def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
	for cents in range(change+1):
		coinCount = cents 
		newCoin = 1
		for j in [c for c in coinValueList if c <= cents]:
			if minCoins[cents-j] + 1 < coinCount:
				coinCount = minCoins[cents-j] + 1
				newCoin = j
		minCoins[cents] = coinCount
		coinsUsed[cents] = newCoin
	return minCoins[change]

def printCoins(coinsUsed, change):
	coin = change
	while coin > 0:
		thisCoin = coinsUsed[coin]
		print(thisCoin)
		coin = coin - thisCoin

def main():
	amount = 63
	coinlist = [1, 5, 10, 21, 25]
	# coinsUsed：用来找零的硬币的阵列
	coinsUsed = [0] * (amount+1)
	# coinCount：为表中相应位置的量找零所需的硬币数量的最小值
	coinCount = [0] * (amount+1)
	print('Make change for ', amount, 'requires:')
	print(dpMakeChange(coinlist, amount, coinCount, coinsUsed), ' coins')
	print('They are: ')
	printCoins(coinsUsed, amount)
	print('The used list is: ')
	print(coinsUsed)

main()
Make change for  63 requires:
3  coins
They are: 
21
21
21
The used list is: 
[1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 21, 1, 1, 1, 25, 1, 1, 1, 1, 5, 10, 1, 1, 1, 10, 1, 1, 1, 1, 5, 10, 21, 1, 1, 10, 21, 1, 1, 1, 25, 1, 10, 1, 1, 5, 10, 1, 1, 1, 10, 1, 10, 21]
