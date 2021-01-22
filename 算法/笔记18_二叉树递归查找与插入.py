def search(value, node):
	if node is None or node.value == value:
		return node
	elif value < node.value:
		return search(value, node.leftChild)
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
