#  File: ExpressionTree.py

import sys

def operate(operator, num1, num2):
		if operator == '+':
			return num1 + num2
		elif operator == '-':
			return num1 - num2
		elif operator == '*':
			return num1 * num2
		elif operator == '/':
			return num1 / num2
		elif operator == '//':
			return num1 // num2
		elif operator == '%':
			return num1 % num2
		elif operator == '**':
			return num1 ** num2

class Stack (object):
	def __init__(self):
		self.stack = []
		
	# add an item on the top of the stack
	def push(self, item):
		self.stack.append(item)

	# remove an item from the top of the stack
	def pop(self):
		return self.stack.pop()

	# check the item on the top of the stack
	def peek(self):
		return self.stack[-1]

	# check if the stack is empty
	def is_empty(self):
		return (len(self.stack) == 0)

	# return the number of elements in the stack
	def size(self):
		return (len(self.stack))

class Node (object):
	def __init__ (self, data = None):
		self.data = data
		self.lchild = None
		self.rchild = None
		self.parent = None
		self.visited = False

class Tree (object):
	def __init__(self):
		self.root = Node(None)

	def create_tree (self, expr):
		newexp = expr.split()

		#now newexp is a list of JUST tokens (no spaces) to go through
		#now start doing stack stuff
		stack = Stack()

		curr_node = Node()
		self.root = curr_node

		#set types of tokens

		operators = ['+', '-', '*', '/', '//', '%', '**']

		for curr_token in newexp:
			
			if curr_token == '(':
				#If the current token is a left parenthesis add a new node as the left child of the current node.
				newnode = Node()
				curr_node.lchild = newnode
				# Push current node on the stack and make current node equal to the left child.
				stack.push(curr_node)
				curr_node = curr_node.lchild
			
			elif curr_token in operators:
				#If the current token is an operator set the current node's data value to the operator.
				curr_node.data = curr_token
				# Push current node on the stack
				stack.push(curr_node)
				# Add a new node as the right child of the current node
				newnode = Node()
				curr_node.rchild = newnode
				# and make the current node equal to the right child.
				curr_node = curr_node.rchild
			
			elif curr_token == ')':
				#If the current token is a right parenthesis make the current node equal to the parent node 
				# by popping the stack if it is not empty.
				if not stack.is_empty():
					curr_node = stack.pop()
			
			else:
				#if is operand so none of the others
				# If the current token is an operand, set the current node's data value to the operand
				curr_node.data = int(curr_token)
				# and make the current node equal to the parent by popping the stack
				curr_node = stack.pop()
	
	def evaluate(self, aNode):
		# infix traverse - left, root, right
		# eval() can solve string expressions

		# empty tree 
		if aNode.data is None: 
			return 0

		# leaf node, if operand
		if aNode.lchild is None and aNode.rchild is None: 
			return aNode.data

		#if operator
		operators = ['+', '-', '*', '/', '//', '%', '**']
		if aNode.data in operators:
			return float(operate(aNode.data, self.evaluate(aNode.lchild), self.evaluate(aNode.rchild)))



	#converts infix input into prefix output as a list
	def pre_order(self, aNode, store):
		# prefix traverse - root, left, right
		if (aNode != None):
			store.append(aNode.data)
			self.pre_order (aNode.lchild, store)
			self.pre_order (aNode.rchild, store)
		return store

	#converts infix input into postfix output as a list
	def post_order(self, aNode, store):
		# postfix traverse - left, right, root
		if (aNode != None):
			self.post_order (aNode.lchild, store)
			self.post_order (aNode.rchild, store)
			store.append(aNode.data)
		return store


def main():
	# read infix expression
	line = sys.stdin.readline()
	expr = line.strip()

	tree = Tree()
	tree.create_tree(expr)

	# evaluate the expression and print the result
	# print(expr, '=', float(eval(str(expr))))
	print(expr, "=", tree.evaluate(tree.root))

	# get the prefix version of the expression and print
	print("\nPrefix Expression: ", end = '')
	#must call arg with empty list to work
	for i in tree.pre_order(tree.root, []):
		print(i, end = ' ')
	

	# get the postfix version of the expression and print
	print("\n\nPostfix Expression: ", end = '')
	#must call arg with empty list to work
	for i in tree.post_order(tree.root, []):
		print(i, end = ' ')

if __name__ == "__main__":
	main()



#  Description: using trees to eval infix input and convert to pre/post fix
