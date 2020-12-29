// O(logn)
int countones(unsigned int n)
{
	int ones = 0; //计数器复位
	while (0 < n)
	{
		ones += (1 & n); //二进制位的与运算，检查最低位
		n >> 1; // 右移1位，n减半
	}
	return ones;
}
// glibc 内置函数 int __builtin_popcount (unsigned int n)
