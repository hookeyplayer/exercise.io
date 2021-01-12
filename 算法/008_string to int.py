# 过滤空格、考虑正负号、如果溢出则返回上下限、遇到非法字符则停止
class Solution:
# 正则
    def myAtoi(self, s: str) -> int:
    	if not s:
    		return 0
    	s = s.strip() # 去除开头空格
    	num, sign = 0, 1
    	if s[0] == '-':
    		s = s[1:]
    		sign = -1
    	elif s[0] == '+':
    		s = s[1:]
    	list = []
    	for c in s:
    		try:
    			# 首先保证c可以转化成数字
    			if int(c) != 0 or list != []:
    				list.append(c)
    			if len(list) > 10: # 2**31 = 2147483647有10位
    				break
    		except:
    			break
    	if list == []:
    		return 0
    	num = int(''.join(list)) # 把list的数组合起来
    	num = sign * num
    	return num
    		


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.myAtoi('-11@¥'))
