# dequeue
from collections import deque

def palchecker(aString):
	chardeque = deque()
	for cha in aString:
		chardeque.appendleft(cha)
	match = True
	while len(chardeque) > 1 and match:
		first = chardeque.popleft()
		last = chardeque.pop()
		if first != last:
			match = False
	return match

test = "racdar"
print(palchecker(test))

# 循环右移3步
# aDeque.rotate(3)

# 插入
# d.insert(2, 200)
# d.insert(-100, 300)

# 队头/尾拓展元素，按照list的顺序
# aDeque.extendleft(["c", "c"])
# aDeque.extend(["c", "c"])

# reverse
# aDeque.reverse()
