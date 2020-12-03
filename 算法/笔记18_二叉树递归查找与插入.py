# 小于父结点的子结点用左箭头来表示，大于父结点的子结点则用右箭头来表示
def search(value, node):
	# 如果node不存在
	if node is None or node.value == value:
		return node
	# 如果value小于当前结点node.value
	elif value < node.value:
		return search(value, node.leftChild)
	# 如果value大于当前结点
	else:
		return search(value, node.rightChild)
		
def insert(value, node):
	if value < node.value:
		if node.leftChild is None:
			node.leftChild = TreeNode(value)
		else:
			insert(value, node.leftChild)

	elif value > node.value:
		if node.rightChild is None:
			node.rightChild = TreeNode(value)
		else:
			insert(value, node.rightChild)