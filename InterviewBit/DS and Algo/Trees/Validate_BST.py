# Python implementation to check if 
# given Binary tree is a BST or not 
# idea is to do Inorder traversal check is this order is sorted or not
# A binary tree node containing data 
# field, left and right pointers 
class Node: 
	# constructor to create new node 
	def __init__(self, val): 
		self.data = val 
		self.left = None
		self.right = None

# global variable prev - to keep track 
# of previous node during Inorder 
# traversal 
prev = None

# function to check if given binary 
# tree is BST 
def isbst(root): 
	
	# prev is a global variable 
	global prev 
	prev = None
	return isbst_rec(root) 


# Helper function to test if binary 
# tree is BST 
# Traverse the tree in inorder fashion 
# and keep track of previous node 
# return true if tree is Binary 
# search tree otherwise false 
def isbst_rec(root): 
	
	# prev is a global variable 
	global prev 

	# if tree is empty return true 
	if root is None: 
		return True

	if isbst_rec(root.left) is False: 
		return False

	# if previous node'data is found 
	# greater than the current node's 
	# data return fals 
	if prev is not None and prev.data > root.data: 
		return False

	# store the current node in prev 
	prev = root 
	return isbst_rec(root.right) 


# driver code to test above function 
root = Node(4) 
root.left = Node(8) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 

if isbst(root): 
	print("It is BST") 
else: 
	print("It is not a BST") 
