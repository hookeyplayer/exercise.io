# O(N)
def traverse_and_print(node):
	# 基准情形，只需打印本结点书名
	if node is None:
		return
	# 在左子结点调用自身
	traverse_and_print(node.leftChild)
	# 访问此结点书名
	print(node.value)
	traverse_and_print(node.rightChild)