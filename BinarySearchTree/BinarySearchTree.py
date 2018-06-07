class Node:
	def __init__(self, val):
		self.l_child = None
		self.r_child = None
		self.data = val

	def insert(self, root, node):
		if root is None:
			root = node
		else:
			if root.data > node.data:
				if root.l_child is None:
					root.l_child = node
				else:
					self.insert(root.l_child, node)
			else:
				if root.r_child is None:
					root.r_child = node
				else:
					self.insert(root.r_child, node)

	def in_order_print(self, root):
		if not root:
			return
		
		self.in_order_print(root.l_child)
		print(root.data)
		self.in_order_print(root.r_child)

	def pre_order_print(self, root):
		if not root:
			return
		print(root.data)
		self.pre_order_print(root.l_child)
		self.pre_order_print(root.r_child)


tree = Node(21)
tree.insert(tree, Node(28))
tree.insert(tree, Node(14))
tree.insert(tree, Node(32))
tree.insert(tree, Node(25))
tree.insert(tree, Node(18))
tree.insert(tree, Node(30))
tree.insert(tree, Node(19))
tree.insert(tree, Node(15))

tree.pre_order_print(tree)