def delete(valueToDelete, node):
	# 如果要删除的结点没有子结点，那直接删掉它
	if node is None:
		return None
	# 要删除的值比当前的根结点小
	elif valueToDelete < node.value:
		# 以左子树为参数，递归调用本方法
		# 将当前结点的左/右链指向返回的结点，填充
		node.leftChild = delete(valueToDelete, node.leftChild)
		return node
	# 要删除的值大于当前结点，则使用递归右下长驱直入
	# 直到没有左子结点为止
	elif valueToDelete > node.value:
		node.rightChild = delete(valueToDelete, node.rightChild)
		return node
	elif valueToDelete == node.value:
		if node.leftChild is None:
			return node.rightChild
		elif node.rightChild is None:
			return node.leftChild
		else:
			node.rightChild = lift(node.rightChild, node)
			return node
# 攀枝剔除
def lift(node, nodeToDelete):
	# 若此函数当前结点有左子结点
	# 则递归本函数，从左子树找后继点
	if node.leftChild:
		node.leftChild = lift(node.leftChild, nodeToDelete)
		return node
	# 若当前无左子结点，即当前只有右继结点
	else:
		# 将右继结点天朝父结点
		nodeToDelete.value = node.value
		# 用右继结点的右子结点填充父结点的左子结点
		return node.rightChild


