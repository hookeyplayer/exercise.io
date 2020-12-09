class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
        isPrime = [True] * n
        for i in xrange(2, n):
            if i * i >= n:
                break
            if not isPrime[i]:
                continue
            for j in xrange(i * i, n, i):
                isPrime[j] = False
        count = 0
        for i in xrange(2, n):
            if isPrime[i]:
                count += 1
        return count

def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)
    
# 超时解法
# def countPrimes(n):
#     import math
#     count=0

#     def judge_prime(w):
#         sqrt_w=int(math.sqrt(w))
#         for i in xrange(2,sqrt_w+1):

#             if x%i==0:
#                 return 0
#         return 1

#     for x in xrange(2,n):

#         count=count+judge_prime(x)

#     return count