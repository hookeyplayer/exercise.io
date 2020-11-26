# The Hamming distance between two integers is:
# the number of positions at which the corresponding bits are different.
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
